"""make_zoo.py -- train the model zoo and save every model's argmax prediction table over the
WHOLE input group.

    python3 code/make_zoo.py            # builds zoo/*.npz, zoo/index.json, cache/*_logits.npz

Everything is a one-hidden-layer MLP on concatenated one-hot inputs, trained full-batch with
(decoupled-weight-decay) Adam in float32 numpy.  Deterministic: every run is a pure function of its
(split_seed, init_seed); two worker processes with single-threaded BLAS; the parent writes the files
in a fixed order.  (Bit-for-bit identical tables are guaranteed on the same numpy/BLAS build; the
tables themselves are committed, so all downstream analysis is exactly reproducible anyway.)

Families (see FAMILIES below for the exact hyper-parameters)
  add/grok  f(a,b) = a+b mod p, p in {23,31,47}; weight decay; train_frac {0.3,0.5,0.7};
            seeds {0,1,2,3} (split_seed = init_seed); 30 log-spaced snapshots incl. step 0 and the last.
  add/memo  p = 53, no weight decay, trained until 100% train accuracy and train loss < 0.02;
            random hold-out with train_frac {0.9,0.7,0.5,0.3} and a class hold-out (5 of 53 answer
            classes never seen); per configuration: (split,init) in {(0,0),(1,0),(2,0)} and init seeds
            {1,2,3,4} on split 0 (init 0..4 on split 0 = a deep ensemble).  Final step only; logits
            saved as float16 to cache/.
  lin       f(x) = <w,x> mod 7 on Z_7^4, w = (3,5,2,6); weight decay, ReLU; train_frac {0.1,0.2,0.4};
            seeds {0,1,2} (split_seed = init_seed); 12 log-spaced snapshots.
  mul       f(a,b) = a*b mod 31; weight decay; train_frac {0.5,0.7}; seeds {0,1,2}; 25 snapshots.

One .npz per run: tables (S, p,...,p) uint8, steps (S,), train_mask (p,...,p) bool.
"""
import json
import os
import sys
import time

os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"

import numpy as np
import scipy.sparse as sp

import core

N_PROC = 2
SCHEMA = 1

# hyper-parameters of each family --------------------------------------------------------------
FAMILIES = {
    "add/grok": dict(task="add", n=2, act="quad", width=256, lr=3e-3, wd=1.0, beta2=0.98, bias=False,
                     init="grok", steps=4000, n_snap=30, snap_first=10, stop_when_fit=False),
    "add/memo": dict(task="add", n=2, act="relu", width=256, lr=5e-3, wd=0.0, beta2=0.999, bias=True,
                     init="memo", steps=4000, n_snap=1, snap_first=None, stop_when_fit=True),
    # ReLU: a quadratic activation cannot fit a 4-term sum mod 7 (it reached only 50% TRAIN accuracy)
    "lin":      dict(task="lin", n=4, act="relu", width=256, lr=3e-3, wd=1.0, beta2=0.98, bias=False,
                     init="grok", steps=8000, n_snap=12, snap_first=10, stop_when_fit=False),
    "mul":      dict(task="mul", n=2, act="quad", width=256, lr=3e-3, wd=1.0, beta2=0.98, bias=False,
                     init="grok", steps=4000, n_snap=25, snap_first=10, stop_when_fit=False),
}


def snapshot_steps(total, n_snap, first):
    """n_snap snapshot steps: 0, then log-spaced from `first` to `total` (inclusive, deduplicated)."""
    if n_snap == 1:
        return [total]
    s = np.unique(np.rint(np.geomspace(first, total, n_snap - 1)).astype(int))
    return [0] + [int(v) for v in s]


def one_hot_inputs(p, n):
    """Sparse (|G|, n*p) one-hot encoding of every group element, rows in flat-index order."""
    C = core.coords(core.group_shape(p, n))
    N = len(C)
    rows = np.repeat(np.arange(N), n)
    cols = (C + p * np.arange(n)[None, :]).ravel()
    return sp.csr_matrix((np.ones(N * n, np.float32), (rows, cols)), shape=(N, n * p))


def make_split(y, q, holdout, train_frac, split_seed):
    """Training mask over the flat inputs.  holdout="random": exactly int(train_frac*|G|) inputs chosen
    by a seeded permutation.  holdout="class": 5 answer classes (seeded choice) are never trained on,
    everything else is.  Returns (mask, held_out_classes or None)."""
    N = len(y)
    rng = np.random.default_rng(10_000 + split_seed)
    if holdout == "random":
        mask = np.zeros(N, bool)
        mask[rng.permutation(N)[: int(train_frac * N)]] = True
        return mask, None
    classes = np.sort(rng.choice(q, 5, replace=False))
    return ~np.isin(y, classes), [int(c) for c in classes]


def train_run(job):
    """Train one network; returns dict(tables (S,|G|) uint8, steps, train_mask, final logits, stats)."""
    t0 = time.time()
    hp = FAMILIES[job["family"]]
    p, n, q = job["p"], hp["n"], job["p"]
    f = core.true_table(hp["task"], p, n)
    y = f.ravel().astype(np.int64)
    N = y.size
    X = one_hot_inputs(p, n)
    mask, classes = make_split(y, q, job["holdout"], job["train_frac"], job["split_seed"])
    idx = np.flatnonzero(mask)
    Xt = X[idx].tocsr()
    XtT = Xt.T.tocsr()
    yt = y[idx]
    m = len(idx)
    Y = np.zeros((m, q), np.float32)
    Y[np.arange(m), yt] = 1.0
    width, act, lr, wd, b2 = hp["width"], hp["act"], np.float32(hp["lr"]), np.float32(hp["wd"]), hp["beta2"]
    rng = np.random.default_rng(job["init_seed"])
    d = n * p
    if hp["init"] == "grok":      # same scales as the pilot's grokking trainer
        W1 = (rng.standard_normal((d, width)) * (1.0 / np.sqrt(d))).astype(np.float32)
        W2 = (rng.standard_normal((width, q)) * (0.5 / np.sqrt(width))).astype(np.float32)
    else:                         # same scales as the pilot's memoriser
        W1 = (rng.standard_normal((d, width)) * 0.5).astype(np.float32)
        W2 = (rng.standard_normal((width, q)) / np.sqrt(width)).astype(np.float32)
    prm = {"W1": W1, "W2": W2}
    if hp["bias"]:
        prm["b1"] = np.zeros(width, np.float32)
        prm["b2"] = np.zeros(q, np.float32)
    mom = {k: np.zeros_like(v) for k, v in prm.items()}
    var = {k: np.zeros_like(v) for k, v in prm.items()}

    def forward(Xs):
        h = Xs @ prm["W1"]
        if hp["bias"]:
            h = h + prm["b1"]
        a = h * h if act == "quad" else np.maximum(h, 0)
        z = a @ prm["W2"]
        if hp["bias"]:
            z = z + prm["b2"]
        return h, a, z

    snaps = snapshot_steps(hp["steps"], hp["n_snap"], hp["snap_first"])
    tables, steps_done = [], []
    logits = None
    t = 0
    while True:
        last = t == hp["steps"]
        if hp["stop_when_fit"] and t > 0 and t % 50 == 0 and not last:
            _, _, z = forward(Xt)
            z = z - z.max(1, keepdims=True)
            lse = np.log(np.exp(z).sum(1))
            loss = float((lse - z[np.arange(m), yt]).mean())
            if (z.argmax(1) == yt).all() and loss < 0.02:
                last = True
        if last or (not hp["stop_when_fit"] and t in snaps):
            _, _, z = forward(X)
            tables.append(z.argmax(1).astype(np.uint8))
            steps_done.append(t)
            if last:
                logits = z
                break
        t += 1
        h, a, z = forward(Xt)
        z -= z.max(1, keepdims=True)
        np.exp(z, out=z)
        z /= z.sum(1, keepdims=True)
        dz = (z - Y) / np.float32(m)
        g = {"W2": a.T @ dz}
        da = dz @ prm["W2"].T
        dh = da * (2.0 * h) if act == "quad" else da * (h > 0)
        g["W1"] = np.asarray(XtT @ dh)
        if hp["bias"]:
            g["b1"] = dh.sum(0)
            g["b2"] = dz.sum(0)
        c1 = np.float32(1.0 / (1.0 - 0.9 ** t))
        c2 = np.float32(1.0 / (1.0 - b2 ** t))
        for k in prm:
            mom[k] = np.float32(0.9) * mom[k] + np.float32(0.1) * g[k]
            var[k] = np.float32(b2) * var[k] + np.float32(1.0 - b2) * g[k] * g[k]
            upd = (mom[k] * c1) / (np.sqrt(var[k] * c2) + np.float32(1e-8))
            if wd > 0 and k in ("W1", "W2"):
                upd = upd + wd * prm[k]
            prm[k] = prm[k] - lr * upd
    tables = np.stack(tables)
    correct = tables == y[None, :].astype(np.uint8)
    out = dict(job=job, tables=tables, steps=np.array(steps_done), train_mask=mask, classes=classes,
               train_acc=correct[:, mask].mean(1), heldout_acc=correct[:, ~mask].mean(1),
               eps=1.0 - correct.mean(1), secs=time.time() - t0,
               logits=logits.astype(np.float16) if job["family"] == "add/memo" else None)
    return out


def all_jobs():
    jobs = []
    for p in (23, 31, 47):
        for frac in (0.3, 0.5, 0.7):
            for s in (0, 1, 2, 3):
                jobs.append(dict(family="add/grok", p=p, holdout="random", train_frac=frac, split_seed=s, init_seed=s))
    memo_cfgs = [("random", fr) for fr in (0.9, 0.7, 0.5, 0.3)] + [("class", None)]
    for holdout, frac in memo_cfgs:
        for ss, is_ in ((0, 0), (1, 0), (2, 0), (0, 1), (0, 2), (0, 3), (0, 4)):
            jobs.append(dict(family="add/memo", p=53, holdout=holdout, train_frac=frac, split_seed=ss, init_seed=is_))
    for frac in (0.1, 0.2, 0.4):
        for s in (0, 1, 2):
            jobs.append(dict(family="lin", p=7, holdout="random", train_frac=frac, split_seed=s, init_seed=s))
    for frac in (0.5, 0.7):
        for s in (0, 1, 2):
            jobs.append(dict(family="mul", p=31, holdout="random", train_frac=frac, split_seed=s, init_seed=s))
    for j in jobs:
        fam = j["family"].replace("/", "")
        split = "class5" if j["holdout"] == "class" else f"f{j['train_frac']}"
        j["run_id"] = f"{fam}_p{j['p']}_{split}_ss{j['split_seed']}_is{j['init_seed']}"
    return jobs


def main():
    from multiprocessing import Pool
    t0 = time.time()
    os.makedirs(core.ZOO_DIR, exist_ok=True)
    os.makedirs(core.CACHE_DIR, exist_ok=True)
    jobs = all_jobs()
    # schedule the most expensive runs first (cost ~ training-set size * steps); order of results is fixed
    cost = lambda j: -(j["p"] ** FAMILIES[j["family"]]["n"]) * FAMILIES[j["family"]]["steps"] * (j["train_frac"] or 0.9)
    order = sorted(range(len(jobs)), key=lambda i: cost(jobs[i]))
    results = [None] * len(jobs)
    print(f"training {len(jobs)} runs with {N_PROC} processes", flush=True)
    with Pool(N_PROC) as pool:
        for k, (i, res) in enumerate(pool.imap_unordered(_indexed, [(i, jobs[i]) for i in order], chunksize=1)):
            results[i] = res
            j = res["job"]
            print(f"[{k + 1:3d}/{len(jobs)}] {j['run_id']:36s} snaps={len(res['steps']):2d} last_step={int(res['steps'][-1]):5d} "
                  f"train_acc={res['train_acc'][-1]:.3f} heldout_acc={res['heldout_acc'][-1]:.3f} eps={res['eps'][-1]:.4f} "
                  f"({res['secs']:.1f}s, total {time.time() - t0:.0f}s)", flush=True)
    models, runs, timing = [], [], {}
    for res in results:
        j = res["job"]
        hp = FAMILIES[j["family"]]
        p, n = j["p"], hp["n"]
        shape = core.group_shape(p, n)
        file = f"zoo/{j['run_id']}.npz"
        save_npz(os.path.join(core.ROOT, file), tables=res["tables"].reshape((-1,) + shape),
                 steps=res["steps"].astype(np.int32), train_mask=res["train_mask"].reshape(shape))
        logits_file = None
        if res["logits"] is not None:
            logits_file = f"cache/{j['run_id']}_logits.npz"
            save_npz(os.path.join(core.ROOT, logits_file), logits=res["logits"])
        frac_actual = float(res["train_mask"].mean())
        timing[j["run_id"]] = round(res["secs"], 2)
        runs.append(dict(run_id=j["run_id"], family=j["family"], file=file, n_snapshots=len(res["steps"]),
                         steps=[int(s) for s in res["steps"]]))
        for s, step in enumerate(res["steps"]):
            models.append(dict(
                id=f"{j['run_id']}_t{int(step):05d}", run_id=j["run_id"], task=hp["task"], p=p, n=n, q=p,
                family=j["family"], holdout=j["holdout"],
                train_frac=j["train_frac"] if j["train_frac"] is not None else round(frac_actual, 6),
                train_frac_actual=frac_actual, heldout_classes=res["classes"],
                split_seed=j["split_seed"], init_seed=j["init_seed"], step=int(step),
                final=bool(s == len(res["steps"]) - 1), weight_decay=hp["wd"], lr=hp["lr"], act=hp["act"],
                width=hp["width"], train_acc=float(res["train_acc"][s]), heldout_acc=float(res["heldout_acc"][s]),
                eps=float(res["eps"][s]), file=file, snap=s, logits_file=logits_file))
    # index.json holds no timings, so a rebuild reproduces it (and the .npz files) byte for byte
    index = dict(schema=SCHEMA, description="model zoo for the coherence paper; see code/make_zoo.py and code/core.py",
                 lin_weights=list(core.LIN_W), families=FAMILIES, n_models=len(models), n_runs=len(runs),
                 runs=runs, models=models)
    with open(os.path.join(core.ZOO_DIR, "index.json"), "w") as fh:
        json.dump(index, fh, indent=1)
    total = time.time() - t0
    os.makedirs(core.RESULTS_DIR, exist_ok=True)
    with open(os.path.join(core.RESULTS_DIR, "zoo_build.json"), "w") as fh:
        json.dump(dict(description="build log of code/make_zoo.py (timings vary between runs; everything else is deterministic)",
                       config=dict(families=FAMILIES, n_processes=N_PROC, blas_threads_per_process=1,
                                   split_seed_rule="np.random.default_rng(10000 + split_seed)",
                                   init_seed_rule="np.random.default_rng(init_seed)", lin_weights=list(core.LIN_W),
                                   jobs=[{k: v for k, v in j.items()} for j in jobs]),
                       numpy_version=np.__version__, n_models=len(models), n_runs=len(runs),
                       train_seconds_per_run=timing, cpu_seconds_training=round(sum(timing.values()), 1),
                       runtime_seconds=round(total, 1)), fh, indent=1)
    print(f"saved {len(models)} models from {len(runs)} runs; total time {total:.1f}s")


def save_npz(path, **arrays):
    """Compressed .npz with fixed zip timestamps, so identical arrays give byte-identical files."""
    import io
    import zipfile
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as zf:
        for name, arr in arrays.items():
            buf = io.BytesIO()
            np.lib.format.write_array(buf, np.ascontiguousarray(arr), allow_pickle=False)
            zi = zipfile.ZipInfo(name + ".npy", date_time=(1980, 1, 1, 0, 0, 0))
            zi.compress_type = zipfile.ZIP_DEFLATED
            zi.external_attr = 0o644 << 16
            zf.writestr(zi, buf.getvalue())


def _indexed(arg):
    i, job = arg
    return i, train_run(job)


if __name__ == "__main__":
    main()

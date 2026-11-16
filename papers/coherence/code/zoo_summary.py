"""zoo_summary.py -- coverage summary of the model zoo.

    python3 code/zoo_summary.py        # writes results/zoo_summary.json

For every family (and every family x p x train_frac cell): number of models, distribution of the
error rate eps over ALL inputs, counts in eps bins of width 0.1, and how many models are exactly
correct.  Also reports lambda = 1 - eps/(1 - 1/q) and delayed-generalisation statistics per run.
Deterministic (no randomness); reads only zoo/index.json.
"""
import json
import os
import time

import numpy as np

import core

EDGES = [round(0.1 * i, 1) for i in range(11)]


def eps_bins(eps):
    """Counts in [0,0.1), [0.1,0.2), ..., [0.9,1.0] (last bin closed).  eps == 0 is also counted separately."""
    eps = np.asarray(eps, dtype=float)
    idx = np.minimum((eps * 10 + 1e-9).astype(int), 9)
    cnt = np.bincount(idx, minlength=10)
    return {f"[{EDGES[i]:.1f},{EDGES[i + 1]:.1f}{']' if i == 9 else ')'}": int(cnt[i]) for i in range(10)}


def describe(recs):
    eps = np.array([r["eps"] for r in recs])
    q = np.array([r["q"] for r in recs])
    lam = core.lam(eps, q)
    qs = [0, 5, 25, 50, 75, 95, 100]
    return dict(
        n_models=len(recs), n_runs=len({r["run_id"] for r in recs}),
        n_exact=int((eps == 0).sum()), n_with_errors=int((eps > 0).sum()),
        n_final=int(sum(r["final"] for r in recs)),
        eps_min=float(eps.min()), eps_max=float(eps.max()), eps_mean=float(eps.mean()),
        eps_percentiles={str(k): float(np.percentile(eps, k)) for k in qs},
        eps_min_nonzero=float(eps[eps > 0].min()) if (eps > 0).any() else None,
        lam_min=float(lam.min()), lam_max=float(lam.max()),
        eps_bins_width_0p1=eps_bins(eps),
        eps_bins_width_0p1_models_with_errors_only=eps_bins(eps[eps > 0]),
        final_eps=sorted(float(r["eps"]) for r in recs if r["final"]),
    )


def main():
    t0 = time.time()
    full = core.load_index(full=True)
    recs = full["models"]
    out = dict(
        description="coverage of the model zoo (zoo/index.json): eps = error rate over ALL inputs of the group",
        config=dict(bin_edges=EDGES, source="zoo/index.json", n_models=len(recs), n_runs=full["n_runs"],
                    families=full["families"], seeds="see results/zoo_build.json (config.jobs)"),
        all=describe(recs), by_family={}, by_cell={}, runs={},
    )
    for fam in sorted({r["family"] for r in recs}):
        R = [r for r in recs if r["family"] == fam]
        out["by_family"][fam] = describe(R)
        cells = sorted({(r["p"], r["holdout"], r["train_frac"]) for r in R})
        for p, holdout, frac in cells:
            C = [r for r in R if (r["p"], r["holdout"], r["train_frac"]) == (p, holdout, frac)]
            out["by_cell"][f"{fam}|p={p}|{holdout}|train_frac={frac}"] = describe(C)
    # per-run trajectory facts (delayed generalisation): first snapshot with train_acc = 1 and with eps < 0.01
    for run in full["runs"]:
        R = sorted([r for r in recs if r["run_id"] == run["run_id"]], key=lambda r: r["step"])
        fit = next((r["step"] for r in R if r["train_acc"] == 1.0), None)
        gen = next((r["step"] for r in R if r["eps"] < 0.01), None)
        out["runs"][run["run_id"]] = dict(
            family=run["family"], p=R[0]["p"], train_frac=R[0]["train_frac"], holdout=R[0]["holdout"],
            split_seed=R[0]["split_seed"], init_seed=R[0]["init_seed"], n_snapshots=len(R),
            first_snapshot_step_train_acc_1=fit, first_snapshot_step_eps_below_0p01=gen,
            final_step=R[-1]["step"], final_train_acc=R[-1]["train_acc"], final_heldout_acc=R[-1]["heldout_acc"],
            final_eps=R[-1]["eps"], eps_trajectory=[round(r["eps"], 6) for r in R])
    grok = [v for v in out["runs"].values() if v["family"] in ("add/grok", "mul")]
    both = [v for v in grok if v["first_snapshot_step_train_acc_1"] is not None and v["first_snapshot_step_eps_below_0p01"] is not None]
    out["delayed_generalisation"] = dict(
        note="add/grok and mul runs; steps are snapshot steps (log-spaced), so ratios are resolved to ~24%",
        n_runs=len(grok), n_runs_reaching_train_acc_1=sum(v["first_snapshot_step_train_acc_1"] is not None for v in grok),
        n_runs_reaching_eps_below_0p01=sum(v["first_snapshot_step_eps_below_0p01"] is not None for v in grok),
        median_ratio_generalise_step_over_fit_step=float(np.median(
            [v["first_snapshot_step_eps_below_0p01"] / v["first_snapshot_step_train_acc_1"] for v in both])) if both else None,
        min_ratio=float(min(v["first_snapshot_step_eps_below_0p01"] / v["first_snapshot_step_train_acc_1"] for v in both)) if both else None,
        max_ratio=float(max(v["first_snapshot_step_eps_below_0p01"] / v["first_snapshot_step_train_acc_1"] for v in both)) if both else None)
    out["runtime_seconds"] = round(time.time() - t0, 3)
    os.makedirs(core.RESULTS_DIR, exist_ok=True)
    path = os.path.join(core.RESULTS_DIR, "zoo_summary.json")
    with open(path, "w") as fh:
        json.dump(out, fh, indent=1)
    print(f"{len(recs)} models, {full['n_runs']} runs")
    print(f"{'family':10s} {'models':>6s} {'runs':>5s} {'exact':>6s}  eps: min / median / max    bins of width 0.1 (0.0-0.1 ... 0.9-1.0)")
    for fam, d in out["by_family"].items():
        print(f"{fam:10s} {d['n_models']:6d} {d['n_runs']:5d} {d['n_exact']:6d}  {d['eps_min']:.4f} / {d['eps_percentiles']['50']:.4f} / {d['eps_max']:.4f}"
              f"    {list(d['eps_bins_width_0p1'].values())}")
    dg = out["delayed_generalisation"]
    print(f"delayed generalisation (add/grok + mul): {dg['n_runs_reaching_eps_below_0p01']} of {dg['n_runs']} runs reach eps < 0.01; "
          f"median (generalise step)/(fit step) = {dg['median_ratio_generalise_step_over_fit_step']}")
    print(f"wrote {path}")


if __name__ == "__main__":
    main()

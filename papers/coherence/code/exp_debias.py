#!/usr/bin/env python3
"""exp_debias.py -- bias-subtracted voting: subtract the label-free output-collision background from the
BLR vote histogram before taking the plurality.

Run (from anywhere; one process, deterministic, about 8 minutes on one core):

    OMP_NUM_THREADS=1 python3 code/exp_debias.py
    python3 code/exp_debias.py --figs-only        # redraw figures/fig_debias from the JSON

Writes  results/exp_debias.json   and   figures/fig_debias.svg / .png

THE RULE
--------
Let mu_c be the fraction of inputs on which the network answers c (label-free: only outputs are needed).
If the two outputs M(x+r), M(r) queried by one BLR vote were independent draws from mu, the vote would take
the value v with probability A(v) = sum_c mu_c mu_{c+v}.  With N_v the number of the k votes equal to v,
the plain corrector answers argmax_v N_v; the BIAS-SUBTRACTED corrector answers argmax_v [N_v / k - A(v)].
A tie for first place is a failure for both rules (as everywhere in the paper).  In channel terms
(T_x(h) = Pr_r[vote - f(x) = h]) input x is
    plain-correctable   iff  T_x(0) > max_{h != 0} T_x(h)
    debias-correctable  iff  T_x(0) - A(f(x)) > max_{h != 0} [T_x(h) - A(f(x) + h)].
For multiplication (4-query bilinear vote M(x+r,y+s) - M(r,y+s) - M(x+r,s) + M(r,s)) the background is the
law of o1 - o2 - o3 + o4 for four independent draws from mu, i.e. the cyclic self-convolution A * A.
All decisions are made in exact integer arithmetic: T = counts / |G|, A = collision counts / |G|^2 (or n^2
when mu is estimated from n sampled inputs; n(n-1) for the unbiased pair estimator).

At k votes the rule changes the plurality only through integer threshold shifts:
    success  iff  N_h <= N_0 - 1 + delta_x(h)   for every h != 0,   delta_x(h) = ceil(k [A(f(x)+h) - A(f(x))]).
delta >= 0 can only help; harm at input x needs some delta_x(h) < 0, i.e. k [A(f(x)) - A(f(x)+h)] >= 1.

SECTIONS (keys of the JSON)
  checks  reproduction of results/exp_channels.json (plain criterion, every add/grok, add/memo, lin model),
          results/exp_tasks.json (mul), theory_checks C4 synthetic fields and C3 finite-size i.i.d. thresholds;
          the exact threshold recursion against brute-force enumeration and against core.plurality_fail_exact.
  probe_reproduction  the lead's pilot numbers recomputed with the pilot's conventions (x != 0, eps > 0 only).
  D1  exact asymptotic criterion for every model, by family and eps bin; per-run eps_all / eps_some.
  D2  finite k for six representatives: exact (generating-function recursion with per-input thresholds),
      Monte Carlo from the exact channel (paired: both rules on the same vote-count samples), Chernoff bounds,
      and real votes on the table (core.sc_votes).
  D3  mu estimated from n in {100, 1000} uniformly sampled unlabeled inputs (with replacement).
  D4  where it does not work: lin statistics, synthetic families of theory_checks C4, a constructed harm case.
  D5  thresholds against the i.i.d. finite-size limit (the same grid procedure as theory_checks C3, both rules).

SEEDS: Monte Carlo np.random.default_rng([61000, rep, k]); real votes [62000, rep, k]; mu estimates for the
representatives [63000, rep, n]; mu estimates for all add/grok models [64000, zoo_index]; candidate-worst
re-estimate [65000, rep, k]; synthetic fields 400..407 (theory_checks C4); i.i.d. fields 7000 + 100 p + s,
s < 24 (theory_checks C3).
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import sys
import json
import math
import time
import itertools

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import core  # noqa: E402

OUT_JSON = os.path.join(core.RESULTS_DIR, "exp_debias.json")
FIG_PATH = os.path.join(core.FIG_DIR, "fig_debias")
FAMILIES = ("add/grok", "add/memo", "lin", "mul")
KS = (3, 9, 17, 33, 65, 129)
K_EXACT_ALL = 65            # exact failure on ALL inputs for k <= 65 (all k when |G| <= 600)
K_REAL = (9, 33)            # real-vote cross-check
R_REAL = 100                # real-vote trials per input
N_MC = 1000                 # Monte Carlo vote-count samples per input (|G| > 600)
N_MC_SMALL = 4000           # same for |G| <= 600
N_MC_WORST = 20000          # re-estimate of the exact-worst input
N_EST = (100, 1000)
D_REP = 200                 # mu-estimate draws per representative
D_ALL = 20                  # mu-estimate draws per add/grok model
ACC_FLOOR = 1e-10           # exact failures below this are at the accuracy floor of the recursion
SEED_MC, SEED_REAL, SEED_EST_REP, SEED_EST_ALL, SEED_WORST = 61000, 62000, 63000, 64000, 65000
SYN_P, SYN_SEEDS = 31, tuple(range(400, 408))
IID_PS, IID_NSEEDS = (23, 31, 47), 24
REP_TARGETS = (0.1, 0.3, 0.5, 0.65, 0.75)
REP_EXTRA = "addgrok_p23_f0.5_ss1_is1_t00036"
EPS_BINS = [(round(0.1 * i, 1), round(0.1 * i + 0.1, 1)) for i in range(10)]


# ----------------------------------------------------------------------------------------------
# small helpers
# ----------------------------------------------------------------------------------------------
def summ(v):
    v = [float(x) for x in v if x is not None and not (isinstance(x, float) and math.isnan(x))]
    if not v:
        return {"n": 0}
    a = np.array(v)
    return {"n": len(v), "median": float(np.median(a)), "min": float(a.min()), "max": float(a.max()),
            "mean": float(a.mean()), "q25": float(np.quantile(a, 0.25)), "q75": float(np.quantile(a, 0.75))}


def jsonable(o):
    if isinstance(o, dict):
        return {str(k): jsonable(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [jsonable(v) for v in o]
    if isinstance(o, np.ndarray):
        return [jsonable(v) for v in o.tolist()]
    if isinstance(o, (np.bool_,)):
        return bool(o)
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.floating, float)):
        f = float(o)
        return None if (math.isnan(f) or math.isinf(f)) else f
    return o


def bg_counts(nc, unbiased=False):
    """Integer background counts a[v] = sum_c n_c n_{c+v} (plug-in, denominator n^2); unbiased=True drops the
    self-pairs (a[0] -= n, denominator n(n-1)).  Returns (a, den)."""
    nc = np.asarray(nc, dtype=np.int64)
    q = len(nc)
    a = np.array([int(np.dot(nc, np.roll(nc, -v))) for v in range(q)], dtype=np.int64)
    n = int(nc.sum())
    if unbiased:
        a[0] -= n
        return a, n * (n - 1)
    return a, n * n


def bg4_counts(a, den):
    """Background of o1 - o2 - o3 + o4 = (o1 - o2) + (o4 - o3): cyclic self-convolution of a."""
    q = len(a)
    a4 = np.array([int(np.dot(a, a[(v - np.arange(q)) % q])) for v in range(q)], dtype=np.int64)
    return a4, den * den


def offsets_bg(a, fx):
    """B[x, h] = a[(f(x) + h) mod q]: background count of the vote VALUE f(x) + h (offset h from the truth)."""
    q = len(a)
    return a[(np.asarray(fx)[:, None] + np.arange(q)[None, :]) % q]


def criteria(C, dT, fx, a, dA):
    """Exact asymptotic criteria.  C: (X, q) integer vote counts (rows sum to dT, column 0 = truth);
    a, dA: integer background counts / denominator.  Returns dict of per-input arrays."""
    C = np.asarray(C, dtype=np.int64)
    B = offsets_bg(a, fx)
    S = C * dA - B * dT                               # scaled debiased score; exact integers
    cmax = C[:, 1:].max(1)
    smax = S[:, 1:].max(1)
    return {"plain_ok": C[:, 0] > cmax, "deb_ok": S[:, 0] > smax,
            "plain_margin": (C[:, 0] - cmax) / float(dT), "deb_margin": (S[:, 0] - smax) / float(dT) / float(dA),
            "hstar_plain": 1 + C[:, 1:].argmax(1), "hstar_deb": 1 + S[:, 1:].argmax(1), "B": B}


def deb_ok_only(C, dT, fx, a, dA):
    C = np.asarray(C, dtype=np.int64)
    S = C * dA - offsets_bg(a, fx) * dT
    return S[:, 0] > S[:, 1:].max(1)


def run_thresholds(rows):
    """rows: list of (eps, all_ok) for the snapshots of one run -> (eps_all, eps_some)."""
    ok = [e for e, o in rows if o]
    bad = [e for e, o in rows if not o]
    return (max(ok) if ok else None), (min(bad) if bad else None)


def cmp_some(a, b):
    """-1 / 0 / +1 for eps_some lowered / unchanged / raised; None = no snapshot with an uncorrectable input (highest)."""
    a = math.inf if a is None else a
    b = math.inf if b is None else b
    return 0 if a == b else (1 if b > a else -1)


def cmp_none(a, b):
    """-1 / 0 / +1 for b worse / equal / better than a, None meaning 'no fully correctable snapshot' (lowest)."""
    if a is None and b is None:
        return 0
    if a is None:
        return 1
    if b is None:
        return -1
    return int(np.sign(round(b - a, 12)))


# ----------------------------------------------------------------------------------------------
# finite-k machinery
# ----------------------------------------------------------------------------------------------
def deltas(B, dA, k):
    """delta[x, h] = ceil(k (B[x,h] - B[x,0]) / dA), exact integer arithmetic."""
    num = int(k) * (B - B[:, :1])
    return -((-num) // dA)


def fail_exact_thresh(T, delta, k):
    """Exact 1 - Pr[N_h <= N_0 - 1 + delta[x,h] for every h != 0], N ~ Multinomial(k, T_x), every row.
    delta = 0 is the plain plurality (tie = failure).  Generating function in the style of
    core.plurality_fail_exact with per-row, per-value upper limits:
      Pr[N_0 = m, N_h <= J_h] = (k!/m!) T_0^m [z^(k-m)] prod_h sum_{j <= J_h} (T_h z)^j / j!.
    Sums of non-negative terms only; absolute accuracy of the failure about 1e-12."""
    T = np.atleast_2d(np.asarray(T, dtype=float))
    delta = np.atleast_2d(np.asarray(delta, dtype=np.int64))
    k = int(k)
    X, q = T.shape
    t0 = T[:, 0]
    lg = [math.lgamma(i + 1.0) for i in range(k + 1)]
    nz = [h for h in range(1, q) if T[:, h].any()]
    zc = [h for h in range(1, q) if not T[:, h].any()]
    success = np.zeros(X)
    for m in range(0, k + 1):
        d = k - m
        poly = np.zeros((X, d + 1))
        poly[:, 0] = 1.0
        alive = np.ones(X, dtype=bool)
        for h in zc:
            alive &= (m - 1 + delta[:, h]) >= 0
        for h in nz:
            jm = np.minimum(m - 1 + delta[:, h], d)
            alive &= jm >= 0
            J = int(jm.max())
            if J <= 0:
                continue
            th = T[:, h]
            new = poly.copy()
            c = np.ones(X)
            for j in range(1, J + 1):
                c = c * th / j
                cj = np.where(jm >= j, c, 0.0)
                new[:, j:] += poly[:, :d + 1 - j] * cj[:, None]
            poly = new
        if m == 0:
            w = np.full(X, math.exp(lg[k]))
        else:
            with np.errstate(divide="ignore"):
                w = np.where(t0 > 0, np.exp(lg[k] - lg[m] + m * np.log(np.where(t0 > 0, t0, 1.0))), 0.0)
        success += np.where(alive, w * poly[:, d], 0.0)
    return np.clip(1.0 - success, 0.0, 1.0)


def fail_enum_thresh(t, delta, k):
    """Brute force over all q^k vote strings (tiny cases; reference for fail_exact_thresh)."""
    q = len(t)
    ok = 0.0
    for votes in itertools.product(range(q), repeat=k):
        cnt = np.bincount(votes, minlength=q)
        if all(cnt[h] <= cnt[0] - 1 + delta[h] for h in range(1, q)):
            ok += float(np.prod(t[list(votes)]))
    return 1.0 - ok


def chernoff_thresh(T, beta, ks):
    """Upper bound on Pr[exists h != 0 : N_h - N_0 >= k beta_h] (ties included) for every row:
    sum_h min_{s >= 0} [e^{-s beta_h} (T_h e^s + T_0 e^{-s} + 1 - T_0 - T_h)]^k, clipped at 1.
    beta = 0 reproduces core.chernoff_union_bound.  The minimum over s is found by golden-section search
    on [0, 40] (the objective is convex); any s gives a valid bound.  Returns (len(ks), X)."""
    T = np.atleast_2d(np.asarray(T, dtype=float))
    t0 = T[:, :1]
    th = T[:, 1:]
    b = np.asarray(beta, dtype=float)[:, 1:]
    R = np.clip(1.0 - t0 - th, 0.0, None)

    def g(s):
        return -s * b + np.log(th * np.exp(s) + t0 * np.exp(-s) + R)
    lo = np.zeros_like(th)
    hi = np.full_like(th, 40.0)
    gr = (math.sqrt(5) - 1) / 2
    for _ in range(100):
        c1 = hi - gr * (hi - lo)
        c2 = lo + gr * (hi - lo)
        left = g(c1) < g(c2)
        hi = np.where(left, c2, hi)
        lo = np.where(left, lo, c1)
    gmin = np.minimum(0.0, g(0.5 * (lo + hi)))
    base = np.exp(gmin)
    return np.stack([np.minimum(1.0, (base ** int(kk)).sum(1)) for kk in ks])


def mc_pair(T, B, dA, k, n, rng, chunk=3_000_000):
    """Paired Monte Carlo from the exact channel: n draws of N ~ Multinomial(k, T_x) per input, both rules
    applied to the same draw.  Returns per-input failure fractions (plain, deb) and discordance counts."""
    T = np.atleast_2d(np.asarray(T, dtype=float))
    X, q = T.shape
    P = T / T.sum(1, keepdims=True)
    per = max(1, int(chunk // max(1, X * q)))
    fp = np.zeros(X, dtype=np.int64)
    fd = np.zeros(X, dtype=np.int64)
    n_pd = np.zeros(X, dtype=np.int64)          # plain fails, deb succeeds
    n_dp = np.zeros(X, dtype=np.int64)          # deb fails, plain succeeds
    Bk = (B * int(k)).astype(np.int64)
    done = 0
    while done < n:
        s = min(per, n - done)
        cnt = rng.multinomial(int(k), P, size=(s, X)).astype(np.int64)
        a = cnt[..., 0] <= cnt[..., 1:].max(-1)
        S = cnt * dA - Bk[None]
        b = S[..., 0] <= S[..., 1:].max(-1)
        fp += a.sum(0)
        fd += b.sum(0)
        n_pd += (a & ~b).sum(0)
        n_dp += (b & ~a).sum(0)
        done += s
    return fp / float(n), fd / float(n), n_pd, n_dp


def mean_se(d, n):
    d = np.asarray(d, dtype=float)
    return float(math.sqrt(float((d * (1 - d)).sum()) / n) / len(d))


def real_votes_pair(M, fx_all, xs, k, rng, q, a, dA, R, chunk_rows=60000):
    """Real BLR votes on the table (core.sc_votes), both rules on the same votes.  Returns per-input failure
    fractions (plain, deb) over R trials."""
    fp = np.zeros(len(xs))
    fd = np.zeros(len(xs))
    xs_rep = np.repeat(np.asarray(xs), R)
    pos_rep = np.repeat(np.arange(len(xs)), R)
    for lo in range(0, len(xs_rep), chunk_rows):
        xr = xs_rep[lo:lo + chunk_rows]
        pr = pos_rep[lo:lo + chunk_rows]
        votes = core.sc_votes(M, xr, k, rng, q)
        m = len(xr)
        cnt = np.bincount((votes + q * np.arange(m)[:, None]).ravel(), minlength=m * q).reshape(m, q).astype(np.int64)
        truth = fx_all[xr]
        top = cnt.max(1)
        fail_p = (cnt.argmax(1) != truth) | ((cnt == top[:, None]).sum(1) > 1)
        S = cnt * dA - a[None, :] * int(k)
        topS = S.max(1)
        fail_d = (S.argmax(1) != truth) | ((S == topS[:, None]).sum(1) > 1)
        np.add.at(fp, pr, fail_p)
        np.add.at(fd, pr, fail_d)
    return fp / R, fd / R


# ----------------------------------------------------------------------------------------------
# self-checks
# ----------------------------------------------------------------------------------------------
def selfchecks():
    rng = np.random.default_rng(66000)
    mx = 0.0
    n = 0
    for trial in range(60):
        q = int(rng.integers(2, 5))
        k = int(rng.integers(1, 7))
        t = rng.dirichlet(np.ones(q))
        if trial % 3 == 0:
            t[int(rng.integers(1, q))] = 0.0
            t /= t.sum()
        dl = rng.integers(-2, 3, size=q)
        mx = max(mx, abs(fail_exact_thresh(t[None], dl[None], k)[0] - fail_enum_thresh(t, dl, k)))
        n += 1
    E = core.error_table("addgrok_p23_f0.5_ss1_is1_t00036")
    T = core.twirled_channel(E, 23)
    dcore = max(float(np.abs(fail_exact_thresh(T, np.zeros(T.shape, np.int64), k) - core.plurality_fail_exact(T, k)).max())
                for k in (3, 9, 17))
    ch = chernoff_thresh(T, np.zeros(T.shape), [9, 33])
    dch = float(np.abs(ch - core.chernoff_union_bound(T, np.array([9, 33]))).max())
    return {"exact_threshold_recursion_vs_bruteforce_max_abs_diff": mx, "n_random_cases": n,
            "exact_threshold_recursion_delta0_vs_core_plurality_fail_exact_max_abs_diff": dcore,
            "chernoff_beta0_vs_core_chernoff_union_bound_max_abs_diff": dch,
            "passed": bool(mx < 1e-12 and dcore < 1e-12 and dch < 1e-9)}


# ----------------------------------------------------------------------------------------------
# D1 (+ D3 for every add/grok model): per-model pass
# ----------------------------------------------------------------------------------------------
def pick_representatives(idx):
    grok = [r for r in idx if r["family"] == "add/grok" and r["p"] == 47]
    reps = []
    for t in REP_TARGETS:
        s0 = [r for r in grok if r["split_seed"] == 0 and r["init_seed"] == 0]
        best = min(s0, key=lambda r: (abs(r["eps"] - t), r["train_frac"], r["step"]))
        seed0 = abs(best["eps"] - t) <= 0.03
        if not seed0:
            best = min(grok, key=lambda r: (abs(r["eps"] - t), r["train_frac"], r["step"], r["id"]))
        reps.append({"id": best["id"], "target_eps": t, "eps": best["eps"], "seed0": seed0})
    r = core.get_record(REP_EXTRA)
    reps.append({"id": REP_EXTRA, "target_eps": None, "eps": r["eps"], "seed0": False,
                 "why": "lowest-eps add/grok snapshot with an uncorrectable input (results/exp_channels.json A5)"})
    return reps


def per_model_pass(idx, rep_ids, log):
    cols = {k: [] for k in (
        "id", "zoo_index", "family", "p", "q", "run_id", "step", "train_frac", "split_seed", "init_seed", "eps",
        "n_inputs", "n_nontrivial", "plain_frac", "deb_frac", "plain_frac_nontrivial", "deb_frac_nontrivial",
        "plain_all", "deb_all", "n_harmed", "n_helped", "plain_min_margin", "deb_min_margin",
        "out_collision_times_q", "bg_zero_minus_min_times_q", "bg_max_minus_min",
        "n_unc_plain_nonzero_f", "frac_unc_plain_hstar_zero_vote", "frac_unc_deb_hstar_zero_vote",
        "unc_plain_deficit_median", "unc_plain_correction_median", "frac_unc_plain_correction_gt_deficit",
        "est100_frac_mean", "est100_n_all_ok", "est100_n_draws_worse_than_plain",
        "est1000_frac_mean", "est1000_n_all_ok", "est1000_n_draws_worse_than_plain")}
    est_all = {}           # id -> {n: list of (frac, all_ok)}
    keep = {}
    p_cache = {}
    t0 = time.time()
    for zi, r in enumerate(idx):
        fam = r["family"]
        if fam not in FAMILIES:
            continue
        q = int(r["q"])
        M = core.load_table(r["id"])
        f = core.model_true_table(r["id"])
        E = core.make_error_table(M, f, q)
        fx = f.ravel() % q
        X = M.size
        if fam == "mul":
            C = core.bilinear_counts(E, q)
            p1 = M.shape[0]
            nontriv = ((np.arange(X) // p1) != 0) & ((np.arange(X) % p1) != 0)
            a2, d2 = bg_counts(np.bincount(M.ravel(), minlength=q))
            a, dA = bg4_counts(a2, d2)
        else:
            C = core.twirled_counts(E, q)
            nontriv = np.arange(X) != 0
            a, dA = bg_counts(np.bincount(M.ravel(), minlength=q))
        dT = X
        assert (C.sum(1) == dT).all()
        cr = criteria(C, dT, fx, a, dA)
        po, do = cr["plain_ok"], cr["deb_ok"]
        eps = float((E != 0).mean())
        assert abs(eps - r["eps"]) < 1e-12
        h0 = (-fx) % q                                     # offset of the 'zero vote' M(x+r) = M(r)
        uncp = ~po & (fx != 0)
        uncd = ~do & (fx != 0)
        B = cr["B"]
        hs = cr["hstar_plain"]
        rows = np.arange(X)
        deficit = (C[rows, hs] - C[:, 0]) / float(dT)
        correction = (B[rows, hs] - B[:, 0]) / float(dA)  # how much the rule moves the truth up vs h*
        A = a / float(dA)
        vals = dict(id=r["id"], zoo_index=zi, family=fam, p=r["p"], q=q, run_id=r["run_id"], step=r["step"],
                    train_frac=r["train_frac"], split_seed=r["split_seed"], init_seed=r["init_seed"], eps=eps,
                    n_inputs=X, n_nontrivial=int(nontriv.sum()),
                    plain_frac=float(po.mean()), deb_frac=float(do.mean()),
                    plain_frac_nontrivial=float(po[nontriv].mean()), deb_frac_nontrivial=float(do[nontriv].mean()),
                    plain_all=bool(po.all()), deb_all=bool(do.all()),
                    n_harmed=int((po & ~do).sum()), n_helped=int((do & ~po).sum()),
                    plain_min_margin=float(cr["plain_margin"].min()), deb_min_margin=float(cr["deb_margin"].min()),
                    out_collision_times_q=(float(a2[0] / d2 * q) if fam == "mul" else float(A[0] * q)),
                    bg_zero_minus_min_times_q=float((A[0] - A.min()) * q), bg_max_minus_min=float(A.max() - A.min()),
                    n_unc_plain_nonzero_f=int(uncp.sum()),
                    frac_unc_plain_hstar_zero_vote=(float((hs[uncp] == h0[uncp]).mean()) if uncp.any() else None),
                    frac_unc_deb_hstar_zero_vote=(float((cr["hstar_deb"][uncd] == h0[uncd]).mean()) if uncd.any() else None),
                    unc_plain_deficit_median=(float(np.median(deficit[uncp])) if uncp.any() else None),
                    unc_plain_correction_median=(float(np.median(correction[uncp])) if uncp.any() else None),
                    frac_unc_plain_correction_gt_deficit=(float((correction[uncp] > deficit[uncp]).mean()) if uncp.any() else None))
        # D3 for every add/grok model with errors: mu from n sampled inputs (plug-in), D_ALL draws
        if fam == "add/grok" and eps > 0:
            rng = np.random.default_rng([SEED_EST_ALL, zi])
            Mf = M.ravel()
            est_all[r["id"]] = {}
            for n in N_EST:
                fr, ok = [], []
                for _ in range(D_ALL):
                    smp = Mf[rng.integers(0, X, n)]
                    ae, de = bg_counts(np.bincount(smp, minlength=q))
                    o = deb_ok_only(C, dT, fx, ae, de)
                    fr.append(float(o.mean()))
                    ok.append(bool(o.all()))
                est_all[r["id"]][n] = (fr, ok)
                vals[f"est{n}_frac_mean"] = float(np.mean(fr))
                vals[f"est{n}_n_all_ok"] = int(sum(ok))
                vals[f"est{n}_n_draws_worse_than_plain"] = int(sum(v < vals["plain_frac"] - 1e-15 for v in fr))
        else:
            for n in N_EST:
                vals[f"est{n}_frac_mean"] = None
                vals[f"est{n}_n_all_ok"] = None
                vals[f"est{n}_n_draws_worse_than_plain"] = None
        for kk in cols:
            cols[kk].append(vals[kk])
        if r["id"] in rep_ids:
            keep[r["id"]] = {"C": C, "a": a, "dA": dA, "fx": fx, "M": M, "q": q, "po": po, "do": do,
                             "plain_margin": cr["plain_margin"], "deb_margin": cr["deb_margin"]}
        if len(cols["id"]) % 200 == 0:
            log(f"  per-model pass: {len(cols['id'])} models ({time.time() - t0:.0f} s)")
    return cols, est_all, keep


def section_d1(cols, iid_refs, iid_mins):
    fam = np.array(cols["family"])
    eps = np.array(cols["eps"], dtype=float)
    pp = np.array(cols["p"])
    pf, df = np.array(cols["plain_frac"]), np.array(cols["deb_frac"])
    pfn, dfn = np.array(cols["plain_frac_nontrivial"]), np.array(cols["deb_frac_nontrivial"])
    pa, da = np.array(cols["plain_all"], dtype=bool), np.array(cols["deb_all"], dtype=bool)
    harm, helped = np.array(cols["n_harmed"]), np.array(cols["n_helped"])
    ids = np.array(cols["id"])
    out = {"definition": ("frac = fraction of ALL inputs of G that are correctable (exp_channels convention; x = 0 and, "
                          "for mul, the 61 inputs with a = 0 or b = 0 are trivially correctable under both rules); "
                          "frac_nontrivial excludes them (exp_tasks convention for mul, the pilot's convention for "
                          "add/lin).  eps bins [lo, hi) of width 0.1 over models with eps > 0 (last bin closed).  "
                          "harmed input = plain-correctable but not debias-correctable; helped = the reverse."),
           "families": {}}
    for f in FAMILIES:
        m = (fam == f) & (eps > 0)
        c = {"n_models_eps_gt_0": int(m.sum()), "n_runs": len(set(np.array(cols["run_id"])[m])),
             "n_fully_correctable_plain": int((m & pa).sum()), "n_fully_correctable_deb": int((m & da).sum()),
             "mean_frac_plain": float(pf[m].mean()), "mean_frac_deb": float(df[m].mean()),
             "n_models_deb_frac_higher": int((m & (df > pf)).sum()), "n_models_deb_frac_lower": int((m & (df < pf)).sum()),
             "n_models_deb_frac_equal": int((m & (df == pf)).sum()),
             "n_models_with_harmed_input": int((m & (harm > 0)).sum()), "n_inputs_harmed_total": int(harm[m].sum()),
             "n_inputs_helped_total": int(helped[m].sum()),
             "n_models_full_plain_not_full_deb": int((m & pa & ~da).sum()),
             "n_models_full_deb_not_full_plain": int((m & da & ~pa).sum()),
             "models_with_harmed_input": [{"id": str(ids[i]), "eps": float(eps[i]), "n_harmed": int(harm[i]),
                                           "n_helped": int(helped[i]), "plain_frac": float(pf[i]), "deb_frac": float(df[i]),
                                           "plain_all": bool(pa[i]), "deb_all": bool(da[i])}
                                          for i in np.flatnonzero(m & (harm > 0))],
             "by_eps_bin": []}
        for lo, hi in EPS_BINS:
            b = m & (eps >= lo) & ((eps < hi) if hi < 1.0 else (eps <= hi))
            if not b.any():
                continue
            c["by_eps_bin"].append({
                "eps_bin": [lo, hi], "n_models": int(b.sum()), "n_runs": len(set(np.array(cols["run_id"])[b])),
                "mean_frac_plain": float(pf[b].mean()), "mean_frac_deb": float(df[b].mean()),
                "median_frac_plain": float(np.median(pf[b])), "median_frac_deb": float(np.median(df[b])),
                "mean_frac_nontrivial_plain": float(pfn[b].mean()), "mean_frac_nontrivial_deb": float(dfn[b].mean()),
                "n_fully_correctable_plain": int((b & pa).sum()), "n_fully_correctable_deb": int((b & da).sum()),
                "n_models_deb_frac_lower": int((b & (df < pf)).sum()), "n_inputs_harmed": int(harm[b].sum())})
        out["families"][f] = c
    # per-p cells for add/grok
    for P in (23, 31, 47):
        m = (fam == "add/grok") & (eps > 0) & (pp == P)
        out["families"][f"add/grok|p={P}"] = {
            "n_models_eps_gt_0": int(m.sum()), "n_fully_correctable_plain": int((m & pa).sum()),
            "n_fully_correctable_deb": int((m & da).sum()), "mean_frac_plain": float(pf[m].mean()),
            "mean_frac_deb": float(df[m].mean()), "n_models_with_harmed_input": int((m & (harm > 0)).sum())}
    # per-run thresholds
    runs = {}
    for i, rid in enumerate(cols["run_id"]):
        runs.setdefault(rid, []).append(i)
    rr = {}
    for rid, ii in sorted(runs.items()):
        ea_p, es_p = run_thresholds([(eps[i], pa[i]) for i in ii])
        ea_d, es_d = run_thresholds([(eps[i], da[i]) for i in ii])
        rr[rid] = {"family": str(fam[ii[0]]), "p": int(pp[ii[0]]), "n_snapshots": len(ii),
                   "train_frac": cols["train_frac"][ii[0]], "eps_all_plain": ea_p, "eps_all_deb": ea_d,
                   "eps_some_plain": es_p, "eps_some_deb": es_d,
                   "eps_all_change": cmp_none(ea_p, ea_d),
                   "eps_some_change": cmp_some(es_p, es_d),
                   "eps_all_deb_id": (str(ids[ii][int(np.argmax([eps[i] if da[i] else -1 for i in ii]))]) if ea_d is not None else None)}
    out["runs"] = rr
    cells = {}
    keys = sorted(set(f"{v['family']}|p={v['p']}" for v in rr.values()))
    for key in keys:
        f0, p0 = key.split("|p=")
        p0 = int(p0)
        rs = [v for v in rr.values() if v["family"] == f0 and v["p"] == p0]
        iid = iid_refs.get(key)
        eap = [v["eps_all_plain"] for v in rs]
        ead = [v["eps_all_deb"] for v in rs]
        c = {"n_runs": len(rs), "iid_finite_size_median": iid,
             "eps_all_plain": summ(eap), "eps_all_deb": summ(ead),
             "eps_some_plain": summ([v["eps_some_plain"] for v in rs]), "eps_some_deb": summ([v["eps_some_deb"] for v in rs]),
             "n_runs_with_eps_all_plain": int(sum(v is not None for v in eap)),
             "n_runs_with_eps_all_deb": int(sum(v is not None for v in ead)),
             "n_runs_eps_all_improved": int(sum(v["eps_all_change"] > 0 for v in rs)),
             "n_runs_eps_all_unchanged": int(sum(v["eps_all_change"] == 0 for v in rs)),
             "n_runs_eps_all_worse": int(sum(v["eps_all_change"] < 0 for v in rs)),
             "n_runs_eps_some_raised": int(sum(v["eps_some_change"] > 0 for v in rs)),
             "n_runs_eps_some_unchanged": int(sum(v["eps_some_change"] == 0 for v in rs)),
             "n_runs_eps_some_lowered": int(sum(v["eps_some_change"] < 0 for v in rs)),
             "eps_all_increase_over_runs_with_both": summ([d - p for p, d in zip(eap, ead) if p is not None and d is not None])}
        if iid is not None:
            mfp = (fam == f0) & (pp == p0)
            c["iid_min_over_fields"] = iid_mins.get(key)
            c["n_runs_eps_some_plain_above_iid_median"] = int(sum(v["eps_some_plain"] is not None and v["eps_some_plain"] > iid for v in rs))
            c["n_runs_eps_some_deb_above_iid_median"] = int(sum(v["eps_some_deb"] is not None and v["eps_some_deb"] > iid for v in rs))
            c["n_runs_without_uncorrectable_snapshot_deb"] = int(sum(v["eps_some_deb"] is None for v in rs))
            c["n_models_full_plain_eps_ge_iid_median"] = int((mfp & pa & (eps >= iid)).sum())
            c["n_models_full_deb_eps_ge_iid_median"] = int((mfp & da & (eps >= iid)).sum())
            c["ids_full_deb_eps_ge_iid_median"] = [str(x) for x in ids[mfp & da & (eps >= iid)]]
            if iid_mins.get(key) is not None:
                c["n_models_full_deb_eps_ge_iid_min"] = int((mfp & da & (eps >= iid_mins[key])).sum())
            c["n_runs_eps_all_deb_above_iid_median"] = int(sum(v is not None and v > iid for v in ead))
            c["n_runs_eps_all_plain_above_iid_median"] = int(sum(v is not None and v > iid for v in eap))
            both = [(p, d) for p, d in zip(eap, ead) if p is not None and d is not None]
            c["gap_closed_per_run"] = summ([(d - p) / (iid - p) for p, d in both])
            if c["eps_all_plain"]["n"] and c["eps_all_deb"]["n"]:
                mp, md = c["eps_all_plain"]["median"], c["eps_all_deb"]["median"]
                c["gap_closed_of_medians"] = (md - mp) / (iid - mp)
        if f0 == "add/memo":
            c["note"] = "add/memo runs have ONE snapshot each"
        cells[key] = c
    out["cells"] = cells
    # all add/grok runs together
    rs = [v for v in rr.values() if v["family"] == "add/grok"]
    out["add/grok_all_runs"] = {"n_runs": len(rs),
                                "n_improved": int(sum(v["eps_all_change"] > 0 for v in rs)),
                                "n_unchanged": int(sum(v["eps_all_change"] == 0 for v in rs)),
                                "n_worse": int(sum(v["eps_all_change"] < 0 for v in rs))}
    # what is left: competitor at debias-uncorrectable inputs
    fz = np.array([np.nan if v is None else v for v in cols["frac_unc_deb_hstar_zero_vote"]], dtype=float)
    fzp = np.array([np.nan if v is None else v for v in cols["frac_unc_plain_hstar_zero_vote"]], dtype=float)
    out["competitor_at_uncorrectable_inputs"] = {
        "definition": "share of uncorrectable inputs with f(x) != 0 whose strongest competitor (largest plain mass, "
                      "resp. largest debiased score) is the zero vote M(x+r) = M(r), offset -f(x); median over models",
        "by_family": {f: {"plain_median": (float(np.nanmedian(fzp[fam == f])) if np.isfinite(fzp[fam == f]).any() else None),
                          "deb_median": (float(np.nanmedian(fz[fam == f])) if np.isfinite(fz[fam == f]).any() else None),
                          "n_models_with_deb_uncorrectable": int(np.isfinite(fz[fam == f]).sum())} for f in FAMILIES}}
    return out


def probe_reproduction(cols):
    """The pilot's conventions: models with eps > 0 of add/grok, add/memo, lin; fractions over x != 0; per-run
    eps_all over the eps > 0 snapshots only."""
    fam = np.array(cols["family"])
    eps = np.array(cols["eps"], dtype=float)
    pa, da = np.array(cols["plain_all"], dtype=bool), np.array(cols["deb_all"], dtype=bool)
    pfn, dfn = np.array(cols["plain_frac_nontrivial"]), np.array(cols["deb_frac_nontrivial"])
    out = {"pilot_claims": {"add/grok fully correctable": "463 -> 521 of 841",
                            "mean frac correctable eps [0.7,0.8)": "0.405 -> 0.953",
                            "mean frac correctable eps [0.8,0.9)": "0.032 -> 0.492",
                            "eps_all medians": "0.527 -> 0.675 (p=23), 0.557 -> 0.686 (p=31), 0.620 -> 0.685 (p=47)",
                            "runs": "improved 28 of 36, worse in none"}}
    m = (fam == "add/grok") & (eps > 0)
    out["add/grok_fully_correctable"] = {"plain": int((m & pa).sum()), "deb": int((m & da).sum()), "n": int(m.sum())}
    for lo, hi in ((0.7, 0.8), (0.8, 0.9)):
        b = m & (eps >= lo) & (eps < hi)
        out[f"add/grok_mean_frac_x_ne_0_eps_{lo}_{hi}"] = {"plain": float(pfn[b].mean()), "deb": float(dfn[b].mean()),
                                                           "n_models": int(b.sum())}
    runs = {}
    for i in np.flatnonzero(m):
        runs.setdefault((cols["p"][i], cols["run_id"][i]), []).append(i)
    per_p = {}
    for (P, rid), ii in runs.items():
        ea_p = max([eps[i] for i in ii if pa[i]], default=None)
        ea_d = max([eps[i] for i in ii if da[i]], default=None)
        per_p.setdefault(P, []).append((ea_p, ea_d))
    imp = wor = 0
    for P in sorted(per_p):
        v = per_p[P]
        out[f"add/grok_p{P}_eps_all_median"] = {"plain": float(np.median([a for a, _ in v])),
                                                "deb": float(np.median([b for _, b in v]))}
        imp += sum(b > a for a, b in v)
        wor += sum(b < a for a, b in v)
    out["add/grok_runs_improved"] = int(imp)
    out["add/grok_runs_worse"] = int(wor)
    return out


# ----------------------------------------------------------------------------------------------
# D2: finite k
# ----------------------------------------------------------------------------------------------
def section_d2(reps, keep, log):
    out = {"selection_rule": ("add/grok p = 47: for each target eps in %s the snapshot with the smallest |eps - target| "
                              "among the runs with split_seed = init_seed = 0 (ties: lower train_frac, then earlier step); "
                              "if none lies within 0.03 of the target, the closest over all seeds (the rule of "
                              "exp_channels A4).  Plus %s." % (list(REP_TARGETS), REP_EXTRA)),
           "ks": list(KS),
           "definition": ("failure = the rule does not return f(x) uniquely (a tie for first place is a failure). "
                          "mean = mean over ALL inputs of G; worst = max over inputs.  exact = generating-function "
                          "recursion with per-input thresholds (all inputs for k <= %d, and for every k when "
                          "|G| <= 600; for p = 47 at k = 129 only on a candidate set: the 25 highest-failure inputs of "
                          "each rule at k = 65 and in the k = 129 Monte Carlo, plus the 25 smallest asymptotic margins "
                          "of each rule).  Exact values below %.0e are at the accuracy floor and flagged unreliable. "
                          "mc = paired Monte Carlo from the exact channel (both rules on the same multinomial vote "
                          "counts), %d samples per input (%d when |G| <= 600); se = standard error of the mean over "
                          "inputs; when no failure is observed, mc_upper95 = 3 / (samples x inputs).  chernoff = "
                          "union-of-Chernoff upper bound (rigorous).  real = actual votes on the table (core.sc_votes), "
                          "%d trials per input, both rules on the same votes; z against the exact mean.  "
                          "frac_inputs_delta_neg = share of inputs where some delta_x(h) < 0 (harm possible at this k); "
                          "frac_inputs_delta_pos = share where some delta_x(h) > 0 (help possible)."
                          % (K_EXACT_ALL, ACC_FLOOR, N_MC, N_MC_SMALL, R_REAL)),
           "models": []}
    for ri, rep in enumerate(reps):
        kp = keep[rep["id"]]
        C, a, dA, fx, M, q = kp["C"], kp["a"], kp["dA"], kp["fx"], kp["M"], kp["q"]
        X = C.shape[0]
        T = C / float(X)
        B = offsets_bg(a, fx)
        beta = (B - B[:, :1]) / float(dA)
        small = X <= 600
        n_mc = N_MC_SMALL if small else N_MC
        ch_p = chernoff_thresh(T, np.zeros_like(beta), KS)
        ch_d = chernoff_thresh(T, beta, KS)
        rows = []
        ex65 = {}
        for ki, k in enumerate(KS):
            dl = deltas(B, dA, k)
            row = {"k": k, "frac_inputs_delta_neg": float((dl[:, 1:] < 0).any(1).mean()),
                   "frac_inputs_delta_pos": float((dl[:, 1:] > 0).any(1).mean())}
            rng = np.random.default_rng([SEED_MC, ri, k])
            mp, md, npd, ndp = mc_pair(T, B, dA, k, n_mc, rng)
            diff = (ndp - npd) / float(n_mc)
            var = (ndp + npd) / float(n_mc) - diff ** 2
            row["mc"] = {"samples_per_input": n_mc,
                         "plain_mean": float(mp.mean()), "plain_se": mean_se(mp, n_mc),
                         "deb_mean": float(md.mean()), "deb_se": mean_se(md, n_mc),
                         "plain_upper95_if_zero": (3.0 / (n_mc * X) if mp.sum() == 0 else None),
                         "deb_upper95_if_zero": (3.0 / (n_mc * X) if md.sum() == 0 else None),
                         "deb_minus_plain_mean": float(diff.mean()),
                         "deb_minus_plain_se": float(math.sqrt(max(0.0, float(var.sum())) / n_mc) / X),
                         "n_inputs_deb_mc_higher": int((md > mp).sum()), "n_inputs_deb_mc_lower": int((md < mp).sum())}
            row["chernoff"] = {"plain_mean": float(ch_p[ki].mean()), "plain_worst": float(ch_p[ki].max()),
                               "deb_mean": float(ch_d[ki].mean()), "deb_worst": float(ch_d[ki].max())}
            if k <= K_EXACT_ALL or small:
                ep = fail_exact_thresh(T, np.zeros_like(dl), k)
                ed = fail_exact_thresh(T, dl, k)
                if k == 65:
                    ex65 = {"p": ep, "d": ed}
                wp, wd = int(ep.argmax()), int(ed.argmax())
                row["exact"] = {"scope": "all inputs",
                                "plain_mean": float(ep.mean()), "plain_worst": float(ep.max()), "plain_worst_input": wp,
                                "deb_mean": float(ed.mean()), "deb_worst": float(ed.max()), "deb_worst_input": wd,
                                "plain_mean_reliable": bool(ep.mean() >= ACC_FLOOR), "deb_mean_reliable": bool(ed.mean() >= ACC_FLOOR),
                                "plain_worst_reliable": bool(ep.max() >= ACC_FLOOR), "deb_worst_reliable": bool(ed.max() >= ACC_FLOOR),
                                "n_inputs_deb_worse": int((ed > ep + 1e-12).sum()),
                                "n_inputs_deb_better": int((ed < ep - 1e-12).sum()),
                                "max_per_input_increase": float((ed - ep).max()),
                                "max_per_input_decrease": float((ep - ed).max()),
                                "mean_of_increase_where_worse": (float((ed - ep)[ed > ep + 1e-12].mean()) if (ed > ep + 1e-12).any() else None)}
                ww = ed > ep + 1e-12
                if ww.any():
                    row["exact"]["where_deb_worse"] = {
                        "n_inputs": int(ww.sum()), "share_with_f_x_zero": float((fx[ww] == 0).mean()),
                        "n_inputs_with_f_x_zero_total": int((fx == 0).sum()),
                        "plain_fail_mean": float(ep[ww].mean()), "deb_fail_mean": float(ed[ww].mean()),
                        "plain_fail_max": float(ep[ww].max()), "deb_fail_max": float(ed[ww].max()),
                        "inputs_asymptotically_deb_correctable": int((kp["do"] & ww).sum())}
                row["mc"]["plain_z_vs_exact"] = (float((mp.mean() - ep.mean()) / mean_se(ep, n_mc)) if mean_se(ep, n_mc) > 0 else None)
                row["mc"]["deb_z_vs_exact"] = (float((md.mean() - ed.mean()) / mean_se(ed, n_mc)) if mean_se(ed, n_mc) > 0 else None)
                cand_p, cand_d = np.array([wp]), np.array([wd])
            else:
                cand = set()
                for v in (ex65.get("p"), ex65.get("d"), mp, md):
                    if v is not None:
                        cand.update(np.argsort(-v, kind="stable")[:25].tolist())
                for v in (kp["plain_margin"], kp["deb_margin"]):
                    cand.update(np.argsort(v, kind="stable")[:25].tolist())
                cand = np.array(sorted(cand))
                ep = fail_exact_thresh(T[cand], np.zeros((len(cand), q), np.int64), k)
                ed = fail_exact_thresh(T[cand], dl[cand], k)
                row["exact"] = {"scope": f"candidate set of {len(cand)} inputs",
                                "plain_worst": float(ep.max()), "plain_worst_input": int(cand[ep.argmax()]),
                                "deb_worst": float(ed.max()), "deb_worst_input": int(cand[ed.argmax()]),
                                "plain_worst_reliable": bool(ep.max() >= ACC_FLOOR), "deb_worst_reliable": bool(ed.max() >= ACC_FLOOR),
                                "n_candidates_deb_worse": int((ed > ep + 1e-12).sum())}
                cand_p, cand_d = np.array([cand[ep.argmax()]]), np.array([cand[ed.argmax()]])
            # independent MC re-estimate of the two exact-worst inputs
            rng = np.random.default_rng([SEED_WORST, ri, k])
            wp_i, wd_i = int(cand_p[0]), int(cand_d[0])
            a1, _, _, _ = mc_pair(T[[wp_i]], B[[wp_i]], dA, k, N_MC_WORST, rng)
            _, b1, _, _ = mc_pair(T[[wd_i]], B[[wd_i]], dA, k, N_MC_WORST, rng)
            row["worst_input_mc_reestimate"] = {"samples": N_MC_WORST,
                                                "plain": float(a1[0]), "plain_se": float(math.sqrt(a1[0] * (1 - a1[0]) / N_MC_WORST)),
                                                "deb": float(b1[0]), "deb_se": float(math.sqrt(b1[0] * (1 - b1[0]) / N_MC_WORST))}
            if k in K_REAL:
                rng = np.random.default_rng([SEED_REAL, ri, k])
                rp, rd = real_votes_pair(M, fx, np.arange(X), k, rng, q, a, dA, R_REAL)
                ex = row["exact"]
                sp_ex = math.sqrt(float((ep * (1 - ep)).sum()) / R_REAL) / X
                sd_ex = math.sqrt(float((ed * (1 - ed)).sum()) / R_REAL) / X
                row["real"] = {"trials_per_input": R_REAL, "plain_mean": float(rp.mean()), "deb_mean": float(rd.mean()),
                               "plain_z_vs_exact": (float((rp.mean() - ex["plain_mean"]) / sp_ex) if sp_ex > 0 else None),
                               "deb_z_vs_exact": (float((rd.mean() - ex["deb_mean"]) / sd_ex) if sd_ex > 0 else None),
                               "plain_se": sp_ex, "deb_se": sd_ex}
            rows.append(row)
            log(f"  D2 {rep['id']} k={k}: mc plain {row['mc']['plain_mean']:.3g} deb {row['mc']['deb_mean']:.3g}")
        def first_k_below(key, rule):
            for r_ in rows:
                v = r_["exact"].get(f"{rule}_{key}") if "exact" in r_ else None
                if v is None:
                    v = r_["mc"][f"{rule}_mean"] if key == "mean" else None
                if v is not None and v < rep["eps"]:
                    return r_["k"]
            return None
        out["models"].append({"id": rep["id"], "target_eps": rep["target_eps"], "eps": rep["eps"], "seed0": rep["seed0"],
                              "n_inputs": X, "q": q,
                              "asymptotic": {"plain_frac": float(kp["po"].mean()), "deb_frac": float(kp["do"].mean()),
                                             "plain_all": bool(kp["po"].all()), "deb_all": bool(kp["do"].all()),
                                             "plain_min_margin": float(kp["plain_margin"].min()),
                                             "deb_min_margin": float(kp["deb_margin"].min()),
                                             "n_harmed": int((kp["po"] & ~kp["do"]).sum()),
                                             "n_helped": int((kp["do"] & ~kp["po"]).sum())},
                              "smallest_k_mean_below_raw_eps": {"plain": first_k_below("mean", "plain"),
                                                                "deb": first_k_below("mean", "deb")},
                              "rows": rows})
    # pooled real-vote z
    zs = [r_["real"][f"{rule}_z_vs_exact"] for mo in out["models"] for r_ in mo["rows"] if "real" in r_
          for rule in ("plain", "deb") if r_["real"][f"{rule}_z_vs_exact"] is not None]
    zm = [r_["mc"][f"{rule}_z_vs_exact"] for mo in out["models"] for r_ in mo["rows"]
          for rule in ("plain", "deb") if r_["mc"].get(f"{rule}_z_vs_exact") is not None]
    out["crosschecks"] = {"real_vote_z": {"n": len(zs), "max_abs": float(np.max(np.abs(zs))) if zs else None,
                                          "rms": float(np.sqrt(np.mean(np.square(zs)))) if zs else None},
                          "mc_vs_exact_z": {"n": len(zm), "max_abs": float(np.max(np.abs(zm))) if zm else None,
                                            "rms": float(np.sqrt(np.mean(np.square(zm)))) if zm else None}}
    return out


# ----------------------------------------------------------------------------------------------
# D3: mu estimated from n unlabeled inputs
# ----------------------------------------------------------------------------------------------
def section_d3(reps, keep, cols, est_all, d1):
    out = {"definition": ("mu is estimated from the network's outputs on n inputs drawn uniformly WITH replacement from "
                          "G (no labels).  plug-in: A(v) = sum_c m_c m_{c+v} / n^2 (m_c = sample counts), the rule "
                          "as stated; unbiased: self-pairs removed, A(0) = sum_c m_c (m_c - 1) / (n (n - 1)).  The "
                          "plug-in A(0) is biased upwards by about 1/n.  'gain retained' = (frac_est - frac_plain) / "
                          "(frac_exact_mu - frac_plain) where the denominator is > 0."),
           "representatives": [], "all_add_grok": {}}
    for ri, rep in enumerate(reps):
        kp = keep[rep["id"]]
        C, fx, M, q = kp["C"], kp["fx"], kp["M"], kp["q"]
        X = C.shape[0]
        fp, fdx = float(kp["po"].mean()), float(kp["do"].mean())
        mo = {"id": rep["id"], "eps": rep["eps"], "plain_frac": fp, "deb_frac_exact_mu": fdx,
              "plain_all": bool(kp["po"].all()), "deb_all_exact_mu": bool(kp["do"].all()), "draws": D_REP, "by_n": {}}
        for n in N_EST:
            rng = np.random.default_rng([SEED_EST_REP, ri, n])
            res = {"plugin": [], "unbiased": []}
            harm = {"plugin": [], "unbiased": []}
            for _ in range(D_REP):
                smp = M.ravel()[rng.integers(0, X, n)]
                nc = np.bincount(smp, minlength=q)
                for est in ("plugin", "unbiased"):
                    ae, de = bg_counts(nc, unbiased=(est == "unbiased"))
                    o = deb_ok_only(C, X, fx, ae, de)
                    res[est].append(o)
                    harm[est].append(int((kp["po"] & ~o).sum()))
            byn = {}
            for est in ("plugin", "unbiased"):
                fr = np.array([o.mean() for o in res[est]])
                allok = np.array([o.all() for o in res[est]])
                d = {"frac": summ(fr), "n_draws_fully_correctable": int(allok.sum()),
                     "n_draws_frac_below_plain": int((fr < fp - 1e-15).sum()),
                     "n_harmed_inputs": summ(harm[est]),
                     "n_draws_with_harmed_input": int(sum(h > 0 for h in harm[est]))}
                if fdx - fp > 0:
                    g = (fr - fp) / (fdx - fp)
                    d["gain_retained"] = summ(g)
                byn[est] = d
            mo["by_n"][str(n)] = byn
        out["representatives"].append(mo)
    # all add/grok models: per-run eps_all with estimated mu (plug-in), D_ALL draws
    fam = np.array(cols["family"])
    eps = np.array(cols["eps"], dtype=float)
    ids = np.array(cols["id"])
    pa, da = np.array(cols["plain_all"], dtype=bool), np.array(cols["deb_all"], dtype=bool)
    pf, df = np.array(cols["plain_frac"]), np.array(cols["deb_frac"])
    grok = np.flatnonzero(fam == "add/grok")
    runs = {}
    for i in grok:
        runs.setdefault((cols["p"][i], cols["run_id"][i]), []).append(i)
    for n in N_EST:
        per_p = {}
        retained = {}
        nworse_runs = 0
        for d in range(D_ALL):
            meds = {}
            for (P, rid), ii in sorted(runs.items()):
                rows = []
                for i in ii:
                    if eps[i] == 0:
                        rows.append((0.0, True))
                    else:
                        rows.append((eps[i], est_all[ids[i]][n][1][d]))
                ea, _ = run_thresholds(rows)
                meds.setdefault(P, []).append(ea)
                ep_ = d1["runs"][rid]["eps_all_plain"]
                ed_ = d1["runs"][rid]["eps_all_deb"]
                if ed_ is not None and ep_ is not None and ed_ > ep_:
                    retained.setdefault(P, []).append((ea - ep_) / (ed_ - ep_) if ea is not None else None)
                if cmp_none(ep_, ea) < 0:
                    nworse_runs += 1
            for P, v in meds.items():
                per_p.setdefault(P, []).append(float(np.median([x for x in v if x is not None])))
        blk = {"draws": D_ALL, "n_run_draw_pairs_eps_all_below_plain": int(nworse_runs),
               "n_run_draw_pairs": int(D_ALL * len(runs))}
        for P in sorted(per_p):
            blk[f"p={P}"] = {"median_eps_all_over_runs_by_draw": summ(per_p[P]),
                             "gain_retained_per_run_and_draw": summ([x for x in retained.get(P, []) if x is not None])}
        m = (fam == "add/grok") & (eps > 0)
        fr = np.array([np.mean(est_all[i][n][0]) for i in ids[m]])
        ok = np.array([est_all[i][n][1] for i in ids[m]])            # (models, D_ALL)
        blk["fully_correctable_models_mean_over_draws"] = float(ok.sum(0).mean())
        blk["fully_correctable_models_range_over_draws"] = [int(ok.sum(0).min()), int(ok.sum(0).max())]
        blk["n_models_full_plain_not_full_in_some_draw"] = int((pa[m] & ~ok.all(1)).sum())
        blk["n_models_full_plain_not_full_in_majority_of_draws"] = int((pa[m] & (ok.mean(1) < 0.5)).sum())
        bins = []
        for lo, hi in EPS_BINS:
            b = (eps[m] >= lo) & ((eps[m] < hi) if hi < 1.0 else (eps[m] <= hi))
            if b.any():
                bins.append({"eps_bin": [lo, hi], "n_models": int(b.sum()), "mean_frac_plain": float(pf[m][b].mean()),
                             "mean_frac_deb_exact_mu": float(df[m][b].mean()), "mean_frac_deb_est_mu": float(fr[b].mean())})
        blk["by_eps_bin"] = bins
        out["all_add_grok"][str(n)] = blk
    out["all_add_grok"]["exact_mu_reference"] = {
        "fully_correctable_plain": int(((fam == "add/grok") & (eps > 0) & pa).sum()),
        "fully_correctable_deb": int(((fam == "add/grok") & (eps > 0) & da).sum())}
    return out


# ----------------------------------------------------------------------------------------------
# D4: synthetic families, the constructed harm case, and the lin statistics
# ----------------------------------------------------------------------------------------------
def eval_field(E, f, q):
    M = (f + E) % q
    C = core.twirled_counts(E, q)
    a, dA = bg_counts(np.bincount(M.ravel(), minlength=q))
    cr = criteria(C, M.size, f.ravel() % q, a, dA)
    return cr, a, dA


def section_d4(cols, tc, log):
    p = q = SYN_P
    n = p * p
    f = core.true_table("add", p)
    a_of = np.arange(n) // p
    b_of = np.arange(n) % p
    eg = np.round(np.arange(0, 1.0001, 0.01), 4)
    out = {"config": {"G": "Z_31 x Z_31", "H": "Z_31", "f": "a + b", "seeds": list(SYN_SEEDS), "eps_grid": "0..1 step 0.01",
                      "construction": "identical to theory_checks section_c4 (rng = default_rng(seed); U = rng.random(n); "
                                      "V = rng.integers(1, p, n)); the two 'collapse' families are new here"},
           "families": {}}
    fams = {
        "incoherent": ("e(x) = V(x) 1[U(x) < eps], V uniform on H \\ {0} (scattered values)", lambda U, V, e: np.where(U < e, V, 0)),
        "offset": ("e(x) = 1[U(x) < eps] (constant offset on a random set)", lambda U, V, e: np.where(U < e, 1, 0)),
        "second_hom": ("M = g = a + 2b on a random set of density eps, f elsewhere", lambda U, V, e: np.where(U < e, b_of, 0)),
        "collapse_random": ("M = 0 on a random set of density eps (the zero-vote mechanism in pure form)",
                            lambda U, V, e: np.where(U < e, (-(a_of + b_of)) % p, 0)),
    }
    for key, (desc, gen) in fams.items():
        fr_p, fr_d, last_p, last_d = [], [], [], []
        nh, nhp, worse_cells = 0, 0, 0
        for sd in SYN_SEEDS:
            rng = np.random.default_rng(sd)
            U = rng.random(n)
            V = rng.integers(1, p, n)
            rp, rd = [], []
            for e in eg:
                E = gen(U, V, e).reshape(p, p) % q
                cr, _, _ = eval_field(E, f, q)
                rp.append(float(cr["plain_ok"].mean()))
                rd.append(float(cr["deb_ok"].mean()))
                h = int((cr["plain_ok"] & ~cr["deb_ok"]).sum())
                nh += h
                nhp += int((cr["deb_ok"] & ~cr["plain_ok"]).sum())
                worse_cells += int(rd[-1] < rp[-1])
            fr_p.append(rp)
            fr_d.append(rd)
            rp_, rd_ = np.array(rp), np.array(rd)
            last_p.append(float(eg[np.argmax(rp_ < 1)] - 0.01) if (rp_ < 1).any() else 1.0)
            last_d.append(float(eg[np.argmax(rd_ < 1)] - 0.01) if (rd_ < 1).any() else 1.0)
        fp_m, fd_m = np.mean(fr_p, 0), np.mean(fr_d, 0)
        d = {"definition": desc, "eps": eg.tolist(), "frac_plain_mean": fp_m.tolist(), "frac_deb_mean": fd_m.tolist(),
             "last_grid_eps_all_correctable_plain": summ(last_p), "last_grid_eps_all_correctable_deb": summ(last_d),
             "n_cells": len(SYN_SEEDS) * len(eg), "n_cells_deb_frac_lower": worse_cells,
             "n_inputs_harmed_total": nh, "n_inputs_helped_total": nhp,
             "max_mean_frac_gain": float((fd_m - fp_m).max()), "max_mean_frac_loss": float((fp_m - fd_m).max())}
        if key in tc["c4"]["families"]:
            ref = np.array(tc["c4"]["families"][key]["correctable_fraction_mean"])
            d["plain_vs_theory_checks_max_abs_diff"] = float(np.abs(ref - fp_m).max())
        out["families"][key] = d
        log(f"  D4 {key}: harmed {nh}, helped {nhp}")

    # deterministic bands: constant offset h = 1 on a < m (theory_checks band_odd), and collapse to 0 on a < m
    for key, desc, gen in (("band_odd", "e(a,b) = 1 for a < m (constant-offset band, theory_checks band_odd)",
                            lambda m: np.where(a_of < m, 1, 0)),
                           ("collapse_band", "M = 0 for a < m, M = f elsewhere (constructed harm case)",
                            lambda m: np.where(a_of < m, (-(a_of + b_of)) % p, 0))):
        rows = []
        for m in range(0, p + 1):
            E = gen(m).reshape(p, p) % q
            cr, a, dA = eval_field(E, f, q)
            po, do = cr["plain_ok"], cr["deb_ok"]
            harmed = np.flatnonzero(po & ~do)
            rows.append({"m": m, "eps": float((E != 0).mean()), "frac_plain": float(po.mean()), "frac_deb": float(do.mean()),
                         "plain_all": bool(po.all()), "deb_all": bool(do.all()), "n_harmed": int(len(harmed)),
                         "n_helped": int((do & ~po).sum()),
                         "harmed_inputs_f_values": sorted(set(int(v) for v in (f.ravel()[harmed] % q))),
                         "harmed_inputs_a_coords": sorted(set(int(v) for v in a_of[harmed]))})
        d = {"definition": desc, "rows": rows,
             "n_m_values_with_harm": int(sum(r_["n_harmed"] > 0 for r_ in rows)),
             "n_m_full_plain_not_full_deb": int(sum(r_["plain_all"] and not r_["deb_all"] for r_ in rows))}
        if key == "band_odd":
            ref = np.array(tc["c4"]["families"]["band_odd"]["correctable_fraction_mean"])
            d["plain_vs_theory_checks_max_abs_diff"] = float(np.abs(ref - np.array([r_["frac_plain"] for r_ in rows])).max())
        out["families"][key] = d
    # worked instance of the harm case: m = 15
    m = 15
    E = np.where(a_of < m, (-(a_of + b_of)) % p, 0).reshape(p, p) % q
    cr, a, dA = eval_field(E, f, q)
    C = core.twirled_counts(E, q)
    po, do = cr["plain_ok"], cr["deb_ok"]
    harmed = np.flatnonzero(po & ~do)
    A = a / float(dA)
    ex = []
    for x in harmed[:6]:
        hs = 1 + int(np.argmax(C[x, 1:]))
        sd = (C[x] / float(n)) - A[(f.ravel()[x] + np.arange(q)) % q]
        hd = 1 + int(np.argmax(sd[1:]))
        ex.append({"x": [int(a_of[x]), int(b_of[x])], "f_x": int(f.ravel()[x]), "T_x0": float(C[x, 0] / n),
                   "max_wrong_T": float(C[x, hs] / n), "A_at_truth": float(A[f.ravel()[x] % q]),
                   "debiased_truth": float(sd[0]), "debiased_best_wrong": float(sd[hd]), "debiased_best_wrong_offset": hd})
    out["harm_case"] = {
        "construction": ("G = Z_31^2, f = a + b, the network answers 0 on the band a < 15 and f elsewhere.  Errors are the "
                         "inputs of the band with f(x) != 0."),
        "eps": float((E != 0).mean()), "plain_all_correctable": bool(po.all()), "deb_all_correctable": bool(do.all()),
        "n_inputs": n, "n_harmed": int(len(harmed)), "n_helped": int((do & ~po).sum()),
        "frac_plain": float(po.mean()), "frac_deb": float(do.mean()),
        "harmed_all_have_f_x_zero": bool((f.ravel()[harmed] % q == 0).all()),
        "A0": float(A[0]), "A_min": float(A.min()), "A_max_nonzero": float(A[1:].max()),
        "examples": ex,
        "why": ("For x with f(x) = 0 the truth IS the zero vote.  The rule subtracts A(0) = sum mu^2, the collision rate "
                "of two INDEPENDENT outputs; but for x = (x1, -x1) with x1 far from 0 the pair (r, x + r) is rarely inside "
                "the band together, so the actual zero-vote mass is far below A(0) and the truth is over-penalised.")}

    # lin vs add/grok statistics from the per-model pass
    fam = np.array(cols["family"])
    eps = np.array(cols["eps"], dtype=float)

    def col(k):
        return np.array([np.nan if v is None else v for v in cols[k]], dtype=float)
    oc, bz, dfc, cor, cgd, hz = (col("out_collision_times_q"), col("bg_zero_minus_min_times_q"),
                                 col("unc_plain_deficit_median"), col("unc_plain_correction_median"),
                                 col("frac_unc_plain_correction_gt_deficit"), col("frac_unc_plain_hstar_zero_vote"))
    stats = {}
    for fname in ("add/grok", "lin", "add/memo", "mul"):
        for lo, hi in ((0.5, 0.7), (0.7, 0.8), (0.8, 0.9), (0.9, 1.0)):
            b = (fam == fname) & (eps >= lo) & (eps < hi)
            if not b.any():
                continue
            u = b & np.isfinite(dfc)
            stats[f"{fname}|eps[{lo},{hi})"] = {
                "n_models": int(b.sum()), "n_models_with_uncorrectable": int(u.sum()),
                "out_collision_times_q_median": float(np.nanmedian(oc[b])),
                "bg_A0_minus_minA_times_q_median": float(np.nanmedian(bz[b])),
                "uncorrectable_deficit_median": (float(np.nanmedian(dfc[u])) if u.any() else None),
                "uncorrectable_correction_median": (float(np.nanmedian(cor[u])) if u.any() else None),
                "share_unc_where_correction_exceeds_deficit_median": (float(np.nanmedian(cgd[u])) if u.any() else None),
                "share_unc_hstar_is_zero_vote_median": (float(np.nanmedian(hz[u])) if u.any() else None)}
    out["family_statistics"] = {
        "definition": ("out_collision_times_q = q sum_c mu_c^2 (1 = balanced outputs; for mul the 2-query value); "
                       "bg_A0_minus_minA_times_q = q (A(0) - min_v A(v)) (the largest penalty difference the rule can "
                       "apply, in units of 1/q); at plain-uncorrectable inputs with f(x) != 0: deficit = T_x(h*) - T_x(0) "
                       "(h* = strongest wrong value), correction = A(f(x)+h*) - A(f(x)) (what the rule adds to the truth "
                       "relative to h*); medians over inputs, then over models"),
        "cells": stats}
    return out


# ----------------------------------------------------------------------------------------------
# D5: i.i.d. finite-size thresholds under both rules (grid procedure of theory_checks C3)
# ----------------------------------------------------------------------------------------------
def iid_first_failure(p, seed, rule, cache):
    q, nG = p, p * p
    rng = np.random.default_rng(seed)
    U = rng.random(nG)
    V = rng.integers(1, q, nG)
    f = core.true_table("add", p)

    def ok_one(e):
        if e not in cache:
            E = np.where(U < e, V, 0).reshape(p, p)
            cr, _, _ = eval_field(E, f, q)
            cache[e] = (bool(cr["plain_ok"].all()), bool(cr["deb_ok"].all()))
        return cache[e][0 if rule == "plain" else 1]

    def ok(lst):
        return [ok_one(e) for e in lst]
    grid = [round(0.20 + 0.04 * i, 6) for i in range(0, 21)]
    c1 = None
    for s in range(0, len(grid), 4):
        r = ok(grid[s:s + 4])
        if not all(r):
            c1 = grid[s + r.index(False)]
            break
    if c1 is None:
        return None
    g2 = [round(c1 - 0.08 + 0.008 * i, 6) for i in range(1, 11)]
    r = ok(g2)
    c2 = g2[r.index(False)] if not all(r) else c1
    g3 = [round(c2 - 0.016 + 0.002 * i, 6) for i in range(1, 9)]
    r = ok(g3)
    c3 = g3[r.index(False)] if not all(r) else c2
    return float((U < round(c3 - 0.002, 6)).mean())


def section_d5(tc, d1, log):
    out = {"procedure": "theory_checks C3 grid (step 0.04 from 0.20, then 0.008, then 0.002; last passing grid point, "
                        "realised error rate), nested i.i.d. fields e = V 1[U < eps], seeds 7000 + 100 p + s, s < 24; "
                        "each rule searched separately on the same fields",
           "rows": {}}
    for P in IID_PS:
        ref = next(r for r in tc["c3_finite_size"]["rows"] if r["p"] == P)
        vp, vd = [], []
        for s in range(IID_NSEEDS):
            cache = {}
            sd = 7000 + 100 * P + s
            vp.append(iid_first_failure(P, sd, "plain", cache))
            vd.append(iid_first_failure(P, sd, "deb", cache))
        key = f"add/grok|p={P}"
        cell = d1["cells"][key]
        row = {"seeds": [7000 + 100 * P + s for s in range(IID_NSEEDS)],
               "iid_eps_last_ok_plain": summ(vp), "iid_eps_last_ok_deb": summ(vd),
               "per_seed_plain": vp, "per_seed_deb": vd,
               "n_seeds_deb_higher": int(sum(b > a for a, b in zip(vp, vd))),
               "n_seeds_deb_lower": int(sum(b < a for a, b in zip(vp, vd))),
               "plain_reproduces_theory_checks": bool(np.allclose(vp, ref["per_seed_eps_last_ok"][:len(vp)], atol=1e-12, rtol=0)),
               "trained_eps_all_median_plain": cell["eps_all_plain"]["median"],
               "trained_eps_all_median_deb": cell["eps_all_deb"]["median"],
               "trained_eps_some_median_plain": cell["eps_some_plain"]["median"],
               "trained_eps_some_median_deb": cell["eps_some_deb"]["median"],
               "n_runs_eps_some_deb_above_iid_deb_median": int(sum(
                   v["eps_some_deb"] is not None and v["eps_some_deb"] > summ(vd)["median"]
                   for v in d1["runs"].values() if v["family"] == "add/grok" and v["p"] == P)),
               "n_runs_eps_all_deb_above_iid_deb_median": int(sum(
                   v["eps_all_deb"] is not None and v["eps_all_deb"] > summ(vd)["median"]
                   for v in d1["runs"].values() if v["family"] == "add/grok" and v["p"] == P))}
        ip, idb = row["iid_eps_last_ok_plain"]["median"], row["iid_eps_last_ok_deb"]["median"]
        mp, md = row["trained_eps_all_median_plain"], row["trained_eps_all_median_deb"]
        row["gap_plain_rule_trained_vs_iid"] = ip - mp
        row["gap_deb_rule_trained_vs_iid_plain"] = ip - md
        row["gap_deb_rule_trained_vs_iid_deb"] = idb - md
        row["fraction_of_gap_closed_vs_iid_plain"] = (md - mp) / (ip - mp)
        row["fraction_of_gap_closed_vs_iid_deb"] = (md - mp) / (idb - mp)
        row["note"] = ("eps_all is a lower bound and eps_some an upper bound on a run's threshold (discrete snapshots); "
                       "the gap fractions use the eps_all medians and are therefore conservative")
        out["rows"][key] = row
        log(f"  D5 p={P}: iid plain {ip:.4f} deb {idb:.4f}; trained {mp:.4f} -> {md:.4f}")
    return out


# ----------------------------------------------------------------------------------------------
# figure
# ----------------------------------------------------------------------------------------------
def make_figure(res):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.lines import Line2D
    import paperstyle as ps
    ps.apply()
    cols = res["D1"]["per_model"]
    fam = np.array(cols["family"])
    eps = np.array(cols["eps"], dtype=float)
    m = (fam == "add/grok") & (eps > 0)
    pf, df = np.array(cols["plain_frac"], dtype=float)[m], np.array(cols["deb_frac"], dtype=float)[m]
    e = eps[m]
    fig, axs = plt.subplots(1, 2, figsize=(7.0, 3.2), constrained_layout=True, gridspec_kw={"width_ratios": [1.35, 1]})
    ax = axs[0]
    ax.scatter(e, pf, s=13, color=ps.BLUE, edgecolor="none", alpha=0.45, zorder=3)
    ax.scatter(e, df, s=13, color=ps.ORANGE, edgecolor="none", alpha=0.45, zorder=3)
    edges = np.round(np.arange(0.0, 1.0001, 0.05), 4)
    cx, mp_, md_ = [], [], []
    for lo, hi in zip(edges[:-1], edges[1:]):
        b = (e >= lo) & (e < hi) if hi < 1 else (e >= lo) & (e <= hi)
        if b.sum() >= 3:
            cx.append(float(np.median(e[b])))
            mp_.append(float(np.median(pf[b])))
            md_.append(float(np.median(df[b])))
    ax.plot(cx, mp_, color=ps.BLUE, lw=2.0, marker="o", ms=5.5, mec=ps.SURFACE, mew=1.0, zorder=5)
    ax.plot(cx, md_, color=ps.ORANGE, lw=2.0, marker="o", ms=5.5, mec=ps.SURFACE, mew=1.0, zorder=5)
    hs = [Line2D([0], [0], color=ps.BLUE, lw=2.0, marker="o", ms=5.5, mec=ps.SURFACE, label="plain plurality"),
          Line2D([0], [0], color=ps.ORANGE, lw=2.0, marker="o", ms=5.5, mec=ps.SURFACE, label="bias-subtracted"),
          Line2D([0], [0], color=ps.INK2, lw=0, marker="o", ms=4, alpha=0.6, mec="none", label="one snapshot"),
          Line2D([0], [0], color=ps.INK2, lw=2.0, label="binned median (width 0.05)")]
    ax.legend(handles=hs, loc="center left", bbox_to_anchor=(0.0, 0.52), fontsize=8, frameon=False, borderaxespad=0.5)
    ax.set_xlim(0, 1)
    ax.set_ylim(-0.03, 1.05)
    ax.set_xlabel(r"error rate $\varepsilon$")
    ax.set_ylabel("fraction of inputs correctable")
    ax.set_title(f"a  Addition nets, {int(m.sum())} snapshots")
    ax = axs[1]
    runs = res["D1"]["runs"]
    for j, P in enumerate((23, 31, 47)):
        rs = sorted([v for v in runs.values() if v["family"] == "add/grok" and v["p"] == P], key=lambda v: v["eps_all_plain"])
        yp = np.array([v["eps_all_plain"] for v in rs], dtype=float)
        yd = np.array([v["eps_all_deb"] for v in rs], dtype=float)
        jit = np.linspace(-0.07, 0.07, len(rs))
        xp, xd = j - 0.2 + jit, j + 0.2 + jit
        for a_, b_, c_, d_ in zip(xp, xd, yp, yd):
            ax.plot([a_, b_], [c_, d_], color=ps.GRID if d_ == c_ else ps.AXIS, lw=0.9, zorder=2)
        ax.scatter(xp, yp, s=26, color=ps.BLUE, edgecolor=ps.SURFACE, linewidth=0.8, zorder=4)
        ax.scatter(xd, yd, s=26, color=ps.ORANGE, edgecolor=ps.SURFACE, linewidth=0.8, zorder=4)
        iid = res["D1"]["cells"][f"add/grok|p={P}"]["iid_finite_size_median"]
        ax.plot([j - 0.38, j + 0.38], [iid, iid], color=ps.REFERENCE, lw=1.0, zorder=3)
    ax.set_xticks([0, 1, 2])
    ax.set_xticklabels([f"$p$ = {P}" for P in (23, 31, 47)])
    ax.set_xlim(-0.5, 2.5)
    ax.set_ylim(0.40, 0.96)
    ax.set_ylabel(r"largest fully correctable $\varepsilon$")
    ax.set_title("b  Per training run (12 per $p$)")
    ax.grid(axis="x", visible=False)
    hb = [Line2D([0], [0], color=ps.BLUE, lw=0, marker="o", ms=5.5, mec=ps.SURFACE, label="plain"),
          Line2D([0], [0], color=ps.ORANGE, lw=0, marker="o", ms=5.5, mec=ps.SURFACE, label="bias-subtracted"),
          Line2D([0], [0], color=ps.REFERENCE, lw=1.0, label="i.i.d. errors, median")]
    ax.legend(handles=hb, loc="upper left", fontsize=8, ncol=2, borderaxespad=0.3, columnspacing=1.0,
              handletextpad=0.4)
    ps.save(fig, FIG_PATH)
    plt.close(fig)
    return FIG_PATH


# ----------------------------------------------------------------------------------------------
def main():
    if "--figs-only" in sys.argv:
        res = json.load(open(OUT_JSON))
        print("figure:", make_figure(res))
        return
    t0 = time.time()

    def log(s):
        print(f"[{time.time() - t0:6.1f} s] {s}", flush=True)
    idx = core.load_index()
    tc = json.load(open(os.path.join(core.RESULTS_DIR, "theory_checks.json")))
    ch = json.load(open(os.path.join(core.RESULTS_DIR, "exp_channels.json")))
    tk = json.load(open(os.path.join(core.RESULTS_DIR, "exp_tasks.json")))
    res = {"meta": {"script": "code/exp_debias.py", "command": "OMP_NUM_THREADS=1 python3 code/exp_debias.py",
                    "numpy": np.__version__, "processes": 1,
                    "seeds": {"mc": f"np.random.default_rng([{SEED_MC}, rep_index, k])",
                              "real_votes": f"np.random.default_rng([{SEED_REAL}, rep_index, k])",
                              "worst_input_reestimate": f"np.random.default_rng([{SEED_WORST}, rep_index, k])",
                              "mu_estimate_representatives": f"np.random.default_rng([{SEED_EST_REP}, rep_index, n])",
                              "mu_estimate_all_add_grok": f"np.random.default_rng([{SEED_EST_ALL}, zoo_index])",
                              "synthetic_fields": list(SYN_SEEDS), "iid_fields": "7000 + 100 p + s, s < 24",
                              "selfcheck": 66000},
                    "config": {"ks": list(KS), "k_exact_all_inputs_max": K_EXACT_ALL, "n_mc": N_MC,
                               "n_mc_small_groups": N_MC_SMALL, "n_mc_worst_reestimate": N_MC_WORST,
                               "real_vote_ks": list(K_REAL), "real_vote_trials_per_input": R_REAL,
                               "n_est": list(N_EST), "draws_rep": D_REP, "draws_all": D_ALL, "acc_floor": ACC_FLOOR},
                    "rule": ("bias-subtracted plurality: argmax_v [N_v / k - A(v)], A(v) = sum_c mu_c mu_{c+v} "
                             "(2-query vote) or the law of o1 - o2 - o3 + o4 (4-query mul vote); tie = failure")}}
    log("self-checks")
    res["checks"] = {"recursion": selfchecks()}
    reps = pick_representatives(idx)
    log("representatives: " + ", ".join(f"{r['id']} ({r['eps']:.3f})" for r in reps))
    iid_refs = {f"add/grok|p={P}": ch["A3"]["cells"][f"add/grok|p={P}"]["iid_finite_size_median"] for P in (23, 31, 47)}
    iid_refs["lin|p=7"] = ch["A3"]["cells"]["lin|p=7"]["iid_finite_size_median"]
    iid_refs["add/memo|p=53"] = ch["A3"]["cells"]["add/memo|p=53"]["iid_finite_size_median"]
    iid_refs["mul|p=31"] = tk["iid_baseline_mul"]["eps_last_ok_realised"]["median"]
    iid_mins = {k: (ch["A3"]["cells"][k]["iid_min_over_fields"] if k in ch["A3"]["cells"] else
                    tk["iid_baseline_mul"]["eps_last_ok_realised"]["min"]) for k in iid_refs}
    log("D1 per-model pass")
    cols, est_all, keep = per_model_pass(idx, set(r["id"] for r in reps), log)
    # reproduction checks against earlier results
    pmc = ch["per_model"]
    ref = {i: (fc, ac) for i, fc, ac in zip(pmc["id"], pmc["frac_correctable"], pmc["all_correctable"])}
    mism_f = mism_a = nchk = 0
    for i, fc, ac in zip(cols["id"], cols["plain_frac"], cols["plain_all"]):
        if i in ref:
            nchk += 1
            mism_f += abs(ref[i][0] - fc) > 1e-9
            mism_a += bool(ref[i][1]) != bool(ac)
    refm = {mm["id"]: (mm["correctable_fraction"], mm["all_correctable"]) for mm in tk["mul"]["models"]}
    mm_f = mm_a = nm = 0
    for i, fn, ac, fa in zip(cols["id"], cols["plain_frac_nontrivial"], cols["plain_all"], cols["family"]):
        if fa == "mul":
            nm += 1
            mm_f += abs(refm[i][0] - fn) > 1e-12
            mm_a += bool(refm[i][1]) != bool(ac)
    res["checks"]["plain_vs_exp_channels"] = {"n_models_compared": nchk, "n_frac_mismatch": int(mism_f),
                                              "n_all_correctable_mismatch": int(mism_a)}
    res["checks"]["plain_vs_exp_tasks_mul"] = {"n_models_compared": nm, "n_frac_mismatch": int(mm_f),
                                               "n_all_correctable_mismatch": int(mm_a)}
    log(f"checks: exp_channels {nchk} models, mismatches {mism_f}/{mism_a}; mul {nm} models, {mm_f}/{mm_a}")
    res["probe_reproduction"] = probe_reproduction(cols)
    res["D1"] = section_d1(cols, iid_refs, iid_mins)
    res["D1"]["iid_references"] = {"values": iid_refs, "min_over_fields": iid_mins,
                                   "source": "results/exp_channels.json A3.cells.<key>.iid_finite_size_median; mul: "
                                             "results/exp_tasks.json iid_baseline_mul.eps_last_ok_realised.median"}
    res["D1"]["representatives"] = reps
    log("D2 finite k")
    res["D2"] = section_d2(reps, keep, log)
    log("D3 estimated mu")
    res["D3"] = section_d3(reps, keep, cols, est_all, res["D1"])
    log("D4 synthetic families")
    res["D4"] = section_d4(cols, tc, log)
    log("D5 i.i.d. thresholds")
    res["D5"] = section_d5(tc, res["D1"], log)
    res["checks"]["synthetic_plain_vs_theory_checks_max_abs_diff"] = max(
        v.get("plain_vs_theory_checks_max_abs_diff", 0.0) for v in res["D4"]["families"].values())
    res["checks"]["iid_plain_reproduces_theory_checks"] = all(v["plain_reproduces_theory_checks"]
                                                              for v in res["D5"]["rows"].values())
    res["D1"]["per_model"] = {k: [round(x, 10) if isinstance(x, float) else x for x in v] for k, v in cols.items()}
    res["meta"]["runtime_seconds"] = round(time.time() - t0, 1)
    res = jsonable(res)
    with open(OUT_JSON, "w") as fh:
        json.dump(res, fh, indent=1)
    log("wrote " + OUT_JSON)
    print("figure:", make_figure(res))
    log("done")


if __name__ == "__main__":
    main()

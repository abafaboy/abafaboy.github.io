"""exp_labelfree.py -- package C2: label-free evaluation of trained networks with the BLR test.

    OMP_NUM_THREADS=1 python3 code/exp_labelfree.py      (one process, deterministic, about 5 min)

Writes results/exp_labelfree.json and figures/fig_labelfree.{svg,png}.

For every add/grok, add/memo and lin model of the zoo (1223 models, 80 runs):
  1. exact pass rate pi of the linearity test, the depolarizing inversion eps_hat, the naive estimate
     1 - pi^(1/3) and the unconditional bound eps >= (1 - pi)/3, against the true error rate;
  2. finite-sample error of eps_hat from n random unlabeled triples (five representative models);
  3. end-to-end protocol: number of votes predicted from pi alone versus the number actually needed
     for a mean failure <= 1e-3 (exact channel of the real network);
  4. per-input confidence from the observed vote margin (the add/grok models with the lowest error
     rate that have uncorrectable inputs, and the two models just below them);
  5. blind spots on constructed tables, the two-generator fix, and the nearest homomorphism of
     every zoo model by brute force (what the pass rate really measures);
  6. baseline: disagreement between two independently initialised networks (add/memo ensembles).

This file also provides fail_bounds(): the exact plurality failure of core.plurality_fail_exact,
restricted to the terms that matter (rigorous two-sided bounds, gap <= tol), about 10x faster.
"""
import functools
import json
import math
import os
import sys
import time

import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
from scipy.special import bdtrc, gammaln
from scipy.stats import binom, rankdata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import core  # noqa: E402

THR = 1e-3            # target mean failure of the protocol
KMAX = 149            # largest (odd) number of votes searched
SEED = 20261116


# --------------------------------------------------------------------------------------------
# fast exact plurality failure
# --------------------------------------------------------------------------------------------
def canonical_rows(N):
    """Sort the wrong-value columns of an integer count table (X, q) in decreasing order (the
    plurality failure is invariant under permutations of the wrong values) and merge equal rows.
    Returns (unique rows (U, q'), inverse (X,), multiplicity (U,)); all-zero columns are dropped."""
    N = np.asarray(N, dtype=np.int64)
    S = np.concatenate([N[:, :1], -np.sort(-N[:, 1:], axis=1)], axis=1)
    U, inv, mult = np.unique(S, axis=0, return_inverse=True, return_counts=True)
    keep = np.concatenate([[True], U[:, 1:].any(0)])
    return U[:, keep], inv.ravel(), mult


def fail_bounds(P, k, tol=1e-11):
    """Rigorous bounds lo <= delta_k <= hi with hi - lo <= tol (plus ~1e-13 round-off) on the exact
    plurality failure delta_k = Pr[N_0 <= max_{h != 0} N_h], N ~ Multinomial(k, P_x), for every row
    of P (column 0 = truth).  Same formula as core.plurality_fail_exact,
        delta_k = sum_m Pr[N_0 = m] * Pr[max_h N_h >= m | N_0 = m],
    but (i) for m > k/2 the second factor is 0, (ii) for m = 1 it is 1 (if any vote is left),
    (iii) a term is skipped when Pr[N_0 = m] * n_wrong * Pr[Bin(k - m, tau_max) >= m] <= tol/k
    (union bound; the skipped mass is added to hi only), and (iv) the generating polynomial is
    rescaled by theta = k so that no factorial under- or overflows.  Only non-negative sums."""
    P = np.atleast_2d(np.asarray(P, dtype=float))
    k = int(k)
    t0 = P[:, 0]
    Wr = P[:, 1:]
    s = Wr.sum(1)
    nW = (Wr > 0).sum(1)
    with np.errstate(divide="ignore", invalid="ignore"):
        taumax = np.where(s > 0, Wr.max(1) / np.where(s > 0, s, 1.0), 0.0)
        logt0 = np.log(t0)
    w = binom.pmf(np.arange(k + 1)[None, :], k, t0[:, None])      # Pr[N_0 = m]
    lo = w[:, 0].copy()                                           # N_0 = 0 always fails
    hi = w[:, 0].copy()
    lgf = gammaln(np.arange(k + 2) + 1.0)                         # log i!
    theta = float(k)
    tol_m = tol / max(1, k)
    for m in range(1, k // 2 + 1):
        d = k - m
        if m == 1:
            lo += w[:, 1]
            hi += w[:, 1]
            continue
        ub = np.minimum(1.0, nW * bdtrc(m - 1, d, taumax))
        need = w[:, m] * ub > tol_m
        hi[~need] += (w[:, m] * ub)[~need]
        A = np.nonzero(need)[0]
        if A.size == 0:
            continue
        WA = Wr[A] * theta
        cols = np.nonzero(WA.any(0))[0]
        poly = np.zeros((A.size, d + 1))
        poly[:, 0] = 1.0
        inv_fact = np.exp(-lgf[:m])
        jj = np.arange(m)
        pad = np.zeros((A.size, d + m))
        for h in cols:
            c = (WA[:, h][:, None] ** jj[None, :]) * inv_fact[None, :]
            pad[:, m - 1:] = poly
            win = sliding_window_view(pad, m, axis=1)             # win[x, n, i] = poly[x, n+i-(m-1)]
            poly = np.einsum("xni,xi->xn", win, c[:, ::-1])
        with np.errstate(divide="ignore"):
            ok = np.exp(lgf[k] - lgf[m] + m * logt0[A] - d * math.log(theta)) * poly[:, d]
        f = np.clip(w[A, m] - ok, 0.0, None)
        lo[A] += f
        hi[A] += f
    return np.clip(lo, 0.0, 1.0), np.clip(hi, 0.0, 1.0)


class MeanFail:
    """Mean over inputs of the exact plurality failure of a model's vote channel, cached per k."""

    def __init__(self, counts):
        self.U, self.inv, self.mult = canonical_rows(counts)
        self.P = self.U / self.U.sum(1, keepdims=True)
        self.cache = {}
        self.n_eval = 0

    def per_input(self, k, tol=1e-11):
        lo, hi = fail_bounds(self.P, k, tol)
        return lo[self.inv], hi[self.inv]

    def bounds(self, k, tol=1e-8):
        key = (int(k), tol)
        if key not in self.cache:
            lo, hi = fail_bounds(self.P, k, tol)
            n = self.mult.sum()
            self.cache[key] = (float((lo * self.mult).sum() / n), float((hi * self.mult).sum() / n))
            self.n_eval += 1
        return self.cache[key]

    def value(self, k):
        lo, hi = self.bounds(k)
        return 0.5 * (lo + hi)

    def ok(self, k, thr=THR):
        lo, hi = self.bounds(k)
        if hi <= thr:
            return True
        if lo > thr:
            return False
        lo, hi = self.bounds(k, 1e-13)
        return 0.5 * (lo + hi) <= thr


def smallest_odd_k(mf, k_guess, thr=THR, kmax=KMAX):
    """Smallest odd k <= kmax with mean failure <= thr, by interpolation search on ln(failure),
    started at k_guess.  Assumes that once the mean failure is below thr it stays below for larger
    odd k (checked on a subsample, see 'monotonicity_check'; the failure is NOT monotone at small k).
    Returns None if the failure at kmax still exceeds thr."""
    def lf(k):
        return math.log(max(mf.value(k), 1e-300))
    g = int(min(max(1, k_guess if k_guess is not None else kmax), kmax)) | 1
    if mf.ok(g, thr):
        hi_k, f_hi, lo_k, f_lo = g, lf(g), -1, 0.0
    else:
        if g == kmax or not mf.ok(kmax, thr):
            return None
        lo_k, f_lo, hi_k, f_hi = g, lf(g), kmax, lf(kmax)
    lthr = math.log(thr)
    while hi_k - lo_k > 2:
        if f_hi < f_lo:
            x = lo_k + (lthr - f_lo) / (f_hi - f_lo) * (hi_k - lo_k)
        else:
            x = 0.5 * (lo_k + hi_k)
        c = int(math.ceil(x)) | 1
        if c >= hi_k:                 # the upper end is the guess: confirm with its neighbour
            c = hi_k - 2
        c = min(max(c, lo_k + 2), hi_k - 2)
        if mf.ok(c, thr):
            hi_k, f_hi = c, lf(c)
        else:
            lo_k, f_lo = c, lf(c)
    return hi_k


# --------------------------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------------------------
def pick_horizon_models(index):
    """The four add/grok p = 47 snapshots closest to eps = 0.05, 0.2, 0.4, 0.6 (same rule as
    exp_horizon.py): the closest seed-0 snapshot if it is within 0.02 of the target, otherwise the
    closest snapshot over all seeds; ties by id."""
    out = []
    pool = [r for r in index if r["family"] == "add/grok" and r["p"] == 47]
    for tgt in (0.05, 0.2, 0.4, 0.6):
        s0 = sorted((abs(r["eps"] - tgt), r["id"]) for r in pool if r["split_seed"] == 0)
        al = sorted((abs(r["eps"] - tgt), r["id"]) for r in pool)
        out.append((tgt, s0[0][1] if s0[0][0] <= 0.02 else al[0][1]))
    return out


EPS_EDGES = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]


def eps_bin(eps):
    if eps == 0:
        return "eps=0"
    for a, b in zip(EPS_EDGES[:-1], EPS_EDGES[1:]):
        if a < eps <= b:
            return "(%.1f,%.1f]" % (a, b)
    raise ValueError(eps)


def run_unit_stats(rows, key):
    """rows: list of dicts with 'run_id' and the error value under `key`.  Model-level bias, MAE and
    max |error|, and the same with the RUN as the unit (mean and standard error over run means)."""
    err = np.array([r[key] for r in rows], dtype=float)
    runs = sorted(set(r["run_id"] for r in rows))
    rb = np.array([np.mean([r[key] for r in rows if r["run_id"] == u]) for u in runs])
    ra = np.array([np.mean([abs(r[key]) for r in rows if r["run_id"] == u]) for u in runs])
    se = (lambda v: float(v.std(ddof=1) / math.sqrt(len(v))) if len(v) > 1 else None)
    return dict(n_models=len(rows), n_runs=len(runs),
                bias=float(err.mean()), mae=float(np.abs(err).mean()), max_abs=float(np.abs(err).max()),
                min_err=float(err.min()), max_err=float(err.max()),
                run_bias_mean=float(rb.mean()), run_bias_se=se(rb),
                run_mae_mean=float(ra.mean()), run_mae_se=se(ra))


def auroc_high_is_right(margin, wrong):
    """Pr[margin of a right output > margin of a wrong output] + 0.5 Pr[equal]."""
    wrong = np.asarray(wrong, dtype=bool)
    n1, n0 = int((~wrong).sum()), int(wrong.sum())
    if n1 == 0 or n0 == 0:
        return None
    rk = rankdata(margin)
    return float((rk[~wrong].sum() - n1 * (n1 + 1) / 2.0) / (n1 * n0))


def vote_margin(table, xs, k, rng, q):
    v = core.sc_votes(table, xs, k, rng, q)
    m = v.shape[0]
    cnt = np.bincount((v + q * np.arange(m)[:, None]).ravel(), minlength=m * q).reshape(m, q)
    part = np.partition(cnt, q - 2, axis=1)
    return cnt.argmax(1), part[:, -1] - part[:, -2]


@functools.lru_cache(maxsize=8)
def hom_tables(p, n):
    """All p^n homomorphisms Z_p^n -> Z_p as rows: H[w, x] = <w, x> mod p (w, x in flat-index order)."""
    C = core.coords(core.group_shape(p, n))
    return ((C @ C.T) % p).astype(np.int16), C


def nearest_homomorphism(M, p):
    """Brute force over all p^n homomorphisms: (coefficients of the nearest, its distance, number of
    homomorphisms at that distance, distance to every homomorphism)."""
    H, C = hom_tables(int(p), M.ndim)
    dist = 1.0 - (H == M.ravel().astype(np.int16)[None, :]).mean(1)
    i = int(dist.argmin())
    return [int(v) for v in C[i]], float(dist[i]), int((dist == dist[i]).sum()), dist


def generator_indices(shape):
    n = len(shape)
    return [int(core.flat_index(np.eye(n, dtype=np.int64)[i], shape)) for i in range(n)]


# --------------------------------------------------------------------------------------------
def main():
    t_start = time.time()
    index = core.load_index()
    models = [r for r in index if r["family"] in ("add/grok", "add/memo", "lin")]
    out = dict(config=dict(
        script="code/exp_labelfree.py", seed=SEED, threshold_mean_failure=THR, kmax=KMAX,
        families=["add/grok", "add/memo", "lin"], n_models=len(models),
        n_runs=len(set(r["run_id"] for r in models)),
        estimator="eps_hat = (1 - ((pi - 1/q)/(1 - 1/q))^(1/3)) (1 - 1/q); naive = 1 - pi^(1/3); "
                  "bound = (1 - pi)/3",
        eps_bins="eps=0 separately, then (a, a+0.1]",
        note="pi is exact (all |G|^2 pairs). Snapshots of one training run are correlated: "
             "run-level means and standard errors use the run as the unit."))

    # ---------------------------------------------------------------- 1. pass rate for every model
    recs, counts = [], {}
    for r in models:
        q = r["q"]
        M = core.load_table(r["id"])
        E = core.error_table(r["id"])
        N = core.twirled_counts(E, q)
        counts[r["id"]] = N
        pi = core.blr_pass_rate(M, q)
        eh = float(core.eps_hat_from_pass(pi, q))
        gens = generator_indices(M.shape)
        g_ok = bool(np.all(N[gens, 0] > N[gens, 1:].max(1)))
        f_coef = [1] * r["n"] if r["task"] == "add" else [int(v) for v in core.LIN_W]
        near, d_near, n_ties, dist_all = nearest_homomorphism(M, q)
        f_flat = core.model_true_table(r["id"]).ravel()
        gen_coef = [int((f_flat[gi] + N[gi].argmax()) % q) for gi in gens]   # self-corrected generator values
        assert abs(dist_all[int(core.flat_index(np.array(f_coef), M.shape))] - r["eps"]) < 1e-9
        recs.append(dict(
            nearest_hom=near, dist_nearest=d_near, n_nearest_ties=n_ties, nearest_is_f=bool(near == f_coef),
            err_hat_vs_nearest=eh - d_near, generator_hom=gen_coef,
            generator_hom_is_nearest=bool(gen_coef == near),
            id=r["id"], run_id=r["run_id"], family=r["family"], p=r["p"], q=q, eps=r["eps"],
            pi=pi, eps_hat=eh, eps_naive=float(1.0 - pi ** (1.0 / 3.0)), eps_lower_bound=(1.0 - pi) / 3.0,
            err_hat=eh - r["eps"], err_naive=float(1.0 - pi ** (1.0 / 3.0)) - r["eps"],
            bound_slack=r["eps"] - (1.0 - pi) / 3.0,
            n_uncorrectable=int((N[:, 0] <= N[:, 1:].max(1)).sum()),
            generators_identified=g_ok,
            generator_min_margin=float(((N[gens, 0] - N[gens, 1:].max(1)) / N[gens].sum(1)).min())))
    print("pass rates done %.1fs" % (time.time() - t_start), flush=True)
    by_id = {r["id"]: r for r in recs}

    est = dict(by_family_and_bin={}, by_family={}, bound={})
    for fam in ("add/grok", "add/memo", "lin"):
        fr = [r for r in recs if r["family"] == fam]
        est["by_family_and_bin"][fam] = {}
        for b in ["eps=0"] + ["(%.1f,%.1f]" % (a, c) for a, c in zip(EPS_EDGES[:-1], EPS_EDGES[1:])]:
            br = [r for r in fr if eps_bin(r["eps"]) == b]
            if br:
                est["by_family_and_bin"][fam][b] = dict(
                    eps_hat=run_unit_stats(br, "err_hat"), naive=run_unit_stats(br, "err_naive"))
        for name, sel in (("all", fr), ("eps>0", [r for r in fr if r["eps"] > 0]),
                          ("0<eps<=0.6", [r for r in fr if 0 < r["eps"] <= 0.6]),
                          ("eps>0.6", [r for r in fr if r["eps"] > 0.6])):
            if sel:
                est["by_family"].setdefault(fam, {})[name] = dict(
                    eps_hat=run_unit_stats(sel, "err_hat"), naive=run_unit_stats(sel, "err_naive"))
        est["bound"][fam] = dict(
            n_models=len(fr), n_violations=int(sum(r["bound_slack"] < -1e-12 for r in fr)),
            min_slack=float(min(r["bound_slack"] for r in fr)),
            median_ratio_bound_over_eps=float(np.median([r["eps_lower_bound"] / r["eps"] for r in fr if r["eps"] > 0])),
            max_ratio_bound_over_eps=float(max(r["eps_lower_bound"] / r["eps"] for r in fr if r["eps"] > 0)))
    worst = sorted(recs, key=lambda r: r["err_hat"])
    est["largest_underestimates"] = [
        {k: r[k] for k in ("id", "family", "eps", "eps_hat", "pi", "n_uncorrectable")} for r in worst[:8]]
    est["largest_overestimates"] = [
        {k: r[k] for k in ("id", "family", "eps", "eps_hat", "pi", "n_uncorrectable")} for r in worst[::-1][:8]]
    est["n_models_abs_err_above_0p05"] = {
        fam: int(sum(abs(r["err_hat"]) > 0.05 for r in recs if r["family"] == fam))
        for fam in ("add/grok", "add/memo", "lin")}
    est["runs_with_abs_err_above_0p05"] = {
        fam: sorted(set(r["run_id"] for r in recs if r["family"] == fam and abs(r["err_hat"]) > 0.05))
        for fam in ("add/grok", "add/memo", "lin")}
    out["estimator"] = est

    nh = dict(note="nearest homomorphism by brute force over all p^n homomorphisms G -> Z_p; "
                   "generator_hom = coefficients read from the exact vote mode at the n generators "
                   "(the k -> infinity limit of self-correcting the generators)", by_family={})
    for fam in ("add/grok", "add/memo", "lin"):
        fr = [r for r in recs if r["family"] == fam and r["eps"] > 0]
        other = [r for r in fr if not r["nearest_is_f"]]
        top = {}
        for r in other:
            top[str(r["nearest_hom"])] = top.get(str(r["nearest_hom"]), 0) + 1
        nh["by_family"][fam] = dict(
            n_models_with_errors=len(fr), n_nearest_is_not_f=len(other),
            n_runs_with_nearest_not_f=len(set(r["run_id"] for r in other)),
            lowest_eps_nearest_not_f=min([r["eps"] for r in other], default=None),
            highest_eps_nearest_is_f=max([r["eps"] for r in fr if r["nearest_is_f"]], default=None),
            mae_eps_hat_vs_eps_all=float(np.mean([abs(r["err_hat"]) for r in fr])),
            mae_eps_hat_vs_dist_nearest_all=float(np.mean([abs(r["err_hat_vs_nearest"]) for r in fr])),
            mae_eps_hat_vs_eps_when_not_f=float(np.mean([abs(r["err_hat"]) for r in other])) if other else None,
            mae_eps_hat_vs_dist_nearest_when_not_f=float(np.mean([abs(r["err_hat_vs_nearest"]) for r in other])) if other else None,
            mean_eps_when_not_f=float(np.mean([r["eps"] for r in other])) if other else None,
            mean_dist_nearest_when_not_f=float(np.mean([r["dist_nearest"] for r in other])) if other else None,
            n_generator_hom_is_nearest=int(sum(r["generator_hom_is_nearest"] for r in fr)),
            n_generator_hom_is_nearest_when_not_f=int(sum(r["generator_hom_is_nearest"] for r in other)),
            most_frequent_nearest_when_not_f=dict(sorted(top.items(), key=lambda kv: -kv[1])[:6]),
            n_abs_err_above_0p05=int(sum(abs(r["err_hat"]) > 0.05 for r in fr)),
            n_abs_err_above_0p05_and_nearest_is_f=int(sum(abs(r["err_hat"]) > 0.05 and r["nearest_is_f"] for r in fr)))
    nh["examples_largest_underestimate"] = [
        {k: r[k] for k in ("id", "eps", "eps_hat", "pi", "nearest_hom", "dist_nearest", "generator_hom")}
        for r in worst[:5]]
    out["nearest_homomorphism"] = nh

    # ---------------------------------------------------------------- 2. finite samples
    rng = np.random.default_rng(SEED + 1)
    reps_ids = [(("add/grok p=47, eps target %.2f" % t), i) for t, i in pick_horizon_models(index)]
    memo = sorted(r["id"] for r in index if r["family"] == "add/memo" and r["holdout"] == "random"
                  and abs(r["train_frac"] - 0.7) < 1e-9 and r["split_seed"] == 0 and r["init_seed"] == 0)
    reps_ids.append(("add/memo random hold-out 30%, split 0, init 0", memo[0]))
    n_rep = 1000
    fs = dict(n_repetitions=n_rep, sizes=[30, 100, 300, 1000, 3000],
              rule="the four add/grok p=47 models of exp_horizon.py plus the add/memo model with "
                   "random 30% hold-out, split seed 0, init seed 0",
              note="each repetition draws n pairs (x, y) uniformly with replacement and evaluates the "
                   "real table; rmse_vs_true is against the true eps, rmse_vs_exact_hat against "
                   "eps_hat(exact pi) (pure sampling error); delta_method = sqrt(pi(1-pi)/n) |d eps_hat/d pi|",
              models=[])
    for label, mid in reps_ids:
        r = by_id[mid]
        q = r["q"]
        M = core.load_table(mid)
        Mf = M.ravel()
        ADD = core.add_table(M.shape)
        ent = dict(label=label, id=mid, eps=r["eps"], pi=r["pi"], eps_hat_exact=r["eps_hat"], by_n=[])
        lam3 = (r["pi"] - 1.0 / q) / (1.0 - 1.0 / q)
        dedp = (1.0 / 3.0) * abs(lam3) ** (-2.0 / 3.0) if lam3 != 0 else float("inf")
        for n in fs["sizes"]:
            x = rng.integers(0, Mf.size, size=(n_rep, n))
            y = rng.integers(0, Mf.size, size=(n_rep, n))
            ph = (((Mf[x] + Mf[y]) % q) == Mf[ADD[x, y]]).mean(1)
            eh = core.eps_hat_from_pass(ph, q)
            ent["by_n"].append(dict(
                n=n, rmse_vs_true=float(np.sqrt(np.mean((eh - r["eps"]) ** 2))),
                rmse_vs_exact_hat=float(np.sqrt(np.mean((eh - r["eps_hat"]) ** 2))),
                bias_vs_true=float(np.mean(eh - r["eps"])),
                delta_method_se=float(math.sqrt(r["pi"] * (1 - r["pi"]) / n) * dedp),
                mean_pass=float(ph.mean()), queries=3 * n))
        fs["models"].append(ent)
    out["finite_sample"] = fs
    print("finite samples done %.1fs" % (time.time() - t_start), flush=True)

    # ---------------------------------------------------------------- 3. votes: predicted vs needed
    prot_models = [r for r in recs if 0 < r["eps"] <= 0.6]
    ks = list(range(1, KMAX + 1, 2))
    # depolarizing predictions (one row per model; same q stacked), from pi and from the true eps
    for q in sorted(set(r["q"] for r in prot_models)):
        grp = [r for r in prot_models if r["q"] == q]
        rows = np.array([core.depolarizing_channel(r["eps_hat"], q, 2) for r in grp]
                        + [core.depolarizing_channel(r["eps"], q, 2) for r in grp])
        first = np.full(len(rows), -1)
        for k in ks:
            todo = np.nonzero(first < 0)[0]
            if todo.size == 0:
                break
            lo, hi = fail_bounds(rows[todo], k, 1e-12)
            first[todo[0.5 * (lo + hi) <= THR]] = k
        for i, r in enumerate(grp):
            r["k_pred"] = int(first[i]) if first[i] > 0 else None
            r["k_pred_true_eps"] = int(first[len(grp) + i]) if first[len(grp) + i] > 0 else None
    print("depolarizing predictions done %.1fs" % (time.time() - t_start), flush=True)
    mono = []
    for i, r in enumerate(prot_models):
        mf = MeanFail(counts[r["id"]])
        r["k_needed"] = smallest_odd_k(mf, r["k_pred"])
        kp = r["k_pred"]
        r["mean_fail_at_k_pred"] = mf.value(kp) if kp is not None else None
        r["n_exact_evaluations"] = mf.n_eval
        if i % 6 == 0 and r["k_needed"] is not None and r["k_needed"] <= 41:
            seq = [mf.value(k) for k in range(1, r["k_needed"] + 9, 2)]
            ups = [(1 + 2 * (j + 1), b) for j, (a, b) in enumerate(zip(seq, seq[1:])) if b > a + 1e-12]
            mono.append(dict(id=r["id"], k_needed=r["k_needed"],
                             non_increasing=bool(all(b <= a + 1e-12 for a, b in zip(seq, seq[1:]))),
                             largest_k_with_increase=(max(u[0] for u in ups) if ups else None),
                             smallest_failure_after_an_increase=(min(u[1] for u in ups) if ups else None),
                             first_k_below_thr=int(1 + 2 * next(j for j, v in enumerate(seq) if v <= THR))))
        if i % 40 == 0:
            print("  needed votes %d/%d %.1fs" % (i, len(prot_models), time.time() - t_start), flush=True)
    for r in prot_models:
        kp, kn = r["k_pred"], r["k_needed"]
        r["diff_pred_minus_needed"] = (kp - kn) if (kp is not None and kn is not None) else None
        # optimistic = the predicted number of votes does not reach the target
        r["optimistic"] = bool((kp is not None) and (kn is None or kp < kn))
    def protocol_summary(sel):
        both = [r for r in sel if r["diff_pred_minus_needed"] is not None]
        d = np.array([r["diff_pred_minus_needed"] for r in both])
        hist = {}
        for v in d:
            hist[str(int(v))] = hist.get(str(int(v)), 0) + 1
        runs = sorted(set(r["run_id"] for r in sel))
        opt_runs = sorted(set(r["run_id"] for r in sel if r["optimistic"]))
        ratio = [r["mean_fail_at_k_pred"] / THR for r in sel if r["optimistic"] and r["mean_fail_at_k_pred"] is not None]
        return dict(
            n_models=len(sel), n_runs=len(runs),
            n_both_within_kmax=len(both),
            n_needed_above_kmax=int(sum(r["k_needed"] is None for r in sel)),
            n_pred_above_kmax=int(sum(r["k_pred"] is None for r in sel)),
            n_pred_within_needed_above_kmax=int(sum(r["k_pred"] is not None and r["k_needed"] is None for r in sel)),
            n_pred_above_needed_within_kmax=int(sum(r["k_pred"] is None and r["k_needed"] is not None for r in sel)),
            diff_histogram=dict(sorted(hist.items(), key=lambda kv: int(kv[0]))),
            diff_mean=float(d.mean()) if len(d) else None,
            diff_median=float(np.median(d)) if len(d) else None,
            diff_min=int(d.min()) if len(d) else None, diff_max=int(d.max()) if len(d) else None,
            n_exact=int((d == 0).sum()), n_within_2=int((np.abs(d) <= 2).sum()),
            n_optimistic=int(sum(r["optimistic"] for r in sel)),
            frac_optimistic=float(np.mean([r["optimistic"] for r in sel])) if sel else None,
            n_pessimistic=int((d > 0).sum()),
            n_runs_with_optimistic=len(opt_runs),
            max_fail_ratio_at_k_pred_when_optimistic=float(max(ratio)) if ratio else None,
            median_fail_ratio_at_k_pred_when_optimistic=float(np.median(ratio)) if ratio else None)
    prot = dict(
        definition="k_pred: smallest odd k <= 149 with exact plurality failure <= 1e-3 on the depolarizing "
                   "2-query channel at eps_hat(pi); k_needed: smallest odd k <= 149 with mean_x delta_k(x) "
                   "<= 1e-3 on the exact vote channel of the network; optimistic = k_pred votes do not "
                   "reach the target (k_pred < k_needed, or k_needed > 149 while k_pred <= 149)",
        all=protocol_summary(prot_models), by_family={}, by_family_and_bin={},
        monotonicity_check=dict(
            rule="every 6th model of the list with k_needed <= 41: all odd k up to k_needed + 8",
            n_checked=len(mono), n_non_increasing=int(sum(m["non_increasing"] for m in mono)),
            largest_k_with_increase=max([m["largest_k_with_increase"] for m in mono if m["largest_k_with_increase"]], default=None),
            smallest_failure_after_an_increase=min([m["smallest_failure_after_an_increase"] for m in mono
                                                    if m["smallest_failure_after_an_increase"] is not None], default=None),
            note="the search needs only that no odd k below k_needed reaches the target (n_first_k_agrees); "
                 "the failure is not monotone at small k: 3 votes are worse than 1 when the vote is right "
                 "less than half of the time",
            n_first_k_agrees=int(sum(m["first_k_below_thr"] == m["k_needed"] for m in mono))))
    for fam in ("add/grok", "add/memo", "lin"):
        sel = [r for r in prot_models if r["family"] == fam]
        prot["by_family"][fam] = protocol_summary(sel)
        prot["by_family_and_bin"][fam] = {}
        for b in sorted(set(eps_bin(r["eps"]) for r in sel)):
            prot["by_family_and_bin"][fam][b] = protocol_summary([r for r in sel if eps_bin(r["eps"]) == b])
    # the same comparison with the true eps in place of eps_hat (isolates the channel shape)
    dd = [r["k_pred_true_eps"] - r["k_needed"] for r in prot_models
          if r["k_pred_true_eps"] is not None and r["k_needed"] is not None]
    prot["oracle_eps_prediction"] = dict(
        note="k predicted from the TRUE eps with the depolarizing channel, minus k_needed",
        n=len(dd), diff_mean=float(np.mean(dd)), diff_min=int(min(dd)), diff_max=int(max(dd)),
        n_optimistic=int(sum(v < 0 for v in dd)) + int(sum(
            r["k_pred_true_eps"] is not None and r["k_needed"] is None for r in prot_models)),
        n_exact=int(sum(v == 0 for v in dd)))
    prot["most_optimistic"] = [
        {k: r[k] for k in ("id", "family", "eps", "eps_hat", "k_pred", "k_needed", "mean_fail_at_k_pred", "n_uncorrectable")}
        for r in sorted([r for r in prot_models if r["optimistic"]],
                        key=lambda r: -(r["mean_fail_at_k_pred"] or 0))[:10]]
    out["protocol"] = prot
    print("protocol done %.1fs" % (time.time() - t_start), flush=True)

    # ---------------------------------------------------------------- 4. per-input confidence
    rng = np.random.default_rng(SEED + 2)
    grok = sorted([r for r in recs if r["family"] == "add/grok"], key=lambda r: (r["eps"], r["id"]))
    first_bad = next(i for i, r in enumerate(grok) if r["n_uncorrectable"] > 0)
    tied = [r for r in grok if r["eps"] == grok[first_bad]["eps"] and r["n_uncorrectable"] > 0]
    chosen = [("just below (2)", grok[first_bad - 2]), ("just below (1)", grok[first_bad - 1])] + \
             [("lowest eps with uncorrectable inputs", r) for r in tied]
    K_CONF, R_CONF = 65, 20
    thr_list = [1, 2, 3, 5, 8, 10, 15, 20, 30]
    conf = dict(k=K_CONF, repetitions_per_input=R_CONF,
                rule="add/grok models sorted by (eps, id); the first one with an uncorrectable input "
                     "(all models tied at that eps with uncorrectable inputs are reported) and the two "
                     "models before it in this order",
                note="margin = votes of the leader minus votes of the runner-up among k real votes; "
                     "SC is wrong if the leader is not f(x) or the margin is 0",
                models=[])
    for role, r in chosen:
        M = core.load_table(r["id"])
        q = r["q"]
        f = core.model_true_table(r["id"]).ravel()
        N = counts[r["id"]]
        unc = N[:, 0] <= N[:, 1:].max(1)
        xs = np.tile(np.arange(M.size), R_CONF)
        pred, margin = vote_margin(M, xs, K_CONF, rng, q)
        wrong = (pred != f[xs]) | (margin == 0)
        ent = dict(role=role, id=r["id"], p=r["p"], eps=r["eps"], n_inputs=int(M.size),
                   n_uncorrectable=int(unc.sum()), n_samples=int(xs.size),
                   sc_failure_rate=float(wrong.mean()),
                   exact_mean_failure=float(MeanFail(N).value(K_CONF)),
                   auroc=auroc_high_is_right(margin, wrong),
                   median_margin_right=float(np.median(margin[~wrong])) if (~wrong).any() else None,
                   median_margin_wrong=float(np.median(margin[wrong])) if wrong.any() else None,
                   by_threshold=[])
        for t in thr_list:
            sel = margin >= t
            ent["by_threshold"].append(dict(
                margin_at_least=t, coverage=float(sel.mean()), n_accepted=int(sel.sum()),
                n_wrong_accepted=int(wrong[sel].sum()),
                failure_rate=float(wrong[sel].mean()) if sel.any() else None))
        u = unc[xs]
        if u.any():
            ent["uncorrectable_inputs"] = dict(
                failure_rate=float(wrong[u].mean()), median_margin=float(np.median(margin[u])),
                frac_wrong_with_margin_ge_5=float((wrong[u] & (margin[u] >= 5)).mean()),
                frac_wrong_with_margin_ge_10=float((wrong[u] & (margin[u] >= 10)).mean()))
        ent["correctable_inputs"] = dict(
            failure_rate=float(wrong[~u].mean()), median_margin=float(np.median(margin[~u])),
            frac_wrong_with_margin_ge_5=float((wrong[~u] & (margin[~u] >= 5)).mean()))
        conf["models"].append(ent)
    out["confidence"] = conf
    print("confidence done %.1fs" % (time.time() - t_start), flush=True)

    # ---------------------------------------------------------------- 5. blind spots
    rng = np.random.default_rng(SEED + 3)
    base_id = pick_horizon_models(index)[0][1]
    p = by_id[base_id]["p"]
    a, b = np.meshgrid(np.arange(p), np.arange(p), indexing="ij")
    f = (a + b) % p
    g = (2 * a + b) % p
    base = core.load_table(base_id)

    def describe(name, M, extra=None):
        N = core.twirled_counts(core.make_error_table(M, f, p), p)
        gens = generator_indices(M.shape)                       # (1,0) and (0,1)
        mode = N[gens].argmax(1)                                # offset from f of the exact vote mode
        strict = N[gens].max(1) > np.sort(N[gens], axis=1)[:, -2]
        sc_vals = [int((f.ravel()[gi] + mo) % p) for gi, mo in zip(gens, mode)]
        pred, tied = core.sc_predict(M, np.repeat(gens, 1000), 65, rng, p)
        freq = [float(((pred[i * 1000:(i + 1) * 1000] == sc_vals[i]) & ~tied[i * 1000:(i + 1) * 1000]).mean())
                for i in range(len(gens))]
        pi = core.blr_pass_rate(M, p)
        d = dict(table=name, pi=pi, eps_hat=float(core.eps_hat_from_pass(pi, p)),
                 eps_naive=float(1 - pi ** (1 / 3)), eps_lower_bound=(1 - pi) / 3,
                 true_eps_wrt_f=float((M != f).mean()), distance_to_g=float((M != g).mean()),
                 sc_value_at_1_0=sc_vals[0], sc_value_at_0_1=sc_vals[1],
                 vote_mode_strict=[bool(v) for v in strict],
                 vote_mode_mass=[float(N[gi].max() / N[gi].sum()) for gi in gens],
                 real_sc65_frequency_of_that_value=freq,
                 identified_homomorphism="%d a + %d b" % (sc_vals[0], sc_vals[1]),
                 identified_is_f=bool(sc_vals == [1, 1]))
        if extra:
            d.update(extra)
        return d
    blind = dict(p=int(p), f="a + b", g="2 a + b", base_model=base_id,
                 note="pasted tables: g written on a uniformly random fraction of the inputs of the "
                      "base model's table (seed %d); SC values at the generators are the exact mode of "
                      "the vote M(x+r) - M(r) over all r, and the frequency with which 65 real votes "
                      "return it (1000 trials)" % (SEED + 3),
                 tables=[describe("pure g = 2a + b", g), describe("base model", base)])
    for frac in (0.1, 0.3, 0.5, 0.7, 0.9):
        mask = np.zeros(p * p, dtype=bool)
        mask[rng.permutation(p * p)[:int(round(frac * p * p))]] = True
        M = np.where(mask.reshape(p, p), g, base)
        blind["tables"].append(describe("base model with g pasted on %.0f%% of inputs" % (100 * frac), M,
                                        dict(pasted_fraction=frac)))
    gz = {}
    for fam in ("add/grok", "add/memo", "lin"):
        gz[fam] = {}
        for bname in sorted(set(eps_bin(r["eps"]) for r in recs if r["family"] == fam)):
            sel = [r for r in recs if r["family"] == fam and eps_bin(r["eps"]) == bname]
            gz[fam][bname] = dict(n_models=len(sel),
                                  n_generators_identified=int(sum(r["generators_identified"] for r in sel)))
    blind["zoo_generator_check"] = dict(
        note="number of models for which the exact vote mode at every generator is the true value "
             "(strictly), i.e. self-correction at the generators names the right homomorphism",
        by_family_and_bin=gz,
        lowest_eps_not_identified={
            fam: min([r["eps"] for r in recs if r["family"] == fam and not r["generators_identified"]], default=None)
            for fam in ("add/grok", "add/memo", "lin")})
    out["blind_spots"] = blind

    # ---------------------------------------------------------------- 6. two-run disagreement
    memo_recs = [r for r in index if r["family"] == "add/memo"]
    dis = dict(note="add/memo, split seed 0, init seeds 0..4 (deep ensemble of 5): all 10 pairs per "
                    "configuration; disagreement = Pr_x[M1(x) != M2(x)] over all inputs, and over the "
                    "held-out inputs only; compared with the mean error rate of the two networks",
               configs=[])
    cfgs = sorted(set((r["holdout"], r["train_frac"]) for r in memo_recs))
    allp_d, allp_e = [], []
    for ho, tf in cfgs:
        ens = sorted([r for r in memo_recs if r["holdout"] == ho and r["train_frac"] == tf and r["split_seed"] == 0],
                     key=lambda r: r["init_seed"])
        tabs = [core.load_table(r["id"]) for r in ens]
        mask = core.load_train_mask(ens[0]["id"])
        ftab = core.model_true_table(ens[0]["id"])
        pairs = []
        for i in range(len(ens)):
            for j in range(i + 1, len(ens)):
                d_all = float((tabs[i] != tabs[j]).mean())
                d_ho = float((tabs[i] != tabs[j])[~mask].mean())
                both_wrong = (tabs[i] != ftab) & (tabs[j] != ftab)
                pairs.append(dict(
                    init_seeds=[ens[i]["init_seed"], ens[j]["init_seed"]], disagreement=d_all,
                    disagreement_heldout=d_ho, mean_eps=0.5 * (ens[i]["eps"] + ens[j]["eps"]),
                    mean_heldout_error=0.5 * float((tabs[i] != ftab)[~mask].mean() + (tabs[j] != ftab)[~mask].mean()),
                    frac_both_wrong_same_answer=float((tabs[i] == tabs[j])[both_wrong].mean()) if both_wrong.any() else None))
                allp_d.append(d_all)
                allp_e.append(pairs[-1]["mean_eps"])
        dis["configs"].append(dict(
            holdout=ho, train_frac=tf, ids=[r["id"] for r in ens], eps=[r["eps"] for r in ens],
            blr_eps_hat=[by_id[r["id"]]["eps_hat"] for r in ens],
            mean_eps=float(np.mean([r["eps"] for r in ens])),
            mean_blr_eps_hat=float(np.mean([by_id[r["id"]]["eps_hat"] for r in ens])),
            mean_disagreement=float(np.mean([q_["disagreement"] for q_ in pairs])),
            min_disagreement=float(min(q_["disagreement"] for q_ in pairs)),
            max_disagreement=float(max(q_["disagreement"] for q_ in pairs)),
            ratio_disagreement_over_eps=float(np.mean([q_["disagreement"] for q_ in pairs]) / np.mean([r["eps"] for r in ens])),
            mean_disagreement_heldout=float(np.mean([q_["disagreement_heldout"] for q_ in pairs])),
            mean_heldout_error=float(np.mean([q_["mean_heldout_error"] for q_ in pairs])),
            mean_frac_both_wrong_same_answer=float(np.mean([q_["frac_both_wrong_same_answer"] for q_ in pairs
                                                            if q_["frac_both_wrong_same_answer"] is not None])),
            pairs=pairs))
    dis["all_pairs"] = dict(
        n_pairs=len(allp_d), pearson_r=float(np.corrcoef(allp_d, allp_e)[0, 1]),
        mean_abs_gap=float(np.mean(np.abs(np.array(allp_d) - np.array(allp_e)))),
        max_abs_gap=float(np.max(np.abs(np.array(allp_d) - np.array(allp_e)))),
        mean_signed_gap=float(np.mean(np.array(allp_d) - np.array(allp_e))))
    memo35 = [r for r in recs if r["family"] == "add/memo"]
    dis["blr_on_same_family"] = dict(
        n_models=len(memo35), mae_eps_hat=float(np.mean([abs(r["err_hat"]) for r in memo35])),
        max_abs_err_eps_hat=float(max(abs(r["err_hat"]) for r in memo35)),
        bias_eps_hat=float(np.mean([r["err_hat"] for r in memo35])))
    out["disagreement_baseline"] = dis

    # ---------------------------------------------------------------- validation of fail_bounds
    vrng = np.random.default_rng(SEED + 4)
    worst_diff, n_cases, viol = 0.0, 0, 0
    for mid in [i for _, i in pick_horizon_models(index)][:3] + [chosen[-1][1]["id"]]:
        N = counts[mid]
        P = N / N.sum(1, keepdims=True)
        rows = vrng.choice(len(P), size=200, replace=False)
        for k in (1, 2, 3, 5, 8, 9, 17, 33, 40):
            ex = core.plurality_fail_exact(P[rows], k)
            lo, hi = fail_bounds(P[rows], k, 1e-11)
            worst_diff = max(worst_diff, float(np.abs(0.5 * (lo + hi) - ex).max()))
            viol += int(((ex < lo - 1e-11) | (ex > hi + 1e-11)).sum())
            n_cases += len(rows)
    out["fail_bounds_validation"] = dict(
        note="fail_bounds vs core.plurality_fail_exact on 200 random inputs of 4 models, 9 values of k",
        n_cases=n_cases, max_abs_difference=worst_diff, n_outside_bounds=viol)

    out["models"] = [{k: v for k, v in r.items() if k not in ("run_id",)} | {"run_id": r["run_id"]} for r in recs]
    out["runtime_seconds"] = round(time.time() - t_start, 1)
    path = os.path.join(core.RESULTS_DIR, "exp_labelfree.json")
    with open(path, "w") as fh:
        json.dump(out, fh, indent=1)
    print("wrote", path, "%.1fs" % (time.time() - t_start), flush=True)
    make_figure(out)


def make_figure(out=None):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import paperstyle as ps
    ps.apply()
    if out is None:
        with open(os.path.join(core.RESULTS_DIR, "exp_labelfree.json")) as fh:
            out = json.load(fh)
    recs = out["models"]
    fams = [("add/grok", ps.BLUE, "o", "modular addition (1080)"),
            ("lin", ps.ORANGE, "s", "linear map on $Z_7^4$ (108)")]
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 3.4))
    ax = axes[0]
    ax.plot([0, 1], [0, 1], color=ps.REFERENCE, lw=1.2, ls="--", zorder=1, label="identity")
    for fam, col, mk, lab in fams:
        sel = [r for r in recs if r["family"] == fam]
        ax.scatter([r["eps"] for r in sel], [r["eps_hat"] for r in sel], s=16, color=col, marker=mk,
                   alpha=0.55, linewidths=0, label=lab, zorder=3)
    ax.set_xlim(-0.03, 1.0)
    ax.set_ylim(-0.03, 1.32)
    ax.set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2])
    ax.set_xlabel("true error rate $\\varepsilon$ (needs labels)")
    ax.set_ylabel("label-free estimate $\\hat\\varepsilon$ from the pass rate")
    ax.set_title("a  Error rate without labels")
    ax.legend(loc="upper left", handletextpad=0.4)

    ax = axes[1]
    top = 220.0
    ax.plot([1, 149], [1, 149], color=ps.REFERENCE, lw=1.2, ls="--", zorder=1)
    rng = np.random.default_rng(0)
    fams_b = [("add/grok", ps.BLUE, "o", "modular addition"), ("lin", ps.ORANGE, "s", "linear map"),
              ("add/memo", ps.AQUA, "D", "memorising nets")]
    n_above = 0
    for fam, col, mk, lab in fams_b:
        sel = [r for r in recs if r["family"] == fam and r.get("k_pred") is not None and "k_needed" in r]
        x = np.array([r["k_pred"] for r in sel], dtype=float)
        y = np.array([r["k_needed"] if r["k_needed"] is not None else top for r in sel], dtype=float)
        n_above += int(sum(r["k_needed"] is None for r in sel))
        jit = np.exp(rng.normal(0, 0.018, size=(2, len(sel))))
        ax.scatter(x * jit[0], y * np.where(y == top, 1.0, jit[1]), s=18, color=col, marker=mk, alpha=0.55,
                   linewidths=0, label=lab, zorder=3)
    ax.axhline(149, color=ps.AXIS, lw=0.8)
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(0.8, 190)
    ax.set_ylim(0.8, 300)
    ticks = [1, 3, 9, 27, 81, 149]
    ax.set_xticks(ticks)
    ax.set_xticklabels([str(t) for t in ticks])
    ax.set_yticks(ticks)
    ax.set_yticklabels([str(t) for t in ticks])
    ax.minorticks_off()
    ax.set_xlabel("votes predicted from the pass rate alone")
    ax.set_ylabel("votes needed (exact channel)")
    ax.set_title("b  Votes for failure $\\leq 10^{-3}$")
    ax.text(0.9, top, "needed > 149 (%d models)" % n_above, color=ps.INK2, fontsize=8.5, va="center", ha="left")
    ax.legend(loc="lower right", handletextpad=0.3)
    fig.tight_layout(w_pad=2.0)
    ps.save(fig, os.path.join(core.FIG_DIR, "fig_labelfree"))
    plt.close(fig)
    print("wrote figures/fig_labelfree", flush=True)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--figure-only":
        make_figure()
    else:
        main()

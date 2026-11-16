"""exp_twirls.py -- package B1: the twirl hierarchy against baselines at matched query budget.

    OMP_NUM_THREADS=1 python3 code/exp_twirls.py          (about 3.5 minutes, one process)

writes results/exp_twirls.json and figures/fig_twirls.{svg,png}.

Models: the add/memo family (p = 53; pure memorisers whose error set is the hold-out mask) in the
configurations random train_frac 0.7, random train_frac 0.5 and class hold-out; for each, the seven
models (split_seed, init_seed) in {(0,0..4), (1,0), (2,0)}.  Plus four add/grok p = 47 snapshots
(organic errors) chosen by a stated rule.

Methods, all evaluated at a budget of Q model queries per answer:
  plain        argmax of the network (Q = 1)
  sampling     plurality of Q samples from softmax(logits), temperature 1          (exact)
  ensemble     plurality of the 5 nets of a split (Q = 5); argmax of averaged logits (Q = 5)
  invariance   plurality of Q orbit votes M(a+r, b-r)                              (exact)
  translation  plurality of Q/2 BLR votes M(x+r) - M(r)                            (exact)
  concat_j3    plurality of Q/6 BLR votes whose two queries are each replaced by the plurality of
               3 orbit votes (three distinct votes: the first one is used)         (exact)
A tie for first place is a failure everywhere.  "Exact" = the multinomial plurality failure of the
exactly enumerated vote channel of every input, by plur_fail() below (validated against
core.plurality_fail_exact and extended to k > 150).
"""
import json
import math
import os
import sys
import time

import numpy as np
from scipy.special import gammaln
from scipy.stats import binom

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import core  # noqa: E402

BUDGETS = [1, 2, 4, 6, 10, 18, 34, 66, 130, 258]
CONCAT_J = 3
CONCAT_K = [1, 3, 5, 11, 21, 43]            # budget 6k = 6, 18, 30, 66, 126, 258
MEMO_CONFIGS = [("random_f0.7", "random", 0.7), ("random_f0.5", "random", 0.5), ("class5", "class", None)]
MEMO_SEEDS = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (2, 0)]     # (split_seed, init_seed)
GROK_TARGETS = [0.1, 0.3, 0.5, 0.65]
RES_TOL = 1e-13          # inputs whose Chernoff bracket is narrower than this skip the exact sum
TAIL_TOL = 1e-16         # per-wrong-value cap on the neglected count tail
PM_TOL = 1e-17           # binomial terms Pr[N_0 = m] below this are skipped
ABS_ACC = 1e-12          # absolute accuracy claimed for plur_fail
RELIABLE = 1e-10         # mean errors below this are flagged: quote the Chernoff upper bound instead
N_REAL = 1000            # real-vote trials per input in the cross-check
MC_SEED = 20261116


# --------------------------------------------------------------------------------------------
# exact plurality failure for any k
# --------------------------------------------------------------------------------------------
def _mul_trunc_exp(poly, u, J):
    """poly(y) * sum_{j <= J} (u y)^j / j!, truncated at the degree of poly.  poly (X, D+1), u (X,)."""
    D = poly.shape[1] - 1
    J = min(int(J), D)
    if J <= 0:
        return poly
    new = poly.copy()
    c = np.ones(len(u))
    for j in range(1, J + 1):
        c = c * u / j
        new[:, j:] += poly[:, :D + 1 - j] * c[:, None]
    return new


def _exp_series(U, D):
    """(X, D+1) array of U^j / j!."""
    e = np.ones((len(U), D + 1))
    for j in range(1, D + 1):
        e[:, j] = e[:, j - 1] * U / j
    return e


def _dp_success(t0, W, k):
    """Pr[N_0 > max_h N_h], N ~ Multinomial(k, (t0, W)), for rows with t0 > 0.  W (X, C) holds the
    wrong masses sorted in decreasing order along each row.  All sums have non-negative terms.
    Returns a lower bound S' with S' <= S <= S' + eta, eta <= C * TAIL_TOL + k * PM_TOL."""
    X, C = W.shape
    sig = float(k)                                   # y = z / sig keeps every coefficient in range
    u = W * sig
    lf = gammaln(np.arange(k + 2) + 1.0)             # lf[i] = ln i!
    logt0 = np.log(t0)
    log1m = np.log1p(-np.minimum(t0, 1.0 - 1e-300))
    # per-column count caps: Pr[Bin(k, max_x W[x, c]) > J_c] <= TAIL_TOL
    sf = binom.sf(np.arange(k + 1)[None, :], k, W.max(0)[:, None])
    J = (sf <= TAIL_TOL).argmax(1).astype(int)
    Jmax = int(J.max()) if C else 0
    success = np.zeros(X)
    # low block: m <= Jmax, every wrong count < min(m, J_c + 1)
    for m in range(1, min(Jmax, k) + 1):
        d = k - m
        caps = np.minimum(J, m - 1)
        if caps.sum() < d:
            continue
        with np.errstate(under="ignore"):
            pm = np.exp(lf[k] - lf[m] - lf[d] + m * logt0 + (d * log1m if d else 0.0))
        act = np.flatnonzero(pm >= PM_TOL)
        if len(act) == 0:
            continue
        free = caps >= d
        poly = np.zeros((len(act), d + 1))
        poly[:, 0] = 1.0
        ua = u[act]
        for c in np.flatnonzero(~free):
            if caps[c] > 0:
                poly = _mul_trunc_exp(poly, ua[:, c], caps[c])
        coef = (poly[:, ::-1] * _exp_series(ua[:, free].sum(1), d)).sum(1)
        success[act] += np.exp(lf[k] - lf[m] + m * logt0[act] - d * math.log(sig)) * coef
    # high block: m > Jmax, every wrong count <= J_c
    if Jmax < k:
        D = k - Jmax - 1
        free = J >= D
        poly = np.zeros((X, D + 1))
        poly[:, 0] = 1.0
        for c in np.flatnonzero(~free):
            if J[c] > 0:
                poly = _mul_trunc_exp(poly, u[:, c], J[c])
        if free.any():
            e = _exp_series(u[:, free].sum(1), D)
            full = np.zeros_like(poly)
            for j in range(D + 1):
                full[:, j:] += poly[:, :D + 1 - j] * e[:, j:j + 1]
            poly = full
        for m in range(Jmax + 1, k + 1):
            d = k - m
            with np.errstate(under="ignore"):
                success += np.exp(lf[k] - lf[m] + m * logt0 - d * math.log(sig)) * poly[:, d]
    return success


def plur_fail(T, k):
    """Failure probability of the k-vote plurality (truth = column 0 must be the strict plurality) for
    every row of the channel T (X, q); any k >= 1.  Absolute accuracy about 1e-12 (the same as
    core.plurality_fail_exact, which it reproduces for k <= 150): rows whose rigorous Chernoff bracket
    is already narrower than RES_TOL return the upper bound, all other rows the exact sum.
    Identical rows (up to the order of the wrong values) are computed once."""
    T = np.atleast_2d(np.asarray(T, dtype=float))
    k = int(k)
    t0 = T[:, 0]
    W = -np.sort(-T[:, 1:], axis=1)
    W = W[:, W.max(0) > 0]
    key = np.concatenate([t0[:, None], W], axis=1)
    uniq, inv = np.unique(key, axis=0, return_inverse=True)
    inv = np.asarray(inv).ravel()
    t0, W = uniq[:, 0], uniq[:, 1:]
    X = len(t0)
    fail = np.full(X, np.nan)
    if W.shape[1] == 0:
        fail[:] = np.where(t0 > 0, 0.0, 1.0)
        return fail[inv]
    w1 = W[:, 0]
    st0 = np.sqrt(t0)[:, None]
    base = np.where(W < t0[:, None], 1.0 - (st0 - np.sqrt(W)) ** 2, 1.0)
    base = np.where(W > 0, base, 0.0)               # a value that never occurs cannot win or tie alone
    upper = np.minimum(1.0, (base ** k).sum(1))
    lower = np.where(w1 > t0, 1.0 - (1.0 - (np.sqrt(w1) - np.sqrt(t0)) ** 2) ** k, 0.0)
    fail[t0 <= 0] = 1.0
    fail[w1 <= 0] = 0.0
    lo_ok = np.isnan(fail) & (upper <= RES_TOL)
    fail[lo_ok] = upper[lo_ok]
    hi_ok = np.isnan(fail) & (lower >= 1.0 - RES_TOL)
    fail[hi_ok] = 1.0
    todo = np.flatnonzero(np.isnan(fail))
    if len(todo):
        Wt = W[todo]
        Wt = Wt[:, Wt.max(0) > 0]
        fail[todo] = np.clip(1.0 - _dp_success(t0[todo], Wt, k), 0.0, 1.0)
    return fail[inv]


def chernoff_mean(T, k):
    """Mean over inputs of the Chernoff/union upper bound (to quote when the exact value is < 1e-12)."""
    return float(core.chernoff_union_bound(T, k).mean())


def validate_plur_fail():
    """plur_fail against core.plurality_fail_exact (k <= 150), brute-force enumeration (tiny) and Monte
    Carlo (k = 258)."""
    rng = np.random.default_rng(424242)
    out = {"vs_core": [], "seed": 424242}
    cases = []
    for q, conc in [(5, 1.0), (31, 0.3), (53, 0.05)]:
        Tm = rng.dirichlet(np.full(q, conc), size=40)
        Tm[0] = 0.0; Tm[0, 0] = 1.0                               # truth certain
        Tm[1, 0] = 0.0; Tm[1] /= Tm[1].sum()                      # truth impossible
        Tm[2, 1] = Tm[2, 0]; Tm[2] /= Tm[2].sum()                 # exact tie of the two leaders
        Tm[3:10, 0] += 1.0; Tm[3:10] /= Tm[3:10].sum(1, keepdims=True)   # truth dominant
        cases.append((f"dirichlet_q{q}", Tm))
    E = core.error_table("addmemo_p53_f0.5_ss0_is0_t00200")
    cases.append(("blr_addmemo_f0.5_rows0-39", core.twirled_channel(E, 53)[:40]))
    cases.append(("inv_addmemo_f0.5_distinct_rows", np.unique(core.invariance_channel_add(E, 53), axis=0)))
    worst = 0.0
    for name, Tm in cases:
        for k in (1, 2, 3, 5, 9, 17, 33, 65, 129, 150):
            Tk = Tm[:12] if (k > 65 and Tm.shape[1] > 40) else Tm
            a = plur_fail(Tk, k)
            b = core.plurality_fail_exact(Tk, k)
            dmax = float(np.abs(a - b).max())
            worst = max(worst, dmax)
            out["vs_core"].append({"case": name, "k": k, "rows": int(Tk.shape[0]), "max_abs_diff": dmax,
                                   "fail_min": float(b.min()), "fail_max": float(b.max())})
    out["vs_core_max_abs_diff"] = worst
    # tiny brute force
    t = np.array([0.4, 0.3, 0.2, 0.1])
    out["vs_enum_q4_k6_abs_diff"] = float(abs(plur_fail(t, 6)[0] - core.plurality_fail_enum(t, 6)))
    # k = 258 (beyond the range of core.plurality_fail_exact) against Monte Carlo, on weak channels where the
    # failure is of order 0.01 - 1: depolarizing rows with lambda^2 in {0.02, 0.04, 0.08} mixed with Dirichlet noise
    rows = []
    for l2 in (0.02, 0.04, 0.08):
        base = np.full(53, (1 - l2) / 53)
        base[0] = 1 / 53 + (52 / 53) * l2
        for _ in range(4):
            r_ = 0.8 * base + 0.2 * rng.dirichlet(np.full(53, 2.0))
            r_[0] = base[0]
            rows.append(r_ / r_.sum())
    Tw = np.array(rows)
    ex = plur_fail(Tw, 258)
    n_mc = 40000
    mc = core.plurality_fail_mc(Tw, 258, n_mc, np.random.default_rng(MC_SEED))
    se = np.sqrt(np.maximum(ex * (1 - ex), 1e-12) / n_mc)
    # concatenated channel: closed form against brute force (inner law by enumerating all p^3 triples of
    # level-set members; outer law by enumerating all r in G), four inputs of two models
    cc = []
    for mid in ("addmemo_p53_f0.7_ss0_is0_t00200", "addmemo_p53_class5_ss0_is0_t00200"):
        Ec = core.error_table(mid)
        p_ = Ec.shape[0]
        Tc = concat_channel(Ec, p_)
        ar = np.arange(p_)
        A_off = np.zeros((p_, p_))
        for c in range(p_):
            vals = Ec[ar, (c - ar) % p_]
            v0, v1, v2 = np.meshgrid(vals, vals, vals, indexing="ij")
            A_off[c] = np.bincount(np.where(v1 == v2, v1, v0).ravel(), minlength=p_) / p_ ** 3
        lev_r = ((ar[:, None] + ar[None, :]) % p_).ravel()
        dmax = 0.0
        for x in (0, 57, 1000, 2808):
            lev_x = (x // p_ + x % p_) % p_
            Tb = np.array([(A_off[(lev_r + lev_x) % p_][:, (ar + h) % p_] * A_off[lev_r]).sum() for h in range(p_)])
            dmax = max(dmax, float(np.abs(Tb / p_ ** 2 - Tc[x]).max()))
        cc.append({"model": mid, "inputs": [0, 57, 1000, 2808], "max_abs_diff": dmax})
    out["concat_channel_vs_brute_force"] = cc
    out["k258_vs_mc"] = {"rows": int(len(Tw)), "n_samples_per_row": n_mc, "seed": MC_SEED,
                         "exact": [float(v) for v in ex], "mc": [float(v) for v in mc],
                         "max_abs_z": float(np.abs((mc - ex) / se).max()),
                         "rms_z": float(np.sqrt((((mc - ex) / se) ** 2).mean()))}
    return out


# --------------------------------------------------------------------------------------------
# channels of the methods
# --------------------------------------------------------------------------------------------
def softmax_channel(model_id):
    """S[x, h] = softmax(logits(x))[f(x) + h]: the offset channel of one temperature-1 sample."""
    L = core.load_logits(model_id).astype(np.float64)
    q = L.shape[1]
    f = core.model_true_table(model_id).ravel()
    P = np.exp(L - L.max(1, keepdims=True))
    P /= P.sum(1, keepdims=True)
    return P[np.arange(len(f))[:, None], (f[:, None] + np.arange(q)[None, :]) % q]


def inner3_channel(I):
    """Offset distribution of the plurality of 3 i.i.d. votes from each row of I, where three distinct
    votes are resolved to the first vote:  a(h) = 3 I_h^2 - 2 I_h^3 + I_h ((1 - I_h)^2 - sum_{g != h} I_g^2)."""
    s2 = (I ** 2).sum(1, keepdims=True)
    return 3 * I ** 2 - 2 * I ** 3 + I * ((1 - I) ** 2 - (s2 - I ** 2))


def concat_channel(E, q):
    """Channel of the concatenated vote A(x+r) - A(r), A(y) = plurality of 3 orbit votes at y.
    The inner offset law depends only on the level f(y); for r uniform on G the pair of levels is
    (c + f(x), c) with c uniform, so T_x(h) = (1/p) sum_c sum_g a_{c+f(x)}(g+h) a_c(g)."""
    p = E.shape[0]
    Iv = core.invariance_channel_add(E, q)                      # rows (a, b); depends on a + b only
    a = inner3_channel(Iv[np.arange(p)])                        # level c = 0 + c  -> row index c
    assert np.allclose(a.sum(1), 1.0)
    Tl = np.zeros((p, q))
    g = np.arange(q)
    for h in range(q):
        for lev in range(p):
            Tl[lev, h] = (a[(np.arange(p) + lev) % p][:, (g + h) % q] * a).sum() / p
    lev_of = (np.arange(p)[:, None] + np.arange(p)[None, :]) % p
    return Tl[lev_of.ravel()]


def concat_real_fail(M, f, k, n_trials, rng):
    """Real concatenated voting on the table M (p, p): fraction of failures per input."""
    p = M.shape[0]
    q = p
    X = p * p
    xs = np.arange(X)
    xa, xb = xs // p, xs % p
    fails = np.zeros(X)

    def A(a, b):
        s = rng.integers(0, p, size=a.shape + (3,))
        v = M[(a[..., None] + s) % p, (b[..., None] - s) % p]
        out = v[..., 0].copy()
        out = np.where(v[..., 1] == v[..., 2], v[..., 1], out)
        return out

    for _ in range(n_trials):
        ra = rng.integers(0, p, size=(X, k))
        rb = rng.integers(0, p, size=(X, k))
        votes = (A((xa[:, None] + ra) % p, (xb[:, None] + rb) % p) - A(ra, rb)) % q
        pred, tied = core.plurality(votes, q)
        fails += (pred != f.ravel()) | tied
    return fails / n_trials


def curve(T, ks, budgets):
    """mean / worst exact failure of the k-vote plurality for each k.  'reliable' is False when the mean is
    below RELIABLE (1e-10): such values are dominated by Chernoff upper bounds and by round-off, and only
    'chernoff_mean_upper' (a rigorous upper bound on the mean) should be quoted for them."""
    rows = []
    for k, Q in zip(ks, budgets):
        d = plur_fail(T, k)
        rows.append({"Q": int(Q), "k": int(k), "mean_err": float(d.mean()), "worst_err": float(d.max()),
                     "chernoff_mean_upper": chernoff_mean(T, k), "reliable": bool(d.mean() >= RELIABLE)})
    return rows


def analyse_model(mid, with_logits, with_concat):
    rec = core.get_record(mid)
    q = rec["q"]
    E = core.error_table(mid)
    eps = float((E != 0).mean())
    out = {"id": mid, "eps": eps, "p": rec["p"], "split_seed": rec["split_seed"], "init_seed": rec["init_seed"],
           "holdout": rec["holdout"], "train_frac": rec["train_frac"], "step": rec["step"]}
    m = {}
    m["plain"] = [{"Q": 1, "mean_err": eps, "worst_err": 1.0 if eps > 0 else 0.0}]
    if with_logits:
        S = softmax_channel(mid)
        assert ((S.argmax(1) != 0) == (E.ravel() != 0)).all()          # float16 logits reproduce the table
        m["sampling"] = curve(S, BUDGETS, BUDGETS)
        st = core.channel_stats(S)
        out["sampling_limit_err"] = float(1.0 - st["strict_mode"].mean())   # Q -> infinity: argmax
        out["softmax_mean_true_prob"] = float(S[:, 0].mean())
    Ti = core.invariance_channel_add(E, q)
    sti = core.channel_stats(Ti)
    out["invariance_floor"] = float(1.0 - sti["strict_mode"].mean())      # level-set mode is not the truth
    out["invariance_t0_min"] = float(sti["t0"].min())
    out["invariance_t0_mean"] = float(sti["t0"].mean())
    out["invariance_margin_min"] = float(sti["margin"].min())
    m["invariance"] = curve(Ti, BUDGETS, BUDGETS)
    bo = [Q for Q in BUDGETS if Q >= 2]
    m["invariance_km1"] = curve(Ti, [Q - 1 for Q in bo], bo)          # Q - 1 votes: odd k, no two-way ties
    Tt = core.twirled_channel(E, q)
    stt = core.channel_stats(Tt)
    out["translation_floor"] = float(1.0 - stt["strict_mode"].mean())
    out["translation_t0_min"] = float(stt["t0"].min())
    nz = np.arange(Tt.shape[0]) != 0
    out["translation_t0_mean_x_ne_0"] = float(stt["t0"][nz].mean())
    out["translation_margin_min"] = float(stt["margin"].min())
    out["pc_law_c2"] = float(core.pc_law(eps, q, 2))
    bt = [Q for Q in BUDGETS if Q >= 2]
    m["translation"] = curve(Tt, [Q // 2 for Q in bt], bt)
    if with_concat:
        Tc = concat_channel(E, q)
        stc = core.channel_stats(Tc)
        out["concat_floor"] = float(1.0 - stc["strict_mode"].mean())
        out["concat_t0_min"] = float(stc["t0"].min())
        m["concat_j3"] = curve(Tc, CONCAT_K, [2 * CONCAT_J * k for k in CONCAT_K])
    out["methods"] = m
    return out


def ensemble(ids):
    """Plurality of the argmax of 5 nets (tie = failure) and argmax of the averaged logits / probabilities."""
    f = core.model_true_table(ids[0]).ravel()
    q = core.get_record(ids[0])["q"]
    preds = np.stack([core.load_table(i).ravel() for i in ids], axis=1)
    win, tied = core.plurality(preds, q)
    Ls = np.stack([core.load_logits(i).astype(np.float64) for i in ids])
    avg_logit = Ls.mean(0).argmax(1)
    Ps = np.exp(Ls - Ls.max(2, keepdims=True))
    Ps /= Ps.sum(2, keepdims=True)
    avg_prob = Ps.mean(0).argmax(1)
    wrong_all = (preds != f[:, None]).all(1)
    return {"members": list(ids), "Q": len(ids),
            "plurality_err": float(((win != f) | tied).mean()),
            "plurality_tie_frac": float(tied.mean()),
            "plurality_wrong_untied_frac": float(((win != f) & ~tied).mean()),
            "plurality_err_if_ties_broken_to_smallest": float((win != f).mean()),
            "avg_logit_err": float((avg_logit != f).mean()),
            "avg_prob_err": float((avg_prob != f).mean()),
            "frac_inputs_all_members_wrong": float(wrong_all.mean()),
            "member_eps": [float((preds[:, j] != f).mean()) for j in range(len(ids))]}


def aggregate(models):
    """Per method and budget: statistics over the models of a configuration."""
    agg = {}
    for meth in models[0]["methods"]:
        rows = []
        for i, r0 in enumerate(models[0]["methods"][meth]):
            me = np.array([mm["methods"][meth][i]["mean_err"] for mm in models])
            we = np.array([mm["methods"][meth][i]["worst_err"] for mm in models])
            row = {"Q": r0["Q"], "n_models": len(models), "mean_err_mean": float(me.mean()),
                   "mean_err_median": float(np.median(me)), "mean_err_min": float(me.min()),
                   "mean_err_max": float(me.max()), "worst_err_mean": float(we.mean()),
                   "worst_err_max": float(we.max())}
            if "k" in r0:
                row["k"] = r0["k"]
            if "chernoff_mean_upper" in r0:
                row["chernoff_mean_upper_max"] = float(max(mm["methods"][meth][i]["chernoff_mean_upper"] for mm in models))
            rows.append(row)
        agg[meth] = rows
    return agg


def budget_to_reach(rows, target):
    for r in rows:
        if r["mean_err"] <= target:
            return r["Q"]
    return None


def winners(agg):
    """At each budget: the method with the smallest mean error (mean over the models), among the methods
    that can be run with at most that budget (each at its largest budget <= Q)."""
    out = []
    for Q in BUDGETS:
        best = {}
        for meth, rows in agg.items():
            ok = [r for r in rows if r["Q"] <= Q]
            if ok:
                best[meth] = min(r["mean_err_mean"] for r in ok)
        w = min(best, key=lambda z: best[z])
        out.append({"Q": Q, "winner": w, "mean_err_by_method": best})
    return out


# --------------------------------------------------------------------------------------------
def make_figure(res, path):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import paperstyle as ps
    ps.apply()
    YMIN = 1e-9
    fig, axes = plt.subplots(1, 2, figsize=(7.4, 3.4), sharey=True)
    panels = [("random_f0.7", "a  Scattered errors (random hold-out)"),
              ("class5", "b  Answer-dependent errors (class hold-out)")]
    for ax, (cfg, title) in zip(axes, panels):
        block = res["memo"][cfg]
        mod = block["models"][0]
        assert mod["split_seed"] == 0 and mod["init_seed"] == 0
        eps = mod["eps"]
        ax.axhline(eps, color=ps.REFERENCE, lw=1.4, ls=(0, (4, 3)), label="plain argmax (1 query)", zorder=1)
        series = [("sampling", "same-input sampling vote", ps.BLUE, "o"),
                  ("invariance", "invariance twirl (orbit votes)", ps.ORANGE, "s"),
                  ("translation", "translation twirl (self-corrector votes)", ps.AQUA, "D")]
        for meth, lab, col, mk in series:
            rows = mod["methods"][meth]
            Q = np.array([r["Q"] for r in rows], float)
            y = np.array([r["mean_err"] for r in rows])
            keep = y >= YMIN
            # extend each line one point below the frame so that it visibly leaves the panel
            n_keep = int(keep.sum())
            if n_keep < len(y):
                Qp, yp = Q[:n_keep + 1], np.maximum(y[:n_keep + 1], YMIN * 1e-3)
            else:
                Qp, yp = Q, y
            ax.plot(Qp, yp, color=col, lw=2.0, zorder=3)
            ax.plot(Q[keep], y[keep], ls="none", marker=mk, ms=6.5, color=col, label=lab, zorder=4)
        en = block["ensemble"]
        ax.plot([en["Q"]], [en["plurality_err"]], ls="none", marker="^", ms=9, color=ps.YELLOW,
                label="5-net ensemble (5 queries)", zorder=5)
        ax.set_xscale("log")
        ax.set_yscale("log")
        ax.set_ylim(YMIN, 2.0)
        ax.set_xlim(0.8, 400)
        ax.set_xticks([1, 2, 4, 10, 34, 130])
        ax.set_xticks([], minor=True)
        ax.set_xticklabels(["1", "2", "4", "10", "34", "130"])
        ax.set_yticks([1, 1e-2, 1e-4, 1e-6, 1e-8])
        ax.set_xlabel("model queries per answer, Q")
        ax.set_title(title, fontsize=10)
        floor = mod["invariance_floor"]

        def sci(v):
            e = int(math.floor(math.log10(v)))
            return f"${v / 10 ** e:.1f}\\times10^{{{e}}}$"
        iv = {r["Q"]: r["mean_err"] for r in mod["methods"]["invariance"]}
        tr = {r["Q"]: r["mean_err"] for r in mod["methods"]["translation"]}
        if cfg == "class5":
            ax.annotate(f"invariance floor =\nplain error = {floor:.3f}", xy=(150, floor), xytext=(40, 1.5e-3),
                        fontsize=8.5, color=ps.INK, ha="left", va="center",
                        arrowprops=dict(arrowstyle="-", color=ps.MUTED, lw=0.8))
            ax.annotate(sci(tr[18]), xy=(18, tr[18]), xytext=(23, tr[18]), fontsize=8.5, color=ps.INK,
                        ha="left", va="center")
        else:
            ax.annotate(f"plain error = {eps:.2f}\ninvariance floor = {floor:.0f}", xy=(1, eps), xytext=(0.92, 8e-9),
                        fontsize=8.5, color=ps.INK, ha="left", va="center")
            ax.annotate(sci(iv[34]), xy=(34, iv[34]), xytext=(27, iv[34]), fontsize=8.5, color=ps.INK,
                        ha="right", va="center")
            ax.annotate(sci(tr[66]), xy=(66, tr[66]), xytext=(84, tr[66]), fontsize=8.5, color=ps.INK,
                        ha="left", va="center")
    axes[0].set_ylabel("mean error over all inputs")
    h, l = axes[0].get_legend_handles_labels()
    fig.legend(h, l, loc="lower center", ncol=3, bbox_to_anchor=(0.5, -0.13), columnspacing=1.4, handletextpad=0.5)
    fig.tight_layout(w_pad=1.2)
    ps.save(fig, path)
    plt.close(fig)


# --------------------------------------------------------------------------------------------
def main():
    t_start = time.time()
    idx = core.load_index()
    res = {"description": "B1: methods at matched query budget (see the module docstring of code/exp_twirls.py)",
           "config": {"budgets_Q": BUDGETS, "translation_votes": "k = Q/2", "invariance_votes": "k = Q",
                      "sampling_votes": "k = Q samples from softmax(logits) at temperature 1 (float16 cached logits)",
                      "concat": {"inner_orbit_votes_j": CONCAT_J, "outer_blr_votes_k": CONCAT_K,
                                 "budget": "Q = 2 j k", "inner_tie_rule": "three distinct orbit votes -> the first vote"},
                      "ensemble": "split_seed 0, init_seed 0..4; plurality of the five argmax tables (tie = failure), "
                                  "and argmax of the mean logits",
                      "tie_rule": "a tie for first place is a failure",
                      "memo_configs": [c[0] for c in MEMO_CONFIGS], "memo_seeds_split_init": MEMO_SEEDS,
                      "grok_rule": "add/grok p=47 snapshot with eps closest to each target (ties: smallest id), "
                                   "over all 360 snapshots of the 12 runs",
                      "grok_targets": GROK_TARGETS,
                      "exact_method": "plur_fail(): multinomial plurality failure of the exactly enumerated channel of "
                                      "every input; absolute accuracy ~1e-12 per input; rows with reliable = false "
                                      "(mean_err < 1e-10) are not exact: quote chernoff_mean_upper (a rigorous "
                                      "upper bound on the mean) for them",
                      "tolerances": {"RES_TOL": RES_TOL, "TAIL_TOL": TAIL_TOL, "PM_TOL": PM_TOL, "ABS_ACC": ABS_ACC,
                                     "RELIABLE": RELIABLE},
                      "real_vote_trials_per_input": N_REAL, "mc_seed": MC_SEED,
                      "invariance_km1": "the invariance twirl with Q - 1 votes (odd number of votes for even Q)",
                      "unit_note": "models sharing a split or an initialisation are not independent; n = 7 models per "
                                   "configuration = 5 initialisations of split 0 + splits 1, 2 at initialisation 0"}}
    print("validating plur_fail ...", flush=True)
    res["validation"] = validate_plur_fail()
    print("  max |plur_fail - core| =", res["validation"]["vs_core_max_abs_diff"],
          " k=258 vs MC max |z| =", res["validation"]["k258_vs_mc"]["max_abs_z"], flush=True)

    memo = {}
    for name, holdout, tf in MEMO_CONFIGS:
        recs = [r for r in idx if r["family"] == "add/memo" and r["holdout"] == holdout
                and (tf is None or abs(r["train_frac"] - tf) < 1e-9)]
        models = []
        for ss, isd in MEMO_SEEDS:
            (r,) = [x for x in recs if x["split_seed"] == ss and x["init_seed"] == isd]
            t0 = time.time()
            models.append(analyse_model(r["id"], with_logits=True, with_concat=True))
            print(f"  {r['id']}  eps={r['eps']:.4f}  {time.time() - t0:.1f}s", flush=True)
        ens_ids = [m["id"] for m in models if m["split_seed"] == 0]
        block = {"models": models, "ensemble": ensemble(ens_ids),
                 "heldout_classes": recs[0].get("heldout_classes") if holdout == "class" else None,
                 "aggregate_all7": aggregate(models),
                 "aggregate_init_seeds_split0": aggregate([m for m in models if m["split_seed"] == 0]),
                 "aggregate_split_seeds_init0": aggregate([m for m in models if m["init_seed"] == 0])}
        block["winner_by_budget"] = winners(block["aggregate_all7"])
        block["budget_to_reach"] = {
            str(t): {meth: [budget_to_reach(m["methods"][meth], t) for m in models]
                     for meth in ("sampling", "invariance", "invariance_km1", "translation", "concat_j3")}
            for t in (1e-2, 1e-3, 1e-6)}
        block["summary_scalars"] = {
            "eps_mean": float(np.mean([m["eps"] for m in models])),
            "invariance_floor_all": [m["invariance_floor"] for m in models],
            "translation_floor_all": [m["translation_floor"] for m in models],
            "concat_floor_all": [m["concat_floor"] for m in models],
            "sampling_limit_err_all": [m["sampling_limit_err"] for m in models],
            "sampling_minus_plain_at_Q": {str(Q): float(np.mean([m["methods"]["sampling"][i]["mean_err"] - m["eps"]
                                                                 for m in models]))
                                          for i, Q in enumerate(BUDGETS)},
            "sampling_min_over_Q_minus_plain_min_over_models": float(min(
                min(r["mean_err"] for r in m["methods"]["sampling"]) - m["eps"] for m in models))}
        memo[name] = block
    res["memo"] = memo

    # real-vote cross-checks on the two figure models at Q = 18
    xc = []
    for cfg in ("random_f0.7", "class5"):
        mod = memo[cfg]["models"][0]
        M = core.load_table(mod["id"])
        f = core.model_true_table(mod["id"])
        E = core.error_table(mod["id"])
        X = M.size
        xs = np.arange(X)
        rng = np.random.default_rng(MC_SEED + 1)
        fi = np.zeros(X); ft = np.zeros(X)
        for _ in range(N_REAL):
            pred, tied = core.plurality(core.invariance_votes_add(M, xs, 18, rng), 53)
            fi += (pred != f.ravel()) | tied
            ft += core.sc_fail(M, f, xs, 9, rng)
        fc = concat_real_fail(M, f, 3, N_REAL, rng)
        exact = {"invariance": plur_fail(core.invariance_channel_add(E, 53), 18),
                 "translation": plur_fail(core.twirled_channel(E, 53), 9),
                 "concat_j3": plur_fail(concat_channel(E, 53), 3)}
        for meth, emp in (("invariance", fi / N_REAL), ("translation", ft / N_REAL), ("concat_j3", fc)):
            d = exact[meth]
            se = math.sqrt(float((d * (1 - d)).sum()) / N_REAL) / X
            xc.append({"model": mod["id"], "method": meth, "Q": 18, "trials_per_input": N_REAL, "inputs": int(X),
                       "seed": MC_SEED + 1, "real_vote_mean_err": float(emp.mean()), "exact_mean_err": float(d.mean()),
                       "se": se, "z": float((emp.mean() - d.mean()) / se) if se > 0 else None})
    res["real_vote_crosscheck"] = xc

    # organic errors: add/grok p = 47
    g47 = sorted([r for r in idx if r["family"] == "add/grok" and r["p"] == 47], key=lambda r: r["id"])
    grok = []
    for tgt in GROK_TARGETS:
        r = min(g47, key=lambda r: (abs(r["eps"] - tgt), r["id"]))
        t0 = time.time()
        a = analyse_model(r["id"], with_logits=False, with_concat=False)
        a["target_eps"] = tgt
        a["run_id"] = r["run_id"]
        a["budget_to_reach"] = {str(t): {meth: budget_to_reach(a["methods"][meth], t)
                                         for meth in ("invariance", "invariance_km1", "translation")}
                                for t in (1e-2, 1e-3, 1e-6)}
        byq = []
        for Q in BUDGETS:
            row = {"Q": Q}
            for stat in ("mean_err", "worst_err"):
                best = {}
                for meth, rows in a["methods"].items():
                    ok = [x[stat] for x in rows if x["Q"] <= Q]
                    if ok:
                        best[meth] = min(ok)
                row["winner_" + stat] = min(best, key=lambda z: best[z])
                row[stat + "_by_method"] = best
            byq.append(row)
        a["winner_by_budget"] = byq
        grok.append(a)
        print(f"  {r['id']}  eps={r['eps']:.4f}  {time.time() - t0:.1f}s", flush=True)
    res["grok_p47"] = grok

    res["runtime_seconds"] = round(time.time() - t_start, 1)
    os.makedirs(core.RESULTS_DIR, exist_ok=True)
    with open(os.path.join(core.RESULTS_DIR, "exp_twirls.json"), "w") as fh:
        json.dump(res, fh, indent=1)
    make_figure(res, os.path.join(core.FIG_DIR, "fig_twirls"))
    print("done in", res["runtime_seconds"], "s")


if __name__ == "__main__":
    if "--figure-only" in sys.argv:
        with open(os.path.join(core.RESULTS_DIR, "exp_twirls.json")) as fh:
            make_figure(json.load(fh), os.path.join(core.FIG_DIR, "fig_twirls"))
    else:
        main()

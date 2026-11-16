#!/usr/bin/env python3
"""theory_checks.py -- verification of claims C1-C7 on SYNTHETIC error fields.

No trained networks are used here: an "error field" is a function e: G -> H and
the model is M = f + e.  Everything that can be enumerated exactly is enumerated
exactly (twirled channels via an FFT autocorrelation that is validated against
brute force; plurality failure of Multinomial(k, T) via an exact generating-
function recursion).  Monte Carlo is used only as a cross-check and its sample
sizes are recorded.

Run (from anywhere):   python3 code/theory_checks.py
                       python3 code/theory_checks.py --figure-only   (redraw Figure 1 from the JSON)
Uses 2 worker processes, OMP_NUM_THREADS=1, fixed seeds; deterministic.
Writes   results/theory_checks.json
         figures/fig_phase_diagram.svg / .png

Notation (see the paper): eps = error rate over all of G, q = |H|,
lambda = 1 - eps/(1-1/q), D_x(r) = e(x+r) - e(r), N_h(x) = #{r : D_x(r) = h},
T_x(h) = N_h(x)/|G|.  "Correctable" = truth is the STRICT mode of T_x
(N_0(x) > N_h(x) for every h != 0); a tie counts as a failure.
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import sys, json, time, math, itertools
from concurrent.futures import ProcessPoolExecutor
import numpy as np
from scipy import fft as sfft
from scipy.special import gammaln
from scipy.stats import norm
from scipy.optimize import brentq

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


# --------------------------------------------------------------------------
# groups, twirled channels, plurality failure
# --------------------------------------------------------------------------
class Ab:
    """Finite abelian group Z_d1 x ... x Z_dk with elements indexed row-major."""

    def __init__(self, dims):
        self.dims = tuple(int(d) for d in dims)
        self.n = int(np.prod(self.dims))
        self.el = np.array(list(itertools.product(*[range(d) for d in self.dims])), dtype=np.int64)
        self.strides = np.array([int(np.prod(self.dims[i + 1:])) for i in range(len(self.dims))], dtype=np.int64)
        d = np.array(self.dims)
        self.add = ((self.el[:, None, :] + self.el[None, :, :]) % d) @ self.strides   # add[i, j] = i + j
        self.neg = ((-self.el) % d) @ self.strides
        self.sub = self.add[:, self.neg]                                              # sub[i, j] = i - j
        idx = np.arange(self.n)
        self.two_torsion = self.add[idx, idx] == 0                                    # 2h = 0 (includes h = 0)

    @property
    def name(self):
        return " x ".join("Z_%d" % d for d in self.dims)


def gname(dims):
    return " x ".join("Z_%d" % d for d in dims)


def twirl_counts(e, Gdims, Hdims):
    """N[..., h, x] = #{r in G : e(x+r) - e(r) = h}.

    e: integer array (..., |G|) of H-indices (row-major).  Computed as the
    autocorrelation of the one-hot indicator I(h, r) = 1[e(r) = h] on the group
    H x G (Wiener-Khinchin); exact after rounding.  Validated against brute force
    in section 'selftest'."""
    e = np.asarray(e)
    nG, nH = int(np.prod(Gdims)), int(np.prod(Hdims))
    batch = e.shape[:-1]
    e2 = e.reshape(-1, nG)
    B = e2.shape[0]
    I = np.zeros((B, nH, nG))
    I[np.arange(B)[:, None], e2, np.arange(nG)[None, :]] = 1.0
    shape = (B,) + tuple(Hdims) + tuple(Gdims)
    I = I.reshape(shape)
    axes = tuple(range(1, len(shape)))
    F = sfft.rfftn(I, axes=axes)
    N = sfft.irfftn(F.real ** 2 + F.imag ** 2, s=shape[1:], axes=axes)
    return np.rint(N).astype(np.int64).reshape(batch + (nH, nG))


def twirl_counts_brute(e, G, H):
    N = np.zeros((H.n, G.n), dtype=np.int64)
    for x in range(G.n):
        D = H.sub[e[G.add[x]], e]
        N[:, x] = np.bincount(D, minlength=H.n)
    return N


def plurality_fail_exact(T, k):
    """delta_k = P[index 0 is NOT the unique plurality winner of k i.i.d. draws from T].

    T: (X, q) array of channels (rows sum to 1).  Exact: success means N_0 = n0 and
    every other count < n0, whose probability is
        k!/n0! * T_0^n0 * [z^(k-n0)] prod_{h != 0} sum_{j < n0} (T_h z)^j / j!.
    Computed with truncated polynomial products (scaled to avoid overflow).  The value is
    invariant under permutations of the wrong values, so rows are sorted and de-duplicated
    first (T_x and T_{-x} coincide after sorting).  Accuracy is limited to ~1e-13 absolute
    because delta = 1 - P[success]."""
    T = np.atleast_2d(np.asarray(T, dtype=float))
    Ts = np.concatenate([T[:, :1], np.sort(T[:, 1:], axis=1)], axis=1)
    U, inv = np.unique(Ts, axis=0, return_inverse=True)
    inv = np.asarray(inv).reshape(-1)
    keep = np.concatenate([[True], (U[:, 1:] > 0).any(0)])
    U = U[:, keep]
    X, q = U.shape
    succ = np.zeros(X)
    with np.errstate(divide="ignore"):
        logT0 = np.log(U[:, 0])
        logTh = np.log(U[:, 1:])
    for n0 in range(1, k + 1):
        m = k - n0
        if m > (q - 1) * (n0 - 1):
            continue
        if m == 0:
            succ += U[:, 0] ** k
            continue
        s = float(m)
        J = min(n0 - 1, m)
        j = np.arange(J + 1)
        with np.errstate(invalid="ignore"):
            C = np.exp(j[None, None, :] * (logTh[:, :, None] + math.log(s)) - gammaln(j + 1)[None, None, :])
        C[:, :, 0] = 1.0
        C = np.nan_to_num(C, nan=0.0)
        buf = np.zeros((X, m + 1 + J))
        buf[:, J] = 1.0
        win = np.lib.stride_tricks.sliding_window_view(buf, J + 1, axis=1)   # win[x, d, i] = poly[d - J + i]
        for h in range(q - 1):
            buf[:, J:] = np.einsum("xdi,xi->xd", win, C[:, h, ::-1])
        coef = buf[:, J + m]
        with np.errstate(divide="ignore", invalid="ignore"):
            logp = gammaln(k + 1) - gammaln(n0 + 1) + n0 * logT0 + np.log(coef) - m * math.log(s)
        succ += np.where(coef > 0, np.exp(logp), 0.0)
    return np.clip(1.0 - succ, 0.0, 1.0)[inv]


def ln_pair_race(t0, th, k):
    """ln P[N_h >= N_0] after k draws (t0 > th).  Exact via exponential tilting:
    P = M^k * sum_{j >= 0} P~(S_k = j) s^(-j),  M = 1 - (sqrt t0 - sqrt th)^2,  s = sqrt(t0/th),
    where under P~ the walk S_k has i.i.d. steps +1 / -1 with probability a = sqrt(t0 th)/M each."""
    if th <= 0:
        return k * math.log(1 - t0)
    M = 1 - (math.sqrt(t0) - math.sqrt(th)) ** 2
    a = math.sqrt(t0 * th) / M
    s = math.sqrt(t0 / th)
    L = 2 * k + 1
    theta = 2 * np.pi * np.arange(L // 2 + 1) / L
    pmf = sfft.irfft((1 - 2 * a + 2 * a * np.cos(theta)) ** k, n=L)[:k + 1]
    jj = np.arange(k + 1)
    val = float(np.sum(np.clip(pmf, 0, None) * np.exp(-jj * math.log(s))))
    return k * math.log(M) + math.log(val)


def chernoff_bound(T, k):
    """sum_{h != 0} (1 - (sqrt T_0 - sqrt T_h)^2)^k ; valid when T_0 > max_h T_h."""
    T = np.atleast_2d(np.asarray(T, dtype=float))
    b = 1.0 - (np.sqrt(T[:, :1]) - np.sqrt(T[:, 1:])) ** 2
    return (b ** k).sum(1)


def rate_I(T):
    T = np.atleast_2d(np.asarray(T, dtype=float))
    with np.errstate(divide="ignore"):
        return -np.log(1.0 - (np.sqrt(T[:, 0]) - np.sqrt(T[:, 1:].max(1))) ** 2)


def lam_of(eps, q):
    return 1.0 - eps / (1.0 - 1.0 / q)


def iid_field(rng, n, q, eps):
    """i.i.d. incoherent field: 0 w.p. 1-eps, else uniform on H \\ {0}."""
    return np.where(rng.random(n) < eps, rng.integers(1, q, n), 0)


def summarize(vals):
    v = np.asarray(vals, dtype=float)
    return {"mean": float(v.mean()), "sd": float(v.std(ddof=1)) if len(v) > 1 else 0.0,
            "median": float(np.median(v)), "min": float(v.min()), "max": float(v.max()),
            "q25": float(np.quantile(v, 0.25)), "q75": float(np.quantile(v, 0.75)), "n": int(len(v))}


# --------------------------------------------------------------------------
# selftest + C1
# --------------------------------------------------------------------------
def section_c1():
    t0 = time.time()
    out = {"checks": []}
    # --- selftest of the FFT twirl against brute force
    rng = np.random.default_rng(101)
    worst = 0
    cases = [((7,), (3,)), ((3, 3), (5,)), ((2, 4), (2, 2)), ((6, 5), (4,)), ((4, 3, 2), (2, 3))]
    for Gd, Hd in cases:
        G, H = Ab(Gd), Ab(Hd)
        for _ in range(20):
            e = rng.integers(0, H.n, G.n)
            worst = max(worst, int(np.abs(twirl_counts(e, Gd, Hd) - twirl_counts_brute(e, G, H)).max()))
    out["selftest_fft_vs_brute"] = {"cases": [[gname(a), gname(b)] for a, b in cases], "fields_per_case": 20,
                                    "max_abs_count_difference": worst}
    out["checks"].append({"id": "selftest.fft", "passed": worst == 0,
                          "detail": "FFT twirled-channel counts equal brute-force enumeration"})

    # --- exact plurality failure vs brute-force enumeration of compositions (small q, k)
    def brute(Tv, k):
        q = len(Tv)
        tot = 0.0
        for comp in itertools.product(range(k + 1), repeat=q - 1):
            n0 = k - sum(comp)
            if n0 < 0:
                continue
            if n0 > max(comp):
                lp = gammaln(k + 1) - gammaln(n0 + 1) - sum(gammaln(c + 1) for c in comp)
                pr = math.exp(lp) * Tv[0] ** n0 * np.prod([Tv[i + 1] ** c for i, c in enumerate(comp)])
                tot += pr
        return 1 - tot
    md = 0.0
    for Tv in ([0.5, 0.3, 0.2], [0.4, 0.3, 0.2, 0.1], [0.34, 0.33, 0.33], [0.2, 0.5, 0.3]):
        for k in (1, 2, 5, 8, 11):
            md = max(md, abs(brute(Tv, k) - plurality_fail_exact([Tv], k)[0]))
    out["exact_dp_vs_bruteforce_max_abs_diff"] = md
    out["checks"].append({"id": "C1.exact_dp", "passed": md < 1e-12,
                          "detail": "generating-function recursion equals enumeration of all count vectors"})

    # --- bound and rate on a set of channels
    rng = np.random.default_rng(102)
    chan = {
        "depolarizing q=5 T0=0.40": [0.40] + [0.15] * 4,
        "depolarizing q=31 T0=0.30": [0.30] + [0.70 / 30] * 30,
        "one strong rival q=5": [0.36, 0.30, 0.14, 0.10, 0.10],
        "near tie q=3": [0.36, 0.34, 0.30],
        "random q=7": None,
        "sparse q=4 (one T_h = 0)": [0.5, 0.3, 0.2, 0.0],
    }
    r = rng.dirichlet(np.ones(7))
    r = np.sort(r)[::-1]
    chan["random q=7"] = [float(v) for v in r]
    ks = [1, 3, 5, 10, 20, 40, 80, 160]
    rows = []
    bound_ok = True
    mc_maxz = 0.0
    mc_samples = 200000
    for name, Tv in chan.items():
        Tv = np.array(Tv)
        I = float(rate_I(Tv)[0])
        ex = [float(plurality_fail_exact(Tv, k)[0]) for k in ks]
        bd = [float(chernoff_bound(Tv, k)[0]) for k in ks]
        bound_ok &= all(e <= b * (1 + 1e-9) + 1e-12 for e, b in zip(ex, bd))
        emp = [(-math.log(e) / k) if e > 1e-11 else None for e, k in zip(ex, ks)]
        # local slope ln(delta_k / delta_2k) / k
        slope = {}
        for ka, kb in ((20, 40), (40, 80), (80, 160)):
            ea, eb = ex[ks.index(ka)], ex[ks.index(kb)]
            if ea > 1e-11 and eb > 1e-11:
                slope["%d->%d" % (ka, kb)] = math.log(ea / eb) / (kb - ka)
        # Monte Carlo cross-check at k = 10 and 40
        mc = {}
        for k in (10, 40):
            cnt = rng.multinomial(k, Tv / Tv.sum(), size=mc_samples)
            fail = (cnt[:, 0] <= cnt[:, 1:].max(1)).mean()
            e = ex[ks.index(k)]
            se = math.sqrt(max(e * (1 - e), 1e-12) / mc_samples)
            z = (fail - e) / se
            mc_maxz = max(mc_maxz, abs(z))
            mc["k=%d" % k] = {"mc": float(fail), "exact": e, "z": float(z)}
        rows.append({"channel": name, "T": [float(v) for v in Tv], "rate_I": I, "k": ks, "delta_exact": ex,
                     "bound": bd, "minus_ln_delta_over_k": emp, "local_slope": slope, "monte_carlo": mc})
    out["channels"] = rows
    out["mc_samples_per_point"] = mc_samples
    out["mc_max_abs_z"] = mc_maxz
    out["checks"].append({"id": "C1.bound", "passed": bool(bound_ok),
                          "detail": "exact delta_k <= sum_h (1-(sqrt T0 - sqrt Th)^2)^k for all channels and k in %s" % ks})
    out["checks"].append({"id": "C1.mc", "passed": mc_maxz < 4.0,
                          "detail": "exact delta_k agrees with %d-sample Monte Carlo (max |z| = %.2f)" % (mc_samples, mc_maxz)})
    # sandwich for k <= 160 and the rate at large k, using exact pairwise race probabilities:
    #   P[N_h* >= N_0] <= delta_k <= sum_h P[N_h >= N_0] <= sum_h (1-(sqrt T0 - sqrt Th)^2)^k
    rel = []
    sandwich_ok = True
    for rw in rows:
        Tv = np.array(rw["T"])
        hs = int(np.argmax(Tv[1:])) + 1
        I = rw["rate_I"]
        for k, ex, bd in zip(rw["k"], rw["delta_exact"], rw["bound"]):
            lo = math.exp(ln_pair_race(Tv[0], Tv[hs], k))
            up = sum(math.exp(ln_pair_race(Tv[0], Tv[h], k)) for h in range(1, len(Tv)))
            sandwich_ok &= (lo <= ex * (1 + 1e-9) + 1e-12) and (ex <= up * (1 + 1e-9) + 1e-12) and (up <= bd * (1 + 1e-9))
        rec = {"channel": rw["channel"], "I": I, "points": []}
        for c in (5, 50, 500):
            k = int(math.ceil(c / I))
            lnlo = ln_pair_race(Tv[0], Tv[hs], k)
            lnup = float(np.logaddexp.reduce([ln_pair_race(Tv[0], Tv[h], k) for h in range(1, len(Tv))]))
            rec["points"].append({"k": k, "k_times_I": k * I, "ratio_lower": -lnlo / (k * I), "ratio_upper": -lnup / (k * I)})
        rel.append(rec)
    out["rate_check"] = {"note": "ratio = -ln(bound on delta_k) / (k I) for the exact lower bound P[N_h* >= N_0] and the "
                                 "exact union upper bound; both tend to 1, so -ln(delta_k)/k -> I",
                         "channels": rel}
    out["checks"].append({"id": "C1.sandwich", "passed": bool(sandwich_ok),
                          "detail": "P[N_h* >= N_0] <= delta_k (exact) <= sum_h P[N_h >= N_0] <= Chernoff sum, all channels, k <= 160"})
    last = [(r_["points"][-1]["ratio_upper"], r_["points"][-1]["ratio_lower"]) for r_ in rel]
    out["checks"].append({"id": "C1.rate", "passed": bool(all(0.98 < u <= l < 1.03 for u, l in last)),
                          "detail": "at k = 500/I: -ln(delta_k)/(k I) lies in [%.4f, %.4f] over the %d channels (-> 1)"
                                    % (min(u for u, l in last), max(l for u, l in last), len(last))})

    # --- the 'iff': ties and wrong modes do not converge to 0
    iff = []
    for name, Tv in (("two-way tie (0.4,0.4,0.2)", [0.4, 0.4, 0.2]), ("three-way tie", [1 / 3, 1 / 3, 1 / 3]),
                     ("wrong mode (0.3,0.4,0.3)", [0.3, 0.4, 0.3]), ("strict mode (0.4,0.35,0.25)", [0.4, 0.35, 0.25])):
        iff.append({"channel": name, "k": [10, 40, 160, 320],
                    "delta": [float(plurality_fail_exact(Tv, k)[0]) for k in (10, 40, 160, 320)]})
    out["iff_examples"] = iff
    ok = iff[0]["delta"][-1] > 0.5 and iff[1]["delta"][-1] > 0.6 and iff[2]["delta"][-1] > 0.9 and \
        iff[3]["delta"][-1] < iff[3]["delta"][0]
    out["checks"].append({"id": "C1.iff", "passed": bool(ok),
                          "detail": "tie channels keep delta_k >= 1/2 (2-way) or 2/3 (3-way); wrong-mode -> 1; strict mode -> 0"})
    out["runtime_s"] = time.time() - t0
    return out


# --------------------------------------------------------------------------
# C2: worst-case radius
# --------------------------------------------------------------------------
def c2_full_enum(Gd, Hd):
    """All q^n error fields: check the three inequalities and the minimal number of errors that breaks an input."""
    G, H = Ab(Gd), Ab(Hd)
    n, q = G.n, H.n
    subH = H.sub.astype(np.int8)
    Nf = q ** n
    # N_h(x) = N_{-h}(-x), so one representative of each pair {x, -x} suffices
    xs_half = [x for x in range(1, n) if x <= G.neg[x]]
    res = {"G": G.name, "H": H.name, "n": n, "q": q, "fields": Nf,
           "min_slack_T0_vs_1-2eps": None, "min_slack_3E_non2torsion_h": None, "min_slack_4E_2torsion_h": None}
    ms0, ms3, ms4 = 10 ** 9, 10 ** 9, 10 ** 9
    min_tie, min_strict = n + 1, n + 1
    chunk = 400000
    for s in range(0, Nf, chunk):
        idx = np.arange(s, min(Nf, s + chunk))
        fields = np.array(np.unravel_index(idx, (q,) * n), dtype=np.int8).T
        wt = (fields != 0).sum(1)
        for x in xs_half:
            D = subH[fields[:, G.add[x]], fields]
            N = np.stack([(D == h).sum(1) for h in range(q)], 1)
            ms0 = min(ms0, int((N[:, 0] - (n - 2 * wt)).min()))
            for h in range(1, q):
                if H.two_torsion[h]:
                    ms4 = min(ms4, int((N[:, 0] - N[:, h] - (n - 4 * wt)).min()))
                else:
                    ms3 = min(ms3, int((N[:, 0] - N[:, h] - (n - 3 * wt)).min()))
            mx = N[:, 1:].max(1)
            tie = N[:, 0] <= mx
            strict = N[:, 0] < mx
            if tie.any():
                min_tie = min(min_tie, int(wt[tie].min()))
            if strict.any():
                min_strict = min(min_strict, int(wt[strict].min()))
    even = (q % 2 == 0)
    res["min_slack_T0_vs_1-2eps"] = ms0
    res["min_slack_3E_non2torsion_h"] = ms3 if ms3 < 10 ** 9 else None
    res["min_slack_4E_2torsion_h"] = ms4 if ms4 < 10 ** 9 else None
    res["min_errors_tie_or_worse"] = min_tie
    res["min_errors_strictly_worse"] = min_strict if min_strict <= n else None
    res["pred_tie"] = math.ceil(n / 4) if even else math.ceil(n / 3)
    res["pred_strict"] = (n // 4 + 1) if even else (n // 3 + 1)
    res["ok"] = bool(ms0 >= 0 and (ms3 >= 0) and (ms4 >= 0) and min_tie == res["pred_tie"]
                     and (min_strict == res["pred_strict"]))
    return res


def _gen_fields(n, q, j, chunk=120000):
    """All fields with exactly j errors that contain the identity as an error point
    (WLOG by translation invariance of the twirled channel)."""
    V = (q - 1) ** j
    vals = (np.array(np.unravel_index(np.arange(V), (q - 1,) * j), dtype=np.int8).T + 1).astype(np.int8)
    Bsz = max(1, chunk // V)
    it = itertools.combinations(range(1, n), j - 1)
    while True:
        batch = list(itertools.islice(it, Bsz))
        if not batch:
            return
        pos = np.array([(0,) + c for c in batch], dtype=np.int64)
        e = np.zeros((len(batch), V, n), dtype=np.int8)
        e[np.arange(len(batch))[:, None, None], np.arange(V)[None, :, None], pos[:, None, :]] = vals[None, :, :]
        yield e.reshape(-1, n)


def c2_min_break(Gd, Hd, budget):
    """Exhaustive search by number of errors: the smallest number of errors for which some
    field makes some input x tie-or-worse / strictly worse."""
    G, H = Ab(Gd), Ab(Hd)
    n, q = G.n, H.n
    subH = H.sub.astype(np.int8)
    even = (q % 2 == 0)
    res = {"G": G.name, "H": H.name, "n": n, "q": q,
           "pred_tie": math.ceil(n / 4) if even else math.ceil(n / 3),
           "pred_strict": (n // 4 + 1) if even else (n // 3 + 1),
           "min_errors_tie_or_worse": None, "min_errors_strictly_worse": None,
           "fields_enumerated": 0, "status": "complete"}
    xs_half = [x for x in range(1, n) if x <= G.neg[x]]          # N_h(x) = N_{-h}(-x)
    need = math.comb(n - 1, res["pred_tie"] - 1) * (q - 1) ** res["pred_tie"]
    if need > budget:
        res["status"] = "not searched (the level with %d errors alone has %d fields > budget %d)" % (res["pred_tie"], need, budget)
        res["ok_tie"] = res["ok_strict"] = None
        return res
    for j in range(1, n + 1):
        count = math.comb(n - 1, j - 1) * (q - 1) ** j
        if count > budget:
            res["status"] = "stopped at %d errors (would need %d fields > budget %d)" % (j, count, budget)
            break
        any_tie = any_strict = False
        for fields in _gen_fields(n, q, j):
            for x in xs_half:
                D = subH[fields[:, G.add[x]], fields]
                n0 = (D == 0).sum(1)
                mx = (D == 1).sum(1)
                for h in range(2, q):
                    np.maximum(mx, (D == h).sum(1), out=mx)
                any_tie |= bool((n0 <= mx).any())
                any_strict |= bool((n0 < mx).any())
                if any_strict:
                    break
            if any_strict:
                break
        res["fields_enumerated"] += count
        if any_tie and res["min_errors_tie_or_worse"] is None:
            res["min_errors_tie_or_worse"] = j
        if any_strict:
            res["min_errors_strictly_worse"] = j
            break
    res["ok_tie"] = (res["min_errors_tie_or_worse"] == res["pred_tie"]) if res["min_errors_tie_or_worse"] else None
    res["ok_strict"] = (res["min_errors_strictly_worse"] == res["pred_strict"]) if res["min_errors_strictly_worse"] else None
    return res


def c2_construction(Gd, Hd, max_x=None):
    """For every x != 0: place ceil(|G|/3) (odd |H|) or ceil(|G|/4) (even |H|) errors that are
    isolated along the orbits of translation by x, all with the same value h (2h != 0 resp. 2h = 0),
    and confirm that truth is not the strict mode of T_x."""
    G, H = Ab(Gd), Ab(Hd)
    n, q = G.n, H.n
    even = (q % 2 == 0)
    if even:
        h = int(np.nonzero(H.two_torsion)[0][1])
        a_target = math.ceil(n / 4)
    else:
        h = 1
        a_target = math.ceil(n / 3)
    xs = range(1, n) if max_x is None else range(1, min(n, max_x + 1))
    nx, ok_all, placed_all = 0, True, True
    worst_margin = -10 ** 9
    for x in xs:
        visited = np.zeros(n, dtype=bool)
        e = np.zeros(n, dtype=np.int64)
        placed = 0
        for r0 in range(n):
            if visited[r0]:
                continue
            cyc = [r0]
            r = int(G.add[r0, x])
            while r != r0:
                cyc.append(r)
                r = int(G.add[r, x])
            visited[cyc] = True
            m = len(cyc)
            for i in range(0, 2 * (m // 2), 2):
                if placed < a_target:
                    e[cyc[i]] = h
                    placed += 1
        D = H.sub[e[G.add[x]], e]
        c = np.bincount(D, minlength=q)
        margin = int(c[0] - c[1:].max())
        worst_margin = max(worst_margin, margin)
        ok_all &= margin <= 0
        placed_all &= placed == a_target
        nx += 1
    return {"G": G.name, "H": H.name, "n": n, "q": q, "h": h, "errors": a_target, "eps": a_target / n,
            "inputs_x_tested": nx, "all_placed": bool(placed_all), "all_broken": bool(ok_all),
            "largest_margin_N0_minus_maxNh": worst_margin}


def section_c2():
    t0 = time.time()
    out = {"checks": []}
    full_cases = [((4,), (2,)), ((6,), (3,)), ((2, 2), (2, 2)), ((2, 3), (4,)), ((2, 4), (2,)), ((2, 4), (3,)),
                  ((2, 4), (4,)), ((2, 4), (2, 2)), ((2, 4), (5,)), ((2, 2, 2), (2,)), ((2, 2, 2), (3,)),
                  ((2, 2, 2), (4,)), ((2, 2, 2), (2, 2)), ((3, 3), (2,)), ((3, 3), (3,)), ((3, 3), (4,)),
                  ((3, 3), (2, 2)), ((3, 3), (5,)), ((8,), (4,)), ((9,), (3,)), ((7,), (5,)), ((6,), (6,)),
                  ((5,), (2, 3))]
    out["full_enumeration"] = [c2_full_enum(a, b) for a, b in full_cases]
    out["checks"].append({"id": "C2.full_enum", "passed": all(r["ok"] for r in out["full_enumeration"]),
                          "detail": "all q^n fields on %d (G,H) pairs: T_x(0) >= 1-2eps; N0-Nh >= |G|-3|E| (2h!=0) and "
                                    ">= |G|-4|E| (2h=0), each tight; minimal breaking error counts as predicted"
                                    % len(full_cases)})
    budget = 1200000
    Hs = [(2,), (3,), (4,), (5,), (2, 2)]
    Gs = [(10,), (11,), (12,), (2, 6), (2, 2, 3), (13,), (15,), (3, 5), (4, 4), (2, 8), (2, 2, 2, 2),
          (3, 6), (18,), (4, 5)]
    rows = []
    for Gd in Gs:
        for Hd in Hs:
            rows.append(c2_min_break(Gd, Hd, budget))
    out["weight_ordered_search"] = {"budget_fields_per_weight": budget, "rows": rows}
    done_tie = [r for r in rows if r["min_errors_tie_or_worse"] is not None]
    done_strict = [r for r in rows if r["min_errors_strictly_worse"] is not None]
    out["weight_ordered_search"]["n_pairs"] = len(rows)
    out["weight_ordered_search"]["n_tie_resolved"] = len(done_tie)
    out["weight_ordered_search"]["n_strict_resolved"] = len(done_strict)
    out["weight_ordered_search"]["unresolved"] = [[r["G"], r["H"], r["status"]] for r in rows
                                                  if r["min_errors_tie_or_worse"] is None]
    out["weight_ordered_search"]["total_fields_enumerated"] = int(sum(r["fields_enumerated"] for r in rows))
    out["checks"].append({"id": "C2.search_tie", "passed": all(r["ok_tie"] for r in done_tie),
                          "detail": "%d/%d (G,H) pairs resolved: min #errors making some input tie-or-worse = "
                                    "ceil(|G|/3) (|H| odd) or ceil(|G|/4) (|H| even)" % (len(done_tie), len(rows))})
    out["checks"].append({"id": "C2.search_strict", "passed": all(r["ok_strict"] for r in done_strict),
                          "detail": "%d/%d pairs resolved: min #errors making some input strictly worse = "
                                    "floor(|G|/3)+1 resp. floor(|G|/4)+1" % (len(done_strict), len(rows))})
    cons = []
    for Gd, Hd in [((31, 31), (31,)), ((30, 30), (30,)), ((30, 30), (3,)), ((32, 32), (2,)), ((9, 3), (3,)),
                   ((9, 3), (5,)), ((2, 4, 3), (4,)), ((2, 4, 3), (2, 2)), ((27,), (5,)), ((16,), (2,)),
                   ((5, 5), (7,)), ((6, 6), (6,))]:
        cons.append(c2_construction(Gd, Hd))
    out["constructions"] = cons
    out["checks"].append({"id": "C2.constructions", "passed": all(c["all_broken"] and c["all_placed"] for c in cons),
                          "detail": "for every x != 0 the isolated same-value construction with ceil(|G|/3) resp. "
                                    "ceil(|G|/4) errors makes truth lose strict-mode status (%d groups)" % len(cons)})
    out["runtime_s"] = time.time() - t0
    return out


# --------------------------------------------------------------------------
# C3: depolarizing law + finite-size threshold
# --------------------------------------------------------------------------
def _law_counts(e, p, q, G, mask3):
    """Exact P[sum = 0] over all votes (c=2), all pairs with distinct points (c=3), all quadruples (c=4)."""
    n = p * p
    N = twirl_counts(e, (p, p), (q,))
    T = N[:, 1:] / n
    S = (e[:, None] + e[None, :] - e[G.add]) % q
    cnt3 = np.bincount(S[mask3], minlength=q) / mask3.sum()
    e2 = e.reshape(p, p)
    Ey = np.stack([np.roll(e2, -y, axis=1) for y in range(1, p)])          # e(r, y+s)
    cnt4 = np.zeros(q)
    for x in range(1, p):
        A = (np.roll(Ey, -x, axis=1) - Ey - np.roll(e2, -x, axis=0)[None] + e2[None]) % q
        cnt4 += np.bincount(A.ravel(), minlength=q)
    cnt4 /= cnt4.sum()
    frac_ok = float((N[0, 1:] > N[1:, 1:].max(0)).mean())
    return {2: np.concatenate([[T[0].mean()], T[1:].mean(1)]), 3: cnt3, 4: cnt4}, frac_ok


def section_c3_law():
    t0 = time.time()
    out = {"checks": []}
    p = 31
    G = Ab((p, p))
    n = G.n
    seeds = list(range(300, 320))
    qs = [2, 3, 5, 31]
    epss = [0.1, 0.3, 0.6, 0.9, 1.0]
    ar = np.arange(n)
    mask3 = (ar[:, None] != 0) & (ar[None, :] != 0) & (ar[:, None] != ar[None, :])
    rows = []
    for q in qs:
        for eps in epss:
            lam = lam_of(eps, q)
            acc = {c: {"p0": [], "ph_dev": [], "p0_minus_pred_real": []} for c in (2, 3, 4)}
            er, fr = [], []
            for sd in seeds:
                rng = np.random.default_rng(sd * 1000 + q * 10 + int(eps * 100))
                e = iid_field(rng, n, q, eps)
                er.append(float((e != 0).mean()))
                lam_r = lam_of(er[-1], q)
                cnts, frac_ok = _law_counts(e, p, q, G, mask3)
                fr.append(frac_ok)
                for c in (2, 3, 4):
                    acc[c]["p0"].append(cnts[c][0])
                    acc[c]["ph_dev"].append(np.abs(cnts[c][1:] - (1 - lam ** c) / q).max())
                    acc[c]["p0_minus_pred_real"].append(cnts[c][0] - (1 / q + (1 - 1 / q) * lam_r ** c))
            z_eps = 0.0 if eps in (0.0, 1.0) else (np.mean(er) - eps) / math.sqrt(eps * (1 - eps) / (n * len(seeds)))
            for c in (2, 3, 4):
                v = np.array(acc[c]["p0"])
                pred = 1 / q + (1 - 1 / q) * lam ** c
                se = v.std(ddof=1) / math.sqrt(len(v))
                diff = v.mean() - pred
                z = 0.0 if abs(diff) < 1e-12 else (diff / se if se > 0 else float("inf"))
                rows.append({"q": q, "eps": eps, "lambda": lam, "c": c, "pred_P0": pred, "sim_P0_mean": float(v.mean()),
                             "sim_P0_se": float(se), "z": float(z),
                             "max_dev_wrong_value_freq_mean_over_seeds": float(np.mean(acc[c]["ph_dev"])),
                             "pred_Ph": (1 - lam ** c) / q,
                             "realised_eps_mean": float(np.mean(er)), "z_of_realised_eps": float(z_eps),
                             "mean_P0_minus_law_at_realised_eps": float(np.mean(acc[c]["p0_minus_pred_real"])),
                             "fraction_inputs_correctable_mean": float(np.mean(fr)),
                             "fraction_inputs_correctable_min": float(np.min(fr))})
    out["config"] = {"G": G.name, "H": ["Z_%d" % q for q in qs], "eps": epss, "seeds": seeds,
                     "seed_rule": "default_rng(seed*1000 + 10*q + int(100*eps))",
                     "note": "exact enumeration of all votes/pairs/quadruples with distinct points for each random field; "
                             "randomness is only in the field. z compares the mean over seeds with the law at the NOMINAL "
                             "eps; mean_P0_minus_law_at_realised_eps compares each field with the law at its own error rate"}
    out["rows"] = rows
    zs = np.array([r["z"] for r in rows])
    devs = np.array([abs(r["sim_P0_mean"] - r["pred_P0"]) for r in rows])
    dreal = np.array([abs(r["mean_P0_minus_law_at_realised_eps"]) for r in rows])
    out["max_abs_z"] = float(np.abs(zs).max())
    out["n_cells"] = len(rows)
    out["n_cells_abs_z_gt_3"] = int((np.abs(zs) > 3).sum())
    out["cells_abs_z_gt_3"] = [{k: r[k] for k in ("q", "eps", "c", "z", "pred_P0", "sim_P0_mean", "realised_eps_mean",
                                                  "z_of_realised_eps", "mean_P0_minus_law_at_realised_eps")}
                               for r in rows if abs(r["z"]) > 3]
    out["max_abs_dev_P0_vs_law_at_nominal_eps"] = float(devs.max())
    out["max_abs_dev_P0_vs_law_at_realised_eps"] = float(dreal.max())
    neg = [r for r in rows if r["lambda"] < 0]
    out["negative_lambda_cells"] = len(neg)
    out["negative_lambda_max_abs_dev_vs_law_at_realised_eps"] = float(max(abs(r["mean_P0_minus_law_at_realised_eps"]) for r in neg))
    # independent replication of the (q=2, eps=0.9) cell, whose 20 fields happen to have a high realised error rate
    rep_seeds = list(range(9000, 9100))
    q, eps = 2, 0.9
    lam = lam_of(eps, q)
    acc = {c: [] for c in (2, 3, 4)}
    er = []
    for sd in rep_seeds:
        e = iid_field(np.random.default_rng(sd), n, q, eps)
        er.append(float((e != 0).mean()))
        cnts, _ = _law_counts(e, p, q, G, mask3)
        for c in (2, 3, 4):
            acc[c].append(cnts[c][0])
    out["replication_q2_eps0.9"] = {"seeds": [rep_seeds[0], rep_seeds[-1]], "n_fields": len(rep_seeds),
                                    "realised_eps_mean": float(np.mean(er)), "rows": [
        {"c": c, "pred_P0": 1 / q + (1 - 1 / q) * lam ** c, "sim_P0_mean": float(np.mean(acc[c])),
         "sim_P0_se": float(np.std(acc[c], ddof=1) / math.sqrt(len(rep_seeds))),
         "z": float((np.mean(acc[c]) - (1 / q + (1 - 1 / q) * lam ** c)) / (np.std(acc[c], ddof=1) / math.sqrt(len(rep_seeds))))}
        for c in (2, 3, 4)]}
    zrep = max(abs(r["z"]) for r in out["replication_q2_eps0.9"]["rows"])
    # the 100-field replication again has a high realised error rate, so a much larger one (c = 2 only, cheap)
    big_seeds = list(range(100000, 104000))
    Eb = np.stack([iid_field(np.random.default_rng(sd), n, q, eps) for sd in big_seeds])
    p0b = []
    for s0 in range(0, len(big_seeds), 500):
        Nb = twirl_counts(Eb[s0:s0 + 500], (p, p), (q,))
        p0b.extend((Nb[:, 0, 1:] / n).mean(1).tolist())
    p0b = np.array(p0b)
    erb = (Eb != 0).mean(1)
    pred2 = 1 / q + (1 - 1 / q) * lam ** 2
    out["replication_large_q2_eps0.9_c2"] = {
        "seeds": [big_seeds[0], big_seeds[-1]], "n_fields": len(big_seeds), "pred_P0": pred2,
        "sim_P0_mean": float(p0b.mean()), "sim_P0_se": float(p0b.std(ddof=1) / math.sqrt(len(p0b))),
        "z": float((p0b.mean() - pred2) / (p0b.std(ddof=1) / math.sqrt(len(p0b)))),
        "realised_eps_mean": float(erb.mean()),
        "z_of_realised_eps": float((erb.mean() - eps) / math.sqrt(eps * (1 - eps) / (n * len(big_seeds))))}
    zbig = abs(out["replication_large_q2_eps0.9_c2"]["z"])
    out["checks"].append({"id": "C3.law", "passed": bool(np.abs(zs).max() < 4.0 and dreal.max() < 2e-3 and zrep < 3.5 and zbig < 3.5),
                          "detail": "P[sum=0] = 1/q+(1-1/q)lambda^c for c=2,3,4, q in %s, eps in %s incl. lambda<0: "
                                    "max |z| = %.2f over %d cells (%d cells with |z|>3, all in the q=2, eps=0.9 field set "
                                    "whose realised error rate is %.4f); max |deviation| from the law at the realised "
                                    "error rate %.1e; replication of that cell on %d new fields: max |z| = %.2f (realised "
                                    "error rate again high, %.4f); on %d further fields (c=2): z = %.2f"
                                    % (qs, epss, np.abs(zs).max(), len(rows), int((np.abs(zs) > 3).sum()),
                                       [r for r in rows if r["q"] == 2 and r["eps"] == 0.9][0]["realised_eps_mean"],
                                       dreal.max(), len(rep_seeds), zrep, out["replication_q2_eps0.9"]["realised_eps_mean"],
                                       len(big_seeds), out["replication_large_q2_eps0.9_c2"]["z"])})
    # eps = 1 (wrong on every input, scattered wrong values): truth is still the mode of the vote
    we = [{k: r[k] for k in ("q", "lambda", "pred_P0", "sim_P0_mean", "pred_Ph", "fraction_inputs_correctable_mean",
                             "fraction_inputs_correctable_min")} for r in rows if r["eps"] == 1.0 and r["c"] == 2]
    out["wrong_everywhere_eps_1"] = we
    r3 = [r for r in we if r["q"] == 3][0]
    out["checks"].append({"id": "C3.wrong_everywhere", "passed": bool(r3["fraction_inputs_correctable_min"] == 1.0),
                          "detail": "eps = 1, q = 3, |G| = 961: T(0) = %.4f (law 1/2) vs T(h) = 1/4; every input correctable "
                                    "in all 20 fields; correctable fraction by q: %s"
                                    % (r3["sim_P0_mean"], {r["q"]: round(r["fraction_inputs_correctable_mean"], 4) for r in we})})
    out["runtime_s"] = time.time() - t0
    return out


def _lam2_gauss(nG, q):
    """Gaussian extreme-value estimate of lambda_c^2 (median): n_eff * Phi(-z) = ln 2,
    z = lambda^2 sqrt(|G| / v), v = p0 + ph - lambda^4, n_eff = (|G|-1)(q-1)/2."""
    neff = (nG - 1) * (q - 1) / 2.0
    z = norm.isf(math.log(2) / neff)

    def fn(l2):
        p0 = 1 / q + (1 - 1 / q) * l2
        ph = (1 - l2) / q
        return l2 * math.sqrt(nG / (p0 + ph - l2 * l2)) - z
    return brentq(fn, 1e-9, 1 - 1e-9), z


def _first_failure(args):
    p, seed = args
    q, nG = p, p * p
    rng = np.random.default_rng(seed)
    U = rng.random(nG)
    V = rng.integers(1, q, nG)

    def ok(eps_list):
        res = []
        bs = 8 if p > 40 else 32
        for s in range(0, len(eps_list), bs):
            E = np.where(U[None, :] < np.asarray(eps_list[s:s + bs])[:, None], V[None, :], 0)
            N = twirl_counts(E, (p, p), (q,))
            res.extend(np.all(N[:, 0, 1:] > N[:, 1:, 1:].max(1), axis=1).tolist())
        return res
    nev = 0
    # level 1: step 0.04 from 0.20 upward until the first failure
    c1 = None
    grid = [round(0.20 + 0.04 * i, 6) for i in range(0, 21)]
    for s in range(0, len(grid), 4):
        r = ok(grid[s:s + 4])
        nev += len(r)
        if not all(r):
            c1 = grid[s + r.index(False)]
            break
    if c1 is None:
        return {"p": p, "seed": seed, "eps_first_fail": None}
    # level 2: step 0.008 inside (c1 - 0.08, c1]
    g2 = [round(c1 - 0.08 + 0.008 * i, 6) for i in range(1, 11)]
    r = ok(g2)
    nev += len(r)
    c2 = g2[r.index(False)] if not all(r) else c1
    # level 3: step 0.002 inside (c2 - 0.016, c2]
    g3 = [round(c2 - 0.016 + 0.002 * i, 6) for i in range(1, 9)]
    r = ok(g3)
    nev += len(r)
    c3 = g3[r.index(False)] if not all(r) else c2
    eps_fail_real = float((U < c3).mean())
    eps_ok = round(c3 - 0.002, 6)
    eps_ok_real = float((U < eps_ok).mean())
    return {"p": p, "seed": seed, "eps_first_fail": c3, "eps_last_ok": eps_ok, "eps_last_ok_realised": eps_ok_real,
            "eps_first_fail_realised": eps_fail_real, "evaluations": nev}


def section_c3_finite(ps=(11, 17, 23, 31, 47, 61), nseeds=24):
    t0 = time.time()
    out = {"checks": []}
    rows = []
    for p in ps:
        q, nG = p, p * p
        rs = [_first_failure((p, 7000 + 100 * p + s)) for s in range(nseeds)]
        eps_ok = np.array([r["eps_last_ok_realised"] for r in rs])
        lam = 1 - eps_ok / (1 - 1 / q)
        lam2 = lam ** 2
        base = 2 * math.sqrt(math.log(nG * q) / (nG * q))
        l2_lead = base * q / (q - 1)
        l2_gap = base
        l2_gauss, z = _lam2_gauss(nG, q)
        row = {"p": p, "G_size": nG, "q": q, "seeds": [r["seed"] for r in rs],
               "eps_last_ok_realised": summarize(eps_ok), "lambda_c": summarize(lam), "lambda_c_sq": summarize(lam2),
               "per_seed_eps_last_ok": [float(v) for v in eps_ok],
               "heuristic_lead": {"lambda_sq": l2_lead, "eps": (1 - math.sqrt(l2_lead)) * (1 - 1 / q)},
               "heuristic_gap": {"lambda_sq": l2_gap, "eps": (1 - math.sqrt(l2_gap)) * (1 - 1 / q)},
               "heuristic_gauss": {"lambda_sq": l2_gauss, "eps": (1 - math.sqrt(l2_gauss)) * (1 - 1 / q), "z": z},
               "chance_eps": 1 - 1 / q}
        for k in ("heuristic_lead", "heuristic_gap", "heuristic_gauss"):
            row[k]["ratio_sim_median_lambda_sq_over_heuristic"] = row["lambda_c_sq"]["median"] / row[k]["lambda_sq"]
            row[k]["eps_error_vs_sim_median"] = row[k]["eps"] - row["eps_last_ok_realised"]["median"]
        rows.append(row)
    out["rows"] = rows
    x = np.log([r["G_size"] * r["q"] for r in rows])
    y = np.log([r["lambda_c_sq"]["median"] for r in rows])
    slope, icpt = np.polyfit(x, y, 1)
    out["fit_log_lambda_c_sq_vs_log_Gq"] = {"slope": float(slope), "intercept": float(icpt),
                                            "note": "pure |G|q^(-1/2) scaling would give slope -0.5; the sqrt(log) factor makes "
                                                    "the effective slope slightly shallower"}
    yy = np.log([r["lambda_c_sq"]["median"] / math.sqrt(math.log(r["G_size"] * r["q"])) for r in rows])
    s2, i2 = np.polyfit(x, yy, 1)
    out["fit_after_dividing_by_sqrt_log"] = {"slope": float(s2), "prefactor": float(math.exp(i2))}
    out["config"] = {"G": "Z_p^2", "H": "Z_p", "p": list(ps), "fields_per_p": nseeds,
                     "procedure": "nested i.i.d. fields e_eps(x) = V(x) 1[U(x) < eps]; exact all-input check via FFT; "
                                  "first failing eps located on a grid: step 0.04 from 0.20, then step 0.008 in the 0.08 "
                                  "window below, then step 0.002 in the 0.016 window below; reported value is the last "
                                  "passing grid point (realised error rate). Failures between grid points below the located "
                                  "window are not excluded."}
    rat = {k: [r[k]["ratio_sim_median_lambda_sq_over_heuristic"] for r in rows]
           for k in ("heuristic_lead", "heuristic_gap", "heuristic_gauss")}
    out["ratio_sim_over_heuristic_lambda_sq"] = rat
    out["max_abs_eps_error"] = {k: float(max(abs(r[k]["eps_error_vs_sim_median"]) for r in rows))
                                for k in ("heuristic_lead", "heuristic_gap", "heuristic_gauss")}
    out["checks"].append({"id": "C3.finite_size",
                          "passed": bool(all(0.6 < v < 1.6 for v in rat["heuristic_gap"])),
                          "detail": "median lambda_c^2 over %d fields vs 2 sqrt(ln(|G|q)/(|G|q)): ratios %s; "
                                    "Gaussian extreme-value version ratios %s; lead's form (extra q/(q-1)) ratios %s"
                                    % (nseeds, [round(v, 3) for v in rat["heuristic_gap"]],
                                       [round(v, 3) for v in rat["heuristic_gauss"]],
                                       [round(v, 3) for v in rat["heuristic_lead"]])})
    out["runtime_s"] = time.time() - t0
    return out


# --------------------------------------------------------------------------
# C4: structured error families and the phase diagram
# --------------------------------------------------------------------------
def _cyc(t, n):
    t = t % n
    return min(t, n - t)


def section_c4():
    t0 = time.time()
    out = {"checks": []}
    p = 31
    n = p * p
    a_of = np.arange(n) // p
    b_of = np.arange(n) % p
    eps_grid = np.round(np.arange(0, 1.0001, 0.01), 4)
    seeds = list(range(400, 408))
    fam = {}

    def stats(N, nG):
        N0 = N[..., 0, :]
        mx = N[..., 1:, :].max(-2)
        return (N0 > mx).mean(-1), ((N0 - mx).min(-1)) / nG, N0, mx

    # 1. incoherent i.i.d.   2. constant offset on a random set   3. second homomorphism on a random set
    for key in ("incoherent", "offset", "second_hom"):
        fr, mg, realised, extra = [], [], [], []
        for sd in seeds:
            rng = np.random.default_rng(sd)
            U = rng.random(n)
            V = rng.integers(1, p, n)
            mask = U[None, :] < eps_grid[:, None]
            if key == "incoherent":
                E = np.where(mask, V[None, :], 0)
            elif key == "offset":
                E = np.where(mask, 1, 0)
            else:                                   # f(a,b) = a+b, g(a,b) = a+2b, u = g - f = b
                E = np.where(mask, b_of[None, :], 0)
            N = twirl_counts(E, (p, p), (p,))
            f_, m_, N0, mx = stats(N, n)
            fr.append(f_)
            mg.append(m_)
            realised.append((E != 0).mean(1))
            if key == "second_hom":
                am = N.argmax(1)                                    # (eps, x)
                top = N.max(1)
                uniq = (N == top[:, None, :]).sum(1) == 1
                returns_g = (am == b_of[None, :]) & uniq & (b_of[None, :] != 0)
                extra.append(returns_g.sum(1) / (b_of != 0).sum())
        fam[key] = {"eps": eps_grid.tolist(), "correctable_fraction_mean": np.mean(fr, 0).tolist(),
                    "correctable_fraction_sd": np.std(fr, 0, ddof=1).tolist(),
                    "worst_margin_mean": np.mean(mg, 0).tolist(), "realised_error_rate_mean": np.mean(realised, 0).tolist(),
                    "G": "Z_31 x Z_31", "H": "Z_31", "seeds": seeds}
        if extra:
            fam[key]["fraction_of_f_ne_g_inputs_where_unique_mode_is_g_mean"] = np.mean(extra, 0).tolist()
    fam["incoherent"]["definition"] = "e(x) = V(x) 1[U(x) < eps], V uniform on H\\{0}"
    fam["offset"]["definition"] = "e(x) = 1 * 1[U(x) < eps] (constant offset on a random set)"
    fam["second_hom"]["definition"] = "M = g on a random set of density eps, f elsewhere; f(a,b)=a+b, g(a,b)=a+2b; " \
                                      "for eps > 1 - 1/q the realised error rate saturates because g = f on b = 0"

    # 4./5. coherent band: e(a,b) = h for a in [0, m), eps = m/n1
    def band(n1, Hd, h, label):
        nG = n1 * n1
        a1 = np.arange(nG) // n1
        ms = np.arange(0, n1 + 1)
        E = np.where(a1[None, :] < ms[:, None], h, 0)
        N = twirl_counts(E, (n1, n1), Hd)
        f_, m_, N0, mx = stats(N, nG)
        H = Ab(Hd)
        thr = n1 / 4.0 if H.two_torsion[h] else n1 / 3.0
        cfac = 4 if H.two_torsion[h] else 3
        pred_f, pred_m = [], []
        for m in ms:
            w = min(m, n1 - m)
            bad = sum(1 for t in range(n1) if min(w, _cyc(t, n1)) >= thr)
            pred_f.append(1 - bad / n1)
            pred_m.append(1.0 if w == 0 else (n1 - cfac * min(w, n1 // 2)) / n1)
        return {"eps": (ms / n1).tolist(), "correctable_fraction_mean": f_.tolist(), "worst_margin_mean": m_.tolist(),
                "predicted_fraction": pred_f, "predicted_worst_margin": pred_m,
                "max_abs_dev_fraction": float(np.abs(f_ - np.array(pred_f)).max()),
                "max_abs_dev_margin": float(np.abs(m_ - np.array(pred_m)).max()),
                "G": "Z_%d x Z_%d" % (n1, n1), "H": gname(Hd), "h": int(h), "two_torsion_value": bool(H.two_torsion[h]),
                "definition": "e(a,b) = h for a in [0, eps*n), else 0 (deterministic): %s" % label,
                "first_eps_with_a_broken_input": float(next((m / n1 for m, v in zip(ms, f_) if v < 1), float("nan"))),
                "last_eps_with_a_broken_input": float(max([m / n1 for m, v in zip(ms, f_) if v < 1] or [float("nan")]))}
    fam["band_odd"] = band(31, (31,), 1, "value h=1 in Z_31 (2h != 0)")
    fam["band_2torsion"] = band(30, (30,), 15, "value h=15 in Z_30 (2h = 0)")
    fam["band_Z30_h1"] = band(30, (30,), 1, "value h=1 in Z_30 (2h != 0, same G, H and error set as band_2torsion)")
    fam["band_Z32_to_Z2"] = band(32, (2,), 1, "value h=1 in Z_2 (2h = 0)")
    fam["band_Z30_to_Z3"] = band(30, (3,), 1, "value h=1 in Z_3")
    out["families"] = fam

    # predictions / checks
    eg = eps_grid
    off = np.array(fam["offset"]["correctable_fraction_mean"])
    offm = np.array(fam["offset"]["worst_margin_mean"])
    offm_pred = 1 - 3 * eg + 3 * eg ** 2
    out["offset_min_fraction"] = float(off.min())
    out["offset_worst_margin_min"] = float(offm.min())
    out["offset_margin_max_abs_dev_from_1-3eps+3eps^2"] = float(np.abs(offm - offm_pred).max())
    out["checks"].append({"id": "C4a.offset", "passed": bool(off.min() == 1.0),
                          "detail": "constant offset on a random set: every input correctable at every eps in [0,1] "
                                    "(min worst-margin %.3f; theory min 1/4 at eps=1/2 minus O(|G|^-1/2) fluctuation)"
                                    % offm.min()})
    sh = np.array(fam["second_hom"]["correctable_fraction_mean"])
    lo = sh[eg <= 0.44].min()
    hi = sh[eg >= 0.56].max()
    rg = np.array(fam["second_hom"]["fraction_of_f_ne_g_inputs_where_unique_mode_is_g_mean"])
    out["second_hom"] = {"min_fraction_eps<=0.44": float(lo), "max_fraction_eps>=0.56": float(hi), "one_over_q": 1 / p,
                         "returns_g_min_for_eps>=0.56": float(rg[eg >= 0.56].min()),
                         "returns_g_max_for_eps<=0.44": float(rg[eg <= 0.44].max()),
                         "fraction_at_0.48_0.50_0.52": [float(sh[np.argmin(abs(eg - v))]) for v in (0.48, 0.50, 0.52)]}
    out["checks"].append({"id": "C4b.second_hom",
                          "passed": bool(lo == 1.0 and abs(hi - 1 / p) < 1e-9 and rg[eg >= 0.56].min() == 1.0),
                          "detail": "second homomorphism on a random set: all inputs correctable for eps <= 0.44, only the "
                                    "f=g inputs (1/q) for eps >= 0.56, where the unique mode is g for every f!=g input"})
    bo, bt = fam["band_odd"], fam["band_2torsion"]
    out["checks"].append({"id": "C4c.band_odd",
                          "passed": bool(bo["max_abs_dev_fraction"] < 1e-12 and bo["max_abs_dev_margin"] < 1e-12),
                          "detail": "band of constant error, 2h != 0 (Z_31): simulated fraction and worst margin equal the "
                                    "closed forms; first broken input at eps = %.4f (ceil(31/3)/31 = %.4f)"
                                    % (bo["first_eps_with_a_broken_input"], 11 / 31)})
    out["checks"].append({"id": "C4d.band_2torsion",
                          "passed": bool(bt["max_abs_dev_fraction"] < 1e-12 and bt["max_abs_dev_margin"] < 1e-12
                                         and fam["band_Z32_to_Z2"]["max_abs_dev_fraction"] < 1e-12
                                         and fam["band_Z30_h1"]["max_abs_dev_fraction"] < 1e-12),
                          "detail": "band of constant error with 2h = 0 (Z_30, h=15): first broken input at eps = %.4f "
                                    "(predicted ceil(30/4)/30 = %.4f); same band with h=1 breaks at %.4f (1/3)"
                                    % (bt["first_eps_with_a_broken_input"], 8 / 30,
                                       fam["band_Z30_h1"]["first_eps_with_a_broken_input"])})
    inc = np.array(fam["incoherent"]["correctable_fraction_mean"])
    out["incoherent_last_eps_all_correctable_all_seeds"] = float(
        eg[np.nonzero(np.array(fam["incoherent"]["correctable_fraction_mean"]) < 1.0)[0][0] - 1])
    out["incoherent_fraction_at_chance_0.97"] = float(inc[np.argmin(abs(eg - 0.97))])
    out["incoherent_fraction_at_eps_1"] = float(inc[-1])
    out["runtime_s"] = time.time() - t0
    return out


# --------------------------------------------------------------------------
# C5: invariance twirl vs translation twirl
# --------------------------------------------------------------------------
def section_c5():
    t0 = time.time()
    out = {"checks": []}
    p = 31
    n = p * p
    a_of = np.arange(n) // p
    b_of = np.arange(n) % p
    f = (a_of + b_of) % p
    ks = [5, 15, 45]
    # (i) answer-dependent errors e(x) = phi(f(x))
    rows = []
    seeds = list(range(500, 520))
    floor_ok = True
    for m_bad in (3, 6, 9, 12, 15):
        tr_asym, tr_k, inv_err = [], [], []
        for sd in seeds:
            rng = np.random.default_rng(sd * 100 + m_bad)
            phi = np.zeros(p, dtype=np.int64)
            pos = rng.choice(p, m_bad, replace=False)
            phi[pos] = rng.integers(1, p, m_bad)
            e = phi[f]
            # invariance orbit of x = (a,b): {(a+r, b-r)}; the error seen by each vote is e there
            e2 = e.reshape(p, p)
            r = np.arange(p)
            orbit_err = e2[(a_of[:, None] + r[None, :]) % p, (b_of[:, None] - r[None, :]) % p]     # (n, p)
            const = (orbit_err == orbit_err[:, :1]).all(1)
            floor_ok &= bool(const.all())
            inv_err.append(float((orbit_err[:, 0] != 0).mean()))      # error of invariance TTA for ANY number of votes
            N1 = twirl_counts(phi, (p,), (p,))                        # (q, lag); T_x = N1[:, f(x)]/p
            bad = N1[0] <= N1[1:].max(0)
            tr_asym.append(float(bad.mean()))                          # f(x) is uniform on Z_p
            T = (N1 / p).T                                            # (lag, q)
            tr_k.append([float(plurality_fail_exact(T, k).mean()) for k in ks])
        rows.append({"wrong_answers": m_bad, "eps": m_bad / p, "invariance_TTA_error_any_k": summarize(inv_err),
                     "translation_twirl_asymptotic_error": summarize(tr_asym),
                     "translation_twirl_mean_delta_k": {"k": ks, "mean_over_seeds": np.mean(tr_k, 0).tolist()}})
    out["answer_dependent"] = {"G": "Z_31 x Z_31", "f": "a+b", "seeds": seeds, "rows": rows,
                               "note": "e(x) = phi(f(x)), phi wrong on m of the 31 answers with random wrong values. "
                                       "The translation-twirl channel of x is the lag-f(x) channel of phi on Z_31 "
                                       "(effective group size 31, not 961)."}
    out["checks"].append({"id": "C5.floor", "passed": bool(floor_ok and all(
        abs(r["invariance_TTA_error_any_k"]["mean"] - r["eps"]) < 1e-12 for r in rows)),
        "detail": "answer-dependent errors: every invariance-orbit vote is identical, so TTA error = eps for any k"})
    out["checks"].append({"id": "C5.translation_fixes", "passed": bool(all(
        r["translation_twirl_asymptotic_error"]["max"] == 0.0 for r in rows if r["wrong_answers"] <= 9)),
        "detail": "translation twirl: asymptotic error 0 for all 20 seeds when <= 9 of 31 answers are wrong; "
                  "asymptotic error by m: %s" % {r["wrong_answers"]: round(r["translation_twirl_asymptotic_error"]["mean"], 4)
                                                 for r in rows}})
    # (ii) scattered i.i.d. errors: query efficiency
    klist = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 35, 39]
    target = 1e-3
    rows2 = []
    for eps in (0.1, 0.3):
        for sd in (540, 541, 542):
            rng = np.random.default_rng(sd * 10 + int(eps * 10))
            e = iid_field(rng, n, p, eps)
            N = twirl_counts(e, (p, p), (p,))
            T_tr = (N / n).T                                              # (x, q)
            T_inv = np.stack([np.bincount(e[f == s], minlength=p) / p for s in range(p)])   # per level set
            d_tr = [float(plurality_fail_exact(T_tr, k).mean()) for k in klist]
            d_inv = [float(plurality_fail_exact(T_inv, k).mean()) for k in klist]
            k_tr = next((k for k, d in zip(klist, d_tr) if d <= target), None)
            k_inv = next((k for k, d in zip(klist, d_inv) if d <= target), None)
            rows2.append({"eps": eps, "seed": sd, "realised_eps": float((e != 0).mean()), "k": klist,
                          "mean_delta_translation": d_tr, "mean_delta_invariance": d_inv,
                          "per_vote_correct_translation": float(T_tr[:, 0].mean()),
                          "per_vote_correct_translation_pred": 1 / p + (1 - 1 / p) * lam_of(eps, p) ** 2,
                          "per_vote_correct_invariance": float(T_inv[:, 0].mean()),
                          "votes_to_reach_target_translation": k_tr, "votes_to_reach_target_invariance": k_inv,
                          "queries_translation": None if k_tr is None else 2 * k_tr,
                          "queries_invariance": k_inv})
    out["scattered"] = {"target_mean_delta": target, "rows": rows2,
                        "note": "exact mean over inputs of the exact plurality failure probability; votes drawn i.i.d. with "
                                "replacement; a translation vote costs 2 model queries, an invariance vote 1; k searched on "
                                "the listed odd values only"}
    out["checks"].append({"id": "C5.query_efficiency", "passed": bool(all(
        r["queries_invariance"] is not None and r["queries_translation"] is not None
        and r["queries_invariance"] < r["queries_translation"] for r in rows2)),
        "detail": "scattered errors: invariance twirl reaches mean delta <= 1e-3 with fewer queries: %s"
                  % [(r["eps"], r["queries_invariance"], r["queries_translation"]) for r in rows2]})
    out["runtime_s"] = time.time() - t0
    return out


# --------------------------------------------------------------------------
# C6: label-free estimation from the linearity-test pass rate
# --------------------------------------------------------------------------
def section_c6():
    t0 = time.time()
    out = {"checks": []}
    p = 31
    G = Ab((p, p))
    n, q = G.n, p
    a_of = np.arange(n) // p
    b_of = np.arange(n) % p

    def pass_rate(e):
        return float((((e[:, None] + e[None, :] - e[G.add]) % q) == 0).mean())      # ALL ordered pairs (x, y)

    def invert(pi):
        v = (pi - 1 / q) / (1 - 1 / q)
        lam = math.copysign(abs(v) ** (1 / 3), v)
        return lam, (1 - lam) * (1 - 1 / q)

    klist = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 35, 39, 47, 55, 63, 71]
    target = 1e-3
    rows = []
    seeds = list(range(600, 610))
    bound_ok = True
    for eps in (0.02, 0.05, 0.1, 0.2, 0.3, 0.5, 0.7, 0.85):
        acc = []
        for sd in seeds:
            rng = np.random.default_rng(sd * 100 + int(eps * 100))
            e = iid_field(rng, n, q, eps)
            er = float((e != 0).mean())
            pi = pass_rate(e)
            lam_hat, eps_hat = invert(pi)
            bound_ok &= (1 - pi) <= 3 * er + 1e-12
            N = twirl_counts(e, (p, p), (q,))
            T0 = float((N[0] / n).mean())
            T0_pred = 1 / q + (1 - 1 / q) * lam_hat ** 2
            rec = {"eps_real": er, "pi": pi, "pi_pred": 1 / q + (1 - 1 / q) * lam_of(er, q) ** 3,
                   "eps_hat": eps_hat, "T0_mean_actual": T0, "T0_pred_from_lam_hat": T0_pred}
            rec["votes_pred"] = rec["votes_actual"] = rec["actual_mean_delta_at_votes_pred"] = None
            if sd in seeds[:3] and eps <= 0.5:
                # votes needed (label-free prediction vs exact), first three seeds
                Tdep = np.array([[T0_pred] + [(1 - lam_hat ** 2) / q] * (q - 1)])
                Tx = (N / n).T
                kp = next((k for k in klist if plurality_fail_exact(Tdep, k)[0] <= target), None)
                ka = next((k for k in klist if plurality_fail_exact(Tx, k).mean() <= target), None)
                rec["votes_pred"], rec["votes_actual"] = kp, ka
                rec["actual_mean_delta_at_votes_pred"] = float(plurality_fail_exact(Tx, kp).mean())
            acc.append(rec)
        ee = np.array([r["eps_hat"] - r["eps_real"] for r in acc])
        rows.append({"eps_nominal": eps, "seeds": seeds,
                     "pi_mean": float(np.mean([r["pi"] for r in acc])),
                     "pi_pred_mean": float(np.mean([r["pi_pred"] for r in acc])),
                     "max_abs_pi_minus_pred": float(max(abs(r["pi"] - r["pi_pred"]) for r in acc)),
                     "eps_hat_bias": float(ee.mean()), "eps_hat_rmse": float(np.sqrt((ee ** 2).mean())),
                     "T0_actual_mean": float(np.mean([r["T0_mean_actual"] for r in acc])),
                     "T0_pred_mean": float(np.mean([r["T0_pred_from_lam_hat"] for r in acc])),
                     "max_abs_T0_pred_error": float(max(abs(r["T0_mean_actual"] - r["T0_pred_from_lam_hat"]) for r in acc)),
                     # first three seeds; None = not computed (eps > 0.5)
                     "votes_for_mean_delta_1e-3_pred_label_free": [r["votes_pred"] for r in acc[:3]],
                     "votes_for_mean_delta_1e-3_actual": [r["votes_actual"] for r in acc[:3]],
                     "actual_mean_delta_at_predicted_votes": [r["actual_mean_delta_at_votes_pred"] for r in acc[:3]]})
    out["incoherent"] = {"G": G.name, "H": "Z_31", "rows": rows, "k_candidates": klist,
                         "note": "pi is the exact pass rate over all |G|^2 ordered pairs (including the O(1/|G|) degenerate "
                                 "ones); pi_pred uses the realised error rate"}
    out["checks"].append({"id": "C6.law", "passed": bool(max(r["max_abs_pi_minus_pred"] for r in rows) < 0.01),
                          "detail": "incoherent fields: max |pi - (1/q+(1-1/q)lambda^3)| over 8 eps x 10 seeds = %.4f"
                                    % max(r["max_abs_pi_minus_pred"] for r in rows)})
    out["checks"].append({"id": "C6.inversion", "passed": bool(max(r["eps_hat_rmse"] for r in rows if r["eps_nominal"] <= 0.7) < 0.01),
                          "detail": "eps_hat RMSE by eps: %s" % {r["eps_nominal"]: round(r["eps_hat_rmse"], 4) for r in rows}})
    vr = [r for r in rows if r["eps_nominal"] <= 0.5]
    pairs = [(r["eps_nominal"], kp, ka) for r in vr for kp, ka in zip(r["votes_for_mean_delta_1e-3_pred_label_free"],
                                                                      r["votes_for_mean_delta_1e-3_actual"])]
    out["votes_pairs_eps_pred_actual"] = pairs
    out["checks"].append({"id": "C6.votes", "passed": bool(all(ka is not None and kp <= ka <= 1.2 * kp for _, kp, ka in pairs)),
                          "detail": "votes for mean delta <= 1e-3 (k searched on a list of odd values), (eps, label-free "
                                    "prediction, exact) for 3 seeds each: %s; the prediction never exceeds and is within "
                                    "20%% of the exact requirement, but it is optimistic at eps = 0.5" % pairs})
    # coherent families: the inversion is biased; only 1 - pi <= 3 eps is unconditional
    coh = []
    rng = np.random.default_rng(650)
    U = rng.random(n)
    for name, build in (
        ("offset on random set", lambda eps: np.where(U < eps, 1, 0)),
        ("second homomorphism on random set", lambda eps: np.where(U < eps, b_of, 0)),
        ("band (a < eps p), value 1", lambda eps: np.where(a_of < round(eps * p), 1, 0)),
        ("answer-dependent (f in first eps*p answers), value 1",
         lambda eps: np.where(((a_of + b_of) % p) < round(eps * p), 1, 0)),
    ):
        for eps in (0.1, 0.2, 0.3, 0.45, 0.7):
            e = build(eps)
            er = float((e != 0).mean())
            pi = pass_rate(e)
            lam_hat, eps_hat = invert(pi)
            bound_ok &= (1 - pi) <= 3 * er + 1e-12
            rec = {"family": name, "eps_real": er, "pi": pi, "eps_hat": eps_hat, "eps_hat_minus_eps": eps_hat - er,
                   "lower_bound_(1-pi)/3": (1 - pi) / 3}
            if name.startswith("offset"):
                rec["pi_theory"] = (1 - er) ** 3 + 2 * er ** 2 * (1 - er)
            if name.startswith("second"):
                rho = float((U < eps).mean())                      # realised density of the set where M = g
                rec["set_density"] = rho
                rec["pi_theory"] = (1 - rho) ** 3 + rho ** 3 + 3 * rho * (1 - rho) / q
                rec["distance_to_g"] = float(((U >= eps) & (b_of != 0)).mean())
            coh.append(rec)
    out["coherent"] = {"seed": 650, "rows": coh}
    out["checks"].append({"id": "C6.bound", "passed": bool(bound_ok),
                          "detail": "1 - pi <= 3 eps on every field examined (incoherent and coherent)"})
    b3 = [r for r in coh if r["family"].startswith("second") and abs(r["eps_real"] - 0.3) < 0.03][0]
    b7 = [r for r in coh if r["family"].startswith("second") and r["eps_real"] > 0.6][0]
    out["blind_spot"] = {"second_hom_eps~0.3": b3, "second_hom_eps~0.7": b7,
                         "note": "at density 0.7 the model is g with 30% of points equal to f; the test reports the distance "
                                 "to g (nearest homomorphism), not to f"}
    out["checks"].append({"id": "C6.blind_spot", "passed": bool(abs(b7["eps_hat"] - b7["distance_to_g"]) < 0.05 and
                                                             b7["eps_real"] - b7["eps_hat"] > 0.3),
                          "detail": "M = g on %.1f%% of inputs: error rate w.r.t. f is %.3f but eps_hat = %.3f, close to the "
                                    "distance to g (%.3f)" % (100 * b7["set_density"], b7["eps_real"], b7["eps_hat"],
                                                              b7["distance_to_g"])})
    worst = max(coh, key=lambda r: abs(r["eps_hat_minus_eps"]))
    out["coherent_worst_bias"] = worst
    out["runtime_s"] = time.time() - t0
    return out


# --------------------------------------------------------------------------
# C7: horizon of a chained computation
# --------------------------------------------------------------------------
def section_c7():
    t0 = time.time()
    out = {"checks": []}
    p = 31
    n, q = p * p, p
    a_of = np.arange(n) // p      # chain state s
    b_of = np.arange(n) % p       # increment a
    f = (a_of + b_of) % p
    eps = 0.2
    rng = np.random.default_rng(700)
    e = iid_field(rng, n, q, eps)
    er = float((e != 0).mean())
    M = (f + e) % p
    N = twirl_counts(e, (p, p), (q,))
    T = (N / n).T

    def markov(g):
        """g: (n,) per-input survival probability; W[s, s'] = g(s, s'-s)/p."""
        g2 = g.reshape(p, p)
        s = np.arange(p)
        W = g2[s[:, None], (s[None, :] - s[:, None]) % p] / p
        ev = np.linalg.eigvals(W)
        rho = float(np.max(ev.real))
        return W, rho

    def surv(W, Tn):
        return float(np.ones(p) @ np.linalg.matrix_power(W, Tn) @ np.ones(p) / p)

    def t50(W):
        v = np.ones(p) / p
        tn = 0
        while tn < 200000:
            v = v @ W
            tn += 1
            if v.sum() <= 0.5:
                return tn
        return None

    rows = []
    # uncorrected
    g = (e == 0).astype(float)
    W, rho = markov(g)
    rows.append({"k": 0, "label": "uncorrected", "mean_delta": er, "T50_formula_ln2_over_mean_delta": math.log(2) / er,
                 "T50_iid_exact": math.log(2) / -math.log(1 - er), "markov_rho": rho, "one_minus_mean_delta": 1 - er,
                 "T50_markov_exact": t50(W)})
    ks = [1, 3, 5, 9, 15, 25, 41]
    deltas = {}
    for k in ks:
        d = plurality_fail_exact(T, k)
        deltas[k] = d
        md = float(d.mean())
        W, rho = markov(1 - d)
        rows.append({"k": k, "label": "self-corrected, %d votes" % k, "mean_delta": md, "max_delta": float(d.max()),
                     "T50_formula_ln2_over_mean_delta": math.log(2) / md, "T50_iid_exact": math.log(2) / -math.log(1 - md),
                     "markov_rho": rho, "one_minus_mean_delta": 1 - md,
                     "decay_rate_ratio_markov_over_iid": math.log(rho) / math.log(1 - md),
                     "T50_markov_exact": t50(W) if md > 5e-6 else None,
                     "chernoff_bound_mean": float(chernoff_bound(T, k).mean())})
    # Monte Carlo of the actual chain (real BLR votes) for small k
    chains = 4000
    mc = []
    s_idx = np.arange(chains)
    for k, Tmax in ((0, 40), (1, 30), (5, 120), (9, 900)):
        rg = np.random.default_rng(710 + k)
        alive = np.ones(chains, dtype=bool)
        fail_time = np.full(chains, Tmax + 1)
        s = rg.integers(0, p, chains)
        for t in range(1, Tmax + 1):
            a = rg.integers(0, p, chains)
            truth = (s + a) % p
            if k == 0:
                okv = M[s * p + a] == truth
            else:
                r1 = rg.integers(0, p, (chains, k))
                r2 = rg.integers(0, p, (chains, k))
                votes = (M[((s[:, None] + r1) % p) * p + (a[:, None] + r2) % p] - M[r1 * p + r2]) % p
                cnt = np.bincount((s_idx[:, None] * q + votes).ravel(), minlength=chains * q).reshape(chains, q)
                ct = cnt[s_idx, truth].copy()
                cnt[s_idx, truth] = -1
                okv = ct > cnt.max(1)
            newly = alive & ~okv
            fail_time[newly] = t
            alive &= okv
            s = truth                      # the reference trajectory (survival is only counted while all steps are right)
        row = [r for r in rows if r["k"] == k][0]
        Tn = max(1, int(round(row["T50_iid_exact"])))
        g = (e == 0).astype(float) if k == 0 else 1 - deltas[k]
        W, _ = markov(g)
        ex = surv(W, Tn)
        emp = float((fail_time > Tn).mean())
        se = math.sqrt(ex * (1 - ex) / chains)
        mc.append({"k": k, "chains": chains, "T_max": Tmax, "T_eval": Tn, "survival_mc": emp, "survival_markov_exact": ex,
                   "survival_iid_formula": (1 - row["mean_delta"]) ** Tn, "z_mc_vs_exact": (emp - ex) / se,
                   "median_failure_time_mc": float(np.median(fail_time))})
    out["incoherent_chain"] = {"G": "Z_31 x Z_31", "task": "running sum s_{t+1} = M(s_t, a_t), a_t uniform", "eps_nominal": eps,
                               "eps_realised": er, "field_seed": 700, "rows": rows, "monte_carlo": mc,
                               "note": "T50_markov_exact is the first T at which the exact survival probability of the "
                                       "Markov chain (uniform start) is <= 1/2; not computed when the horizon exceeds 2e5 steps"}
    zmax = max(abs(m["z_mc_vs_exact"]) for m in mc)
    out["checks"].append({"id": "C7.mc", "passed": bool(zmax < 4),
                          "detail": "simulated chains (%d per k) match the exact Markov survival (max |z| = %.2f)" % (chains, zmax)})
    rr = [r["decay_rate_ratio_markov_over_iid"] for r in rows if "decay_rate_ratio_markov_over_iid" in r]
    out["checks"].append({"id": "C7.formula_incoherent", "passed": bool(all(0.9 < v < 1.1 for v in rr)),
                          "detail": "incoherent field: exact chain decay rate / (-ln(1 - mean delta_k)) for k=%s: %s"
                                    % (ks, [round(v, 4) for v in rr])})
    hz = [r["T50_iid_exact"] for r in rows if r["k"] > 0]
    out["horizon_growth_per_vote"] = {"k": ks, "T50": hz,
                                      "ln_T50_slope_between_last_two": math.log(hz[-1] / hz[-2]) / (ks[-1] - ks[-2]),
                                      "min_rate_I_over_inputs": float(rate_I(T).min()),
                                      "mean_channel_rate_I": float(rate_I(T.mean(0, keepdims=True))[0])}
    # structured counterexample: errors only when both the state and the next state lie in a band B
    Bset = np.arange(p) < 15
    e_s = np.where(Bset[a_of] & Bset[f], 1, 0)
    er_s = float((e_s != 0).mean())
    W, rho = markov((e_s == 0).astype(float))
    beta = 15 / p
    rho_theory = ((1 - beta) + math.sqrt((1 - beta) * (1 + 3 * beta))) / 2
    out["structured_chain"] = {"definition": "uncorrected chain; e(s,a) != 0 iff s in B and s+a in B, |B| = 15 of 31",
                               "eps": er_s, "one_minus_eps": 1 - er_s, "markov_rho": rho, "rho_closed_form": rho_theory,
                               "T50_formula": math.log(2) / -math.log(1 - er_s), "T50_markov_exact": t50(W),
                               "survival_T20_formula": (1 - er_s) ** 20, "survival_T20_exact": surv(W, 20)}
    out["checks"].append({"id": "C7.structured_deviation", "passed": bool(abs(rho - rho_theory) < 1e-9 and rho > 1 - er_s + 0.02),
                          "detail": "state-correlated errors: exact per-step survival factor %.4f vs 1-eps = %.4f "
                                    "(the i.i.d. formula underestimates the horizon)" % (rho, 1 - er_s)})
    out["runtime_s"] = time.time() - t0
    return out


# --------------------------------------------------------------------------
# figure
# --------------------------------------------------------------------------
def make_figure(c4, path):
    sys.path.insert(0, HERE)
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import paperstyle as ps
    ps.apply()
    fam = c4["families"]
    series = [("incoherent", "Scattered values (incoherent)", ps.SERIES[0]),
              ("offset", "Offset on a random set", ps.SERIES[1]),
              ("second_hom", "Second homomorphism", ps.SERIES[2]),
              ("band_odd", "Offset on a band, 2h \u2260 0", ps.SERIES[3]),
              ("band_2torsion", "Offset on a band, 2h = 0", ps.SERIES[4])]
    fig, axes = plt.subplots(1, 2, figsize=(7.4, 3.9), gridspec_kw={"wspace": 0.32})
    refs = [(0.25, "1/4"), (1 / 3, "1/3"), (0.5, "1/2"), (30 / 31, "chance")]
    handles = []
    for ax, key, ylab in ((axes[0], "correctable_fraction_mean", "fraction of inputs correctable"),
                          (axes[1], "worst_margin_mean", "worst-input margin")):
        for xv, lab in refs:
            ax.axvline(xv, color=ps.REFERENCE, lw=0.8, ls=(0, (4, 3)), zorder=1)
        handles = []
        for i, (k, lab, col) in enumerate(series):
            d = fam[k]
            xs = d.get("realised_error_rate_mean", d["eps"])          # x axis = realised error rate
            if k.startswith("band"):
                # band families are defined only at the grid points eps = w/n. Draw each jump at the grid
                # point with the lower value, so every low value covers exactly its own grid points (a break
                # starts at the first broken grid point and ends at the last one); dots mark the grid points.
                X, Y = [xs[0]], [d[key][0]]
                for x0, x1, y0, y1 in zip(xs[:-1], xs[1:], d[key][:-1], d[key][1:]):
                    if y1 < y0:
                        X += [x1, x1]; Y += [y0, y1]
                    elif y1 > y0:
                        X += [x0, x1]; Y += [y1, y1]
                    else:
                        X += [x1]; Y += [y1]
                ln, = ax.plot(X, Y, color=col, lw=1.6, label=lab, zorder=3 + (5 - i))
                ax.plot(xs, d[key], ls="none", marker="o", markersize=2.2, markeredgewidth=0, color=col,
                        zorder=3 + (5 - i))
            else:
                ln, = ax.plot(xs, d[key], color=col, lw=1.8, label=lab, zorder=3 + (5 - i))
            handles.append(ln)
        ax.set_xlim(0, 1.0)
        ax.set_xlabel("error rate \u03b5")
        ax.set_ylabel(ylab)
        ax.set_xticks([0, 0.25, 0.5, 0.75, 1.0])
    box = dict(facecolor=ps.SURFACE, edgecolor="none", pad=1.0)
    ax = axes[0]
    ax.set_ylim(-0.04, 1.2)
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
    for xv, lab in refs:
        ax.text(xv, 1.19, lab, ha="center", va="top", fontsize=8.5, color=ps.INK2, bbox=box, zorder=9)
    ax.set_title("a  Correctable inputs")
    ax = axes[1]
    ax.axhline(0, color=ps.INK2, lw=0.9, zorder=2)
    ax.set_ylim(-1.08, 1.3)
    ax.set_yticks([-1, -0.5, 0, 0.5, 1.0])
    for xv, lab in refs:
        ax.text(xv, 1.29, lab, ha="center", va="top", fontsize=8.5, color=ps.INK2, bbox=box, zorder=9)
    ax.set_title("b  Worst-input margin")
    ax.text(0.02, -0.62, "below 0: some input\nis uncorrectable", ha="left", va="top", fontsize=8.5,
            color=ps.INK2, linespacing=1.2, zorder=9)
    fig.legend(handles=handles, loc="lower center", ncol=3, bbox_to_anchor=(0.5, -0.13), fontsize=9,
               handlelength=1.8, columnspacing=1.2)
    ps.save(fig, path)
    plt.close(fig)


# --------------------------------------------------------------------------
def _jsonable(o):
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.floating,)):
        return float(o)
    if isinstance(o, (np.bool_,)):
        return bool(o)
    if isinstance(o, np.ndarray):
        return o.tolist()
    raise TypeError(type(o))


def main():
    t0 = time.time()
    sections = [("c2", section_c2), ("c3_finite_size", section_c3_finite), ("c1", section_c1), ("c3_law", section_c3_law),
                ("c4", section_c4), ("c5", section_c5), ("c6", section_c6), ("c7", section_c7)]
    res = {}
    with ProcessPoolExecutor(max_workers=2) as ex:
        futs = {name: ex.submit(fn) for name, fn in sections}
        for name, _ in sections:
            res[name] = futs[name].result()
            print("[%6.1fs] %-15s done (section runtime %.1fs)" % (time.time() - t0, name, res[name]["runtime_s"]), flush=True)
    make_figure(res["c4"], os.path.join(ROOT, "figures", "fig_phase_diagram"))
    checks = []
    for name in ("c1", "c2", "c3_law", "c3_finite_size", "c4", "c5", "c6", "c7"):
        for c in res[name]["checks"]:
            checks.append(dict(c, section=name))
    import scipy
    outd = {"meta": {"script": "code/theory_checks.py", "command": "python3 code/theory_checks.py",
                     "python": sys.version.split()[0], "numpy": np.__version__, "scipy": scipy.__version__,
                     "processes": 2, "omp_num_threads": os.environ.get("OMP_NUM_THREADS"),
                     "runtime_s_total": None,
                     "definition_correctable": "N_0(x) > N_h(x) for all h != 0; ties count as failures",
                     "seeds": "every section constructs numpy default_rng generators from fixed integers recorded in the "
                              "section's output (c1: 101,102; c3_law: 300-319, 9000-9099, 100000-103999; "
                              "c3_finite_size: 7000+100p+s, s<24; "
                              "c4: 400-407; c5: 500-519, 540-542; c6: 600-609, 650; c7: 700, 710-719)"},
            "checks": checks}
    for name in ("c1", "c2", "c3_law", "c3_finite_size", "c4", "c5", "c6", "c7"):
        outd[name] = res[name]
    outd["meta"]["runtime_s_total"] = time.time() - t0
    outd["meta"]["all_checks_passed"] = bool(all(c["passed"] for c in checks))
    with open(os.path.join(ROOT, "results", "theory_checks.json"), "w") as fh:
        json.dump(outd, fh, indent=1, default=_jsonable)
    print("\n%d checks, %d passed, total %.1fs" % (len(checks), sum(c["passed"] for c in checks), time.time() - t0))
    for c in checks:
        print(" %s %-24s %s" % ("PASS" if c["passed"] else "FAIL", c["id"], c["detail"]))


if __name__ == "__main__":
    if "--figure-only" in sys.argv:
        # redraw Figure 1 from the saved JSON without recomputing
        with open(os.path.join(ROOT, "results", "theory_checks.json")) as fh:
            make_figure(json.load(fh)["c4"], os.path.join(ROOT, "figures", "fig_phase_diagram"))
    else:
        main()

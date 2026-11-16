#!/usr/bin/env python3
"""exp_channels.py -- package A: the twirled channels of trained networks.

    python3 code/exp_channels.py              compute everything, write results/exp_channels.json, draw figures
    python3 code/exp_channels.py --figs-only  redraw the three figures from the existing JSON

Deterministic (all seeds are listed in the JSON under meta.seeds); one process, OMP_NUM_THREADS=1.
Families analysed: add/grok, add/memo, lin (all use the 2-query BLR vote).  mul is not touched here.

Sections of the JSON
  A1  the depolarizing law for the MEAN per-vote correctness on real networks
  A2  coherence of the wrong votes (largest wrong-vote mass versus matched incoherent fields)
  A3  correctability (truth = strict mode of the twirled channel) versus error rate, per training run
  A4  failure probability versus number of votes for representative models (exact, eps-only, Chernoff, real votes)
  A5  anatomy of the residual coherence in two add/grok models
  per_model  one row per model (columnar), every statistic used above

Conventions: flat index 0 is the identity of G; "x != 0" statistics drop that row.  A tie counts as a failure.
Matched nulls for a model with n_err errors on G (20 fields each, seeded by the model's position in the zoo index):
  iid   = error set a uniformly random n_err-subset of G, wrong values i.i.d. uniform on Z_q \\ {0}
          (the incoherent model conditioned on the model's realised error rate);
  shuf  = the model's own error table with its positions permuted uniformly at random
          (keeps the exact histogram of error values, destroys their arrangement).
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
import json
import math
import sys
import time

import numpy as np
import scipy.fft as sfft
import scipy.stats as sstats

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import core  # noqa: E402

OUT_JSON = os.path.join(core.RESULTS_DIR, "exp_channels.json")
FAMILIES = ("add/grok", "add/memo", "lin")
N_NULL = 20
SEED_IID, SEED_SHUF, SEED_FS, SEED_VOTE, SEED_PERM, SEED_CHECK = 51000, 52000, 53000, 54000, 55000, 56000
KS = (1, 3, 5, 9, 17, 33, 65, 129)
K_REAL_MAX = 33
REAL_REPS = 100            # real-vote repetitions per input for the mean
REAL_WORST = 20000         # real-vote repetitions for the worst input
ACC_FLOOR = 1e-10          # exact failure values below this are at the accuracy floor of plurality_fail_exact
EPS_TARGETS_GROK47 = (0.1, 0.3, 0.5, 0.65)
SEED0_TOL = 0.03           # "seed 0 preferred": use a seed-0 snapshot if one lies within this distance of the target
N_PERM = 200               # permutations for the anatomy nulls
FS_FIELDS = 24             # i.i.d. fields per group for the finite-size threshold


# ----------------------------------------------------------------------------------------------
# helpers
# ----------------------------------------------------------------------------------------------
def onehot_counts(Eb, q):
    """Batched twirled counts.  Eb: (B, *shape) ints in Z_q.  Returns (B, |G|, q) int64 with
    N[b, x, h] = #{r : E_b(x+r) - E_b(r) = h}.  Autocorrelation of the one-hot indicator on G x H
    (same identity as core.twirled_counts, real FFT); checked against core.twirled_counts in selfcheck()."""
    Eb = np.asarray(Eb, dtype=np.int64) % q
    B = Eb.shape[0]
    shape = Eb.shape[1:]
    nG = int(np.prod(shape))
    I = np.zeros((B, nG, q))
    I[np.arange(B)[:, None], np.arange(nG)[None, :], Eb.reshape(B, nG)] = 1.0
    I = I.reshape((B,) + tuple(shape) + (q,))
    axes = tuple(range(1, I.ndim))
    F = sfft.rfftn(I, axes=axes)
    N = sfft.irfftn(F.real ** 2 + F.imag ** 2, s=I.shape[1:], axes=axes)
    R = np.rint(N)
    if float(np.abs(N - R).max()) > 1e-6:
        raise FloatingPointError("onehot_counts: not integral")
    R = R.astype(np.int64).reshape(B, nG, q)
    assert (R.sum(2) == nG).all() and (R >= 0).all()
    return R


def stats_from_counts(N):
    """N: (B, |G|, q) exact counts.  Per-field statistics over the inputs x != 0."""
    nG = N.shape[1]
    Nx = N[:, 1:, :]
    n0 = Nx[:, :, 0]
    nw = Nx[:, :, 1:].max(2)
    t0 = n0 / nG
    P = t0.mean(1)
    sd = t0.std(1, ddof=1)
    binom = np.sqrt(np.clip(P * (1 - P), 0, None) / nG)
    with np.errstate(divide="ignore", invalid="ignore"):
        od = np.where(binom > 0, sd / binom, np.nan)
    rate_min = core.hellinger_rate(t0, nw / nG).min(1)         # worst-input exponent (0 if some input is uncorrectable)
    return dict(t0_mean=P, t0_sd=sd, binom_sd=binom, overdisp=od,
                maxwrong=nw.max(1) / nG, min_margin=(n0 - nw).min(1) / nG,
                n_unc=(n0 <= nw).sum(1), rate_min=rate_min)


def summ(v):
    v = np.asarray([x for x in v if x is not None and np.isfinite(x)], dtype=float)
    if len(v) == 0:
        return {"n": 0}
    return {"n": int(len(v)), "mean": float(v.mean()), "median": float(np.median(v)),
            "q25": float(np.quantile(v, 0.25)), "q75": float(np.quantile(v, 0.75)),
            "min": float(v.min()), "max": float(v.max())}


def jsonable(o):
    if isinstance(o, dict):
        return {str(k): jsonable(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [jsonable(v) for v in o]
    if isinstance(o, np.ndarray):
        return jsonable(o.tolist())
    if isinstance(o, (np.bool_,)):
        return bool(o)
    if isinstance(o, np.integer):
        return int(o)
    if isinstance(o, (float, np.floating)):
        f = float(o)
        return f if math.isfinite(f) else None
    return o


def selfcheck():
    """onehot_counts against core.twirled_counts on random fields of every group shape used."""
    rng = np.random.default_rng(SEED_CHECK)
    out = []
    for shape, q in [((23, 23), 23), ((31, 31), 31), ((47, 47), 47), ((53, 53), 53), ((7, 7, 7, 7), 7)]:
        Eb = np.where(rng.random((4,) + shape) < rng.random((4,) + (1,) * len(shape)),
                      rng.integers(1, q, (4,) + shape), 0)
        N = onehot_counts(Eb, q)
        ref = np.stack([core.twirled_counts(e, q) for e in Eb])
        ok = bool((N == ref).all())
        assert ok
        out.append({"shape": list(shape), "q": q, "fields": 4, "identical_to_core_twirled_counts": ok})
    return out


# ----------------------------------------------------------------------------------------------
# per-model pass (A1, A2, A3 inputs)
# ----------------------------------------------------------------------------------------------
def structure_z(E, f, q):
    """Chi-square-approximation z-scores of the G statistic (2 N MI) between the error INDICATOR and
    (i) each coordinate (max over coordinates reported), (ii) the true label f(x)."""
    shape = E.shape
    Ef = E.ravel()
    ind = (Ef != 0).astype(np.int64)
    nG = Ef.size
    C = core.coords(shape)

    def gz(lev, nlev):
        tab = np.zeros((2, nlev))
        np.add.at(tab, (ind, lev), 1.0)
        ex = tab.sum(1, keepdims=True) * tab.sum(0, keepdims=True) / nG
        with np.errstate(divide="ignore", invalid="ignore"):
            g = 2.0 * np.where(tab > 0, tab * np.log(tab / ex), 0.0).sum()
        dof = nlev - 1
        return float((g - dof) / math.sqrt(2.0 * dof))
    zc = [gz(C[:, i], shape[i]) for i in range(len(shape))]
    zl = gz(np.asarray(f).ravel().astype(np.int64), q)
    return max(zc), zl


def per_model_pass(models, log):
    cols = {}

    def put(k, v):
        cols.setdefault(k, []).append(v)
    counts_cache = {}
    t_start = time.time()
    for mi, (zi, r) in enumerate(models):
        q, p, n = r["q"], r["p"], r["n"]
        shape = core.group_shape(p, n)
        nG = int(np.prod(shape))
        E = core.error_table(r["id"])
        Ef = E.ravel()
        n_err = int((Ef != 0).sum())
        eps = n_err / nG
        base = dict(id=r["id"], zoo_index=zi, family=r["family"], p=p, q=q, G_size=nG, run_id=r["run_id"],
                    step=r["step"], train_frac=r["train_frac"], holdout=r["holdout"], init_seed=r["init_seed"],
                    split_seed=r["split_seed"], n_err=n_err, eps=eps)
        for k, v in base.items():
            put(k, v)
        assert abs(eps - r["eps"]) < 1e-12
        keys_null = ["t0_mean", "t0_sd", "overdisp", "maxwrong", "min_margin"]
        if n_err == 0:
            for k in ["lam", "t0_mean", "law", "naive", "dev_law", "dev_naive", "collision_identity_resid",
                      "value_conc", "fs_term", "n_eff_wrong", "top_wrong_share", "t0_sd", "binom_sd", "overdisp",
                      "maxwrong", "depol_pw", "min_margin", "lam_sq", "gz_coord_max", "gz_label",
                      "coh_ratio_iid", "coh_ratio_shuf", "coh_ratio_depol", "n_iid_ge_obs", "n_shuf_ge_obs",
                      "min_margin_iid_median", "min_margin_shuf_median", "n_unc_iid_fields", "n_unc_shuf_fields",
                      "rate_min", "rate_law", "rate_ratio_law", "rate_min_iid_median", "rate_law_ratio_iid_median",
                      "out_collision", "err_collision", "shift_inv_mean", "shift_inv_identity_resid", "tz_mean",
                      "t0_mean_fne0", "frac_hstar_minus_f", "frac_unc_beaten_by_minus_f", "gmax_is_minus_f",
                      "frac_x_zero_vote_beats_truth"]:
                put(k, None)
            for nm in ("iid", "shuf"):
                for k in ("t0_mean", "overdisp", "maxwrong"):
                    put(f"{k}_{nm}_median", None)
                put(f"maxwrong_{nm}_min", None)
                put(f"maxwrong_{nm}_max", None)
            put("n_uncorrectable", 0)
            put("frac_correctable", 1.0)
            put("all_correctable", True)
            continue
        N = core.twirled_counts(E, q)                        # verified library routine for the model itself
        st = stats_from_counts(N[None])
        hist = np.bincount(Ef, minlength=q).astype(float)
        pi = hist / nG
        S = float((pi ** 2).sum())
        ident = (nG * S - 1.0) / (nG - 1.0)                  # exact identity for mean_{x != 0} T_x(0)
        law = float(core.pc_law(eps, q, 2))
        lam_ = float(core.lam(eps, q))
        t0m = float(st["t0_mean"][0])
        wrong_sq = float((pi[1:] ** 2).sum())
        put("lam", lam_)
        put("t0_mean", t0m)
        put("law", law)
        put("naive", (1 - eps) ** 2)
        put("dev_law", t0m - law)
        put("dev_naive", t0m - (1 - eps) ** 2)
        put("collision_identity_resid", t0m - ident)
        put("value_conc", wrong_sq - eps ** 2 / (q - 1))     # >= 0 (Cauchy-Schwarz), 0 iff wrong values uniform
        put("fs_term", (1.0 - S) / (nG - 1.0))               # dev_law = value_conc - fs_term exactly
        put("n_eff_wrong", eps ** 2 / wrong_sq)              # effective number of wrong values (q-1 if uniform)
        put("top_wrong_share", float(hist[1:].max() / n_err))
        put("t0_sd", float(st["t0_sd"][0]))
        put("binom_sd", float(st["binom_sd"][0]))
        put("overdisp", float(st["overdisp"][0]))
        mw = float(st["maxwrong"][0])
        put("maxwrong", mw)
        dp = float(core.pw_law(eps, q, 2))
        put("depol_pw", dp)
        put("min_margin", float(st["min_margin"][0]))
        put("lam_sq", lam_ ** 2)
        n_unc = int(st["n_unc"][0])
        put("n_uncorrectable", n_unc)
        put("frac_correctable", (nG - n_unc) / nG)
        put("all_correctable", n_unc == 0)
        zc, zl = structure_z(E, core.model_true_table(r["id"]), q)
        put("gz_coord_max", zc)
        put("gz_label", zl)
        # worst-input exponent versus the exponent predicted from eps alone
        rl = float(core.rate_law(eps, q, 2))
        put("rate_min", float(st["rate_min"][0]))
        put("rate_law", rl)
        put("rate_ratio_law", float(st["rate_min"][0]) / rl if rl > 0 else None)
        # the "zero vote": M(x+r) = M(r), i.e. the vote offset is h = -f(x)
        ff = core.model_true_table(r["id"]).ravel().astype(np.int64) % q
        h0 = (-ff) % q
        Mf = (Ef + ff) % q
        mu = np.bincount(Mf, minlength=q) / nG                # histogram of the model's OUTPUTS
        S_out = float((mu ** 2).sum())
        tz = N[np.arange(nG), h0] / nG                        # Pr_r[M(x+r) = M(r)]
        valid = (np.arange(nG) != 0) & (ff != 0)              # x != 0 and -f(x) is a WRONG value
        hstar = 1 + N[:, 1:].argmax(1)
        nwx = N[np.arange(nG), hstar]
        unc = valid & (N[:, 0] <= nwx)
        gi = 1 + int(nwx[1:].argmax())
        put("out_collision", S_out)
        put("err_collision", S)
        put("shift_inv_mean", float(tz[1:].mean()))
        put("shift_inv_identity_resid", float(tz[1:].mean()) - (nG * S_out - 1.0) / (nG - 1.0))
        put("tz_mean", float(tz[valid].mean()))
        put("t0_mean_fne0", float((N[valid, 0] / nG).mean()))
        put("frac_hstar_minus_f", float((hstar[valid] == h0[valid]).mean()))
        put("frac_unc_beaten_by_minus_f", float((N[unc, h0[unc]] >= N[unc, 0]).mean()) if unc.any() else None)
        put("gmax_is_minus_f", bool(hstar[gi] == h0[gi]))
        put("frac_x_zero_vote_beats_truth", float((tz[valid] >= N[valid, 0] / nG).mean()))
        # matched nulls
        rng_i = np.random.default_rng([SEED_IID, zi])
        rng_s = np.random.default_rng([SEED_SHUF, zi])
        Eb_i = np.zeros((N_NULL, nG), dtype=np.int64)
        Eb_s = np.empty((N_NULL, nG), dtype=np.int64)
        for b in range(N_NULL):
            pos = rng_i.permutation(nG)[:n_err]
            Eb_i[b, pos] = rng_i.integers(1, q, n_err)
            Eb_s[b] = Ef[rng_s.permutation(nG)]
        res = {}
        for nm, Eb in (("iid", Eb_i), ("shuf", Eb_s)):
            res[nm] = stats_from_counts(onehot_counts(Eb.reshape((N_NULL,) + shape), q))
            for k in ("t0_mean", "overdisp", "maxwrong"):
                put(f"{k}_{nm}_median", float(np.nanmedian(res[nm][k])))
            put(f"maxwrong_{nm}_min", float(res[nm]["maxwrong"].min()))
            put(f"maxwrong_{nm}_max", float(res[nm]["maxwrong"].max()))
        put("coh_ratio_iid", mw / float(np.median(res["iid"]["maxwrong"])))
        put("coh_ratio_shuf", mw / float(np.median(res["shuf"]["maxwrong"])))
        put("coh_ratio_depol", mw / dp)
        put("n_iid_ge_obs", int((res["iid"]["maxwrong"] >= mw - 1e-15).sum()))
        put("n_shuf_ge_obs", int((res["shuf"]["maxwrong"] >= mw - 1e-15).sum()))
        put("min_margin_iid_median", float(np.median(res["iid"]["min_margin"])))
        put("min_margin_shuf_median", float(np.median(res["shuf"]["min_margin"])))
        rmi = float(np.median(res["iid"]["rate_min"]))
        put("rate_min_iid_median", rmi)
        put("rate_law_ratio_iid_median", rmi / rl if rl > 0 else None)
        put("n_unc_iid_fields", int((res["iid"]["n_unc"] > 0).sum()))
        put("n_unc_shuf_fields", int((res["shuf"]["n_unc"] > 0).sum()))
        if (mi + 1) % 200 == 0:
            log(f"  per-model pass {mi + 1}/{len(models)}  ({time.time() - t_start:.0f} s)")
    L = len(cols["id"])
    assert all(len(v) == L for v in cols.values()), {k: len(v) for k, v in cols.items()}
    return cols


def col(cols, k, mask=None, dtype=float):
    v = cols[k]
    if mask is not None:
        v = [x for x, m in zip(v, mask) if m]
    if dtype is None:
        return v
    return np.array([np.nan if x is None else x for x in v], dtype=dtype)


# ----------------------------------------------------------------------------------------------
# A1
# ----------------------------------------------------------------------------------------------
def section_a1(cols):
    fam = np.array(cols["family"])
    p = np.array(cols["p"])
    eps = np.array(cols["eps"])
    run = np.array(cols["run_id"])
    has = eps > 0
    out = {"definition": "t0_mean = mean over x != 0 of T_x(0); law = pc_law(eps, q, 2) at the model's realised eps; "
                         "naive = (1-eps)^2; dev = measured - prediction; overdisp = sd over x != 0 of T_x(0) "
                         "(ddof 1) divided by sqrt(P(1-P)/|G|) with P = t0_mean",
           "identity": "mean_{x != 0} T_x(0) = (|G| S - 1)/(|G| - 1), S = sum_v pi_v^2 the collision probability "
                       "of the error-value histogram (pi_0 = 1 - eps): the MEAN per-vote correctness depends only "
                       "on the histogram of error values, not on where the errors are.  Hence "
                       "dev_law = value_conc - fs_term with value_conc = sum_{v != 0} pi_v^2 - eps^2/(q-1) >= 0 and "
                       "fs_term = (1 - S)/(|G| - 1).",
           "identity_max_abs_residual": float(np.nanmax(np.abs(col(cols, "collision_identity_resid")[has]))),
           "decomposition_max_abs_residual": float(np.nanmax(np.abs(
               col(cols, "dev_law")[has] - (col(cols, "value_conc")[has] - col(cols, "fs_term")[has])))),
           "cells": {}}

    def cell(mask):
        m = mask & has
        d = col(cols, "dev_law")[m]
        dn = col(cols, "dev_naive")[m]
        t0 = col(cols, "t0_mean")[m]
        d_iid = col(cols, "t0_mean_iid_median")[m] - col(cols, "law")[m]
        runs = sorted(set(run[m]))
        per_run_mean_abs = [float(np.abs(col(cols, "dev_law")[m & (run == rr)]).mean()) for rr in runs]
        central = m & (eps >= 0.05) & (eps <= 0.9)
        od = col(cols, "overdisp")
        return {
            "n_models": int(m.sum()), "n_runs": len(runs),
            "eps_range": [float(eps[m].min()), float(eps[m].max())],
            "dev_law_mean_abs": float(np.abs(d).mean()), "dev_law_max_abs": float(np.abs(d).max()),
            "dev_law_mean_signed": float(d.mean()), "dev_law_min": float(d.min()), "dev_law_max": float(d.max()),
            "dev_law_frac_positive": float((d > 0).mean()),
            "dev_law_argmax_id": np.array(cols["id"])[m][int(np.abs(d).argmax())],
            "dev_law_argmax_eps": float(eps[m][int(np.abs(d).argmax())]),
            "dev_naive_mean_abs": float(np.abs(dn).mean()), "dev_naive_max_abs": float(np.abs(dn).max()),
            "dev_naive_mean_signed": float(dn.mean()),
            "rel_dev_law_max_abs": float(np.abs(d / t0).max()),
            "matched_iid_dev_law_mean_abs": float(np.abs(d_iid).mean()),
            "matched_iid_dev_law_max_abs": float(np.abs(d_iid).max()),
            "per_run_mean_abs_dev_law": summ(per_run_mean_abs),
            "value_conc": summ(col(cols, "value_conc")[m]),
            "n_eff_wrong_over_qm1": summ(col(cols, "n_eff_wrong")[m] / (np.array(cols["q"])[m] - 1)),
            "overdisp_all": summ(od[m]),
            "overdisp_eps_0p05_to_0p9": summ(od[central]),
            "overdisp_matched_iid_eps_0p05_to_0p9": summ(col(cols, "overdisp_iid_median")[central]),
            "overdisp_matched_shuf_eps_0p05_to_0p9": summ(col(cols, "overdisp_shuf_median")[central]),
            "overdisp_over_matched_iid_eps_0p05_to_0p9": summ(od[central] / col(cols, "overdisp_iid_median")[central]),
            "n_models_eps_0p05_to_0p9": int(central.sum()),
            "by_eps_bin": {f"[{lo:.1f},{lo + 0.1:.1f})": {
                "n_models": int(b.sum()), "n_runs": len(set(run[b])),
                "dev_law_mean_abs": float(np.abs(col(cols, "dev_law")[b]).mean()),
                "dev_law_max_abs": float(np.abs(col(cols, "dev_law")[b]).max()),
                "overdisp_median": float(np.nanmedian(od[b])),
                "overdisp_matched_iid_median": float(np.nanmedian(col(cols, "overdisp_iid_median")[b])),
                "overdisp_over_matched_iid_median": float(np.nanmedian(od[b] / col(cols, "overdisp_iid_median")[b])),
                "overdisp_over_matched_iid_max": float(np.nanmax(od[b] / col(cols, "overdisp_iid_median")[b]))}
                for lo in np.arange(10) / 10.0
                for b in [m & (eps >= lo) & (eps < lo + 0.1 + (1e-9 if lo > 0.85 else 0))] if b.sum() > 0},
        }
    out["overdispersion_note"] = ("The binomial value sqrt(P(1-P)/|G|) is NOT a calibrated reference: for matched i.i.d. fields "
                                  "the ratio is below 1 (the |G| terms of N_0(x) share one fixed error set and are negatively "
                                  "dependent; at small eps the ratio tends to sqrt(2 eps)).  The calibrated statistic is "
                                  "overdisp_over_matched_iid = overdisp(model) / median overdisp of its 20 matched i.i.d. fields.")
    for f in FAMILIES:
        out["cells"][f] = cell(fam == f)
        for pp in sorted(set(p[fam == f])):
            if len(set(p[fam == f])) > 1:
                out["cells"][f"{f}|p={pp}"] = cell((fam == f) & (p == pp))
    out["cells"]["all"] = cell(np.ones(len(eps), bool))
    return out


# ----------------------------------------------------------------------------------------------
# A2
# ----------------------------------------------------------------------------------------------
def section_a2(cols):
    fam = np.array(cols["family"])
    p = np.array(cols["p"])
    eps = np.array(cols["eps"])
    run = np.array(cols["run_id"])
    has = eps > 0
    ri = col(cols, "coh_ratio_iid")
    rs = col(cols, "coh_ratio_shuf")
    rd = col(cols, "coh_ratio_depol")
    nge = col(cols, "n_iid_ge_obs")
    nges = col(cols, "n_shuf_ge_obs")
    bins = [(round(0.1 * i, 1), round(0.1 * (i + 1), 1)) for i in range(10)]
    out = {"definition": "maxwrong = max over x != 0, h != 0 of T_x(h).  coh_ratio_iid = maxwrong / median of the "
                         f"same statistic over {N_NULL} matched i.i.d. fields PER MODEL (same group, exactly the same "
                         "number of errors, wrong values uniform); coh_ratio_shuf = the same with position-shuffled "
                         "copies of the model's own error table; coh_ratio_depol = maxwrong / ((1 - lambda^2)/q) "
                         "(the depolarizing value is a MEAN over inputs, so even i.i.d. fields exceed it at the max).",
           "n_null_fields_per_model": N_NULL, "cells": {}}

    def cell(mask):
        m = mask & has
        runs = sorted(set(run[m]))
        per_run_med = [float(np.median(ri[m & (run == rr)])) for rr in runs]
        per_run_med_s = [float(np.median(rs[m & (run == rr)])) for rr in runs]
        c = {"n_models": int(m.sum()), "n_runs": len(runs),
             "coh_ratio_iid": summ(ri[m]), "coh_ratio_shuf": summ(rs[m]), "coh_ratio_depol": summ(rd[m]),
             "frac_ratio_iid_gt_1": float((ri[m] > 1).mean()),
             "frac_ratio_iid_gt_1p5": float((ri[m] > 1.5).mean()),
             "frac_ratio_iid_gt_2": float((ri[m] > 2).mean()),
             "frac_obs_exceeds_all_iid_fields": float((nge[m] == 0).mean()),
             "frac_obs_exceeds_all_shuf_fields": float((nges[m] == 0).mean()),
             "per_run_median_ratio_iid": summ(per_run_med),
             "per_run_median_ratio_shuf": summ(per_run_med_s),
             "argmax_ratio_iid_id": np.array(cols["id"])[m][int(ri[m].argmax())],
             "argmax_ratio_iid_eps": float(eps[m][int(ri[m].argmax())]),
             "by_eps_bin": {}}
        if m.sum() >= 5:
            sr = sstats.spearmanr(eps[m], ri[m])
            c["spearman_ratio_iid_vs_eps"] = {"rho": float(sr.statistic), "p_value_models_as_independent": float(sr.pvalue)}
        for lo, hi in bins:
            b = m & (eps >= lo) & ((eps < hi) | ((hi == 1.0) & (eps <= hi)))
            if b.sum() == 0:
                continue
            c["by_eps_bin"][f"[{lo},{hi})"] = {
                "n_models": int(b.sum()), "n_runs": len(set(run[b])),
                "ratio_iid_median": float(np.median(ri[b])), "ratio_iid_q25": float(np.quantile(ri[b], 0.25)),
                "ratio_iid_q75": float(np.quantile(ri[b], 0.75)), "ratio_iid_max": float(ri[b].max()),
                "ratio_shuf_median": float(np.median(rs[b])),
                "maxwrong_median": float(np.median(col(cols, "maxwrong")[b])),
                "maxwrong_iid_median": float(np.median(col(cols, "maxwrong_iid_median")[b])),
                "depol_pw_median": float(np.median(col(cols, "depol_pw")[b])),
                "frac_obs_exceeds_all_iid_fields": float((nge[b] == 0).mean()),
                "min_margin_median": float(np.median(col(cols, "min_margin")[b])),
                "min_margin_iid_median": float(np.median(col(cols, "min_margin_iid_median")[b])),
                "lam_sq_median": float(np.median(col(cols, "lam_sq")[b])),
                "rate_min_over_rate_law_median": float(np.median(col(cols, "rate_ratio_law")[b])),
                "rate_min_over_rate_law_min": float(np.min(col(cols, "rate_ratio_law")[b])),
                "matched_iid_rate_min_over_rate_law_median": float(np.median(col(cols, "rate_law_ratio_iid_median")[b])),
                "rate_min_median": float(np.median(col(cols, "rate_min")[b])),
                "rate_law_median": float(np.median(col(cols, "rate_law")[b])),
                "frac_hstar_minus_f_median": float(np.median(col(cols, "frac_hstar_minus_f")[b])),
                "frac_models_global_max_wrong_is_minus_f": float(np.mean([bool(v) for v, bb in zip(cols["gmax_is_minus_f"], b) if bb])),
                "out_collision_times_q_median": float(np.median(col(cols, "out_collision")[b] * np.array(cols["q"])[b])),
            }
        allc_ = np.array(cols["all_correctable"], dtype=bool)
        mc = m & allc_
        c["exponent_fully_correctable_models"] = {
            "definition": "rate_min = worst-input exponent I_min = min_x -ln(1 - (sqrt T_x(0) - sqrt T_x(h*))^2); rate_law = the "
                          "same for the depolarizing channel at the model's eps; votes needed scale as 1/rate.  Models with "
                          "every input correctable only.",
            "n_models": int(mc.sum()), "n_runs": len(set(run[mc])),
            "rate_min_over_rate_law": summ(col(cols, "rate_ratio_law")[mc]),
            "matched_iid_rate_min_over_rate_law": summ(col(cols, "rate_law_ratio_iid_median")[mc])}
        return c
    for f in FAMILIES:
        out["cells"][f] = cell(fam == f)
        for pp in sorted(set(p[fam == f])):
            if len(set(p[fam == f])) > 1:
                out["cells"][f"{f}|p={pp}"] = cell((fam == f) & (p == pp))
    for ho in sorted(set(np.array(cols["holdout"])[fam == "add/memo"])):
        out["cells"][f"add/memo|holdout={ho}"] = cell((fam == "add/memo") & (np.array(cols["holdout"]) == ho))
    # structure of the error indicator (chi-square z of the G statistic), models with 0.05 <= eps <= 0.95
    st = {}
    for f in FAMILIES:
        m = (fam == f) & (eps >= 0.05) & (eps <= 0.95)
        zc, zl = col(cols, "gz_coord_max")[m], col(cols, "gz_label")[m]
        st[f] = {"n_models": int(m.sum()), "gz_coord_max": summ(zc), "gz_label": summ(zl),
                 "frac_gz_coord_max_gt_3": float((zc > 3).mean()), "frac_gz_label_gt_3": float((zl > 3).mean())}
    out["indicator_structure_eps_0p05_to_0p95"] = {
        "definition": "z = (G - dof)/sqrt(2 dof), G = 2 N MI(error indicator; feature) in nats, dof = levels - 1; "
                      "gz_coord_max = max over the input coordinates, gz_label = feature is the true label f(x). "
                      "Under independence z is approximately standard normal (the max over n coordinates slightly more).",
        "cells": st}
    return out


# ----------------------------------------------------------------------------------------------
# A3
# ----------------------------------------------------------------------------------------------
def first_failure(shape, q, seed):
    """Same procedure as theory_checks.section_c3_finite: nested i.i.d. fields e_eps(x) = V(x) 1[U(x) < eps],
    exact all-input check, three grid levels (0.04 from 0.20, 0.008, 0.002).  Returns the realised error rate of
    the last passing grid point."""
    nG = int(np.prod(shape))
    rng = np.random.default_rng(seed)
    U = rng.random(nG)
    V = rng.integers(1, q, nG)

    def ok(eps_list):
        res = []
        for s in range(0, len(eps_list), 8):
            E = np.where(U[None, :] < np.asarray(eps_list[s:s + 8])[:, None], V[None, :], 0)
            N = onehot_counts(E.reshape((len(E),) + tuple(shape)), q)
            res.extend(np.all(N[:, 1:, 0] > N[:, 1:, 1:].max(2), axis=1).tolist())
        return res
    c1 = None
    grid = [round(0.20 + 0.04 * i, 6) for i in range(0, 21)]
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


def section_a3(cols, log):
    fam = np.array(cols["family"])
    p = np.array(cols["p"])
    eps = np.array(cols["eps"])
    run = np.array(cols["run_id"])
    allc = np.array(cols["all_correctable"], dtype=bool)
    fracc = np.array(cols["frac_correctable"], dtype=float)
    tc = json.load(open(os.path.join(core.RESULTS_DIR, "theory_checks.json")))
    iid_ref = {}
    for row in tc["c3_finite_size"]["rows"]:
        if row["p"] in (23, 31, 47):
            iid_ref[f"add/grok|p={row['p']}"] = {
                "G_size": row["G_size"], "q": row["q"], "source": "results/theory_checks.json c3_finite_size.rows",
                "eps_last_ok": {k: row["eps_last_ok_realised"][k] for k in ("median", "min", "max", "q25", "q75", "n")}}
    # own simulations: replication of p = 23 with the seeds of theory_checks, then lin and memo groups
    rep = [first_failure((23, 23), 23, 7000 + 100 * 23 + s) for s in range(FS_FIELDS)]
    replication = {"p": 23, "seeds": "7000 + 100*23 + s, s < 24 (those of theory_checks)", "eps_last_ok": summ(rep),
                   "theory_checks_median": iid_ref["add/grok|p=23"]["eps_last_ok"]["median"],
                   "identical_median": bool(abs(np.median(rep) - iid_ref["add/grok|p=23"]["eps_last_ok"]["median"]) < 1e-12)}
    for key, shape, q, sb in (("lin|p=7", (7, 7, 7, 7), 7, 0), ("add/memo|p=53", (53, 53), 53, 1)):
        seeds = [SEED_FS + 100 * sb + s for s in range(FS_FIELDS)]
        vals = [first_failure(shape, q, sd) for sd in seeds]
        nG = int(np.prod(shape))
        iid_ref[key] = {"G_size": nG, "q": q, "source": "simulated here (same grid procedure as theory_checks)",
                        "seeds": seeds, "eps_last_ok": summ(vals), "per_field": vals,
                        "heuristic_eps": float((1 - math.sqrt(2 * math.sqrt(math.log(nG * q) / (nG * q)))) * (1 - 1 / q))}
        log(f"  finite-size i.i.d. {key}: median {np.median(vals):.4f}")
    out = {"definition": "an input x is correctable iff T_x(0) > max_{h != 0} T_x(h) (exact integer comparison); "
                         "frac_correctable is over ALL inputs of G (x = 0 is always correctable).  Per training run: "
                         "eps_all = largest eps among its snapshots at which every input is correctable, "
                         "eps_some = smallest eps among its snapshots at which some input is not.  Snapshots are "
                         "discrete, so eps_all is a lower bound on the run's last fully-correctable error rate.",
           "iid_finite_size_reference": iid_ref, "iid_replication_check": replication,
           "runs": {}, "cells": {}, "bands": {}}
    for rr in sorted(set(run)):
        m = run == rr
        f0, p0 = fam[m][0], int(p[m][0])
        ea = float(eps[m & allc].max()) if (m & allc).any() else None
        es = float(eps[m & ~allc].min()) if (m & ~allc).any() else None
        ids = np.array(cols["id"])
        out["runs"][rr] = {"family": f0, "p": p0, "n_snapshots": int(m.sum()),
                           "train_frac": float(np.array(cols["train_frac"])[m][0]),
                           "init_seed": int(np.array(cols["init_seed"])[m][0]),
                           "eps_all": ea, "eps_some": es,
                           "eps_all_id": (ids[m & allc][int(eps[m & allc].argmax())] if ea is not None else None),
                           "eps_some_id": (ids[m & ~allc][int(eps[m & ~allc].argmin())] if es is not None else None),
                           "overlap": (ea is not None and es is not None and es < ea),
                           "n_snapshots_strictly_between": (int((m & (eps > min(ea, es)) & (eps < max(ea, es))).sum())
                                                            if ea is not None and es is not None else None)}
    for key in sorted(set(f"{a}|p={b}" for a, b in zip(fam, p))):
        f0, p0 = key.split("|p=")
        p0 = int(p0)
        m = (fam == f0) & (p == p0)
        runs = [v for v in out["runs"].values() if v["family"] == f0 and v["p"] == p0]
        ud = (1 - 1 / p0) / 2
        iid_med = iid_ref[key]["eps_last_ok"]["median"]
        ea = [v["eps_all"] for v in runs if v["eps_all"] is not None]
        es = [v["eps_some"] for v in runs if v["eps_some"] is not None]
        pos = [(v - 1 / 3) / (iid_med - 1 / 3) for v in ea]
        c = {"n_models": int(m.sum()), "n_runs": len(runs),
             "worst_case_radius": 1 / 3, "unique_decoding_radius": ud, "iid_finite_size_median": iid_med,
             "eps_all": summ(ea), "eps_some": summ(es),
             "n_runs_with_eps_all": len(ea), "n_runs_with_eps_some": len(es),
             "n_runs_overlap_eps_some_lt_eps_all": int(sum(v["overlap"] for v in runs)),
             "n_runs_eps_all_above_worst_case": int(sum(v > 1 / 3 for v in ea)),
             "n_runs_eps_all_above_unique_decoding": int(sum(v > ud for v in ea)),
             "n_runs_eps_all_above_iid_median": int(sum(v > iid_med for v in ea)),
             "n_runs_eps_some_below_unique_decoding": int(sum(v < ud for v in es)),
             "n_runs_eps_some_below_iid_median": int(sum(v < iid_med for v in es)),
             "position_eps_all_between_worst_case_0_and_iid_1": summ(pos),
             "position_eps_some_between_worst_case_0_and_iid_1": summ([(v - 1 / 3) / (iid_med - 1 / 3) for v in es]),
             "iid_min_over_fields": iid_ref[key]["eps_last_ok"]["min"],
             "n_models_fully_correctable_with_eps_ge_iid_min": int((m & allc & (eps >= iid_ref[key]["eps_last_ok"]["min"])).sum()),
             "iid_median_minus_eps_all": summ([iid_med - v for v in ea]),
             "min_eps_with_uncorrectable_input": (float(eps[m & ~allc].min()) if (m & ~allc).any() else None),
             "max_eps_all_correctable": (float(eps[m & allc].max()) if (m & allc).any() else None),
             "n_models_eps_lt_third_with_uncorrectable_input": int((m & (eps < 1 / 3) & ~allc).sum())}
        if f0 == "add/memo":
            c["note"] = "add/memo runs have ONE snapshot each, so eps_all / eps_some are single-model values"
        out["cells"][key] = c
        edges = [("0<eps<1/3", 0.0, 1 / 3), ("1/3<=eps<ud", 1 / 3, ud), ("ud<=eps<iid", ud, iid_med), ("eps>=iid", iid_med, 1.01)]
        bd = {}
        for nm, lo, hi in edges:
            b = m & (eps > 0) & (eps >= lo) & (eps < hi)
            bd[nm] = {"n_models": int(b.sum()), "n_runs": len(set(run[b])),
                      "n_all_correctable": int((b & allc).sum()),
                      "n_some_uncorrectable": int((b & ~allc).sum()),
                      "median_frac_correctable": (float(np.median(fracc[b])) if b.any() else None),
                      "min_frac_correctable": (float(fracc[b].min()) if b.any() else None)}
        out["bands"][key] = bd
    # add/memo by hold-out configuration
    memo = {}
    ho = np.array(cols["holdout"])
    tf = np.array(cols["train_frac"])
    for h0, t0 in sorted(set(zip(ho[fam == "add/memo"], tf[fam == "add/memo"]))):
        m = (fam == "add/memo") & (ho == h0) & (tf == t0)
        memo[f"{h0}|train_frac={t0}"] = {"n_models": int(m.sum()), "eps_min": float(eps[m].min()), "eps_max": float(eps[m].max()),
                                         "n_all_correctable": int((m & allc).sum()),
                                         "min_frac_correctable": float(fracc[m].min()),
                                         "min_margin_min": float(np.nanmin(col(cols, "min_margin")[m])),
                                         "lam_sq_median": float(np.nanmedian(col(cols, "lam_sq")[m])),
                                         "min_margin_median": float(np.nanmedian(col(cols, "min_margin")[m])),
                                         "min_margin_iid_median": float(np.nanmedian(col(cols, "min_margin_iid_median")[m])),
                                         "overdisp_over_matched_iid": summ(col(cols, "overdisp")[m] / col(cols, "overdisp_iid_median")[m]),
                                         "coh_ratio_iid": summ(col(cols, "coh_ratio_iid")[m]),
                                         "coh_ratio_shuf": summ(col(cols, "coh_ratio_shuf")[m]),
                                         "gz_label": summ(col(cols, "gz_label")[m]),
                                         "out_collision_times_q": summ(col(cols, "out_collision")[m] * 53.0),
                                         "rate_min_over_rate_law": summ(col(cols, "rate_ratio_law")[m]),
                                         "ids_not_all_correctable": [i for i, mm in zip(cols["id"], m & ~allc) if mm]}
    out["add_memo_by_config"] = memo
    return out


# ----------------------------------------------------------------------------------------------
# A4
# ----------------------------------------------------------------------------------------------
def exact_fail_all(N, k):
    """Exact delta_k(x) for every input from integer counts N (|G|, q); rows that agree up to a permutation of the
    wrong values are evaluated once (delta depends only on T_x(0) and the multiset of wrong masses)."""
    nG = int(N[0].sum())
    key = np.concatenate([N[:, :1], -np.sort(-N[:, 1:], axis=1)], axis=1)
    uniq, inv = np.unique(key, axis=0, return_inverse=True)
    keep = np.concatenate([[True], uniq[:, 1:].any(0)])
    d = core.plurality_fail_exact(uniq[:, keep] / nG, k)
    return d[np.asarray(inv).ravel()], len(uniq)


def pick_representatives(cols):
    fam = np.array(cols["family"])
    p = np.array(cols["p"])
    eps = np.array(cols["eps"])
    seed0 = (np.array(cols["init_seed"]) == 0) & (np.array(cols["split_seed"]) == 0)
    ids = np.array(cols["id"])
    tf = np.array(cols["train_frac"])
    step = np.array(cols["step"])

    def closest(mask, target):
        best = None
        for use_seed0 in (True, False):
            m = mask & (seed0 if use_seed0 else True)
            idx = np.flatnonzero(m)
            if len(idx) == 0:
                continue
            order = sorted(idx, key=lambda i: (abs(eps[i] - target), tf[i], step[i]))
            i = order[0]
            if use_seed0 and abs(eps[i] - target) > SEED0_TOL:
                continue
            best = (int(i), use_seed0)
            break
        return best
    reps = []
    for t in EPS_TARGETS_GROK47:
        i, s0 = closest((fam == "add/grok") & (p == 47), t)
        reps.append({"label": f"add/grok p=47, eps~{t}", "target_eps": t, "id": ids[i], "seed0": s0})
    i, s0 = closest(fam == "lin", 0.3)
    reps.append({"label": "lin, eps~0.3", "target_eps": 0.3, "id": ids[i], "seed0": s0})
    m = (fam == "add/memo") & (np.array(cols["holdout"]) == "random") & (np.abs(tf - 0.7) < 1e-9) & seed0
    assert m.sum() == 1
    reps.append({"label": "add/memo p=53, random hold-out 30%", "target_eps": 0.3, "id": ids[np.flatnonzero(m)[0]], "seed0": True})
    rule = ("add/grok p=47: for each target eps in (0.1, 0.3, 0.5, 0.65) the snapshot with the smallest |eps - target| "
            "among the runs with split_seed = init_seed = 0 (ties: lower train_frac, then earlier step); if no seed-0 "
            f"snapshot lies within {SEED0_TOL} of the target, the closest snapshot over all seeds.  lin: the same rule "
            "with target 0.3.  add/memo: the random-hold-out model with train_frac 0.7 (eps = 0.30), split_seed 0, init_seed 0.")
    return reps, rule


def section_a4(cols, log):
    reps, rule = pick_representatives(cols)
    out = {"selection_rule": rule, "ks": list(KS),
           "definition": "exact_mean = mean over ALL inputs of G of the exact failure probability of the plurality of "
                         "k votes (tie = failure) computed from the model's exact twirled channel; exact_worst = max "
                         "over inputs.  pred_* = the same routine applied to the depolarizing channel at the model's "
                         "eps (identical for every x != 0; the mean includes x = 0, which never fails).  chernoff_* = "
                         "core.chernoff_union_bound.  Values below 1e-10 are at the accuracy floor of the exact routine "
                         "(absolute accuracy ~1e-12) and are flagged; where the Chernoff bound of the worst input is "
                         "already below 1e-11 the exact routine is skipped and only the bound is given.  real_* = "
                         f"actual votes with core.sc_fail ({REAL_REPS} repetitions for every input; {REAL_WORST} for the "
                         "worst input); z = (empirical - exact)/SE.",
           "models": []}
    zs = []
    for ri_, rep in enumerate(reps):
        t0 = time.time()
        rec = core.get_record(rep["id"])
        q = rec["q"]
        E = core.error_table(rep["id"])
        M = core.load_table(rep["id"])
        f = core.model_true_table(rep["id"])
        nG = E.size
        eps = float((E != 0).mean())
        N = core.twirled_counts(E, q)
        T = N / nG
        cs = core.channel_stats(T[1:])
        dep = core.depolarizing_channel(eps, q, 2)
        mo = dict(rep)
        mo.update({"family": rec["family"], "p": rec["p"], "q": q, "G_size": nG, "run_id": rec["run_id"], "step": rec["step"],
                   "train_frac": rec["train_frac"], "init_seed": rec["init_seed"], "eps": eps,
                   "abs_eps_minus_target": abs(eps - rep["target_eps"]),
                   "raw_accuracy": 1 - eps, "lam": float(core.lam(eps, q)),
                   "all_correctable": bool(cs["strict_mode"].all()),
                   "n_uncorrectable": int((~cs["strict_mode"]).sum()),
                   "t0_mean": float(cs["t0"].mean()), "t0_min": float(cs["t0"].min()),
                   "min_margin": float(cs["margin"].min()), "lam_sq": float(core.lam(eps, q)) ** 2,
                   "min_rate": float(cs["rate"].min()), "rate_from_eps_alone": float(core.rate_law(eps, q, 2)),
                   "rows": []})
        rng = np.random.default_rng([SEED_VOTE, ri_])
        xs_all = np.arange(nG)
        for k in KS:
            ch = core.chernoff_union_bound(T, k)
            row = {"k": k, "chernoff_mean": float(ch.mean()), "chernoff_worst": float(ch.max()),
                   "pred_worst": float(core.plurality_fail_exact(dep[None], k)[0]),
                   "pred_chernoff": float(core.chernoff_union_bound(dep[None], k)[0])}
            row["pred_mean"] = row["pred_worst"] * (nG - 1) / nG
            row["pred_reliable"] = bool(row["pred_worst"] >= ACC_FLOOR)
            if ch.max() < 1e-11:
                row.update({"exact_mean": None, "exact_worst": None, "exact_skipped": True,
                            "note": "exact value below the accuracy floor; bounded by chernoff_worst"})
                d = None
            else:
                d, nu = exact_fail_all(N, k)
                iw = int(d.argmax())
                row.update({"exact_mean": float(d.mean()), "exact_worst": float(d.max()), "exact_skipped": False,
                            "worst_input_flat": iw, "worst_input_coords": core.coords(E.shape)[iw].tolist(),
                            "n_distinct_channel_rows": nu,
                            "exact_mean_reliable": bool(d.mean() >= ACC_FLOOR),
                            "exact_worst_reliable": bool(d.max() >= ACC_FLOOR),
                            "bound_holds_everywhere": bool((ch >= d - 1e-12).all()),
                            "frac_inputs_fail_gt_raw_eps": float((d > eps).mean()),
                            "ratio_exact_worst_over_pred": (float(d.max() / row["pred_worst"]) if row["pred_worst"] > ACC_FLOOR and d.max() > ACC_FLOOR else None)})
            if k <= K_REAL_MAX and d is not None:
                fails = 0
                for _ in range(REAL_REPS):
                    fails += int(core.sc_fail(M, f, xs_all, k, rng, q).sum())
                emp = fails / (REAL_REPS * nG)
                se = math.sqrt(float((d * (1 - d)).sum()) / REAL_REPS) / nG
                z = (emp - row["exact_mean"]) / se if se > 0 else None
                fw = int(core.sc_fail(M, f, np.full(REAL_WORST, iw), k, rng, q).sum())
                empw = fw / REAL_WORST
                dw = float(d[iw])
                sew = math.sqrt(dw * (1 - dw) / REAL_WORST)
                zw = (empw - dw) / sew if sew > 0 else None
                row.update({"real_mean": emp, "real_mean_se": se, "real_mean_z": z, "real_mean_trials": REAL_REPS * nG,
                            "real_worst": empw, "real_worst_se": sew, "real_worst_z": zw, "real_worst_trials": REAL_WORST})
                zs += [v for v in (z, zw) if v is not None]
            mo["rows"].append(row)
        # headline strings are built by the writer; give the numbers plainly
        mo["headline"] = {"raw_error": eps,
                          "note": "None = below the accuracy floor of the exact routine (1e-10); use the Chernoff bound there",
                          "worst_input_failure_by_k": {str(r["k"]): (r["exact_worst"] if not r["exact_skipped"] and r["exact_worst"] >= ACC_FLOOR else None) for r in mo["rows"]},
                          "worst_input_chernoff_by_k": {str(r["k"]): r["chernoff_worst"] for r in mo["rows"]},
                          "mean_failure_by_k": {str(r["k"]): (r["exact_mean"] if not r["exact_skipped"] and r["exact_mean"] >= ACC_FLOOR else None) for r in mo["rows"]},
                          "pred_from_eps_alone_by_k": {str(r["k"]): (r["pred_worst"] if r["pred_reliable"] else None) for r in mo["rows"]},
                          "pred_chernoff_from_eps_alone_by_k": {str(r["k"]): r["pred_chernoff"] for r in mo["rows"]},
                          "votes_for_worst_input_below_1e-6_chernoff": int(core.votes_needed(mo["min_rate"], 1e-6, q)) if mo["min_rate"] > 0 else None,
                          "votes_for_1e-6_chernoff_from_eps_alone": int(core.votes_needed(mo["rate_from_eps_alone"], 1e-6, q)),
                          "smallest_k_in_grid_mean_below_raw": next((r["k"] for r in mo["rows"] if not r["exact_skipped"] and r["exact_mean"] < eps), None),
                          "smallest_k_in_grid_worst_below_raw": next((r["k"] for r in mo["rows"] if not r["exact_skipped"] and r["exact_worst"] < eps), None)}
        out["models"].append(mo)
        log(f"  A4 {rep['id']} eps={eps:.4f} done ({time.time() - t0:.0f} s)")
    zs = np.array(zs)
    out["real_vote_crosscheck"] = {"n_z": int(len(zs)), "max_abs_z": float(np.abs(zs).max()), "mean_z": float(zs.mean()),
                                   "rms_z": float(np.sqrt((zs ** 2).mean())), "n_abs_z_gt_3": int((np.abs(zs) > 3).sum()),
                                   "n_abs_z_gt_2": int((np.abs(zs) > 2).sum())}
    return out


# ----------------------------------------------------------------------------------------------
# A5
# ----------------------------------------------------------------------------------------------
def entropy(counts):
    c = np.asarray(counts, dtype=float).ravel()
    c = c[c > 0]
    pr = c / c.sum()
    return float(-(pr * np.log(pr)).sum())


def mutual_info(a, b, na, nb):
    tab = np.zeros((na, nb))
    np.add.at(tab, (a, b), 1.0)
    return entropy(tab.sum(1)) + entropy(tab.sum(0)) - entropy(tab)


def anatomy(model_id, seed):
    rec = core.get_record(model_id)
    p, q = rec["p"], rec["q"]
    E = core.error_table(model_id)
    mask = core.load_train_mask(model_id)
    nG = E.size
    Ef = E.ravel()
    ind = (Ef != 0).astype(np.int64)
    C = core.coords(E.shape)
    a, b = C[:, 0], C[:, 1]
    feats = {"a": a, "b": b, "a+b": (a + b) % p, "a-b": (a - b) % p}
    N = core.twirled_counts(E, q)
    cs = core.channel_stats(N / nG)
    margin_counts = N[:, 0] - N[:, 1:].max(1)
    order = [i for i in np.argsort(margin_counts, kind="stable") if i != 0]
    hist = np.bincount(Ef, minlength=q)
    out = {"id": model_id, "p": p, "eps": float(ind.mean()), "step": rec["step"], "run_id": rec["run_id"],
           "train_frac": rec["train_frac"], "train_acc": rec["train_acc"], "heldout_acc": rec["heldout_acc"],
           "n_errors": int(ind.sum()), "n_errors_on_training_inputs": int((ind.astype(bool) & mask.ravel()).sum()),
           "error_rate_on_training_inputs": float(ind[mask.ravel()].mean()),
           "error_rate_on_heldout_inputs": float(ind[~mask.ravel()].mean()),
           "n_uncorrectable_inputs": int((margin_counts[1:] <= 0).sum()),
           "lam_sq": float(core.lam(ind.mean(), q)) ** 2,
           "t0_mean_x_ne_0": float(cs["t0"][1:].mean()),
           "wrong_value_top3": [{"value": int(v), "share_of_errors": float(hist[v] / ind.sum())}
                                for v in (1 + np.argsort(-hist[1:], kind="stable")[:3])],
           "n_eff_wrong_values": float(ind.sum() ** 2 / (hist[1:].astype(float) ** 2).sum()), "q_minus_1": q - 1}
    # outputs of the model: are the wrong answers concentrated on a few classes?
    ff = core.model_true_table(model_id).ravel().astype(np.int64) % q
    Mf = (Ef + ff) % q
    mu_all = np.bincount(Mf, minlength=q) / nG
    mu_err = np.bincount(Mf[ind == 1], minlength=q) / max(1, int(ind.sum()))
    h0 = (-ff) % q
    valid = (np.arange(nG) != 0) & (ff != 0)
    tz = N[np.arange(nG), h0] / nG
    vu = valid & (margin_counts <= 0)
    out["outputs"] = {
        "definition": "mu = histogram of the model's predicted class over all inputs, mu_err = over its wrong inputs only; "
                      "collision = sum of squares (1/q if balanced).  The 'zero vote' is M(x+r) = M(r), offset h = -f(x); its "
                      "mass averaged over x != 0 equals (|G| sum mu^2 - 1)/(|G| - 1) exactly.",
        "out_collision": float((mu_all ** 2).sum()), "out_collision_times_q": float(q * (mu_all ** 2).sum()),
        "err_out_collision": float((mu_err ** 2).sum()), "err_out_collision_times_q": float(q * (mu_err ** 2).sum()),
        "top3_predicted_classes_among_errors": [{"class": int(c), "share": float(mu_err[c])} for c in np.argsort(-mu_err, kind="stable")[:3]],
        "n_classes_covering_half_of_wrong_outputs": int(1 + np.searchsorted(np.cumsum(np.sort(mu_err)[::-1]), 0.5)),
        "mean_zero_vote_mass_x_with_f_ne_0": float(tz[valid].mean()),
        "mean_truth_mass_x_with_f_ne_0": float((N[valid, 0] / nG).mean()),
        "predicted_zero_vote_mass_eps2_times_err_collision": float(ind.mean() ** 2 * (mu_err ** 2).sum()),
        "frac_inputs_strongest_wrong_value_is_minus_f": float((cs["hstar"][valid] == h0[valid]).mean()),
        "chance_level": 1.0 / (q - 1),
        "frac_uncorrectable_inputs_beaten_by_minus_f": (float((N[vu, h0[vu]] >= N[vu, 0]).mean()) if vu.any() else None),
        "n_uncorrectable_inputs_with_f_ne_0": int(vu.sum()),
        "n_inputs_with_f_ne_0": int(valid.sum())}
    # smallest-margin inputs (x and -x share a margin; list one of each pair)
    seen, lst = set(), []
    for i in order:
        neg = int(core.flat_index(-C[i], E.shape))
        if neg in seen:
            continue
        seen.add(int(i))
        hs = int(cs["hstar"][i])
        both = one = 0
        Ex = core.translate(E, int(i)).ravel()                     # e(x + r)
        hit = ((Ex - Ef) % q) == hs
        both = int((hit & (Ex != 0) & (Ef != 0)).sum())
        one = int((hit & ((Ex != 0) ^ (Ef != 0))).sum())
        lst.append({"x": C[i].tolist(), "a+b": int((C[i, 0] + C[i, 1]) % p), "N0": int(N[i, 0]), "hstar": hs,
                    "N_hstar": int(N[i, hs]), "margin_counts": int(margin_counts[i]), "margin": float(margin_counts[i] / nG),
                    "T0": float(N[i, 0] / nG), "T_hstar": float(N[i, hs] / nG),
                    "hstar_votes_from_two_errors": both, "hstar_votes_from_one_error": one,
                    "hstar_equals_minus_f": bool(hs == (-(C[i, 0] + C[i, 1])) % p)})
        if len(lst) == 8:
            break
    out["smallest_margin_inputs"] = lst
    # is h*(x) linear in x over the 40 smallest-margin inputs?
    top = order[:40]
    hs_top = cs["hstar"][top]
    al, be = np.meshgrid(np.arange(p), np.arange(p), indexing="ij")
    match = ((al[..., None] * C[top, 0] + be[..., None] * C[top, 1]) % p == hs_top).sum(-1)
    ia, ib = np.unravel_index(match.argmax(), match.shape)
    out["hstar_linear_fit_top40"] = {"best_alpha": int(ia), "best_beta": int(ib), "n_matching": int(match.max()), "n_inputs": len(top),
                                     "note": "number of the 40 smallest-margin inputs x = (a, b) whose strongest wrong value "
                                             "equals alpha a + beta b mod p, maximised over all p^2 linear forms"}
    # margins by class of x
    cls = {"a=0": (a == 0) & (b != 0), "b=0": (b == 0) & (a != 0), "a+b=0": ((a + b) % p == 0) & (a != 0),
           "a=b": (a == b) & (a != 0), "generic": (a != 0) & (b != 0) & ((a + b) % p != 0) & (a != b)}
    out["by_input_class"] = {k: {"n": int(m.sum()), "mean_T0": float(cs["t0"][m].mean()), "mean_maxwrong": float(cs["tw"][m].mean()),
                                 "min_margin": float(cs["margin"][m].min()), "mean_margin": float(cs["margin"][m].mean())}
                             for k, m in cls.items()}
    # dependence of the error indicator / value on a, b, a+b, a-b; permutation nulls
    rng = np.random.default_rng(seed)
    perms = [rng.permutation(nG) for _ in range(N_PERM)]
    Hi, Hv = entropy(np.bincount(ind)), entropy(hist)
    dep = {}
    for nm, lev in feats.items():
        mi_i = mutual_info(ind, lev, 2, p) / Hi
        mi_v = mutual_info(Ef, lev, q, p) / Hv
        null_i = np.array([mutual_info(ind[pm], lev, 2, p) / Hi for pm in perms])
        null_v = np.array([mutual_info(Ef[pm], lev, q, p) / Hv for pm in perms])
        rate = np.bincount(lev, weights=ind, minlength=p) / np.bincount(lev, minlength=p)
        dep[nm] = {"nmi_indicator": float(mi_i), "nmi_indicator_null_mean": float(null_i.mean()), "nmi_indicator_null_max": float(null_i.max()),
                   "nmi_indicator_z": float((mi_i - null_i.mean()) / null_i.std(ddof=1)),
                   "nmi_value": float(mi_v), "nmi_value_null_mean": float(null_v.mean()), "nmi_value_null_max": float(null_v.max()),
                   "nmi_value_z": float((mi_v - null_v.mean()) / null_v.std(ddof=1)),
                   "error_rate_by_level_min": float(rate.min()), "error_rate_by_level_max": float(rate.max()),
                   "error_rate_by_level_sd": float(rate.std(ddof=1)),
                   "binomial_sd_of_level_rate": float(math.sqrt(ind.mean() * (1 - ind.mean()) / (nG / p)))}
    out["dependence"] = dep
    out["dependence_definition"] = ("nmi_indicator = MI(1[e != 0]; feature)/H(1[e != 0]); nmi_value = MI(e; feature)/H(e) with e the "
                                    f"error value including 0; nulls from {N_PERM} random permutations of the positions; z = (observed - "
                                    "null mean)/null sd.  error_rate_by_level = error rate within each of the p level sets of the feature.")
    # additive (row + column) model for the error indicator: fraction of indicator variance explained
    I2 = ind.reshape(E.shape).astype(float)
    mu = I2.mean()
    ra, cb = I2.mean(1) - mu, I2.mean(0) - mu
    out["indicator_variance_explained"] = {"by_a": float((ra ** 2).mean() / (mu * (1 - mu))), "by_b": float((cb ** 2).mean() / (mu * (1 - mu))),
                                           "expected_by_chance_each": float((p - 1) / (nG - 1))}
    return out


def section_a5(cols):
    fam = np.array(cols["family"])
    eps = np.array(cols["eps"])
    allc = np.array(cols["all_correctable"], dtype=bool)
    ids = np.array(cols["id"])
    g = fam == "add/grok"
    hi = ids[g & allc][int(eps[g & allc].argmax())]
    lo = ids[g & ~allc][int(eps[g & ~allc].argmin())]
    # the zero-vote mechanism over ALL models with eps > 0
    has = eps > 0
    fracc = np.array(cols["frac_correctable"], dtype=float)
    gmax = np.array([bool(v) if v is not None else False for v in cols["gmax_is_minus_f"]])
    fub = col(cols, "frac_unc_beaten_by_minus_f")
    fh = col(cols, "frac_hstar_minus_f")
    S_out, S_err = col(cols, "out_collision"), col(cols, "err_collision")
    qq = np.array(cols["q"], dtype=float)
    run = np.array(cols["run_id"])
    mech = {"definition": "zero vote = M(x+r) = M(r), i.e. vote offset h = -f(x) (the corrector would output 0).  "
                          "gmax_is_minus_f: the largest wrong-vote mass of the model sits at h = -f(x).  frac_hstar_minus_f: "
                          "fraction of inputs (x != 0, f(x) != 0) whose strongest wrong value is -f(x) (chance 1/(q-1) for "
                          "incoherent errors).  frac_unc_beaten_by_minus_f: among uncorrectable inputs with f(x) != 0, the "
                          "fraction where the zero vote ties or beats the truth.  Two-histogram criterion: predict 'mostly "
                          "correctable' iff err_collision (sum_v pi_v^2, the mean truth mass) exceeds out_collision "
                          "(sum_c mu_c^2, the mean zero-vote mass); both are histograms, no channel needed.",
            "cells": {}}
    for f in FAMILIES:
        m = (fam == f) & has
        mu_ = m & ~allc
        with np.errstate(invalid="ignore"):
            pred_ok = S_err > S_out
        mostly = fracc > 0.5
        cell = {"n_models": int(m.sum()), "n_runs": len(set(run[m])), "chance_level_1_over_qm1": summ(1.0 / (qq[m] - 1)),
                "frac_models_gmax_is_minus_f": float(gmax[m].mean()),
                "frac_models_gmax_is_minus_f_eps_ge_0p4": float(gmax[m & (eps >= 0.4)].mean()) if (m & (eps >= 0.4)).any() else None,
                "n_models_eps_ge_0p4": int((m & (eps >= 0.4)).sum()),
                "frac_hstar_minus_f": summ(fh[m]),
                "frac_hstar_minus_f_eps_ge_0p4": summ(fh[m & (eps >= 0.4)]),
                "n_models_with_uncorrectable_input": int(mu_.sum()),
                "n_runs_with_uncorrectable_input": len(set(run[mu_])),
                "frac_unc_beaten_by_minus_f": summ(fub[mu_]),
                "n_models_all_uncorrectable_inputs_beaten_by_minus_f": int((fub[mu_] == 1.0).sum()),
                "n_models_no_uncorrectable_input_beaten_by_minus_f": int((fub[mu_] == 0.0).sum()),
                "two_histogram_criterion": {
                    "pred_ok_and_mostly_correctable": int((m & pred_ok & mostly).sum()),
                    "pred_ok_and_mostly_uncorrectable": int((m & pred_ok & ~mostly).sum()),
                    "pred_fail_and_mostly_correctable": int((m & ~pred_ok & mostly).sum()),
                    "pred_fail_and_mostly_uncorrectable": int((m & ~pred_ok & ~mostly).sum()),
                    "pred_ok_and_all_correctable": int((m & pred_ok & allc).sum()),
                    "pred_ok_and_some_uncorrectable": int((m & pred_ok & ~allc).sum()),
                    "pred_fail_and_all_correctable": int((m & ~pred_ok & allc).sum()),
                    "accuracy_for_mostly_correctable": float(((pred_ok == mostly)[m]).mean())},
                "out_collision_times_q": {"all_correctable": summ((S_out * qq)[m & allc]), "some_uncorrectable": summ((S_out * qq)[mu_])},
                "shift_inv_identity_max_abs_resid": float(np.nanmax(np.abs(col(cols, "shift_inv_identity_resid")[m])))}
        if m.sum() >= 5:
            sr = sstats.spearmanr((S_out * qq)[m], col(cols, "coh_ratio_iid")[m])
            cell["spearman_coh_ratio_iid_vs_out_collision"] = float(sr.statistic)
        mech["cells"][f] = cell
    return {"zero_vote_mechanism_all_models": mech,
            "selection_rule": "highest_eps_fully_correctable = the add/grok model with the largest eps among those whose every input is "
                              "correctable; lowest_eps_with_uncorrectable = the add/grok model with the smallest eps among those with "
                              "at least one uncorrectable input",
            "highest_eps_fully_correctable": anatomy(hi, SEED_PERM),
            "lowest_eps_with_uncorrectable": anatomy(lo, SEED_PERM + 1)}


# ----------------------------------------------------------------------------------------------
# figures
# ----------------------------------------------------------------------------------------------
def make_figures(res):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import paperstyle as ps
    ps.apply()
    cols = res["per_model"]
    fam = np.array(cols["family"])
    p = np.array(cols["p"])
    eps = np.array(cols["eps"], dtype=float)
    has = eps > 0
    t0 = col(cols, "t0_mean")
    dev = col(cols, "dev_law")
    paths = []

    # ---- fig_law -------------------------------------------------------------------------
    fig, axs = plt.subplots(1, 2, figsize=(7.2, 3.3), constrained_layout=True)
    ax = axs[0]
    e = np.linspace(0, 1, 400)
    ax.plot(e, (1 - e) ** 2, color=ps.MUTED, lw=1.0, ls=(0, (4, 3)), label=r"naive $(1-\varepsilon)^2$", zorder=2)
    ax.plot(e[e <= 1 - 1 / 31 + 0.035], core.pc_law(e[e <= 1 - 1 / 31 + 0.035], 31, 2), color=ps.INK, lw=1.4, label="law (no free parameter)", zorder=4)
    ax.plot(e[e <= 0.9], core.pc_law(e[e <= 0.9], 7, 2), color=ps.INK, lw=1.4, zorder=4)
    for f, c, lab in (("add/grok", ps.BLUE, "addition nets ($q$ = 23, 31, 47)"), ("lin", ps.ORANGE, "linear-map nets ($q$ = 7)")):
        m = (fam == f) & has
        ax.scatter(eps[m], t0[m], s=26, color=c, edgecolor=ps.SURFACE, linewidth=0.5, alpha=0.85, label=lab, zorder=3)
    ax.annotate("law, $q$ = 7", xy=(0.80, core.pc_law(0.80, 7, 2)), xytext=(0.80, 0.33), fontsize=8.5, color=ps.INK,
                ha="center", arrowprops=dict(arrowstyle="-", color=ps.MUTED, lw=0.7))
    ax.annotate("law, $q$ = 31", xy=(0.60, core.pc_law(0.60, 31, 2)), xytext=(0.36, 0.06), fontsize=8.5, color=ps.INK,
                ha="center", arrowprops=dict(arrowstyle="-", color=ps.MUTED, lw=0.7))
    ax.set_xlabel(r"error rate $\varepsilon$ of the trained network")
    ax.set_ylabel("mean probability a vote is correct")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title("a  One vote: measured vs law")
    ax.legend(loc="upper right", fontsize=8, handlelength=1.6)
    ax = axs[1]
    ax.axhline(0, color=ps.INK2, lw=0.8, zorder=2)
    for f, c, lab in (("add/grok", ps.BLUE, "addition nets"), ("lin", ps.ORANGE, "linear-map nets")):
        m = (fam == f) & has
        ax.scatter(eps[m], dev[m], s=26, color=c, edgecolor=ps.SURFACE, linewidth=0.5, alpha=0.85, label=lab, zorder=3)
    ax.set_xlabel(r"error rate $\varepsilon$")
    ax.set_ylabel("measured minus law")
    ax.set_xlim(0, 1)
    ax.set_title("b  Residual")
    ax.legend(loc="upper left", fontsize=8)
    path = os.path.join(core.FIG_DIR, "fig_law")
    ps.save(fig, path)
    plt.close(fig)
    paths.append(path)

    # ---- fig_correctable -----------------------------------------------------------------
    from matplotlib.lines import Line2D
    a3 = res["A3"]
    fig, axs = plt.subplots(1, 2, figsize=(7.2, 3.4), constrained_layout=True, gridspec_kw={"width_ratios": [1.45, 1]})
    ax = axs[0]
    fracc = np.array(cols["frac_correctable"], dtype=float)
    pcs = ((23, ps.BLUE), (31, ps.ORANGE), (47, ps.AQUA))
    ax.axvline(1 / 3, color=ps.MUTED, lw=1.0, ls=(0, (4, 3)), zorder=2)
    for pp, c in pcs:
        ref = a3["cells"][f"add/grok|p={pp}"]["iid_finite_size_median"]
        ax.axvline(ref, color=c, lw=1.0, zorder=2)
    hs = []
    for pp, c in pcs:
        m = (fam == "add/grok") & (p == pp)
        hs.append(ax.scatter(eps[m], fracc[m], s=26, color=c, edgecolor=ps.SURFACE, linewidth=0.5, alpha=0.85,
                             label=f"addition nets, $p$ = {pp}", zorder=3))
    hs += [Line2D([0], [0], color=ps.MUTED, lw=1.0, ls=(0, (4, 3)), label="worst-case guarantee, 1/3"),
           Line2D([0], [0], color=ps.INK2, lw=1.0, label="incoherent errors break\n(line colour = $p$)")]
    ax.set_xlabel(r"error rate $\varepsilon$")
    ax.set_ylabel("fraction of inputs correctable")
    ax.set_xlim(0, 1)
    ax.set_ylim(-0.03, 1.05)
    ax.set_title("a  Correctable inputs, every snapshot")
    ax.legend(handles=hs, loc="lower left", fontsize=8, frameon=True, facecolor=ps.SURFACE, edgecolor="none", framealpha=1.0,
              borderaxespad=0.6)
    ax = axs[1]
    ax.axhline(1 / 3, color=ps.MUTED, lw=1.0, ls=(0, (4, 3)), zorder=2)
    for j, (pp, c) in enumerate(pcs):
        runs = sorted(k for k, v in a3["runs"].items() if v["family"] == "add/grok" and v["p"] == pp)
        ys = np.array([a3["runs"][k]["eps_all"] for k in runs], dtype=float)
        xs = j + np.linspace(-0.22, 0.22, len(ys))[np.argsort(np.argsort(ys))]
        ax.scatter(xs, ys, s=34, color=c, edgecolor=ps.SURFACE, linewidth=0.8, zorder=4)
        ref = a3["cells"][f"add/grok|p={pp}"]["iid_finite_size_median"]
        ud = a3["cells"][f"add/grok|p={pp}"]["unique_decoding_radius"]
        ax.plot([j - 0.36, j + 0.36], [ref, ref], color=c, lw=1.0, zorder=3)
        ax.plot([j - 0.36, j + 0.36], [ud, ud], color=ps.MUTED, lw=1.2, ls=(0, (1, 2)), zorder=3)
        med = float(np.median(ys))
        ax.plot([j - 0.32, j + 0.32], [med, med], color=ps.INK, lw=2.0, zorder=5)
    hb = [Line2D([0], [0], color=ps.INK2, lw=1.0, label="incoherent errors (colour = $p$)"),
          Line2D([0], [0], color=ps.INK, lw=2.0, label="median of the 12 runs"),
          Line2D([0], [0], color=ps.MUTED, lw=1.2, ls=(0, (1, 2)), label="unique-decoding radius"),
          Line2D([0], [0], color=ps.MUTED, lw=1.0, ls=(0, (4, 3)), label="worst-case guarantee, 1/3")]
    ax.legend(handles=hb, loc="lower center", fontsize=8, handlelength=1.8, borderaxespad=0.3)
    ax.set_xticks([0, 1, 2])
    ax.set_xticklabels([f"$p$ = {pp}" for pp, _ in pcs])
    ax.set_xlim(-0.5, 2.5)
    ax.set_ylim(0.0, 0.9)
    ax.set_ylabel(r"largest fully correctable $\varepsilon$")
    ax.set_title("b  Per training run")
    ax.grid(axis="x", visible=False)
    path = os.path.join(core.FIG_DIR, "fig_correctable")
    ps.save(fig, path)
    plt.close(fig)
    paths.append(path)

    # ---- fig_votes -----------------------------------------------------------------------
    a4 = res["A4"]
    grok = [m for m in a4["models"] if m["family"] == "add/grok"]
    colors = [ps.BLUE, ps.ORANGE, ps.AQUA, ps.YELLOW]
    pos = {k: i + 1 for i, k in enumerate(KS)}
    fig, axs = plt.subplots(1, 2, figsize=(7.2, 3.4), constrained_layout=True, sharey=True)
    for ax, key, pkey, title in ((axs[0], "exact_mean", "pred_mean", "a  Mean over inputs"), (axs[1], "exact_worst", "pred_worst", "b  Worst input")):
        for mo, c in zip(grok, colors):
            ks = [r["k"] for r in mo["rows"] if not r["exact_skipped"] and r[key] >= ACC_FLOOR]
            ys = [r[key] for r in mo["rows"] if not r["exact_skipped"] and r[key] >= ACC_FLOOR]
            pk = [r["k"] for r in mo["rows"] if r[pkey] >= ACC_FLOOR]
            py = [r[pkey] for r in mo["rows"] if r[pkey] >= ACC_FLOOR]
            ax.plot([pos[k] for k in pk], py, color=c, lw=1.0, zorder=3)
            ax.plot([0, pos[ks[0]]], [mo["eps"], ys[0]], color=c, lw=1.0, ls=(0, (1, 2)), zorder=3)
            ax.plot([pos[k] for k in ks], ys, color=c, lw=2.0, marker="o", ms=5.5, mec=ps.SURFACE, mew=1.0, zorder=4,
                    label=rf"$\varepsilon$ = {mo['eps']:.2f}")
            ax.plot([0], [mo["eps"]], color=c, marker="s", ms=6.5, mec=ps.SURFACE, mew=1.0, ls="none", zorder=5)
        ax.set_yscale("log")
        ax.set_ylim(1e-10, 2.5)
        ax.set_xticks([0] + [pos[k] for k in KS])
        ax.set_xticklabels(["raw"] + [str(k) for k in KS])
        ax.set_xlim(-0.4, len(KS) + 0.4)
        ax.set_xlabel("number of votes $k$")
        ax.set_title(title)
    axs[0].set_ylabel("failure probability")
    from matplotlib.lines import Line2D
    h, l = axs[0].get_legend_handles_labels()
    h += [Line2D([0], [0], color=ps.INK2, lw=2.0), Line2D([0], [0], color=ps.INK2, lw=1.0),
          Line2D([0], [0], color=ps.INK2, marker="s", ms=6, mec=ps.SURFACE, ls="none")]
    l += ["exact, measured channel", r"predicted from $\varepsilon$ alone", "raw network"]
    axs[0].legend(h[:4], l[:4], loc="lower left", fontsize=8, title="raw error rate", title_fontsize=8)
    axs[1].legend(h[4:], l[4:], loc="lower left", fontsize=8)
    path = os.path.join(core.FIG_DIR, "fig_votes")
    ps.save(fig, path)
    plt.close(fig)
    paths.append(path)
    return paths


# ----------------------------------------------------------------------------------------------
def main():
    if "--figs-only" in sys.argv:
        res = json.load(open(OUT_JSON))
        print("figures:", make_figures(res))
        return
    t0 = time.time()

    def log(s):
        print(f"[{time.time() - t0:6.1f} s] {s}", flush=True)
    idx = core.load_index()
    models = [(i, r) for i, r in enumerate(idx) if r["family"] in FAMILIES]
    res = {"meta": {
        "script": "code/exp_channels.py", "command": "python3 code/exp_channels.py",
        "families": list(FAMILIES), "n_models": len(models),
        "n_models_by_family": {f: sum(r["family"] == f for _, r in models) for f in FAMILIES},
        "n_models_eps_gt_0_by_family": {f: sum(r["family"] == f and r["eps"] > 0 for _, r in models) for f in FAMILIES},
        "n_runs_by_family": {f: len(set(r["run_id"] for _, r in models if r["family"] == f)) for f in FAMILIES},
        "unit_of_analysis": "snapshots of one training run are correlated; run-level summaries are given wherever a "
                            "spread is quoted (36 add/grok runs, 9 lin runs; the 35 add/memo models are 35 separate runs)",
        "seeds": {"matched_iid_fields": f"np.random.default_rng([{SEED_IID}, zoo_index])",
                  "matched_shuffles": f"np.random.default_rng([{SEED_SHUF}, zoo_index])",
                  "finite_size_fields": f"{SEED_FS} + 100*g + s, s < {FS_FIELDS}; g = 0 (lin group), 1 (p = 53)",
                  "real_votes": f"np.random.default_rng([{SEED_VOTE}, representative_index])",
                  "anatomy_permutations": [SEED_PERM, SEED_PERM + 1], "selfcheck": SEED_CHECK},
        "n_null_fields_per_model": N_NULL, "ks": list(KS), "numpy": np.__version__}}
    res["selfcheck_onehot_counts"] = selfcheck()
    log("selfcheck ok; per-model pass over %d models" % len(models))
    cols = per_model_pass(models, log)
    res["per_model"] = cols
    log("A1")
    res["A1"] = section_a1(cols)
    log("A2")
    res["A2"] = section_a2(cols)
    log("A3")
    res["A3"] = section_a3(cols, log)
    log("A5")
    res["A5"] = section_a5(cols)
    log("A4")
    res["A4"] = section_a4(cols, log)
    res["meta"]["runtime_seconds"] = round(time.time() - t0, 1)
    res = jsonable(res)
    # round the bulky per-model floats (statistics above were computed at full precision)
    res["per_model"] = {k: [round(x, 10) if isinstance(x, float) else x for x in v] for k, v in res["per_model"].items()}
    with open(OUT_JSON, "w") as fh:
        json.dump(res, fh, indent=1)
    log("wrote " + OUT_JSON)
    print("figures:", make_figures(res))
    log("done")


if __name__ == "__main__":
    main()

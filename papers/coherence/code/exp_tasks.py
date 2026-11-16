"""exp_tasks.py -- packages B2 and B3: tasks where the corrector is not handed the answer.

    OMP_NUM_THREADS=1 python3 code/exp_tasks.py          (about 1 minute, one process)

writes results/exp_tasks.json and figures/fig_tasks.{svg,png}.

B2  "mul": a*b mod 31, all 150 zoo snapshots (6 runs), corrected with the 4-query bilinear vote
    M(x+r,y+s) - M(r,y+s) - M(x+r,s) + M(r,s), whose wrapper only adds and subtracts.
B3  "lin": f(x) = <w,x> mod 7 on Z_7^4 with a secret w, all 108 zoo snapshots (9 runs), corrected with
    the 2-query BLR vote; the wrapper knows only that the map is additive.  Includes the matched
    i.i.d. finite-size baselines and the extraction of w from four self-corrected generator values.

Conventions: the inputs with a trivial vote (x = 0 or y = 0 for mul, x = 0 for lin: the vote is
identically the truth) are excluded from per-vote means and correctable fractions ("non-trivial
inputs").  eps is always the error rate over ALL inputs.  A tie for first place is a failure.
Snapshots of one training run are correlated: the run is the unit in the per-run summaries.
"""
import json
import math
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import core  # noqa: E402
from exp_twirls import plur_fail  # noqa: E402   exact plurality failure, validated in exp_twirls.py

KS = [1, 3, 5, 9, 17, 33, 65, 129]
REP_TARGETS = [0.1, 0.3, 0.5]
K_EXTRACT = 129
SEED = 20261117
N_IID = 24


def summ(v):
    v = np.asarray([x for x in v if x is not None], dtype=float)
    if len(v) == 0:
        return {"n": 0}
    return {"n": int(len(v)), "median": float(np.median(v)), "min": float(v.min()), "max": float(v.max()),
            "mean": float(v.mean())}


def run_thresholds(models):
    """Per training run: eps_all = largest eps among its snapshots at which EVERY input is correctable
    (truth is the strict mode of the vote channel); eps_some = smallest eps among its snapshots at which
    SOME input is not correctable.  None when no snapshot qualifies."""
    runs = {}
    for m in models:
        runs.setdefault(m["run_id"], []).append(m)
    out = []
    for rid in sorted(runs):
        ms = runs[rid]
        ok = [m["eps"] for m in ms if m["all_correctable"]]
        bad = [m["eps"] for m in ms if not m["all_correctable"]]
        out.append({"run_id": rid, "n_snapshots": len(ms), "n_all_correctable": len(ok),
                    "n_all_correctable_with_errors": int(sum(1 for e in ok if e > 0)),
                    "eps_all": max(ok) if ok else None, "eps_some": min(bad) if bad else None,
                    "eps_min": min(m["eps"] for m in ms), "eps_max": max(m["eps"] for m in ms),
                    "separated": (max(ok) < min(bad)) if ok and bad else None})
    return out


def law_fit(models, key_meas, key_law):
    r = np.array([m[key_meas] - m[key_law] for m in models])
    return {"n": int(len(r)), "rms": float(np.sqrt((r ** 2).mean())), "max_abs": float(np.abs(r).max()),
            "mean_signed": float(r.mean()), "min": float(r.min()), "max": float(r.max())}


def iid_baseline(shape, q, channel_fn, nontrivial, grid, seeds):
    """Nested i.i.d. incoherent fields (U < eps -> uniform wrong value V): for each field and grid eps the
    exact vote channel; correctable fraction over the non-trivial inputs and per-vote correctness."""
    nG = int(np.prod(shape))
    per_field = []
    frac = np.zeros((len(seeds), len(grid)))
    pc = np.zeros((len(seeds), len(grid)))
    real = np.zeros((len(seeds), len(grid)))
    t0sd = np.zeros((len(seeds), len(grid)))
    tmin = np.zeros((len(seeds), len(grid)))
    mmin = np.zeros((len(seeds), len(grid)))
    for i, sd in enumerate(seeds):
        rng = np.random.default_rng(sd)
        U = rng.random(nG)
        V = rng.integers(1, q, nG)
        for j, e in enumerate(grid):
            E = np.where(U < e, V, 0).reshape(shape)
            T = channel_fn(E, q)[nontrivial]
            frac[i, j] = (T[:, 0] > T[:, 1:].max(1)).mean()
            pc[i, j] = T[:, 0].mean()
            t0sd[i, j] = T[:, 0].std()
            tmin[i, j] = T[:, 0].min()
            mmin[i, j] = (T[:, 0] - T[:, 1:].max(1)).min()
            real[i, j] = (E != 0).mean()
        allok = frac[i] == 1.0
        first_fail = int(np.argmin(allok)) if not allok.all() else None
        per_field.append({"seed": int(sd),
                          "eps_last_ok_grid": float(grid[first_fail - 1]) if first_fail else (None if first_fail == 0 else float(grid[-1])),
                          "eps_last_ok_realised": float(real[i, first_fail - 1]) if first_fail else None,
                          "eps_first_fail_grid": float(grid[first_fail]) if first_fail is not None else None})
    law_c = 4 if len(shape) == 2 else 2
    return {"shape": list(shape), "q": int(q), "n_fields": len(seeds), "seeds": [int(s) for s in seeds],
            "construction": "U ~ Uniform(0,1)^|G|, V ~ Uniform{1..q-1}^|G|; E_eps = V where U < eps else 0 (nested in eps)",
            "eps_grid": [float(e) for e in grid],
            "eps_realised_mean": [float(v) for v in real.mean(0)],
            "p_all_correctable": [float(v) for v in (frac == 1.0).mean(0)],
            "correctable_fraction_mean": [float(v) for v in frac.mean(0)],
            "correctable_fraction_min": [float(v) for v in frac.min(0)],
            "per_vote_correct_mean": [float(v) for v in pc.mean(0)],
            "per_vote_correct_minus_law_max_abs": float(np.abs(pc - core.pc_law(real, q, law_c)).max()),
            "per_vote_correct_minus_law_rms": float(np.sqrt(((pc - core.pc_law(real, q, law_c)) ** 2).mean())),
            "t0_sd_mean": [float(v) for v in t0sd.mean(0)],
            "t0_min_mean": [float(v) for v in tmin.mean(0)],
            "margin_min_mean": [float(v) for v in mmin.mean(0)],
            "eps_last_ok_realised": summ([f["eps_last_ok_realised"] for f in per_field]),
            "eps_first_fail_grid": summ([f["eps_first_fail_grid"] for f in per_field]),
            "per_field": per_field,
            "lam_c_heuristic_c2": float(core.lam_c_heuristic(nG, q)),
            "eps_c_heuristic_c2": float(core.eps_from_lam(core.lam_c_heuristic(nG, q), q)),
            "eps_c_heuristic_c4": float(core.eps_from_lam(math.sqrt(core.lam_c_heuristic(nG, q)), q))}


# --------------------------------------------------------------------------------------------
# B2: multiplication
# --------------------------------------------------------------------------------------------
def special_count_law(p):
    """Distribution of the number of 'special' cells (a = 0 or b = 0) among the four query points of the
    bilinear vote at a generic input; the same for every (x, y) with x, y != 0."""
    def dist(x, y):
        r = np.arange(p)[:, None]
        s = np.arange(p)[None, :]
        sp = lambda a, b: ((a % p == 0) | (b % p == 0)).astype(int)
        n = sp(x + r, y + s) + sp(r, y + s) + sp(x + r, s) + sp(r, s)
        return np.bincount(n.ravel(), minlength=5) / float(p * p)
    d = dist(1, 1)
    assert np.allclose(d, dist(3, 7)) and np.allclose(d, dist(p - 1, 2))
    return d


def section_mul(idx):
    recs = sorted([r for r in idx if r["family"] == "mul"], key=lambda r: r["id"])
    p = q = 31
    a = np.arange(p)
    special = ((a[:, None] == 0) | (a[None, :] == 0)).ravel()          # a = 0 or b = 0  <=>  answer 0
    gen = ~special
    nspec = special_count_law(p)
    models = []
    chan = {}
    for r in recs:
        E = core.error_table(r["id"])
        T = core.bilinear_channel(E, q)
        assert np.all(T[special, 0] == 1.0)                           # trivial vote on special inputs
        err = (E != 0).ravel()
        eps = float(err.mean())
        eg, es = float(err[gen].mean()), float(err[special].mean())
        lg, ls = core.lam(eg, q), core.lam(es, q)
        two = 1.0 / q + (1 - 1.0 / q) * float((nspec * lg ** (4 - np.arange(5)) * ls ** np.arange(5)).sum())
        st = core.channel_stats(T[gen])
        Mt = core.load_table(r["id"]).ravel()
        models.append({"id": r["id"], "run_id": r["run_id"], "step": r["step"], "train_frac": r["train_frac"],
                       "eps": eps, "eps_generic": eg, "eps_special": es,
                       "n_errors": int(err.sum()), "n_errors_special": int(err[special].sum()),
                       "frac_errors_on_special": float(err[special].sum() / err.sum()) if err.any() else None,
                       "frac_generic_errors_predicting_0": float((Mt[gen & err] == 0).mean()) if (gen & err).any() else None,
                       "pc_meas": float(st["t0"].mean()), "pc_law_c4": float(core.pc_law(eps, q, 4)),
                       "pc_law_c4_generic_eps": float(core.pc_law(eg, q, 4)), "pc_law_two_rate": two,
                       "t0_min": float(st["t0"].min()), "t0_sd": float(st["t0"].std()),
                       "margin_min": float(st["margin"].min()),
                       "correctable_fraction": float(st["strict_mode"].mean()),
                       "all_correctable": bool(st["strict_mode"].all())})
        chan[r["id"]] = T[gen]
    runs = run_thresholds(models)
    werr = [m for m in models if m["eps"] > 0]
    ratio = [m["eps_special"] / m["eps_generic"] for m in werr if m["eps_generic"] > 0]
    bins = [(0.0, 0.05), (0.05, 0.2), (0.2, 0.5), (0.5, 0.8), (0.8, 1.01)]
    conc_bins = []
    for lo, hi in bins:
        mm = [m for m in werr if lo < m["eps"] <= hi]
        conc_bins.append({"eps_range": [lo, hi], "n_models": len(mm),
                          "eps_special_mean": float(np.mean([m["eps_special"] for m in mm])) if mm else None,
                          "eps_generic_mean": float(np.mean([m["eps_generic"] for m in mm])) if mm else None,
                          "n_special_rate_higher": int(sum(m["eps_special"] > m["eps_generic"] for m in mm)),
                          "frac_errors_on_special_mean": float(np.mean([m["frac_errors_on_special"] for m in mm])) if mm else None})
    out = {"n_models": len(models), "n_runs": len(runs), "p": p, "q": q, "n_generic_inputs": int(gen.sum()),
           "n_special_inputs": int(special.sum()), "special_share_of_inputs": float(special.mean()),
           "special_cells_among_4_queries_distribution": [float(v) for v in nspec],
           "models": models, "runs": runs,
           "eps_all": summ([r["eps_all"] for r in runs]), "eps_some": summ([r["eps_some"] for r in runs]),
           "n_runs_separated": int(sum(1 for r in runs if r["separated"])),
           "pooled": {"max_eps_all_correctable": max(m["eps"] for m in models if m["all_correctable"]),
                      "min_eps_some_uncorrectable": min(m["eps"] for m in models if not m["all_correctable"]),
                      "n_all_correctable": int(sum(m["all_correctable"] for m in models)),
                      "n_all_correctable_with_errors": int(sum(m["all_correctable"] and m["eps"] > 0 for m in models))},
           "law_fit": {"all_models_law_c4": law_fit(models, "pc_meas", "pc_law_c4"),
                       "models_with_errors_law_c4": law_fit(werr, "pc_meas", "pc_law_c4"),
                       "models_with_errors_law_c4_generic_eps": law_fit(werr, "pc_meas", "pc_law_c4_generic_eps"),
                       "models_with_errors_two_rate_law": law_fit(werr, "pc_meas", "pc_law_two_rate"),
                       "two_rate_law": "1/q + (1-1/q) E[lam_generic^(4-n) lam_special^n], n = number of special "
                                       "cells among the four query points (exact distribution above)"},
           "special_inputs": {"n_models_with_errors": len(werr),
                              "n_special_rate_higher_than_generic": int(sum(m["eps_special"] > m["eps_generic"] for m in werr)),
                              "n_special_rate_lower_than_generic": int(sum(m["eps_special"] < m["eps_generic"] for m in werr)),
                              "ratio_special_over_generic": summ(ratio),
                              "n_models_errors_only_on_special": int(sum(m["n_errors"] == m["n_errors_special"] for m in werr)),
                              "n_models_no_error_on_special": int(sum(m["n_errors_special"] == 0 for m in werr)),
                              "by_eps_bin": conc_bins}}
    # law residual restricted to the range where the vote still carries signal
    mid = [m for m in werr if 0.02 <= m["eps"] <= 0.7]
    out["law_fit"]["models_eps_0.02_to_0.7_law_c4"] = law_fit(mid, "pc_meas", "pc_law_c4") if mid else None
    out["law_fit"]["models_eps_0.02_to_0.7_two_rate_law"] = law_fit(mid, "pc_meas", "pc_law_two_rate") if mid else None
    # representative models
    reps = []
    rng = np.random.default_rng(SEED)
    xs_gen = np.flatnonzero(gen)
    for tgt in REP_TARGETS:
        m = min(models, key=lambda z: (abs(z["eps"] - tgt), z["id"]))
        T = chan[m["id"]]
        M = core.load_table(m["id"])
        f = core.model_true_table(m["id"]).ravel()
        rows = []
        for k in KS:
            d = plur_fail(T, k)
            row = {"k": k, "Q": 4 * k, "mean_fail": float(d.mean()), "worst_fail": float(d.max()),
                   "reliable": bool(d.mean() >= 1e-10),
                   "chernoff_mean_upper": float(core.chernoff_union_bound(T, k).mean()),
                   "law_fail": float(plur_fail(core.depolarizing_channel(m["eps"], q, 4)[None, :], k)[0])}
            if k <= 33:
                row["max_abs_diff_vs_core_exact"] = float(np.abs(d - core.plurality_fail_exact(T, k)).max())
            if k in (5, 17):
                n_tr = 1000
                fl = []
                for _ in range(10):                                   # 10 chunks of 100 trials per input
                    xs = np.repeat(xs_gen, n_tr // 10)
                    pred, tied = core.plurality(core.bilinear_votes(M, xs, k, rng, q), q)
                    fl.append((pred != f[xs]) | tied)
                fl = np.concatenate(fl)
                se = math.sqrt(float((d * (1 - d)).sum()) / n_tr) / len(d)
                row.update({"real_vote_mean_fail": float(fl.mean()), "real_vote_trials_per_input": n_tr,
                            "real_vote_se": se, "real_vote_z": float((fl.mean() - d.mean()) / se) if se > 0 else None})
            rows.append(row)
        reps.append({"target_eps": tgt, "id": m["id"], "eps": m["eps"], "pc_meas": m["pc_meas"],
                     "pc_law_c4": m["pc_law_c4"], "t0_min": m["t0_min"], "failure_vs_k": rows})
    out["representatives"] = {"rule": "mul snapshot with eps closest to the target (ties: smallest id), over all 150",
                              "real_vote_seed": SEED, "models": reps,
                              "note": "plain model error on the non-trivial inputs is eps_generic; one vote (k = 1) "
                                      "fails with probability 1 - pc_meas"}
    return out


# --------------------------------------------------------------------------------------------
# B3: hidden linear map
# --------------------------------------------------------------------------------------------
def section_lin(idx):
    recs = sorted([r for r in idx if r["family"] == "lin"], key=lambda r: r["id"])
    p = q = 7
    shape = (7, 7, 7, 7)
    w = np.array(core.LIN_W)
    unit = core.flat_index(np.eye(4, dtype=np.int64), shape)
    f = core.true_table("lin", 7, 4).ravel()
    assert (f[unit] == w).all()
    nz = np.arange(7 ** 4) != 0
    models = []
    for i, r in enumerate(recs):
        E = core.error_table(r["id"])
        T = core.twirled_channel(E, q)
        assert T[0, 0] == 1.0
        eps = float((E != 0).mean())
        st = core.channel_stats(T[nz])
        # exact identity: the input-averaged per-vote correctness is the collision probability of the
        # error-value histogram, sum_h p_h^2 (all x), i.e. (|G| sum_h p_h^2 - 1)/(|G| - 1) over x != 0
        ph = np.bincount(E.ravel(), minlength=q) / E.size
        coll = float((ph ** 2).sum())
        ident = (E.size * coll - 1.0) / (E.size - 1.0)
        assert abs(st["t0"].mean() - ident) < 1e-12
        wrong_hist = ph[1:] / ph[1:].sum() if ph[1:].sum() > 0 else np.full(q - 1, np.nan)
        M = core.load_table(r["id"])
        Tu = T[unit]
        du = plur_fail(Tu, K_EXTRACT)
        strict_u = Tu[:, 0] > Tu[:, 1:].max(1)
        rng = np.random.default_rng(SEED + 1000 + i)
        n_rep = 200
        xs = np.tile(unit, n_rep)
        pred, tied = core.sc_predict(M, xs, K_EXTRACT, rng, q)
        ok = ((pred == f[xs]) & ~tied).reshape(n_rep, 4).all(1)
        models.append({"id": r["id"], "run_id": r["run_id"], "step": r["step"], "train_frac": r["train_frac"],
                       "eps": eps, "pc_meas": float(st["t0"].mean()), "pc_law_c2": float(core.pc_law(eps, q, 2)),
                       "t0_min": float(st["t0"].min()), "t0_sd": float(st["t0"].std()),
                       "margin_min": float(st["margin"].min()),
                       "pc_identity_from_histogram": ident,
                       "wrong_value_share_max": float(np.nanmax(wrong_hist)),
                       "wrong_value_share_min": float(np.nanmin(wrong_hist)),
                       "correctable_fraction": float(st["strict_mode"].mean()),
                       "all_correctable": bool(st["strict_mode"].all()),
                       "extraction": {"raw_unit_values_correct": int((M.ravel()[unit] == w).sum()),
                                      "raw_w_correct": bool((M.ravel()[unit] == w).all()),
                                      "unit_vectors_correctable": int(strict_u.sum()),
                                      "unit_t0": [float(v) for v in Tu[:, 0]],
                                      "unit_fail_k129": [float(v) for v in du],
                                      "p_recover_w_exact": float(np.prod(1.0 - du)),
                                      "p_fail_recover_w_exact": float(-np.expm1(np.log1p(-np.minimum(du, 1 - 1e-15)).sum())),
                                      "p_fail_reliable": bool(du.sum() >= 1e-10),
                                      "p_fail_chernoff_upper": float(min(1.0, core.chernoff_union_bound(Tu, K_EXTRACT).sum())),
                                      "real_first_run_recovered": bool(ok[0]),
                                      "real_recovered_fraction": float(ok.mean()), "real_repeats": n_rep,
                                      "real_seed": SEED + 1000 + i}})
    runs = run_thresholds(models)
    pr = np.array([m["extraction"]["p_recover_w_exact"] for m in models])
    eps_a = np.array([m["eps"] for m in models])
    ext_runs = []
    for rr in runs:
        ms = [m for m in models if m["run_id"] == rr["run_id"]]
        good = [m["eps"] for m in ms if m["extraction"]["p_recover_w_exact"] >= 0.99]
        bad = [m["eps"] for m in ms if m["extraction"]["p_recover_w_exact"] < 0.99]
        ext_runs.append({"run_id": rr["run_id"], "n_snapshots": len(ms), "n_p_recover_ge_0.99": len(good),
                         "max_eps_p_recover_ge_0.99": max(good) if good else None,
                         "min_eps_p_recover_lt_0.99": min(bad) if bad else None,
                         "final_id": ms[-1]["id"], "final_eps": ms[-1]["eps"],
                         "final_p_recover_w_exact": ms[-1]["extraction"]["p_recover_w_exact"],
                         "final_p_fail_chernoff_upper": ms[-1]["extraction"]["p_fail_chernoff_upper"],
                         "final_raw_w_correct": ms[-1]["extraction"]["raw_w_correct"],
                         "final_raw_unit_values_correct": ms[-1]["extraction"]["raw_unit_values_correct"],
                         "n_raw_w_correct": int(sum(m["extraction"]["raw_w_correct"] for m in ms))})
    out = {"n_models": len(models), "n_runs": len(runs), "p": p, "q": q, "G_size": 7 ** 4, "w": [int(v) for v in w],
           "models": models, "runs": runs,
           "eps_all": summ([r["eps_all"] for r in runs]), "eps_some": summ([r["eps_some"] for r in runs]),
           "n_runs_separated": int(sum(1 for r in runs if r["separated"])),
           "n_runs_with_an_all_correctable_snapshot": int(sum(1 for r in runs if r["eps_all"] is not None)),
           "pooled": {"max_eps_all_correctable": max(m["eps"] for m in models if m["all_correctable"]),
                      "min_eps_some_uncorrectable": min(m["eps"] for m in models if not m["all_correctable"]),
                      "n_all_correctable": int(sum(m["all_correctable"] for m in models)),
                      "eps_min": float(eps_a.min()), "eps_max": float(eps_a.max())},
           "law_identity_note": "For the 2-query vote, mean_x T_x(0) = sum_h p_h^2 exactly (p_h = share of inputs with "
                                "error value h), so the input-averaged per-vote correctness depends only on the "
                                "histogram of error values, not on where the errors sit; it equals the law iff the "
                                "wrong values are equally frequent.  Checked to 1e-12 for all 108 models "
                                "(pc_identity_from_histogram).  Spatial coherence shows only in the spread of T_x(0) "
                                "over inputs (t0_sd, t0_min, margin_min).",
           "law_fit": {"all_models_law_c2": law_fit(models, "pc_meas", "pc_law_c2"),
                       "models_eps_below_0.6_law_c2": law_fit([m for m in models if m["eps"] < 0.6], "pc_meas", "pc_law_c2"),
                       "models_eps_above_0.6_law_c2": law_fit([m for m in models if m["eps"] >= 0.6], "pc_meas", "pc_law_c2")},
           "extraction": {"k": K_EXTRACT, "queries_total": 2 * K_EXTRACT * 4,
                          "rule": "self-correct M on the four unit vectors with k = 129 BLR votes each (independent "
                                  "randomness); w is recovered iff all four pluralities are correct and untied; "
                                  "p_recover_w_exact = prod_i (1 - delta_129(e_i)) from the exact channel",
                          "n_models": len(models),
                          "n_p_recover_ge_0.99": int((pr >= 0.99).sum()),
                          "n_p_recover_ge_1_minus_1e-6": int((pr >= 1 - 1e-6).sum()),
                          "n_p_recover_le_0.01": int((pr <= 0.01).sum()),
                          "n_between": int(((pr > 0.01) & (pr < 0.99)).sum()),
                          "max_eps_p_recover_ge_0.99": float(eps_a[pr >= 0.99].max()) if (pr >= 0.99).any() else None,
                          "min_p_recover_among_eps_below_0.5": float(pr[eps_a < 0.5].min()) if (eps_a < 0.5).any() else None,
                          "n_eps_below_0.5": int((eps_a < 0.5).sum()),
                          "min_eps_p_recover_lt_0.99": float(eps_a[pr < 0.99].min()) if (pr < 0.99).any() else None,
                          "n_raw_w_correct": int(sum(m["extraction"]["raw_w_correct"] for m in models)),
                          "n_raw_w_wrong_but_p_recover_ge_0.99": int(sum((not m["extraction"]["raw_w_correct"]) and
                                                                         m["extraction"]["p_recover_w_exact"] >= 0.99 for m in models)),
                          "n_real_first_run_recovered": int(sum(m["extraction"]["real_first_run_recovered"] for m in models)),
                          "max_abs_real_fraction_minus_exact": float(max(abs(m["extraction"]["real_recovered_fraction"] -
                                                                             m["extraction"]["p_recover_w_exact"]) for m in models)),
                          "per_run": ext_runs}}
    return out


# --------------------------------------------------------------------------------------------
def make_figure(res, path):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import paperstyle as ps
    ps.apply()
    fig, axes = plt.subplots(1, 2, figsize=(7.4, 3.3))
    mul, lin = res["mul"], res["lin"]
    ax = axes[0]
    em = np.linspace(0, 30 / 31, 300)
    el = np.linspace(0, 6 / 7, 300)
    ax.plot(em, core.pc_law(em, 31, 4), color=ps.REFERENCE, lw=1.4, zorder=2)
    ax.plot(el, core.pc_law(el, 7, 2), color=ps.REFERENCE, lw=1.4, ls=(0, (4, 3)), zorder=2)
    ax.plot([m["eps"] for m in mul["models"]], [m["pc_meas"] for m in mul["models"]], ls="none", marker="o", ms=5.5,
            color=ps.BLUE, label="multiplication, 4-query vote (150 snapshots)", zorder=3)
    ax.plot([m["eps"] for m in lin["models"]], [m["pc_meas"] for m in lin["models"]], ls="none", marker="s", ms=5.5,
            color=ps.ORANGE, label="hidden linear map, 2-query vote (108 snapshots)", zorder=3)
    ax.annotate("law, c = 4", xy=(0.215, core.pc_law(0.215, 31, 4)), xytext=(0.02, 0.13), fontsize=8.5,
                color=ps.INK, ha="left", arrowprops=dict(arrowstyle="-", color=ps.MUTED, lw=0.8))
    ax.annotate("law, c = 2", xy=(0.40, core.pc_law(0.40, 7, 2)), xytext=(0.50, 0.62), fontsize=8.5,
                color=ps.INK, ha="left", arrowprops=dict(arrowstyle="-", color=ps.MUTED, lw=0.8))
    ax.set_xlabel("error rate of the network, $\\varepsilon$")
    ax.set_ylabel("probability one vote is correct")
    ax.set_xlim(-0.02, 1.0)
    ax.set_ylim(0, 1.03)
    ax.set_title("a  One vote against the law", fontsize=10)
    ax = axes[1]
    bm, bl = res["iid_baseline_mul"], res["iid_baseline_lin"]
    ax.plot(bm["eps_realised_mean"], bm["correctable_fraction_mean"], color=ps.REFERENCE, lw=1.4, zorder=2)
    ax.plot(bl["eps_realised_mean"], bl["correctable_fraction_mean"], color=ps.REFERENCE, lw=1.4, ls=(0, (4, 3)), zorder=2)
    ax.plot([m["eps"] for m in mul["models"]], [m["correctable_fraction"] for m in mul["models"]], ls="none",
            marker="o", ms=5.5, color=ps.BLUE, zorder=3)
    ax.plot([m["eps"] for m in lin["models"]], [m["correctable_fraction"] for m in lin["models"]], ls="none",
            marker="s", ms=5.5, color=ps.ORANGE, zorder=3)
    ax.set_xlabel("error rate of the network, $\\varepsilon$")
    ax.set_ylabel("fraction of inputs correctable")
    ax.set_xlim(-0.02, 1.0)
    ax.set_ylim(-0.03, 1.05)
    ax.set_title("b  Correctable inputs", fontsize=10)
    return fig, axes, ps, plt, path


def finish_figure(res, fig, axes, ps, plt, path):
    ax = axes[1]
    bm, bl = res["iid_baseline_mul"], res["iid_baseline_lin"]

    def cross(b, level=0.5):
        g = np.array(b["eps_realised_mean"]); c = np.array(b["correctable_fraction_mean"])
        j = int(np.argmax(c < level))
        return float(g[j])
    xm, xl = cross(bm), cross(bl)
    ax.annotate("i.i.d. errors,\nmultiplication", xy=(xm, 0.5), xytext=(xm - 0.20, 0.30), fontsize=8.5, color=ps.INK,
                ha="right", va="center", arrowprops=dict(arrowstyle="-", color=ps.MUTED, lw=0.8))
    ax.annotate("i.i.d. errors,\nlinear map", xy=(xl, 0.5), xytext=(xl + 0.08, 0.72), fontsize=8.5, color=ps.INK,
                ha="left", va="center", arrowprops=dict(arrowstyle="-", color=ps.MUTED, lw=0.8))
    h, l = axes[0].get_legend_handles_labels()
    fig.legend(h, l, loc="lower center", ncol=2, bbox_to_anchor=(0.5, -0.08), columnspacing=1.6, handletextpad=0.4)
    fig.tight_layout(w_pad=1.5)
    ps.save(fig, path)
    plt.close(fig)


def main():
    t_start = time.time()
    idx = core.load_index()
    res = {"description": "B2 (mul, 4-query bilinear vote) and B3 (lin, 2-query BLR vote); see code/exp_tasks.py",
           "config": {"KS": KS, "rep_targets": REP_TARGETS, "k_extract": K_EXTRACT, "seed": SEED,
                      "n_iid_fields": N_IID, "tie_rule": "a tie for first place is a failure",
                      "nontrivial_inputs": "mul: x != 0 and y != 0 (900 of 961); lin: x != 0 (2400 of 2401)",
                      "eps": "error rate over all inputs", "unit": "training run (6 mul runs, 9 lin runs)",
                      "eps_all_definition": "largest eps among a run's snapshots with every input correctable",
                      "eps_some_definition": "smallest eps among a run's snapshots with some input not correctable",
                      "exact_method": "exp_twirls.plur_fail (absolute accuracy ~1e-12); rows with reliable = false "
                                      "(mean below 1e-10) are not exact: quote chernoff_mean_upper for them"}}
    res["mul"] = section_mul(idx)
    print("mul done", round(time.time() - t_start, 1), "s", flush=True)
    res["lin"] = section_lin(idx)
    print("lin done", round(time.time() - t_start, 1), "s", flush=True)
    nz = np.arange(7 ** 4) != 0
    grid_l = np.round(np.arange(0.05, 0.851, 0.01), 4)
    res["iid_baseline_lin"] = iid_baseline((7, 7, 7, 7), 7, core.twirled_channel, nz, grid_l,
                                           [9300 + s for s in range(N_IID)])
    a = np.arange(31)
    gen = ~((a[:, None] == 0) | (a[None, :] == 0)).ravel()
    grid_m = np.round(np.arange(0.05, 0.951, 0.02), 4)
    res["iid_baseline_mul"] = iid_baseline((31, 31), 31, core.bilinear_channel, gen, grid_m,
                                           [9400 + s for s in range(N_IID)])
    res["iid_baseline_mul"]["note"] = ("i.i.d. errors on all 961 cells, including the special cells a = 0 or b = 0; "
                                       "4-query bilinear vote; correctable fraction over the 900 generic inputs")
    print("baselines done", round(time.time() - t_start, 1), "s", flush=True)
    # trained versus i.i.d.: interpolate the baseline's mean correctable fraction at each model's eps
    for fam, b in (("lin", res["iid_baseline_lin"]), ("mul", res["iid_baseline_mul"])):
        g = np.array(b["eps_realised_mean"]); c = np.array(b["correctable_fraction_mean"]); cmin = np.array(b["correctable_fraction_min"])
        ms = [m for m in res[fam]["models"] if g[0] <= m["eps"] <= g[-1]]
        for m in ms:
            m["iid_correctable_fraction_mean_at_eps"] = float(np.interp(m["eps"], g, c))
            m["iid_correctable_fraction_min_at_eps"] = float(np.interp(m["eps"], g, cmin))
            m["t0_sd_over_iid"] = float(m["t0_sd"] / np.interp(m["eps"], g, b["t0_sd_mean"]))
            m["iid_margin_min_mean_at_eps"] = float(np.interp(m["eps"], g, b["margin_min_mean"]))
        diff = np.array([m["correctable_fraction"] - np.interp(m["eps"], g, c) for m in ms])
        below_min = [m["id"] for m in ms if m["correctable_fraction"] < np.interp(m["eps"], g, cmin) - 1e-12]
        band = sorted([m for m in ms if 0.45 <= m["eps"] <= 0.80], key=lambda m: m["eps"])
        res[fam]["vs_iid_baseline"] = {
            "n_models_in_grid_range": len(ms),
            "correctable_fraction_minus_iid_mean": summ(diff),
            "n_models_below_iid_mean_by_more_than_0.01": int((diff < -0.01).sum()),
            "n_models_above_iid_mean_by_more_than_0.01": int((diff > 0.01).sum()),
            "n_models_below_the_min_over_iid_fields": len(below_min),
            "interpolation_axis": "mean realised eps of the i.i.d. fields",
            "t0_sd_over_iid": summ([m["t0_sd_over_iid"] for m in ms]),
            "t0_sd_over_iid_eps_below_0.5": summ([m["t0_sd_over_iid"] for m in ms if m["eps"] < 0.5]),
            "t0_sd_over_iid_eps_0.5_to_0.8": summ([m["t0_sd_over_iid"] for m in ms if 0.5 <= m["eps"] <= 0.8]),
            "n_margin_min_below_iid_mean": int(sum(m["margin_min"] < m["iid_margin_min_mean_at_eps"] for m in ms)),
            "transition_band_eps_0.45_to_0.80": [
                {"id": m["id"], "eps": m["eps"], "correctable_fraction": m["correctable_fraction"],
                 "iid_mean": m["iid_correctable_fraction_mean_at_eps"], "iid_min": m["iid_correctable_fraction_min_at_eps"]}
                for m in band],
            "iid_eps_last_ok_realised": b["eps_last_ok_realised"],
            "trained_eps_all": res[fam]["eps_all"], "trained_eps_some": res[fam]["eps_some"]}
    res["runtime_seconds"] = round(time.time() - t_start, 1)
    os.makedirs(core.RESULTS_DIR, exist_ok=True)
    with open(os.path.join(core.RESULTS_DIR, "exp_tasks.json"), "w") as fh:
        json.dump(res, fh, indent=1)
    finish_figure(res, *make_figure(res, os.path.join(core.FIG_DIR, "fig_tasks")))
    print("done in", res["runtime_seconds"], "s")


if __name__ == "__main__":
    if "--figure-only" in sys.argv:
        with open(os.path.join(core.RESULTS_DIR, "exp_tasks.json")) as fh:
            _res = json.load(fh)
        finish_figure(_res, *make_figure(_res, os.path.join(core.FIG_DIR, "fig_tasks")))
    else:
        main()

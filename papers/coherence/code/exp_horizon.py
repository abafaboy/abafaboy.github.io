"""exp_horizon.py -- package C1: horizon of chained computation with a trained network.

    OMP_NUM_THREADS=1 python3 code/exp_horizon.py        (one process, deterministic, about 2 min)

Writes results/exp_horizon.json and figures/fig_horizon.{svg,png}.

Task: a running sum s_{t+1} = s_t + a_t (mod p), a_t uniform, s_0 uniform, in which every step is
computed by the network table M(s_t, a_t) -- raw (k = 0) or through the BLR self-corrector with k
votes (2k model queries per step, fresh randomness at every step).  A chain survives to T if all of
its first T steps were correct.  For four add/grok p = 47 snapshots (eps close to 0.05, 0.2, 0.4,
0.6) and k in {0, 1, 3, 5, 9, 17, 33, 65}:
  * exact per-step failure delta_k(s, a) from the exact twirled channel (core.plurality_fail_exact),
    the exact survival rate (Perron root of W[s, s'] = (1 - delta_k(s, s' - s))/p) and the i.i.d.
    approximation 1 - mean delta_k; exact 50% horizon T50 = ln 2 / (-ln rate);
  * the prediction from eps alone (depolarizing 2-query channel);
  * a simulation with real votes (core.sc_predict), compared with the exact survival curve;
  * an adaptive stopping rule (vote until the leader is m votes ahead of the runner-up).
Below mean delta = 1e-9 the exact routine (absolute accuracy ~1e-12) is replaced by a rigorous
two-sided bound (union bound above; Bonferroni with negative association of multinomial counts below).
"""
import json
import math
import os
import sys
import time

import numpy as np
from scipy.special import bdtrc
from scipy.stats import beta as beta_dist
from scipy.stats import binom

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import core  # noqa: E402
from exp_labelfree import MeanFail, pick_horizon_models, smallest_odd_k  # noqa: E402

SEED = 20261117
KS = [0, 1, 3, 5, 9, 17, 33, 65]
T_MAX = 20000
FLOOR = 1e-9                 # below this mean failure the exact routine is not trusted
VOTE_BUDGET = 4.0e8          # per simulated configuration
REACH = 10000                # simulate only if the exact T50 is at most this
ADAPT_M = [2, 3, 4, 6, 8]
ADAPT_REPS = 100             # repetitions of every input
ADAPT_CAP = 3000             # maximal number of votes of the adaptive rule (counted as a failure)


def union_sandwich(P, k):
    """Rigorous bounds lo <= delta_k(x) <= hi for every row of P, accurate in RELATIVE terms when the
    failure is small.  delta_k = sum_m Pr[N_0 = m] Pr[max_h N_h >= m | N_0 = m]; with p_h = Pr[Bin(k-m,
    tau_h) >= m] the inner probability is at most S1 = sum_h p_h (union bound) and at least
    max(max_h p_h, S1 - sum_{h<h'} p_h p_h') (Bonferroni; Pr[N_h >= m, N_h' >= m] <= p_h p_h' because
    multinomial counts are negatively associated).  For m > k/2 the inner probability is 0."""
    P = np.atleast_2d(np.asarray(P, dtype=float))
    t0 = P[:, 0]
    Wr = P[:, 1:]
    s = Wr.sum(1)
    tau = Wr / np.where(s > 0, s, 1.0)[:, None]
    w = binom.pmf(np.arange(k + 1)[None, :], k, t0[:, None])
    lo = w[:, 0].copy()
    hi = w[:, 0].copy()
    for m in range(1, k // 2 + 1):
        ph = bdtrc(m - 1, k - m, tau)
        S1 = ph.sum(1)
        low = np.maximum(ph.max(1), S1 - 0.5 * (S1 ** 2 - (ph ** 2).sum(1)))
        hi += w[:, m] * np.minimum(1.0, S1)
        lo += w[:, m] * np.clip(low, 0.0, 1.0)
    return lo, np.minimum(hi, 1.0)


def transfer_matrix(D):
    """W[s, s'] = (1 - D[s, s' - s]) / p for a (p, p) table of per-step failures D[s, a]."""
    p = D.shape[0]
    W = np.zeros((p, p))
    s, a = np.meshgrid(np.arange(p), np.arange(p), indexing="ij")
    W[s, (s + a) % p] = (1.0 - D) / p
    return W


def survival_exact(W, T):
    p = W.shape[0]
    return float(np.ones(p) @ np.linalg.matrix_power(W, int(T)) @ np.ones(p) / p)


def first_T_below_half(W, t_guess):
    """Smallest integer T with exact survival (uniform start) <= 1/2."""
    hi = max(1, int(t_guess))
    while survival_exact(W, hi) > 0.5:
        hi *= 2
    lo = 0
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if survival_exact(W, mid) <= 0.5:
            hi = mid
        else:
            lo = mid
    return hi


def t50(gap):
    return math.log(2.0) / (-math.log1p(-gap)) if 0 < gap < 1 else (float("inf") if gap <= 0 else 0.0)


def simulate(M, f, k, n_chains, rng, block):
    """First failing step (1-based) of n_chains chains; T_MAX + 1 if the chain survives T_MAX steps.
    While a chain is alive its state is the true running sum, so the steps of a block can be
    evaluated together; every step uses fresh votes from core.sc_predict."""
    p = M.shape[0]
    Mf, ff = M.ravel(), f.ravel()
    s = rng.integers(0, p, n_chains)
    tau = np.full(n_chains, T_MAX + 1, dtype=np.int64)
    alive = np.arange(n_chains)
    t0, votes = 0, 0
    while alive.size and t0 < T_MAX:
        B = min(block, T_MAX - t0)
        a = rng.integers(0, p, (alive.size, B))
        cs = np.cumsum(a, axis=1)
        xs = (((s[alive][:, None] + cs - a) % p) * p + a).ravel()
        if k == 0:
            bad = Mf[xs] != ff[xs]
        else:
            pred, tied = core.sc_predict(M, xs, k, rng, p)
            bad = (pred != ff[xs]) | tied
            votes += xs.size * k
        bad = bad.reshape(alive.size, B)
        anyb = bad.any(1)
        tau[alive[anyb]] = t0 + bad.argmax(1)[anyb] + 1
        s[alive] = (s[alive] + cs[:, -1]) % p
        alive = alive[~anyb]
        t0 += B
    return tau, votes


def adaptive(M, f, m, reps, rng, cap=ADAPT_CAP):
    """Vote until the leading value is m votes ahead of the runner-up; every input `reps` times.
    Returns (wrong, votes_used, capped) per sample."""
    p = M.shape[0]
    Mf, ff = M.ravel().astype(np.int64), f.ravel()
    G = Mf.size
    ADD = core.add_table(M.shape)
    xs = np.tile(np.arange(G), reps)
    n = xs.size
    cnt = np.zeros((n, p), dtype=np.int16)
    top1 = np.zeros(n, dtype=np.int16)
    top2 = np.zeros(n, dtype=np.int16)
    used = np.full(n, cap, dtype=np.int32)
    act = np.arange(n)
    for t in range(1, cap + 1):
        r = rng.integers(0, G, act.size)
        v = (Mf[ADD[xs[act], r]] - Mf[r]) % p
        c = cnt[act, v]
        cnt[act, v] = c + 1
        t1, t2 = top1[act], top2[act]
        lead = c == t1                      # the vote goes to (one of) the leaders
        second = (c == t2) & ~lead          # the vote goes to a runner-up
        t1 = np.where(lead, c + 1, t1)
        t2 = np.where(second, c + 1, t2)
        top1[act], top2[act] = t1, t2
        done = (t1 - t2) >= m
        used[act[done]] = t
        act = act[~done]
        if act.size == 0:
            break
    capped = np.zeros(n, dtype=bool)
    capped[act] = True
    wrong = (cnt.argmax(1) != ff[xs]) | capped
    return wrong, used, capped


def main():
    t_start = time.time()
    index = core.load_index()
    chosen = pick_horizon_models(index)
    out = dict(config=dict(
        script="code/exp_horizon.py", seed=SEED, ks=KS, t_max=T_MAX, floor=FLOOR,
        vote_budget_per_simulation=VOTE_BUDGET, reach=REACH,
        model_rule=pick_horizon_models.__doc__.strip(),
        chain="s_{t+1} = M(s_t, a_t), a_t uniform on Z_p, s_0 uniform; survive to T = first T steps all "
              "correct; self-corrected step = plurality of k votes M(x+r) - M(r), tie = failure; "
              "cost 2k model queries per step (1 for the raw model)",
        simulation_rule="simulate when exact T50 <= %d; 4000 chains if the expected number of votes "
                        "4000 * E[min(tau, T_max)] * k is within the budget, else 2000 chains, else skip" % REACH,
        adaptive=dict(m=ADAPT_M, repetitions_per_input=ADAPT_REPS, cap=ADAPT_CAP,
                      inputs="every input of G, uniformly weighted")), models=[])
    rng = np.random.default_rng(SEED)
    for tgt, mid in chosen:
        rec = core.get_record(mid)
        p = q = rec["p"]
        M = core.load_table(mid)
        f = core.model_true_table(mid)
        E = core.error_table(mid)
        N = core.twirled_counts(E, q)
        T = N / N.sum(1, keepdims=True)
        eps = float((E != 0).mean())
        st = core.channel_stats(T)
        rates = st["rate"]
        ent = dict(id=mid, target_eps=tgt, eps=eps, p=p, split_seed=rec["split_seed"], step=rec["step"],
                   n_uncorrectable=int((~st["strict_mode"]).sum()),
                   min_rate_I_x=float(np.min(rates)),
                   rate_of_mean_channel=float(core.channel_rate(T.mean(0)[None, :])[0]),
                   rate_depolarizing_law=float(core.rate_law(eps, q, 2)),
                   mean_t0=float(T[:, 0].mean()), t0_depolarizing=float(core.pc_law(eps, q, 2)),
                   per_k=[])
        dep = np.asarray(core.depolarizing_channel(eps, q, 2))[None, :]
        for k in KS:
            e = dict(k=k, queries_per_step=(1 if k == 0 else 2 * k))
            if k == 0:
                d = (E != 0).ravel().astype(float)
                d_lo = d_hi = d
                dd = dd_lo = dd_hi = eps
            else:
                d = core.plurality_fail_exact(T, k)
                d_lo, d_hi = union_sandwich(T, k)
                e["n_inputs_core_outside_sandwich"] = int(((d < d_lo - 1e-11) | (d > d_hi + 1e-11)).sum())
                dd = float(core.plurality_fail_exact(dep, k)[0])
                a_, b_ = union_sandwich(dep, k)
                dd_lo, dd_hi = float(a_[0]), float(b_[0])
            D = d.reshape(p, p)
            md = float(d.mean())
            e.update(mean_delta_core=md, mean_delta_sandwich=[float(d_lo.mean()), float(d_hi.mean())],
                     max_delta=float(d.max()))
            W = transfer_matrix(D)
            if md >= FLOOR:
                rho = float(np.max(np.linalg.eigvals(W).real))
                gap = 1.0 - rho
                e.update(method="exact (core.plurality_fail_exact + Perron root)", mean_delta=md,
                         rate_exact=rho, gap_exact=gap, rate_iid=1.0 - md, T50_exact=t50(gap), T50_iid=t50(md),
                         gap_over_mean_delta=gap / md,
                         T50_exact_bounds=[t50(gap), t50(gap)])
            else:
                # tiny failure: gap = mean delta up to O(max_s row^2); rigorous bracket from row sums
                rl = d_lo.reshape(p, p).mean(1)
                rh = d_hi.reshape(p, p).mean(1)
                mid_ = 0.5 * (float(d_lo.mean()) + float(d_hi.mean()))
                e.update(method="rigorous sandwich (union bound / Bonferroni with negative association); "
                                "gap = mean delta to first order, bracket = [min, max] row sum",
                         mean_delta=mid_, rate_exact=None, gap_exact=mid_, rate_iid=None,
                         T50_exact=t50(mid_), T50_iid=t50(mid_), gap_over_mean_delta=None,
                         T50_exact_bounds=[t50(float(rh.max())), t50(float(rl.min()))])
            if dd >= FLOOR:
                e.update(delta_eps_only=dd, T50_eps_only=t50(dd), T50_eps_only_bounds=[t50(dd), t50(dd)])
            else:
                e.update(delta_eps_only=0.5 * (dd_lo + dd_hi), T50_eps_only=t50(0.5 * (dd_lo + dd_hi)),
                         T50_eps_only_bounds=[t50(dd_hi), t50(dd_lo)])
            e["T50_ratio_exact_over_eps_only"] = e["T50_exact"] / e["T50_eps_only"]
            # ---- simulation with real votes
            if md >= FLOOR and e["T50_exact"] <= REACH:
                exp_steps = (1.0 - e["rate_exact"] ** T_MAX) / e["gap_exact"]
                n_chains = 0
                for n_try in (4000, 2000):
                    if n_try * exp_steps * max(k, 1) <= VOTE_BUDGET:
                        n_chains = n_try
                        break
                if n_chains:
                    block = int(max(1, min(math.ceil(e["T50_exact"] / 3.0), 4.0e6 / (n_chains * max(k, 1)), 512)))
                    tau, votes = simulate(M, f, k, n_chains, rng, block)
                    n_fail = int((tau <= T_MAX).sum())
                    at_risk = float(np.minimum(tau, T_MAX).sum())
                    haz = n_fail / at_risk
                    cps = sorted(set(int(min(T_MAX, max(1, round(c * e["T50_exact"])))) for c in (0.25, 0.5, 1, 2, 3)))
                    checks = []
                    for Tc in cps:
                        se_ = survival_exact(W, Tc)
                        ss = float((tau > Tc).mean())
                        sd = math.sqrt(se_ * (1 - se_) / n_chains)
                        checks.append(dict(T=Tc, survival_sim=ss, survival_exact=se_,
                                           z=(ss - se_) / sd if sd > 0 else None))
                    zs = [abs(c["z"]) for c in checks if c["z"] is not None]
                    e["simulation"] = dict(
                        n_chains=n_chains, block=block, n_failed=n_fail, n_censored=n_chains - n_fail,
                        votes_used=int(votes), hazard=haz, T50_sim=t50(haz),
                        T50_sim_rel_se=1.0 / math.sqrt(max(1, n_fail)),
                        median_first_failure_sim=int(np.sort(tau)[(n_chains + 1) // 2 - 1]),
                        median_first_failure_exact=first_T_below_half(W, e["T50_exact"]),
                        checkpoints=checks, max_abs_z=max(zs) if zs else None)
            ent["per_k"].append(e)
            print("%s k=%d mean delta %.3e T50 %.4g (eps-only %.4g) sim %s  %.1fs" % (
                mid, k, e["mean_delta"], e["T50_exact"], e["T50_eps_only"],
                ("%.4g" % e["simulation"]["T50_sim"]) if "simulation" in e else "-", time.time() - t_start), flush=True)
        # ---- raw versus corrected, slopes
        pk = {e["k"]: e for e in ent["per_k"]}
        ent["T50_raw"] = pk[0]["T50_exact"]
        ent["smallest_k_in_grid_beating_raw"] = next((k for k in KS[1:] if pk[k]["T50_exact"] > pk[0]["T50_exact"]), None)
        ent["T50_gain_over_raw"] = {str(k): pk[k]["T50_exact"] / pk[0]["T50_exact"] for k in KS[1:]}
        ent["slopes_ln_T50_per_vote"] = [
            dict(k_from=k1, k_to=k2,
                 exact=(math.log(pk[k2]["T50_exact"]) - math.log(pk[k1]["T50_exact"])) / (k2 - k1),
                 eps_only=(math.log(pk[k2]["T50_eps_only"]) - math.log(pk[k1]["T50_eps_only"])) / (k2 - k1))
            for k1, k2 in zip(KS[1:-1], KS[2:])]
        ent["slope_last_interval"] = ent["slopes_ln_T50_per_vote"][-1]
        ent["slope_per_model_query_last_interval"] = ent["slopes_ln_T50_per_vote"][-1]["exact"] / 2.0

        # ---- adaptive stopping rule
        mf = MeanFail(N)
        kb = next((k for k in range(1, 150, 2) if mf.value(k) < eps), None)
        ent["smallest_odd_k_beating_raw"] = dict(
            k=kb, mean_delta=(mf.value(kb) if kb else None), raw_eps=eps,
            mean_delta_at_k_minus_2=(mf.value(kb - 2) if kb and kb > 1 else None),
            note="smallest odd k with mean_x delta_k(x) < eps (i.i.d. rate; the Perron correction is below 1%)")
        ad = []
        for m in ADAPT_M:
            wrong, used, capped = adaptive(M, f, m, ADAPT_REPS, rng)
            n = wrong.size
            nf = int(wrong.sum())
            ci_lo = float(beta_dist.ppf(0.025, nf, n - nf + 1)) if nf > 0 else 0.0
            ci_hi = float(beta_dist.ppf(0.975, nf + 1, n - nf)) if nf < n else 1.0
            target = nf / n if nf > 0 else 1.0 - 0.05 ** (1.0 / n)       # one-sided 95% bound if no failure seen
            mean_votes = float(used.mean())
            k_eq = smallest_odd_k(mf, int(mean_votes) | 1, thr=target)
            k_cost = int(math.ceil(mean_votes)) | 1                       # odd fixed k >= mean adaptive votes
            a = dict(m=m, n_samples=n, n_failures=nf, n_capped=int(capped.sum()),
                     failure=nf / n, failure_ci95=[ci_lo, ci_hi],
                     failure_upper95_if_none_seen=(None if nf > 0 else target),
                     mean_votes=mean_votes, mean_queries=2.0 * mean_votes,
                     median_votes=float(np.median(used)), p99_votes=float(np.percentile(used, 99)),
                     max_votes=int(used.max()),
                     fixed_k_same_failure=k_eq,
                     fixed_k_same_failure_exact_failure=(mf.value(k_eq) if k_eq is not None else None),
                     query_ratio_fixed_over_adaptive=(k_eq / mean_votes if k_eq is not None else None),
                     comparison_target=("observed failure" if nf > 0 else "95% upper bound (no failure observed)"),
                     fixed_k_same_cost=(k_cost if k_cost <= 149 else None),
                     fixed_k_same_cost_exact_failure=(mf.value(k_cost) if k_cost <= 149 else None))
            ad.append(a)
            print("  adaptive m=%d fail %.3e (%d/%d) mean votes %.2f fixed k same failure %s  %.1fs" % (
                m, a["failure"], nf, n, mean_votes, k_eq, time.time() - t_start), flush=True)
        ent["adaptive"] = ad
        out["models"].append(ent)

    zs = [c["z"] for mdl in out["models"] for e in mdl["per_k"] if "simulation" in e
          for c in e["simulation"]["checkpoints"] if c["z"] is not None]
    out["simulation_summary"] = dict(
        n_configurations=int(sum("simulation" in e for mdl in out["models"] for e in mdl["per_k"])),
        n_checkpoints=len(zs), max_abs_z=float(np.max(np.abs(zs))), rms_z=float(np.sqrt(np.mean(np.square(zs)))),
        n_abs_z_above_2=int(np.sum(np.abs(zs) > 2)), n_abs_z_above_3=int(np.sum(np.abs(zs) > 3)),
        max_rel_dev_T50_sim=float(max(abs(e["simulation"]["T50_sim"] / e["T50_exact"] - 1.0)
                                      for mdl in out["models"] for e in mdl["per_k"] if "simulation" in e)),
        note="checkpoints of one configuration share the same chains and are not independent")
    gs = [e["gap_over_mean_delta"] for mdl in out["models"] for e in mdl["per_k"] if e["gap_over_mean_delta"] is not None]
    out["perron_vs_iid"] = dict(
        note="(1 - Perron root) / mean delta_k over all models and k with mean delta >= floor; "
             "1 means the i.i.d. approximation is exact",
        min=float(min(gs)), max=float(max(gs)), n=len(gs))
    out["runtime_seconds"] = round(time.time() - t_start, 1)
    path = os.path.join(core.RESULTS_DIR, "exp_horizon.json")
    with open(path, "w") as fh:
        json.dump(out, fh, indent=1)
    print("wrote", path, flush=True)
    make_figure(out)


def make_figure(out=None):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.lines import Line2D
    import paperstyle as ps
    ps.apply()
    if out is None:
        with open(os.path.join(core.RESULTS_DIR, "exp_horizon.json")) as fh:
            out = json.load(fh)
    YMAX = 1e12
    fig, axes = plt.subplots(1, 2, figsize=(7.4, 3.5), gridspec_kw=dict(width_ratios=[1.25, 1.0]))
    pos = {k: i for i, k in enumerate(KS)}
    ax = axes[0]
    label_at = [(4.22, 1e8, "right"), (6.32, 1e9, "left"), (7.2, None, "left"), (7.2, None, "left")]
    for mdl, col, (lx, ly, ha) in zip(out["models"], ps.SERIES, label_at):
        xs = [pos[e["k"]] for e in mdl["per_k"]]
        ex = [e["T50_exact"] for e in mdl["per_k"]]
        eo = [e["T50_eps_only"] for e in mdl["per_k"]]
        ax.plot(xs, eo, color=col, lw=1.0, ls=(0, (4, 2)), zorder=2)
        ax.plot(xs, ex, color=col, lw=2.0, zorder=3)
        sx = [pos[e["k"]] for e in mdl["per_k"] if "simulation" in e]
        sy = [e["simulation"]["T50_sim"] for e in mdl["per_k"] if "simulation" in e]
        ax.plot(sx, sy, ls="none", marker="o", ms=6.5, color=col, zorder=4)
        ax.text(lx, ly if ly is not None else ex[-1], "$\\varepsilon$ = %.2f" % mdl["eps"], color=ps.INK,
                fontsize=8.5, ha=ha, va="center")
        axes[1].plot(xs, [e["T50_ratio_exact_over_eps_only"] for e in mdl["per_k"]], color=col, lw=2.0,
                     marker="o", ms=6.5, label="$\\varepsilon$ = %.2f" % mdl["eps"], zorder=3)
    handles = [Line2D([], [], color=ps.INK2, lw=2.0, label="exact"),
               Line2D([], [], color=ps.INK2, lw=0, marker="o", ms=6.5, label="simulated"),
               Line2D([], [], color=ps.INK2, lw=1.0, ls=(0, (4, 2)), label="from $\\varepsilon$ alone")]
    ax.set_yscale("log")
    ax.set_ylim(0.15, YMAX)
    ax.set_xlim(-0.35, len(KS) + 0.25)
    ax.set_xticks(range(len(KS)))
    ax.set_xticklabels(["raw"] + [str(k) for k in KS[1:]])
    ax.set_yticks([1, 1e3, 1e6, 1e9, 1e12])
    ax.minorticks_off()
    ax.set_xlabel("votes per step $k$")
    ax.set_ylabel("50% horizon $T_{50}$ (steps)")
    ax.set_title("a  Horizon of a chained sum")
    ax.legend(handles=handles, loc="upper left", handlelength=2.2)
    ax = axes[1]
    ax.axhline(1.0, color=ps.REFERENCE, lw=1.0, ls="--", zorder=1)
    ax.set_yscale("log")
    ax.set_ylim(5e-5, 3)
    ax.set_xlim(-0.35, len(KS) - 0.65)
    ax.set_xticks(range(len(KS)))
    ax.set_xticklabels(["raw"] + [str(k) for k in KS[1:]])
    ax.set_yticks([1e-4, 1e-3, 1e-2, 1e-1, 1])
    ax.minorticks_off()
    ax.set_xlabel("votes per step $k$")
    ax.set_ylabel("exact $T_{50}$ / predicted from $\\varepsilon$")
    ax.set_title("b  Error rate alone is optimistic")
    ax.legend(loc="lower left")
    fig.tight_layout(w_pad=1.6)
    ps.save(fig, os.path.join(core.FIG_DIR, "fig_horizon"))
    plt.close(fig)
    print("wrote figures/fig_horizon", flush=True)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--figure-only":
        make_figure()
    else:
        main()

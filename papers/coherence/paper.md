---
title: "Coherence, Not Error Rate, Limits the Self-Correction of Learned Computation"
subtitle: "When does voting over a random self-reduction repair a trained network? An exact criterion, sharp worst-case radii and a depolarizing law, studied at toy scale"
kicker: "Research preprint · November 2026 · not peer reviewed"
author:
  - "<b>Abafa Mukhamedov</b> (commissioned and published this work)"
  - "<b>Claude</b>, an AI research agent built by Anthropic (conceived, implemented, ran and wrote it)"
date: "16 November 2026"
description: "When does voting over a random self-reduction repair a trained network? An exact per-input criterion, sharp worst-case radii, and exhaustive measurements on 1,373 small networks trained on modular arithmetic, whose correctability is decided by the coherence of their errors rather than by their error rate."
pdf: "paper.pdf"
abstract: |
  A trained network approximating a homomorphism $f$ can be repaired without labels by a plurality vote over $f(x) = f(x+r) - f(r)$ with random shifts $r$. Voting succeeds at an input exactly when the truth is the mode of a computable distribution, the twirled channel; the two-query vote is guaranteed only below error rate 1/3 (odd output group) or 1/4, both sharp, while independent scattered errors allow correction up to chance. In 1,373 small networks trained on modular arithmetic, mean two-query vote correctness matches the independent-error law to $2.3 \times 10^{-3}$, but an identity forces this. Coherence shows at the worst inputs: in addition networks it grows from none below error rate 0.1 to 8 to 10 times the independent level above 0.8. In all 36 addition runs every input stays correctable beyond 1/3, in 33 beyond the unique-decoding radius, in none up to the independent-error limit. A network with 50.2% accuracy reaches a worst-input failure of $4.4 \times 10^{-7}$ with 129 votes, but error-rate-only predictions are optimistic in the tail. The rival answer is usually 0, from over-predicted output classes. A heuristic subtracting a label-free background from the votes lifts the median fully correctable error rate of addition runs from 0.53–0.62 to about 0.68. Scope: toy scale, exact algebraic tasks, a corrector given the group law; nothing is claimed about language models; the mathematics is classical.
footer: "Generated from paper.md by build.py. Every number in the text is read from a JSON file in results/, written by a script in code/."
---

# Introduction {#sec-intro}

A trained network is a fixed function. Repeating a computation and taking a vote, the classical remedy for unreliable components (von Neumann, 1956), does not help it: an input it gets wrong, it gets wrong every time. Voting over samples helps language models (Wang et al., 2023), but only against the part of the error that changes between calls (Liu, 2026).

Program checking has another remedy. If the target $f$ is a homomorphism, $f(x+y) = f(x) + f(y)$, then $f(x) = f(x+r) - f(r)$ for every $r$ (Blum, Luby and Rubinfeld, 1993). Querying a program $M$ at the two uniformly random points $x+r$ and $r$ turns its fixed error pattern into noise in the vote $M(x+r) - M(r)$, and a plurality over several $r$ returns $f(x)$ at *every* input, provided $M$ is "not wrong too often". Such an identity is a *random self-reduction*, and the voter is a *self-corrector*.

We ask whether, for a trained network, "not wrong too often" is a bound on the error rate, as in the classical guarantees, or a property of the structure of the errors. In words from quantum computing (Wallman and Emerson, 2016), errors are *incoherent* when they act like independent noise with scattered wrong values, and *coherent* when they line up and reinforce one another under the randomisation.

We study the question where everything can be computed exactly: 1,373 snapshots from 86 training runs of small networks on modular addition, multiplication and a hidden linear map, with error rates from 0 to 0.98, each enumerated on its whole input group. Snapshots of one run are correlated, so the run is the unit of analysis. The contributions are:

1. **An exact criterion.** Voting succeeds at $x$ if and only if the truth is the strict mode of one computable distribution, the *twirled channel* $T_x$ (Proposition 1).
2. **The worst case.** The two-query plurality vote is guaranteed below error rate $1/3$ for odd $|H|$ and $1/4$ otherwise, both sharp; for odd $|H|$ this is inside the unique-decoding radius of the code (Theorem 2, Proposition 3).
3. **The incoherent case.** For independent scattered errors a $c$-query vote is correct with probability $1/q + (1-1/q)\lambda^c$, and only finite size limits correction (Theorem 4). Synthetic fields with equal error rates break at $1/4$, $1/3$, $0.484$, near $0.78$, or never (Section 4).
4. **Trained networks.** Mean vote correctness follows the incoherent law because an identity forces it (Proposition 9); coherence shows at the worst inputs. Addition networks stay correctable beyond $1/3$ in all 36 runs, beyond the unique-decoding radius in 33, up to the incoherent limit in none. The rival answer is the vote for 0, from over-predicted output classes (Section 5).
5. **Bias-subtracted voting.** Subtracting from the vote counts the background predicted by the output histogram, which needs no labels, raises the median error rate up to which addition runs stay fully correctable from 0.53–0.62 to about 0.68 and makes no run worse, but it leaves the linear-map and multiplication thresholds unchanged, can hurt inputs whose answer is 0 at finite vote counts, and has no guarantee (Section 6).
6. **Baselines, other tasks, chains, evaluation.** Re-sampling the same input and ensembles give nothing at equal query budget (Section 7); multiplication is corrected with additions only (Section 8); 9 votes lengthen the 50% horizon of a chained sum from 13.5 to $3.6 \times 10^5$ steps (Section 9); the linearity test estimates the error rate without labels below 0.6 (Section 10). Error-rate-only predictions are optimistic in the tail.

**Scope.** Exact algebraic maps on groups of at most 2,809 elements, small networks, and a corrector that is *given* the group law; we claim nothing about language models. The mathematics is classical (the corrector and tester of Blum, Luby and Rubinfeld; Fourier multiplicativity), and two worst-case thresholds coincide with known decoding radii. The thesis of the title has been argued for repeated sampling of language models (Liu, 2026; Brilliant, 2026) and for quantum noise (Wallman and Emerson, 2016). What we add, to our knowledge, is the per-input criterion, the sharp plurality thresholds and an exhaustive measurement of the twirled channels of trained networks.

# Setting and notation {#sec-setting}

**Task and model.** $G$ and $H$ are finite abelian groups, $q = |H|$, and the task $f: G \to H$ is a homomorphism; the running example is $f(a,b) = a + b \bmod p$ on $G = \mathbb{Z}_p^2$. A network is represented by its table of argmax predictions $M: G \to H$, with *error field* $e = M - f$, error set $E = \{x : e(x) \neq 0\}$ and *error rate* $\varepsilon = |E|/|G|$. A random guess has error rate $1 - 1/q$ (chance), and the *advantage*
$$\lambda = 1 - \frac{\varepsilon}{1 - 1/q}$$
is 1 for a perfect model, 0 at chance and negative below chance.

**The self-corrector.** A *vote* for the value at $x$ is $V_r(x) = M(x+r) - M(r)$ with a uniform shift $r \in G$. It costs two queries, and since $f$ is a homomorphism,
$$V_r(x) = f(x) + D_x(r), \quad D_x(r) = e(x+r) - e(r).$$
The self-corrector $\mathrm{SC}_k(x)$ returns the plurality (most frequent value) of $k$ votes with independent shifts. A tie for first place counts as a failure throughout, and $\delta_k(x)$ is the failure probability at $x$. The corrector uses the group operations but no labels.

**The twirled channel.** $T_x(h) = \Pr_r[D_x(r) = h]$, $h \in H$, is the *twirled channel* at $x$. In quantum information, to twirl a noise process is to average it over a group of random operations (Emerson, Alicki and Życzkowski, 2005); here the group is the shifts of the input. The counts $N_h(x) = |G|\,T_x(h)$ form an autocorrelation, so one fast Fourier transform gives every channel exactly. An input is *correctable* when the truth is the strict mode, $T_x(0) > \max_{h \neq 0} T_x(h)$; the difference is the *margin*.

**Incoherent errors.** In the *incoherent* field the $e(x)$ are independent, non-zero with probability $\varepsilon$ and uniform on the $q - 1$ wrong values. A vote that combines $c$ distinct queries is then correct with probability $1/q + (1-1/q)\lambda^c$ and takes each wrong value with probability $(1-\lambda^c)/q$ (Theorem 4): with probability $\lambda^c$ it is the truth, otherwise uniform. This is the classical counterpart of the depolarizing channel of quantum information, and by the *coherence* of a real error field we mean its departure from this form. The linearity test $M(x) + M(y) = M(x+y)$ has $c = 3$. Multiplication $f(a,b) = ab \bmod p$ is bilinear, not a homomorphism, and is corrected by the vote $M(a+r, b+s) - M(r, b+s) - M(a+r, s) + M(r,s)$ with $c = 4$.

# Theory {#sec-theory}

All statements are proved in the appendix and were checked on synthetic error fields (Table 1). No trained network appears in this section.

## The exact criterion {#sec-criterion}

::: theorem
**Proposition 1 (exact criterion and rate).** Fix an input $x$ and $k \geq 1$ votes with independent uniform shifts.

*(a)* The offsets of the $k$ votes from $f(x)$ are independent draws from $T_x$. Hence $\delta_k(x) = \Pr[N_0 \leq \max_{h \neq 0} N_h]$, where the counts $(N_h)_{h \in H}$ are multinomial with $k$ trials and cell probabilities $T_x$.

*(b)* $\delta_k(x) \to 0$ as $k \to \infty$ if and only if $T_x(0) > \max_{h \neq 0} T_x(h)$. If $T_x(0) = T_x(h)$ for some $h \neq 0$, then $\delta_k(x) \geq 1/2$ for every $k$. If $T_x(0) < T_x(h)$ for some $h$, then $\delta_k(x) \to 1$.

*(c)* If the truth is the strict mode, then
$$\delta_k(x) \leq \sum_{h \neq 0} \left(1 - \left(\sqrt{T_x(0)} - \sqrt{T_x(h)}\right)^2\right)^k .$$

*(d)* If the truth is the strict mode and $h^*$ is a most likely wrong value with $T_x(h^*) > 0$, then $-\tfrac{1}{k}\ln \delta_k(x) \to I_x$, where
$$I_x = -\ln\left(1 - \left(\sqrt{T_x(0)} - \sqrt{T_x(h^*)}\right)^2\right).$$
:::

Part (a) is due to Blum, Luby and Rubinfeld, and (b) to (d) are standard large-deviation facts. Correctability at $x$ is thus a property of one computable distribution, not of the error rate: Section 4 has fields with $\varepsilon = 0.27$ that have uncorrectable inputs and fields with $\varepsilon = 0.75$ that have none. The bound (c) is loose and the rate (d) is approached slowly (Table 1), so we compute the exact multinomial probabilities of (a), and report bounds below an accuracy floor of $10^{-10}$.

## The worst case: one third and one quarter {#sec-worst}

::: theorem
**Theorem 2 (worst-case radius of the two-query plurality corrector).** Let $e: G \to H$ be any error field with error set $E$. For every input $x$ and every $h \neq 0$:

*(i)* $N_0(x) \geq |G| - 2|E|$, that is, $T_x(0) \geq 1 - 2\varepsilon$;

*(ii)* $N_0(x) - N_h(x) \geq |G| - 4|E|$;

*(iii)* if $2h \neq 0$, then $N_0(x) - N_h(x) \geq |G| - 3|E|$.

Consequently every input is correctable when $\varepsilon < 1/4$. If $|H|$ is odd, every input is correctable when $\varepsilon < 1/3$. For $1/4 \leq \varepsilon < 1/3$ the only wrong values that can tie with or beat the truth are elements of order 2.
:::

::: theorem
**Proposition 3 (sharpness).** Let $|G| \geq 2$ and $|H| \geq 2$, and put $\tau = 3$ if $|H|$ is odd and $\tau = 4$ if $|H|$ is even. The smallest number of errors for which some field leaves some input uncorrectable is $\lceil |G|/\tau \rceil$. The smallest number for which some wrong value strictly beats the truth at some input is $\lfloor |G|/\tau \rfloor + 1$. For every $x \neq 0$ there is a field with $\lceil |G|/\tau \rceil$ errors at which $x$ is uncorrectable.
:::

Part (i) is the two-query bound of Blum, Luby and Rubinfeld and (ii) follows from it; part (iii) and Proposition 3 are, to our knowledge, not stated in the literature, though the proof is elementary and they may be folklore. The extremal field has errors *isolated* along the orbit $x, 2x, 3x, \dots$ of the input, all with the *same* wrong value $h$. Each spoils two votes, with offsets $+h$ and $-h$. If $h \neq -h$ these disagree and the truth loses only when $|G| - 2|E| \leq |E|$; if $h = -h$ they agree, and it loses when $|G| - 2|E| \leq 2|E|$. When $\tau$ does not divide $|G|$ the breaking error rate lies slightly above $1/\tau$, for example $321/961 = 0.334$ on $\mathbb{Z}_{31}^2$.

::: box
**Relation to the unique-decoding radius.** The homomorphisms $G \to H$ form an error-correcting code (Grigorescu, Kopparty and Sudan, 2006; Dinur et al., 2008). Two of them agree on at most a fraction $1/p$ of the inputs, $p$ the smallest prime dividing $\gcd(|G|,|H|)$, so a table closer than $(1 - 1/p)/2$ to a homomorphism has a unique nearest one. This *unique-decoding radius* is $1/4$ for $p = 2$ and $1/3$ for $p = 3$, as in Theorem 2, but $0.4$ for $p = 5$ and $0.484$ for $p = 31$. Theorem 2 concerns one decoder, not the code: for odd $|H|$ with $p \geq 5$ its guarantee stops inside the unique-decoding radius, and the fields that defeat it contain no competing homomorphism.
:::

## Incoherent errors: the depolarizing law {#sec-depol}

::: theorem
**Theorem 4 (depolarizing law).** Let the errors $e(x)$, $x \in G$, be independent with $\Pr[e(x) = 0] = 1 - \varepsilon$ and $\Pr[e(x) = h] = \varepsilon/(q-1)$ for every $h \neq 0$, and let $\lambda = 1 - \varepsilon/(1 - 1/q)$. For distinct points $x_1, \dots, x_c$ and signs $s_i = \pm 1$, the sum $S = \sum_i s_i\, e(x_i)$ satisfies
$$\begin{aligned} \Pr[S = 0] &= \dfrac{1}{q} + \left(1 - \dfrac{1}{q}\right)\lambda^c, \\ \Pr[S = h] &= \dfrac{1 - \lambda^c}{q} \quad \text{for every } h \neq 0 . \end{aligned}$$
:::

::: theorem
**Corollary 5 (no threshold short of chance).** For even $c$, $\Pr[S = 0] - \Pr[S = h] = \lambda^c > 0$ whenever $\lambda \neq 0$. In expectation over an incoherent field, the truth is therefore the strict mode of the vote at every error rate except exactly chance, including error rates above chance and $\varepsilon = 1$.
:::

This is not new mathematics: each independent error multiplies the characteristic function of the sum by $\lambda$, and for binary outputs the statement is the piling-up lemma of linear cryptanalysis. We restate it in channel language because it is the reference for trained networks, with $c = 2$ for the vote, $c = 3$ for the linearity test and $c = 4$ for the bilinear vote. It does not contradict coding theory, where beyond the unique-decoding radius one must accept a list of candidates or use advice (Dinur et al., 2008; Hirahara and Shimizu, 2026): an incoherent field is far from every homomorphism in the same structureless way.

**Finite size (heuristic).** On one realised field the truth must beat every wrong value at every input. The gap $N_0(x) - N_h(x)$ has mean $|G|\lambda^2$ and, near chance, standard deviation about $\sqrt{2|G|/q}$, over about $|G|q$ pairs $(x, h)$; treating the gaps as independent Gaussians puts the first failure at
$$\lambda_c^2 \approx 2\sqrt{\frac{\ln(|G|q)}{|G|q}}, \qquad \varepsilon_c = (1 - \lambda_c)\left(1 - \frac{1}{q}\right).$$
This is not proved, but it matches simulation within 0.002 for $p \geq 17$ (Table 1); for the trained addition networks' groups the simulated limits are 0.73 to 0.84 (Table 2).

## Invariance twirl and transitive twirl {#sec-twirls}

Test-time augmentation votes over transformations that keep the answer, such as $(a,b) \mapsto (a+r, b-r)$ for $a + b$: an *invariance twirl*, moving the query within the inputs that share its answer. The self-corrector's shift is a *transitive twirl*: it moves the query anywhere, at the price of a second query that removes the shift.

::: theorem
**Proposition 6 (invariance twirl versus transitive twirl).** Let $f(a,b) = a+b$ on $G = \mathbb{Z}_p^2$.

*(a)* The invariance vote $M(a+r, b-r)$, with $r$ uniform on $\mathbb{Z}_p$, is the value of $M$ at a uniform point of the level set $\{f = a+b\}$. If the error depends only on the answer, $e = \varphi \circ f$, every vote equals $M(a,b)$, and the output error rate is exactly $\varepsilon$ for any number of votes.

*(b)* For the same field the translation vote at $x$ has the channel $T_x(h) = \Pr_s[\varphi(f(x)+s) - \varphi(s) = h]$, $s$ uniform on $\mathbb{Z}_p$: the twirled channel of $\varphi$ on the answer group, which decides correctability as in Proposition 1.

*(c)* For an incoherent field an invariance vote (one query) is correct with probability $1 - \varepsilon$ on average, a translation vote (two queries) with $1/q + (1-1/q)\lambda^2$.
:::

So neither twirl dominates: the invariance twirl is the cheaper one on incoherent errors and useless on answer-dependent ones.

## Estimating the error rate without labels {#sec-labelfree}

The linearity test checks $M(x) + M(y) = M(x+y)$ at random $x, y$, without labels. It is the *self-tester* of Blum, Luby and Rubinfeld, and its pass rate is well understood (Bellare et al., 1996; Ben-Or et al., 2008); we apply it, we do not propose a new estimator.

::: theorem
**Proposition 7 (what the pass rate says).** Let $\pi = \Pr_{x,y}[M(x) + M(y) = M(x+y)]$ for independent uniform $x, y$.

*(a)* (Unconditional.) $1 - \pi \leq 3\,d$, where $d$ is the fraction of inputs on which $M$ differs from any fixed homomorphism. In particular $\varepsilon \geq (1-\pi)/3$.

*(b)* (Incoherent errors.) Under the assumptions of Theorem 4, $\mathbb{E}\,\pi = 1/q + (1-1/q)\lambda^3 + O(1/|G|)$. Inverting, $\hat\lambda = \left((\pi - 1/q)/(1-1/q)\right)^{1/3}$ and $\hat\varepsilon = (1-\hat\lambda)(1-1/q)$.

*(c)* (Blind spot.) $\pi$ depends on $M$ alone. It carries information about the distance of $M$ to the nearest homomorphism, which need not be $f$.
:::

Feeding $\hat\lambda$ into the depolarizing channel and Proposition 1 predicts, without labels, how many votes a network needs.

## Chains and horizon {#sec-chains}

::: theorem
**Proposition 8 (survival of a chain).** A model computes the running sum $s_{t+1} = s_t + a_t$ on $\mathbb{Z}_p$ from a uniform start with independent uniform $a_t$. Let $g(s,a)$ be the probability that the step on $(s,a)$ is correct ($\mathbf{1}[e(s,a) = 0]$ raw, $1 - \delta_k(s,a)$ with $k$ fresh votes), $W[s,s'] = g(s, s'-s)/p$, and $\bar g$ the mean of $g$.

*(a)* The probability that all of $L$ steps are correct is $\tfrac{1}{p}\mathbf{1}^{\top} W^L \mathbf{1}$, and its $L$-th root tends to $\rho(W)$, the largest eigenvalue (Perron root) of $W$.

*(b)* If the row or the column sums of $W$ are constant (for example when $g$ depends only on the answer or only on the state), it is exactly $\bar g^{\,L}$.

*(c)* For independent uniform inputs it would be $\bar g^{\,L}$, with a 50% horizon of $\ln 2/(-\ln \bar g)$ steps.
:::

A constant failure rate per step is thus an assumption: if the raw model errs exactly when the current and next state both lie in a set of 15 of the 31 residues, $1 - \varepsilon = 0.766$ but $\rho(W) = 0.8205$, and 20 steps survive with probability $0.0182$, not $0.0048$.

## How the statements were checked {#sec-checks}

| Statement | Check | Outcome |
|:----|:-------|:--------|
| Prop. 1(a) | exact routine against enumeration and Monte Carlo | agrees to $4 \times 10^{-16}$ |
| Prop. 1(c, d) | six channels, $k \leq 160$ | bound holds but is loose ($q = 31$, $T(0) = 0.3$, 40 votes: exact $3.4 \times 10^{-3}$, bound $3.4 \times 10^{-2}$); near ties converge slowly ($0.45$ at 160 votes) |
| Theorem 2 | all 3,386,884 fields on 23 pairs $(G, H)$ with $\lvert G\rvert \leq 9$ | holds, minimal slack 0 |
| Proposition 3 | the 23 pairs; 70 pairs with $10 \leq \lvert G\rvert \leq 20$, searched by number of errors | as predicted in all 23, and in 63 (ties) and 57 (strict wins) of the 70; the rest unresolved |
| Theorem 4 | 60 cells: $q \in \{2,3,5,31\}$, $c = 2, 3, 4$, 20 fields each | within $9.6 \times 10^{-4}$ at the realised error rate; the three cells with $\lvert z\rvert > 3$ against the nominal rate share one field set with realised rate 0.908 |
| Corollary 5 | $\varepsilon = 1$ on $\lvert G\rvert = 961$ | $q = 3$: every input correctable; $q = 31$: 4.0% (finite size) |
| Finite-size estimate | 24 fields for each of six $p$ from 11 to 61 | within 0.002 of simulation for $p \geq 17$; 0.022 low at $p = 11$ |
| Proposition 6 | $m$ of 31 answers wrong; scattered errors | invariance error exactly $m/31$, translation corrects up to $m = 15$; scattered: invariance cheaper (9 against 14 to 18 queries at $\varepsilon = 0.1$) |
| Proposition 7 | 80 incoherent and 20 coherent fields | RMSE of $\hat\varepsilon$ at most $1.1 \times 10^{-2}$ up to $\varepsilon = 0.85$; coherent: $\hat\varepsilon \leq \varepsilon$ in all 20 |
| Proposition 8 | incoherent field, $k \leq 41$ | decay rate within $10^{-4}$ of $-\ln(1 - \bar\delta_k)$ |

: **Table 1.** How each statement was checked, on synthetic error fields only (`code/theory_checks.py`, `results/theory_checks.json`).

# Same error rate, different fates {#sec-fates}

Five synthetic families on $\mathbb{Z}_{31}^2 \to \mathbb{Z}_{31}$ show the gap between error rate and correctability (Figure 1; closed forms in the appendix). *Scattered values* is the incoherent field. *Offset on a random set* adds one value $h$ on a random set of inputs. *Second homomorphism* replaces $f$ by $g(a,b) = a + 2b$ on a random set of density $\rho$, an error rate of $\rho(1 - 1/q)$. The *band* families add $h$ on a band $\{(a, b) : a < \varepsilon p\}$, with $2h \neq 0$, and with $2h = 0$ on $\mathbb{Z}_{30}$.

![**Figure 1.** Five synthetic error families at the same error rates. **a** Fraction of inputs at which the truth is the strict mode of the twirled channel. **b** Smallest margin over inputs; at or below zero, some input is uncorrectable. Band curves are exact; the random families are means over 8 fields, each point an exact enumeration of all votes. The band with $2h = 0$ is on $\mathbb{Z}_{30}$ with $h = 15$. Dashed lines: $1/4$, $1/3$, $1/2$ and chance. Notice the offset on a random set, which never breaks, against the same offset on a band, which breaks just above $1/3$ ($2h \neq 0$) or $1/4$ ($2h = 0$).](figures/fig_phase_diagram.svg)

Scattered values stay fully correctable up to $\varepsilon = 0.75$ in all 8 fields, near the estimated finite-size limit of 0.781. The offset on a random set never breaks at any of 101 error rates: its wrong votes $\pm h$ each have probability $\varepsilon(1-\varepsilon)$. The same offset on a band breaks on $[11/31, 20/31]$, and with $h = 15$ on $\mathbb{Z}_{30}$ on $[8/30, 22/30]$, while $h = 1$ on that band breaks only on $[1/3, 2/3]$: inputs whose shift exceeds the band width see every error isolated along their orbit, the extremal field of Theorem 2, and the order of the wrong value decides between $1/3$ and $1/4$. A constant offset on a contiguous region is a plausible failure of a learned model, so the worst case is not exotic. The second homomorphism breaks at density $1/2$ (error rate $0.484$), where the corrector switches to $g$; only this family is limited by the code. Near $\varepsilon = 0.4$, three families are fully correctable, one has lost a third of its inputs and one half.

# Trained networks: where coherence shows {#sec-trained}

**The zoo.** All networks are one-hidden-layer perceptrons of width 256 on one-hot inputs, trained full batch with Adam and decoupled weight decay (`code/make_zoo.py`); we store each snapshot's argmax prediction at every input. *Addition* networks learn $a + b \bmod p$, $p \in \{23, 31, 47\}$, with training fractions 0.3, 0.5 and 0.7, four seeds and weight decay 1; 30 log-spaced snapshots per run trace memorisation and the late generalisation known as grokking (Power et al., 2022): 36 runs, 1,080 snapshots, 841 with errors. *Memorisers* learn addition mod 53 without weight decay until the training set is fit, with 10% to 70% of the inputs or 5 of the 53 answers held out: 35 networks whose error set is the hold-out set by construction. The *hidden linear map* $\langle w, x\rangle \bmod 7$ on $\mathbb{Z}_7^4$ has 9 runs (108 snapshots), *multiplication* mod 31 has 6 runs (150 snapshots). Each snapshot is compared with 20 matched *i.i.d. fields* (as many errors, at random positions, with random wrong values) and 20 *shuffles* (its own error values at permuted positions).

## The mean vote sees only histograms {#sec-identity}

::: theorem
**Proposition 9 (the mean is fixed by histograms).** Let $\pi_v$ be the fraction of inputs with $e(x) = v$, so that $\pi_0 = 1 - \varepsilon$, and $\mu_c$ the fraction with $M(x) = c$. Then
$$\begin{aligned} \dfrac{1}{|G|}\sum_{x \in G} T_x(0) &= \sum_{v \in H} \pi_v^2 \\ &\geq (1-\varepsilon)^2 + \dfrac{\varepsilon^2}{q-1} \\ &= \dfrac{1}{q} + \left(1 - \dfrac{1}{q}\right)\lambda^2 , \end{aligned}$$
with equality if and only if the wrong values are equally frequent, and $\frac{1}{|G|}\sum_{x} \Pr_r[M(x+r) = M(r)] = \sum_{c} \mu_c^2$.
:::

*Proof.* $\sum_x N_0(x)$ counts the pairs $(x,r)$ with $e(x+r) = e(r)$; with $y = x + r$ these are the pairs $(y, r)$ with $e(y) = e(r)$, of which there are $\sum_v (|G|\pi_v)^2$. The inequality is Cauchy–Schwarz over the wrong values, whose shares sum to $\varepsilon$, and the last equality is algebra. The same count with $M$ in place of $e$ gives the statement about outputs. $\square$

The mean probability that a vote is correct therefore depends only on how often each error value occurs, not on where the errors are; it differs from the depolarizing law only by the unevenness of the wrong values and a term of order $1/|G|$. Over the 984 networks with errors and a two-query vote, the largest deviation is $2.3 \times 10^{-3}$ and the mean $2.7 \times 10^{-4}$, against $2.1 \times 10^{-4}$ for matched i.i.d. fields, while $(1-\varepsilon)^2$ is 50 to 350 times worse (Figure 2). **This agreement is not evidence of incoherence.** It shows only that wrong answers are spread nearly evenly over the wrong values (effective number over $q - 1$: median 0.93 for addition). Coherence must be read from individual inputs.

![**Figure 2.** Mean vote correctness follows the incoherent law, as Proposition 9 forces. **a** Mean over inputs $x \neq 0$ of $T_x(0)$ against error rate: 841 addition snapshots with errors ($q = 23, 31, 47$; 36 runs) and 108 linear-map snapshots ($q = 7$; 9 runs). Solid: law for $q = 31$ and $7$; dashed: $(1-\varepsilon)^2$. **b** Measured minus law at each snapshot's $q$: at most $2.3 \times 10^{-3}$. This shows that wrong values are evenly spread, not where errors are.](figures/fig_law.svg)

## Coherence at the worst input {#sec-coherence}

Our *coherence ratio* is a network's largest wrong-vote mass, $\max_{x \neq 0,\, h \neq 0} T_x(h)$, divided by its median over the 20 matched i.i.d. fields. For addition snapshots its median is 1.82 (per-run medians 1.11 to 2.37), and it grows with the error rate: 1.00 below $\varepsilon = 0.1$, 1.25 between 0.3 and 0.4, 1.80 between 0.6 and 0.7, then 3.90, 8.16 and 10.04 in the three bins above 0.7. Against shuffles it is 1.00 to 1.03 below $\varepsilon = 0.3$: there the small excess comes from the value histogram, above it from the arrangement of the errors. Linear-map snapshots have a median ratio of 2.42 and exceed all their i.i.d. fields in all 108 cases. The worst-input margin agrees: addition medians 0.204, 0.133 and 0.004 in the bins from 0.4 to 0.7, against 0.218, 0.169 and 0.045 for i.i.d. fields.

A structured error *set* costs nothing by itself: the class hold-out memorisers, whose errors fill five answer classes, have 9.2 times the i.i.d. spread of $T_x(0)$ across inputs, yet a coherence ratio of 1.00 against shuffles and a worst margin of 0.803 against 0.809 for i.i.d. fields. What matters is whether wrong *values* line up under the shifts.

## Where trained networks sit {#sec-where}

| $p$ | unique decoding | fully correctable up to | first uncorrectable at | i.i.d. limit |
|:--:|:--:|:--:|:--:|:--:|
| 23 | 0.478 | 0.527 [0.471, 0.688] | 0.627 [0.584, 0.679] | 0.732 (0.715) |
| 31 | 0.484 | 0.557 [0.471, 0.696] | 0.690 [0.615, 0.724] | 0.779 (0.763) |
| 47 | 0.489 | 0.620 [0.482, 0.705] | 0.726 [0.661, 0.775] | 0.835 (0.822) |

: **Table 2.** Correctability of the 36 addition runs (12 per modulus). "Fully correctable up to": the largest snapshot error rate in a run with every input correctable; "first uncorrectable at": the smallest with an uncorrectable input; per-run median [minimum, maximum]. The two bracket each run's transition. References from Section 3: the worst-case radius is $1/3$ for all three; unique-decoding radius $(1-1/p)/2$; i.i.d. limit, the median over 24 incoherent fields (minimum in parentheses).

In all 36 addition runs every input stays correctable beyond $1/3$, in 33 (11 of 12 per modulus) beyond the unique-decoding radius, and in none up to the i.i.d. median (Table 2, Figure 3). None of the 263 snapshots with errors below the unique-decoding radius has an uncorrectable input; none of the 232 at or above the i.i.d. median is fully correctable. The highest fully correctable snapshot ($\varepsilon = 0.705$) is memorising, right on 98.3% of its training inputs and 0.06% of the rest; 34 of the 35 memorisers are fully correctable. **The error rate does not even order correctability within a run**: in 5 runs, all with training fraction 0.3, a snapshot has an uncorrectable input while one with a higher error rate has none (for example, uncorrectable inputs at $\varepsilon = 0.639$ but none at $0.665$).

![**Figure 3.** Addition networks stay correctable far beyond the worst case but break before incoherent errors would. **a** Fraction of correctable inputs, all 1,080 addition snapshots (36 runs). Dashed: worst case $1/3$; vertical lines: i.i.d. limit per $p$ (0.73, 0.78, 0.84). Every snapshot below 0.584 is fully correctable; beyond the line of its colour, none keeps more than 6% of its inputs correctable. **b** Per run, the largest fully correctable error rate (a lower bound on the transition). Black: medians; dotted: unique-decoding radius; coloured: i.i.d. limit.](figures/fig_correctable.svg)

## How many votes {#sec-votes}

| Network | $\varepsilon$ | $k = 9$ | $17$ | $33$ | $65$ | $129$ | ratio ($k$) |
|:----|--:|--:|--:|--:|--:|--:|--:|
| addition | 0.090 | $9.2 \times 10^{-5}$ | $8.4 \times 10^{-9}$ | ($< 10^{-14}$) | ($< 10^{-29}$) | ($< 10^{-59}$) | 3.7 (17) |
| addition | 0.305 | 0.068 | $4.0 \times 10^{-3}$ | $8.7 \times 10^{-6}$ | ($< 10^{-9}$) | ($< 10^{-19}$) | 2.3 (33) |
| addition | 0.498 | 0.45 | 0.21 | 0.034 | $6.5 \times 10^{-4}$ | $4.4 \times 10^{-7}$ | 53 (129) |
| addition | 0.665 | 0.82 | 0.73 | 0.51 | 0.23 | 0.040 | 4.0 (129) |
| linear map | 0.276 | 0.14 | 0.033 | $2.5 \times 10^{-3}$ | $2.5 \times 10^{-5}$ | $4.1 \times 10^{-9}$ | 142 (65) |
| memoriser | 0.300 | 0.060 | $3.2 \times 10^{-3}$ | $5.2 \times 10^{-6}$ | ($< 10^{-10}$) | ($< 10^{-20}$) | 2.5 (33) |

: **Table 3.** Exact worst-input failure of the $k$-vote corrector for six fully correctable networks chosen by a recorded rule (seed-0 snapshot nearest a target error rate; addition $p = 47$, memoriser $p = 53$). Parentheses: Chernoff upper bound, where the exact value is below $10^{-10}$. Ratio: exact failure over the prediction from the error rate alone, at the largest $k$ with an exact value (in brackets).

**One vote is always worse than the raw network**, because a vote uses two queries: mean failure 0.171, 0.515, 0.742 and 0.877 at $\varepsilon = 0.090$, 0.305, 0.498 and 0.665 (Table 3, Figure 4). Three votes are worse too, except at $\varepsilon = 0.09$; beyond that, failure falls exponentially. The network with 50.2% accuracy fails on its worst input with probability $4.4 \times 10^{-7}$ after 129 votes, on average with $2.8 \times 10^{-8}$.

**Predictions from the error rate alone are optimistic in the tail.** The depolarizing channel at the network's $\varepsilon$ predicts the mean at few votes (0.397 against 0.401 at $k = 9$, $\varepsilon = 0.498$) but underestimates the worst input more as $k$ grows: 53-fold at $k = 129$, and 142-fold at $k = 65$ for the linear map; a worst-input Chernoff bound of $10^{-6}$ needs 181 votes against 113 predicted. Part of the gap is finite size: matched i.i.d. fields reach a median 0.72 of the predicted worst-input exponent, fully correctable addition snapshots 0.60. Real votes agree with the exact values (70 comparisons, $|z| \leq 2.56$).

![**Figure 4.** Failure against the number of votes $k$ for four addition networks ($p = 47$, raw error rates 0.09 to 0.66; squares: raw). **a** Mean over inputs. **b** Worst input. Thick: exact; thin: predicted from the error rate alone. One vote is worse than raw, and so are three except at $\varepsilon = 0.09$; then failure falls exponentially. The thin lines match the mean but fall below the worst input as $k$ grows, 53-fold at $k = 129$ for $\varepsilon = 0.50$. Values below $10^{-10}$ are omitted.](figures/fig_votes.svg)

## The mechanism: the zero vote {#sec-mechanism}

The wrong value that competes with the truth is almost always the *zero vote*, $M(x+r) = M(r)$, with offset $h = -f(x)$. It carries the largest wrong-vote mass in 83% of the addition snapshots with errors and 99.0% of those with $\varepsilon \geq 0.4$ (chance: about $1/(q-1)$), and in 367 of the 378 snapshots with an uncorrectable input it ties or beats the truth at every uncorrectable input with $f(x) \neq 0$.

Its source is that the networks over-predict a few output classes. By Proposition 9 the mean zero-vote mass is the output collision $\sum_c \mu_c^2$, which is $1/q$ for balanced outputs. The lowest-error snapshot with an uncorrectable input ($p = 23$, $\varepsilon = 0.584$) answers 0 on 62.5% of the inputs it gets wrong; its output collision is 4.36 times $1/q$, and the zero vote ties or beats the truth at all 290 of its uncorrectable inputs. Such a network is partly close to a constant function, and since a vote is unchanged when a constant is added to $M$, the corrector reads a constant table as the zero homomorphism. The wrong values $e(x) = c - f(x)$ are still evenly spread in histogram, which is why the mean cannot see them.

**A two-histogram criterion** follows: predict that most inputs are correctable if and only if $\sum_v \pi_v^2 > \sum_c \mu_c^2$, mean truth mass against mean zero-vote mass. It is right for 839 of 841 addition snapshots, all 35 memorisers and 100 of 108 linear-map snapshots, and no snapshot predicted to fail is fully correctable; but it concerns the average input, and 101 addition snapshots pass it with some input uncorrectable. The output collision needs no labels. For the linear map the mechanism is less complete: the zero vote is the largest competitor in all 108 snapshots but beats the truth at only a median 59% of uncorrectable inputs.

# Bias-subtracted voting {#sec-debias}

If the two outputs of a vote were independent draws from the output histogram $\mu$, the vote would equal $v$ with probability $A(v) = \sum_c \mu_c\, \mu_{c+v}$, computable without labels (at $v = 0$, the output collision of Proposition 9). The *bias-subtracted* corrector returns $\operatorname{argmax}_v\, [N_v/k - A(v)]$, with $N_v$ the number of votes equal to $v$, so that $x$ is correctable if and only if $T_x(0) - A(f(x)) > \max_{h \neq 0}\, [T_x(h) - A(f(x)+h)]$ (for multiplication the background is $A * A$).

**On addition networks it helps** (Figure 5). Fully correctable snapshots rise from 463 to 521 of 841; none loses that status. The largest fully correctable error rate of a run (Table 2) rises in 11, 9 and 8 of the 12 runs for $p = 23$, 31 and 47 and falls in none, with medians 0.675, 0.686 and 0.685 instead of 0.527, 0.557 and 0.620. The i.i.d. limits barely move under the rule (0.732, 0.782, 0.835), so it closes 72%, 58% and 30% of the gap to them; what remains grows with $p$. With $\mu$ estimated from 1,000 sampled outputs the medians move by at most 0.005, and no run falls below the plurality. At finite $k$, no input of the four addition networks of Table 3 can do worse for any $k \leq 129$, and mean failure falls by 8% to 45% (from 0.021 to 0.015 at $\varepsilon = 0.498$ and 33 votes). The lowest-error snapshot with uncorrectable inputs (Section 5; $p = 23$, $\varepsilon = 0.584$) becomes fully correctable, with mean failure 0.0054 instead of 0.50 at 129 votes.

**Where it does nothing or harms.** The rule sees errors only through the output histogram. Linear-map outputs are nearly balanced (median $q \sum_c \mu_c^2$ of 1.02 to 1.11), so the correction exceeds the deficit at only a median 5% to 9% of uncorrectable inputs; no run's threshold changes, and 6,112 inputs gained are offset by 5,940 lost. No multiplication threshold moves either, though four snapshots with $0.55 \leq \varepsilon \leq 0.64$ gain many inputs. The four tested synthetic families of Section 4 keep their thresholds; a new one, collapse to 0 on a random set, stays fully correctable up to density 0.89 instead of 0.49. In 176 addition snapshots, all with $\varepsilon \geq 0.70$, some inputs lose correctability (2,690, against 124,654 gained), and 25 near-chance snapshots end with fewer correctable inputs. At finite $k$ the rule over-penalises the answer 0: in the snapshot above and in one with $\varepsilon = 0.743$, every input with $f(x) = 0$, $x \neq 0$, fails more often for $9 \leq k \leq 65$ (on average 0.29 instead of 0.047 at $\varepsilon = 0.743$, $k = 33$), although all stay correctable as $k \to \infty$. A constructed network answering 0 on the band $a < m$ of $\mathbb{Z}_{31}^2$ is fully correctable by plurality for $m = 13$ to 15 but not under the rule.

The rule is a heuristic read off the zero-vote mechanism, not a theorem: it has no worst-case guarantee and addresses only output collapse.

![**Figure 5.** Bias-subtracted voting on the addition networks (`code/exp_debias.py`). **a** Fraction of inputs correctable with many votes, for the 841 addition snapshots with errors, under the plurality (blue) and under the rule $\operatorname{argmax}_v\, [N_v/k - A(v)]$ with the label-free background $A(v) = \sum_c \mu_c \mu_{c+v}$ of the output histogram (orange). Dots: snapshots; lines: medians in bins of width 0.05. The two rules agree below $\varepsilon = 0.5$; the mean fraction rises from 0.41 to 0.95 for $0.7 \leq \varepsilon < 0.8$ and from 0.03 to 0.49 for $0.8 \leq \varepsilon < 0.9$. **b** Per run, the largest snapshot error rate with every input correctable, under each rule; thin lines join the two values of a run (12 runs per modulus). Horizontal lines: median over 24 i.i.d. fields (0.732, 0.779, 0.835). No run gets worse and 28 of 36 improve; the medians rise from 0.53, 0.56 and 0.62 to 0.67, 0.69 and 0.68.](figures/fig_debias.svg)

# Twirls and baselines at equal query budget {#sec-baselines}

On the memorisers, whose logits are stored, we compare methods at equal numbers $Q$ of queries per answer: same-input *sampling* (plurality of $Q$ samples from the softmax), a five-network *ensemble* trained on the same split, the *invariance twirl* ($Q$ orbit votes $M(a+r, b-r)$), the *translation twirl* ($Q/2$ self-corrector votes) and a *concatenated twirl* that replaces each query of a translation vote by a plurality of 3 orbit votes. All are computed exactly, ties fail, and each configuration has 7 networks (Table 4, Figure 6).

| Method | queries per vote | scattered, $0.30$ | scattered, $0.50$ | by answer, $0.094$ |
|:----|:--:|:--:|:--:|:--:|
| Same-input sampling | 1 | never (0.300) | never (0.500) | never (0.094) |
| Five-network ensemble | 5 | never (0.300) | never (0.500) | never (0.094) |
| Invariance twirl | 1 | 18 / 34 | 34 / 130 | never (0.094) |
| Translation twirl | 2 | 66 / 130 | 130 / 258 | 18 / 34 |
| Concatenated twirl | 6 | 66 / 126 | 258 / not reached | 66 / 126 |

: **Table 4.** Smallest budget $Q$ per answer at which the mean error reaches $10^{-3}$ / $10^{-6}$, on the grid $Q = 1, 2, 4, 6, 10, 18, 34, 66, 130, 258$ (concatenated: 6, 18, 30, 66, 126, 258), identical for all 7 networks of a configuration; "never": stuck at the value in parentheses. Columns: memorisers for addition mod 53 with 30% or 50% of the inputs held out (scattered errors, $\varepsilon = 0.30$ and $0.50$) or 5 answer classes held out (answer-dependent errors, $\varepsilon = 0.094$).

**Re-sampling the same input gives nothing.** Sampling converges to the argmax error, is worse at $Q \leq 2$, and gains at most $4.3 \times 10^{-5}$. The ensemble equals the single network to all digits, but nearly by construction: the memorisers err on the same hold-out set, so this says nothing about ensembles in general. **The twirls split as Proposition 6 predicts**: on scattered errors the invariance twirl needs about a quarter of the queries; on answer-dependent errors it stays at the plain error at every budget, while the translation twirl reaches $9.2 \times 10^{-9}$ at $Q = 34$. **On organic errors the picture is mixed.** On four addition snapshots ($p = 47$) the invariance twirl wins at $\varepsilon = 0.09$ and $0.50$, but at $\varepsilon = 0.30$ the translation twirl is 290 times better at $Q = 66$, because one answer class has 78.7% of its inputs wrong, and at $\varepsilon = 0.645$ the invariance twirl wins on the mean but loses on the worst input. **The concatenated twirl does not pay**: it is worse than the better pure twirl at every matched budget (only 3 inner votes were tried).

![**Figure 6.** Methods at equal query budget on two memorisers for addition mod 53: exact mean error over all 2,809 inputs against queries per answer $Q$. **a** Scattered errors ($\varepsilon = 0.30$): the invariance twirl reaches $2.7 \times 10^{-7}$ at $Q = 34$; the translation twirl needs about four times the budget. **b** Answer-dependent errors ($\varepsilon = 0.094$): the invariance twirl stays at the plain error; only the translation twirl corrects ($1.0 \times 10^{-4}$ at $Q = 18$). Sampling converges to the plain error and the ensemble (triangle) equals it. Small budgets are non-monotone because two votes can tie.](figures/fig_twirls.svg)

# Other tasks: multiplication without multiplying and a hidden linear map {#sec-other}

**Multiplication.** The four-query vote corrects $ab \bmod 31$ with additions and subtractions only (Figure 7). Proposition 9 does not cover $c = 4$, so here the law is a real test of the mean: for the 55 snapshots with $0.02 \leq \varepsilon \leq 0.7$ the per-vote correctness on inputs with $a, b \neq 0$ follows $1/q + (1-1/q)\lambda^4$ with root-mean-square residual 0.0060 (i.i.d. fields: 0.0016). All 58 snapshots with errors and $\varepsilon \leq 0.515$ are fully correctable; per run the transition lies between medians of 0.460 and 0.627 (6 runs). **This does not support the thesis**: matched i.i.d. fields stay fully correctable up to a median 0.531, so the threshold of trained networks is the incoherent finite-size limit. Coherence appears only beyond it, as an abrupt collapse (correctable fraction 0.036 at $\varepsilon = 0.608$, against 0.753 for i.i.d. fields), and in the 35 earliest snapshots ($\varepsilon > 0.8$), whose votes are right *less often than chance* (0.0032 to 0.0314 against $1/q = 0.0323$): a near-constant network makes the vote 0, never the product of non-zero inputs. Correctable is not corrected: at $\varepsilon = 0.515$, 129 votes (516 queries) still fail with mean probability 0.41.

**Hidden linear map.** For $\langle w, x\rangle \bmod 7$ on $\mathbb{Z}_7^4$ the corrector knows only that $f$ is additive. Only the 3 runs with training fraction 0.4 learn; they lose all-input correctability between $\varepsilon = 0.458$ and $0.573$, with no snapshot in between, while matched i.i.d. fields keep it to a median 0.677 [0.665, 0.690]. This supports the thesis but rests on 3 runs. Self-correcting the four unit vectors with 129 votes each (1,032 queries, for 2,401 inputs) recovers $w$ with probability at least 0.99 for exactly the 15 snapshots with $\varepsilon \leq 0.363$, and at most 0.029 for all 90 with $\varepsilon \geq 0.573$. Recovery shows that a network has learned the map, not that a poorly trained one hides it.

![**Figure 7.** Multiplication mod 31 with an adding-only four-query vote (150 snapshots, 6 runs) and the hidden linear map on $\mathbb{Z}_7^4$ with the two-query vote (108 snapshots, 9 runs). **a** Mean per-vote correctness on non-trivial inputs, with the laws for $c = 4$, $q = 31$ and $c = 2$, $q = 7$. For $c = 2$ the agreement is forced (Proposition 9); for $c = 4$ it is a test, which the earliest multiplication snapshots fail by falling below chance. **b** Fraction of correctable inputs; grey: mean of 24 i.i.d. fields. Multiplication follows the i.i.d. curve to its limit, then collapses faster; the linear map breaks earlier.](figures/fig_tasks.svg)

# Long chains {#sec-long}

Four fully correctable addition snapshots ($p = 47$, $\varepsilon = 0.050$ to $0.616$) compute the running sum of Proposition 8, raw or with $k$ votes per step. Table 5 gives the exact 50% horizon $T_{50} = \ln 2 / (-\ln \rho(W))$; below 1, a single step fails more often than not.

| $\varepsilon$ | raw | $k = 1$ | 3 | 5 | 9 | 17 | 33 | 65 |
|:--:|--:|--:|--:|--:|--:|--:|--:|--:|
| 0.050 | 13.5 | 6.8 | 25.9 | 710 | $3.6 \times 10^{5}$ | $1.6 \times 10^{11}{}^{*}$ | $1.5 \times 10^{22}{}^{*}$ | $2.4 \times 10^{43}{}^{*}$ |
| 0.220 | 2.8 | 1.4 | 1.7 | 6.9 | 60 | 6,386 | $9.9 \times 10^{7}$ | $1.9 \times 10^{16}{}^{*}$ |
| 0.419 | 1.3 | 0.65 | 0.53 | 1.1 | 2.7 | 13.1 | 369 | $3.2 \times 10^{5}$ |
| 0.616 | 0.72 | 0.37 | 0.26 | 0.39 | 0.57 | 0.88 | 1.9 | 6.1 |

: **Table 5.** Exact 50% horizon (steps) of a chained sum mod 47, raw and with $k$ votes ($2k$ queries) per step. Asterisks: per-step failure below $10^{-9}$; midpoint of a two-sided bound (e.g. $[1.5, 1.8] \times 10^{11}$ at $\varepsilon = 0.05$, $k = 17$). Only horizons up to $10^4$ steps were also simulated.

The horizon grows exponentially with $k$ (Figure 8), from 13.5 steps raw to $3.6 \times 10^5$ with 9 votes at $\varepsilon = 0.05$. **One vote halves it** (ratio 0.50 to 0.52), three votes are still worse than raw except at $\varepsilon = 0.05$, and at $\varepsilon = 0.62$ even 65 votes (130 queries per step) give 6 steps. **The prediction from the error rate alone is optimistic, increasingly with $k$**: within 1.3% up to $k = 3$, too long at every $k \geq 5$, and at $k = 65$ too long by factors of $10^4$, 11, 3.2 and 3.2 for the four networks (exact over predicted: $1.0 \times 10^{-4}$, 0.087, 0.32, 0.31). The Perron correction of Proposition 8, by contrast, changes these horizons by under 1% ($(1 - \rho)$ over the mean failure lies in $[0.9974, 1.0073]$). Real-vote simulations agree with the exact survival curves (89 checkpoints, $|z| \leq 2.80$). Voting until the leader is $m$ votes ahead needs 1.9 to 3.3 times fewer votes than a fixed $k$ at equal failure (10 settings).

![**Figure 8.** Horizon of a chained sum mod 47 computed by four addition networks ($\varepsilon = 0.05$ to $0.62$), raw or with $k$ votes per step. **a** Steps $T_{50}$ until half of the chains have erred. Solid: exact (Perron root from the exact channels); dots: real-vote simulation (4,000 chains; 2,000 for $\varepsilon = 0.22$, $k = 17$); thin dashed: error-rate-only prediction. **b** Exact over predicted horizon: below 1 from $k = 5$ on, down to $10^{-4}$ at $\varepsilon = 0.05$, $k = 65$. The $k$ axis is a doubling grid.](figures/fig_horizon.svg)

# Label-free evaluation {#sec-eval}

The pass rate $\pi$ of the linearity test costs three queries per sample and needs no labels; we computed it exactly for 1,223 networks (Figure 9).

**Below $\varepsilon = 0.6$ the estimate is accurate.** The mean absolute error of $\hat\varepsilon$ is 0.0021 for the 364 addition snapshots with $0 < \varepsilon \leq 0.6$ and 0.0004 for the memorisers, although their error set is the hold-out mask; 1,000 random triples give root-mean-square errors of 0.004 to 0.024 on five representative networks. Below $\varepsilon \approx 0.5$ these errors look incoherent to the three-query test: coherence lives in the tails.

**Above about 0.7 the estimate is unusable.** Errors range from $-0.83$ to $+0.45$; 196 networks get $\hat\varepsilon$ above chance, and early snapshots nearer to another homomorphism, usually the zero map, are badly underestimated (59 addition and 60 linear-map snapshots; one with $\varepsilon = 0.905$ has $\hat\varepsilon = 0.076$). The bound $\varepsilon \geq (1 - \pi)/3$ held for all 1,223 networks but is loose.

**The vote prediction is never pessimistic and often optimistic.** For 413 networks with $0 < \varepsilon \leq 0.6$, the votes predicted from $\pi$ for a mean failure of $10^{-3}$ were exact for 199 and too few for 210 (51%; largest shortfall 58 votes), with optimism rising from 2 of 77 addition snapshots below $\varepsilon = 0.1$ to 57 of 58 between 0.5 and 0.6. The true $\varepsilon$ does no better (205 optimistic): the shortfall lies in the shape of the channel, not in the estimate.

**The vote margin is not a safe confidence signal under coherent errors.** With 65 real votes, the margin between the two leading values separates right from wrong outputs on the two fully correctable addition snapshots with the highest error rates below the first uncorrectable one (area under the ROC curve 0.975 and 0.964; 0.04% and 0.20% wrong among outputs with margin at least 5), but not on the snapshot with 290 uncorrectable inputs (area 0.62; 44% wrong at margin 5, 24% at margin 10).

**Baselines and fixes have limited reach.** Two-network disagreement (Jiang et al., 2022) underestimates the memorisers' error rate at 70% hold-out (0.466 against 0.700), because wrong networks share their wrong answer on a third of the inputs where both err. Reading the homomorphism off self-corrected generators names the task below $\varepsilon = 0.584$ (addition) and 0.573 (linear map), but finds a different nearest homomorphism in only 22 of 59 and 7 of 60 cases.

![**Figure 9.** Evaluation without labels. **a** Error rate estimated from the exact pass rate of the linearity test against the true one, for 1,080 addition and 108 linear-map snapshots: accurate below about 0.6, failing both ways above 0.7 (too high where the pass rate is below $1/q$, too low near another homomorphism). **b** Votes for mean failure $10^{-3}$, predicted from the pass rate against needed on the exact channel, for 413 networks with $0 < \varepsilon \leq 0.6$. No point lies below the diagonal; the top row holds 12 networks needing more than 149 votes. Points jittered by about 2%.](figures/fig_labelfree.svg)

# Related work {#sec-related}

**Self-testing, self-correcting and homomorphism codes.** Blum, Luby and Rubinfeld (1993) introduced the linearity test and the corrector used here; the random self-reducibility of low-degree polynomials is attributed to Lipton (1991) and to Blum, Luby and Rubinfeld, and Rubinfeld and Sudan (1996) extended testing to polynomials. Bellare et al. (1996) and Ben-Or et al. (2008) relate the pass rate to the distance from the nearest homomorphism. Grigorescu, Kopparty and Sudan (2006) and Dinur et al. (2008) study homomorphism codes under adversarial errors, including list decoding; Amireddy et al. (2024) correct linear functions on the Boolean cube up to nearly a $1/4$ fraction of errors; Hirahara and Shimizu (2026), in a technical report, give random self-reductions for all linear problems when the program is right on only a small fraction of inputs. These are worst-case analyses. Lecture notes define the corrector by plurality (Rubinfeld, lecture notes; Dinur, lecture notes); we did not find the $1/3$ versus $1/4$ thresholds stated.

**Random self-reducibility and learned models.** Goldwasser et al. (2025) use ideas from random self-reducibility to remove planted backdoors without detecting them, when the ground truth is close to a linear, polynomial or Fourier-heavy function; their adversary is a malicious trainer, in real-valued regression, and to our reading of the abstract and section list they neither characterise correctability per input nor measure honestly trained networks. Erata et al. (2026) learn randomized self-reductions for numerical functions; to our reading of the abstract, they discover the identity, whereas we take it as given. Amit et al. (2024) seek per-input trust through models that output proofs for a verifier.

**Voting and correlated errors.** Self-consistency (Wang et al., 2023) and deep ensembles (Lakshminarayanan, Pritzel and Blundell, 2017) vote over samples or models. Liu (2026) bounds majority-vote accuracy over repeated language-model calls by the first two moments of per-example correctness; Brilliant (2026), in a preprint that is not peer reviewed, argues that correlated errors limit self-correction in language models; Cordero-Encinar and Duncan (2025) certify that a vote equals the modal answer. Meyerson et al. (2025) complete a million-step task by voting at every step, and Mehta (2026) uses agreement across reruns of an agent as an uncertainty signal. All of these resample the same input, so a stable error survives (Section 7); a random self-reduction moves the query, and the limit becomes coherence under shifts.

**Invariance and twirling.** Test-time augmentation (Kimura, 2024), group averaging (Foit, Hogg and Villar, 2025) and randomized smoothing (Cohen, Rosenfeld and Kolter, 2019) are invariance twirls in our terms. Twirling over random unitaries reduces quantum noise to one fidelity parameter (Emerson, Alicki and Życzkowski, 2005), and randomized compiling turns coherent into stochastic noise (Wallman and Emerson, 2016); we borrow only the vocabulary.

**Evaluation, grokking and horizons.** Jiang et al. (2022) estimate test error from the disagreement of two networks, and Li et al. (2019) train for consistency under logical relations. Our tasks follow Power et al. (2022); Nanda et al. (2023) reverse-engineered the algorithm small transformers learn for modular addition, and Kvinge et al. (2026) probe which group-theoretic structures such networks capture; we study the errors that remain. Kwa et al. (2025) measure the length of tasks agents complete with 50% success, and Ord (2025) models such data with a constant failure rate per unit of length; Section 9 shows how far a rate predicted from the error rate alone can be off.

# Discussion {#sec-discussion}

**What the results say.** For voting over a random self-reduction, a trained network's error rate is a poor guide in both directions. Against the worst case it is too pessimistic: every addition run stays correctable past $1/3$, most past the unique-decoding radius, and a network right on half of its inputs is repaired on its worst input to a failure below $10^{-6}$. Against incoherent noise it is too optimistic: no addition snapshot at the incoherent limit is fully correctable, and error-rate-only predictions of votes and horizons are optimistic in the tail, for horizons by up to four orders of magnitude. Within a run it does not even order correctability. What decides is how the wrong values line up under shifts, which the twirled channel records and input averages cannot see.

**The coherence is simple.** Its main form here is output collapse: a network over-predicts a few classes, acts on part of its domain like a constant function, and the corrector, which sees only differences, reads that as the zero homomorphism. This is invisible to the mean vote correctness and, below error rate 0.6, to the linearity test, but visible in the output histogram, without labels. Subtracting the background this histogram predicts repairs much of the collapse in addition networks (Section 6), but it is a heuristic aimed at this one mechanism: it cannot see coherent errors that leave the outputs balanced, as in the linear map, and at finite vote counts it can over-penalise the answer 0.

**What would have to hold beyond toy tasks.** The target needs a random self-reduction, which linear and low-degree maps have and some numerical functions can be given (Erata et al., 2026), but most tasks lack. The shifted queries must be inputs on which the model is as reliable as on the original; here the domains are uniform, whereas for natural data a random shift leaves the data distribution. And the corrector must beat using the given structure directly, which here it does not (Section 13). By analogy only, the distinction between errors that average out under a randomisation and errors that line up with it may help in thinking about voting in language models and agents; nothing here tests that.

**Open questions.** Which training dynamics cause output collapse, and does a penalty on the output collision remove it? Do correctors with more queries have sharp worst-case thresholds? Can the coherence ratio be estimated from outputs alone?

# Limitations and what is not shown {#sec-limits}

**Toy scale, exact tasks.** Groups have at most 2,809 elements and outputs at most 53 classes, and the tasks are exact algebraic maps. Exact enumeration is the point of the design, but nothing here shows how the measurements change with scale.

**The corrector is given the group law.** For an exact homomorphism a few corrected generator values determine the whole function (Section 8 recovers the linear map from four), so there is no practical gain over using the structure directly. The experiments measure the structure of errors; they do not offer a useful algorithm.

**One architecture, one recipe.** All networks are one-hidden-layer perceptrons on one-hot inputs, trained full batch with Adam, and every family with weight decay uses the same value, 1. Other architectures and regularisers may produce differently structured errors, and the zero-vote mechanism may be specific to this setting.

**Correlated snapshots, few runs.** The run is the unit: 36 addition, 9 linear-map and 6 multiplication runs. Only 3 linear-map runs learn the task, so the linear-map threshold rests on 3 runs with no snapshot between 0.458 and 0.573. Per-run thresholds are brackets because snapshots are discrete, and correlations pooled over snapshots are descriptive. The memorisers' error set is the hold-out mask by construction, which makes the ensemble baseline nearly uninformative.

**Heuristics and computed quantities.** The finite-size limit is a heuristic checked by simulation, not proved. Failures below $10^{-10}$ are bounds. Horizons were simulated only up to $10^4$ steps; longer ones are computed from the transfer matrix, and those beyond about $10^9$ steps from a two-sided bound whose lower side uses the standard negative association of multinomial counts. The search for the votes needed (Section 10) assumes that failure stays below the target once there, checked in full on 43 of 413 networks. The exhaustive checks of Theorem 2 and Proposition 3 cover groups of at most 20 elements, with some pairs unresolved, and the remark after the proof of Theorem 2 is not machine-checked. The bias-subtracted rule (Section 6) was compared only with the plurality, not with other label-free fixes, and its finite-vote behaviour was computed for six networks and with the exact output histogram only.

**Limited search for prior work.** arXiv, Semantic Scholar, DBLP, OpenReview, ECCC and Crossref were unreachable from the build machine, so prior work was found by web search only; the two closest papers (Goldwasser et al., 2025; Erata et al., 2026) were read only as abstracts, and six reference entries are marked as not checked against the source. Every novelty statement is therefore "to our knowledge".

**Authorship and verification.** This paper was conceived, implemented, run and written by an AI research agent (Claude, built by Anthropic) working autonomously in a single session at the request of Abafa Mukhamedov. The proofs were checked by exhaustive enumeration on small groups and by independent AI reviewers, but no human has verified the proofs, the code or the text. It is not peer reviewed.

# Reproducibility {#sec-repro}

Everything ran on a 4-core CPU under Linux with Python 3.13.18, NumPy 2.5.3, SciPy 1.18.1, Matplotlib 3.11.2 and pandoc 3.1.3 (the PDF also needs Node with Playwright). From the paper directory, in this order:

```
python3 code/core.py --selftest       # self-tests, about 6 s
python3 code/make_zoo.py              # zoo/ and cache/, 136 s, 2 processes
python3 code/zoo_summary.py           # 11 s
python3 code/theory_checks.py         # Sections 3-4, 47 s, 2 processes
export OMP_NUM_THREADS=1              # for the six experiment scripts
python3 code/exp_channels.py          # Section 5, 310 s
python3 code/exp_twirls.py            # Section 7, 199 s
python3 code/exp_tasks.py             # Section 8, 38 s
python3 code/exp_labelfree.py         # Section 10, 273 s
python3 code/exp_horizon.py           # Section 9, 116 s
python3 code/exp_debias.py            # Section 6, 464 s
python3 build.py                      # index.html and paper.pdf
```

Each script writes one JSON file in `results/` and its figures; every number in the text is read from those files, and figures can be redrawn from the JSON alone (`--figs-only` or `--figure-only`). The tables in `zoo/` are committed but the logits in `cache/` are not, so `make_zoo.py` must run before `exp_twirls.py`. `exp_channels.py` reads `results/theory_checks.json`, and `exp_debias.py` reads the results of `theory_checks.py`, `exp_channels.py` and `exp_tasks.py`; `exp_tasks.py` imports code from `exp_twirls.py`, and `exp_horizon.py` from `exp_labelfree.py`. All seeds are fixed and recorded in the JSON files.

Determinism checks actually done: the zoo was built twice with identical array contents; `theory_checks.py`, `exp_channels.py`, `exp_twirls.py`, `exp_horizon.py` and `exp_debias.py` were each run twice with identical results apart from timings; the random-number-dependent results of `exp_labelfree.py` agreed across two runs. `exp_tasks.py` was not run twice for this purpose, and `results/exp_labelfree.json` predates two cosmetic edits to its script (its figure was redrawn from the JSON). Identical tables are expected only on the same NumPy and BLAS build, which is why they are committed.

# Proofs {.unnumbered #sec-proofs}

Throughout, $N_h(x) = |G|\,T_x(h)$ is the number of shifts $r$ with $D_x(r) = h$.

## Proof of Proposition 1 {.unnumbered}

*(a)* Since $f$ is a homomorphism, $V_r(x) = f(x+r) + e(x+r) - f(r) - e(r)$, which is $f(x) + D_x(r)$. For uniform $r$ the offset $D_x(r)$ has distribution $T_x$ by definition, and independent shifts give independent offsets, so the counts are multinomial. The plurality returns $f(x)$ exactly when $N_0 > N_h$ for all $h \neq 0$.

*(b)* By the law of large numbers $N_h/k \to T_x(h)$ almost surely for every $h$. If $T_x(0) > T_x(h)$ for all $h \neq 0$, then almost surely $N_0 > \max_{h \neq 0} N_h$ for all large $k$, so $\delta_k(x) \to 0$. If $T_x(0) < T_x(h)$ for some $h$, then $\Pr[N_h > N_0] \to 1$ and $\delta_k(x) \to 1$. If $T_x(0) = T_x(h)$ for some $h \neq 0$, the pair $(N_0, N_h)$ is exchangeable, so $\Pr[N_h \geq N_0] = \Pr[N_0 \geq N_h]$. The two events cover the sample space, so each has probability at least $1/2$, and the first implies failure.

*(c)* Write $t_0 = T_x(0)$ and $t_h = T_x(h) < t_0$. Failure implies $N_h \geq N_0$ for some $h \neq 0$. The difference $N_h - N_0$ is a sum of $k$ independent steps equal to $+1$, $-1$, $0$ with probabilities $t_h$, $t_0$, $1 - t_0 - t_h$. For every $s \geq 1$, Markov's inequality gives
$$\begin{aligned} \Pr[N_h \geq N_0] &\leq \mathbb{E}\left[s^{N_h - N_0}\right] \\ &= \left(1 - t_0 - t_h + s\,t_h + t_0/s\right)^k . \end{aligned}$$
If $t_h > 0$, the choice $s = \sqrt{t_0/t_h} > 1$ turns the right-hand side into $(1 - (\sqrt{t_0} - \sqrt{t_h})^2)^k$. If $t_h = 0$ the event is $\{N_0 = 0\}$, of probability $(1-t_0)^k$, which is the same expression. Summing over $h \neq 0$ gives the bound. The requirement $s \geq 1$ is where $t_h < t_0$ is used.

*(d)* Let $\mu_h = 1 - (\sqrt{t_0} - \sqrt{t_h})^2$, which increases with $t_h$ on $[0, t_0]$, and $\mu = \mu_{h^*}$. By (c), $\delta_k(x) \leq (q-1)\mu^k$, so $\liminf -\tfrac1k \ln\delta_k(x) \geq -\ln\mu = I_x$. For the other direction, $\delta_k(x) \geq \Pr[S_k \geq 0]$ with $S_k = N_{h^*} - N_0$. Let $s = \sqrt{t_0/t_{h^*}}$ and define a new probability $\tilde{\Pr}$ by the density $s^{S_k}/\mu^k$. Under $\tilde{\Pr}$ the steps of $S_k$ are still independent and equal $+1$ and $-1$ with the same probability $a = \sqrt{t_0 t_{h^*}}/\mu > 0$ each. Therefore
$$\begin{aligned} \Pr[S_k \geq 0] &= \mu^k \sum_{j \geq 0} \tilde{\Pr}[S_k = j]\, s^{-j} \\ &\geq \mu^k\, s^{-1}\, \tilde{\Pr}\left[S_k \in \{0, 1\}\right]. \end{aligned}$$
For a symmetric walk with steps in $\{-1, 0, 1\}$ the local limit theorem gives $\tilde{\Pr}[S_k \in \{0,1\}] \geq c/\sqrt{k}$ for some $c > 0$ and all $k \geq 1$. (Two values are used so that the argument also covers $a = 1/2$, where $S_k$ has the parity of $k$.) Hence $\delta_k(x) \geq c\, s^{-1} k^{-1/2} \mu^k$ and $\limsup -\tfrac1k\ln\delta_k(x) \leq I_x$. $\square$

## Proof of Theorem 2 {.unnumbered}

For $x = 0$ all offsets are zero and the claims are trivial. Let $x \neq 0$ have order $m \geq 2$. Translation by $x$ partitions $G$ into $|G|/m$ orbits, each a cycle $r, r+x, \dots, r+(m-1)x$. Fix one cycle, write $e_i = e(r + ix)$ for $i \in \mathbb{Z}_m$ and $d_i = e_{i+1} - e_i$; the $d_i$ are the $m$ values of $D_x$ on this orbit. Let $a$ be the number of error points on the cycle, and let $n_0$ and $n_h$ be the numbers of $i$ with $d_i = 0$ and with $d_i = h$. We show
$$\begin{aligned} n_0 &\geq m - 2a, \\ n_0 - n_h &\geq m - 4a, \\ n_0 - n_h &\geq m - 3a \ \text{ if } 2h \neq 0 . \end{aligned}$$
Summing over the orbits gives (i), (ii) and (iii).

If $a = 0$ then $n_0 = m$ and $n_h = 0$. If $a = m$ then $n_0 \geq 0 \geq m - 2a$ and $n_0 - n_h \geq -m \geq m - 3a$.

Let $0 < a < m$. The error points split into $R \geq 1$ maximal runs of cyclically consecutive error points, of lengths $L_1, \dots, L_R$ with $\sum_j L_j = a$. Call the difference $d_i$ *touched* if $e_i \neq 0$ or $e_{i+1} \neq 0$. A run of length $L$ touches exactly $L+1$ differences, the $L-1$ inside it and the two at its ends, and no difference is touched by two runs, because two adjacent error points lie in the same run. So $m - a - R$ differences are untouched, and each of them equals 0. Since $R \leq a$, this gives $n_0 \geq m - a - R \geq m - 2a$.

Now consider the $L+1$ differences touched by one run, and let $z$ and $g$ be the numbers of them equal to $0$ and to $h$. Always $g - z \leq L + 1 \leq 3L - 1$. If $L \geq 2$, then $g - z \leq L+1 \leq 2L - 1$. If $L = 1$ and the error value is $u \neq 0$, the two touched differences are $u$ and $-u$; both equal $h$ only if $u = h = -h$, so $g - z \leq 1 = 2L - 1$ whenever $2h \neq 0$. Since only touched differences can equal $h \neq 0$,
$$\begin{aligned} n_0 - n_h &= (m - a - R) + \sum_{\text{runs}} (z - g) \\ &\geq m - a - R - \sum_{j} (3L_j - 1) \\ &= m - 4a , \end{aligned}$$
and, if $2h \neq 0$, the same computation with $2L_j - 1$ in place of $3L_j - 1$ gives $m - 3a$.

The consequences follow because $N_0(x) > N_h(x)$ whenever the right-hand side of (ii) or (iii) is positive, and because a group of odd order has no element with $2h = 0$ other than $0$. $\square$

*Remark (not part of the exhaustive check).* The proof shows slightly more. A value $h$ of order 2 gains the extra count only from isolated errors whose value is $h$ itself. If the error field never takes a value of order 2, the bound (iii) holds for every $h \neq 0$, and the guarantee $\varepsilon < 1/3$ holds for even $|H|$ as well.

## Proof of Proposition 3 {.unnumbered}

The lower bounds are Theorem 2: an input can be uncorrectable only if $|G| - \tau|E| \leq 0$, and a wrong value can strictly win only if $|G| - \tau|E| < 0$.

*Construction.* Choose $h$ with $2h \neq 0$ if $|H|$ is odd, and $h \neq 0$ with $2h = 0$ if $|H|$ is even. Fix $x \neq 0$ of order $m$. On each orbit of $x$ the positions $0, 2, 4, \dots, 2\lfloor m/2 \rfloor - 2$ are pairwise non-adjacent on the cycle, so the orbits offer $C(m) = (|G|/m)\lfloor m/2 \rfloor$ positions at which errors are isolated. Place $A \leq C(m)$ errors of value $h$ at such positions. Each isolated error touches two differences, equal to $h$ and $-h$, and all other differences vanish. Hence $N_0(x) = |G| - 2A$, and $N_h(x) = A$ in the odd case, $N_h(x) = 2A$ in the even case. So $N_0(x) - N_h(x) = |G| - \tau A$.

*Ties.* Since $\lfloor m/2 \rfloor / m \geq 1/3$ for every $m \geq 2$ and $C(m)$ is an integer, $C(m) \geq \lceil |G|/3 \rceil \geq \lceil |G|/\tau \rceil$. Taking $A = \lceil |G|/\tau \rceil$ gives $N_0(x) \leq N_h(x)$ for the chosen $x$, which was arbitrary.

*Strict wins.* We need $A = \lfloor |G|/\tau \rfloor + 1$. If $\tau = 4$, then $C(m) \geq |G|/3 > |G|/4$ and $C(m)$ is an integer, so $C(m) \geq \lfloor |G|/4 \rfloor + 1$ and the construction applies. If $\tau = 3$ and $G$ has an element $x$ of order $m \notin \{1, 3\}$, then $\lfloor m/2 \rfloor/m > 1/3$, so $C(m) > |G|/3$ and again $C(m) \geq \lfloor |G|/3 \rfloor + 1$. In the remaining case every non-zero element of $G$ has order 3. Take any $x \neq 0$; its $|G|/3$ orbits have length 3. Put one error of value $h$ on every orbit but one, and on the last orbit put the values $(h, -h, 0)$. An orbit with one error has differences $(-h, 0, h)$ and contributes 1 to $N_0$ and 1 to $N_h$. The last orbit has differences $(-2h, h, h)$ and contributes 0 to $N_0$ and at least 2 to $N_h$. So $N_h(x) \geq N_0(x) + 2$ with $|G|/3 + 1$ errors. $\square$

## Proof of Theorem 4 and Corollary 5 {.unnumbered}

Let $\chi$ be a non-trivial character of $H$. Since $\sum_{h \neq 0}\chi(h) = -1$,
$$\begin{aligned} \mathbb{E}\,\chi(e(x)) &= (1 - \varepsilon) + \dfrac{\varepsilon}{q-1}\sum_{h \neq 0}\chi(h) \\ &= 1 - \varepsilon - \dfrac{\varepsilon}{q-1} = \lambda . \end{aligned}$$
The distribution of $e(x)$ is invariant under $h \mapsto -h$, so $\mathbb{E}\,\chi(-e(x)) = \lambda$ as well. The points are distinct, so the errors are independent and $\mathbb{E}\,\chi(S) = \lambda^c$, while the trivial character gives 1. By Fourier inversion on $H$,
$$\begin{aligned} \Pr[S = h] &= \dfrac{1}{q} \sum_{\chi} \overline{\chi(h)}\; \mathbb{E}\,\chi(S) \\ &= \dfrac{1}{q}\left(1 + \lambda^c\left(q\,\mathbf{1}[h = 0] - 1\right)\right), \end{aligned}$$
which is the claim. The difference of the two probabilities is $\lambda^c$, positive for even $c$ and $\lambda \neq 0$. The queries of the vote, $x + r$ and $r$, are distinct when $x \neq 0$; those of the linearity test, $x$, $y$, $x+y$, when $x \neq 0$, $y \neq 0$ and $x \neq y$; those of the bilinear vote when $a \neq 0$ and $b \neq 0$. $\square$

*The finite-size estimate (heuristic).* For fixed $x \neq 0$ and $h \neq 0$, $N_0(x) - N_h(x)$ is the sum over $r$ of $\mathbf{1}[D_x(r) = 0] - \mathbf{1}[D_x(r) = h]$. Each term has mean $\lambda^2$ and variance $p_0 + p_h - (p_0 - p_h)^2 \approx 2/q$ near chance, where $p_0 \approx p_h \approx 1/q$, and the terms are nearly uncorrelated. The gap is thus approximately Gaussian with mean $|G|\lambda^2$ and standard deviation $\sqrt{2|G|/q}$. The smallest of $n \approx |G|q$ such gaps is about $\sqrt{2\ln n}$ standard deviations below the mean, and setting it to zero gives the estimate in the text. The independence and Gaussian assumptions are not justified here.

## Closed forms for the synthetic families {.unnumbered}

For the two random families the statements are expectations over the random set, for $x \neq 0$; the band formulas are exact.

*Constant offset $h$ on a random set of density $\varepsilon$, $2h \neq 0$.* $D_x(r) \in \{0, h, -h\}$ with $T_x(0) = (1-\varepsilon)^2 + \varepsilon^2$ and $T_x(\pm h) = \varepsilon(1-\varepsilon)$. The margin is $1 - 3\varepsilon + 3\varepsilon^2 \geq 1/4$.

*Second homomorphism.* Let $M = g$ on a random set $S$ of density $\rho$ and $M = f$ elsewhere, $u = g - f$, $q' = |\operatorname{im} u|$, and $u(x) \neq 0$. If neither $r$ nor $x+r$ is in $S$, then $D_x(r) = 0$; if both are, $D_x(r) = u(x)$; if exactly one is, $D_x(r)$ is $u(x+r)$ or $-u(r)$, uniform on the image of $u$. Hence $T_x(0) = (1-\rho)^2 + 2\rho(1-\rho)/q'$ and $T_x(u(x)) = \rho^2 + 2\rho(1-\rho)/q'$. The truth is the mode if and only if $\rho < 1/2$; beyond that the mode is $u(x)$ and the corrector returns $g(x)$. The error rate is $\rho(1 - 1/q')$.

*Band.* Let $\ell: G \to \mathbb{Z}_n$ be a surjective homomorphism and $e(x) = h$ if $\ell(x) \in \{0, \dots, w-1\}$, else 0, so $\varepsilon = w/n$. For $x$ with $\ell(x) = t$ let $|t|$ be the cyclic distance of $t$ from 0 and $\nu = \min(w, n - w, |t|)$, the number of band positions that the shift $t$ moves out of the band. Then $N_0(x) = |G|(1 - 2\nu/n)$ and $N_h(x) = N_{-h}(x) = |G|\nu/n$ if $2h \neq 0$, while $N_h(x) = 2|G|\nu/n$ if $2h = 0$. So $x$ is uncorrectable if and only if $\nu \geq n/3$, respectively $\nu \geq n/4$. The band has uncorrectable inputs exactly for $\varepsilon \in [1/3, 2/3]$, respectively $[1/4, 3/4]$, and these are the inputs with $|t| \geq n/3$, respectively $n/4$.

## Proof of Proposition 6 {.unnumbered}

*(a)* The map $r \mapsto (a+r, b-r)$ is a bijection from $\mathbb{Z}_p$ onto the level set of $f$ through $(a,b)$. If $e = \varphi \circ f$, then $M = f + \varphi\circ f$ is constant on level sets, so every vote equals $M(a,b)$.

*(b)* $D_x(r) = \varphi(f(x+r)) - \varphi(f(r)) = \varphi(f(x) + s) - \varphi(s)$ with $s = f(r)$, which is uniform on $\mathbb{Z}_p$ when $r$ is uniform on $G$. Proposition 1 then applies.

*(c)* An invariance vote is correct exactly when the sampled point of the level set is not an error, which has probability $1 - \varepsilon$ on average over level sets. The translation vote is Theorem 4 with $c = 2$. $\square$

## Proof of Proposition 7 {.unnumbered}

*(a)* Let $g$ be a homomorphism and $d$ the fraction of inputs with $M \neq g$. If $M$ agrees with $g$ at $x$, $y$ and $x+y$, the test passes. Each of the three points is uniform on $G$, so the test fails with probability at most $3d$ by the union bound. Take $g = f$.

*(b)* $M(x) + M(y) - M(x+y) = e(x) + e(y) - e(x+y)$. For $x \neq 0$, $y \neq 0$, $x \neq y$ the three points are distinct and Theorem 4 applies with $c = 3$. The remaining pairs are a fraction at most $3/|G|$ of all pairs.

*(c)* The definition of $\pi$ does not involve $f$. $\square$

## Proof of Proposition 8 {.unnumbered}

*(a)* As long as all steps so far are correct, the state follows the true running sum, so from state $s$ the chain moves to $s'$ and stays correct with probability $g(s, s'-s)/p = W[s,s']$. Summing over paths from a uniform start gives $\tfrac1p \mathbf{1}^{\top}W^L\mathbf{1}$. This is $1/p$ times the sum of the entries of $W^L$, which is a matrix norm of $W^L$ because $W$ is non-negative; by Gelfand's formula its $L$-th root tends to the spectral radius $\rho(W)$.

*(b)* If all row sums equal $\kappa$, then $W\mathbf{1} = \kappa\mathbf{1}$ and the probability is $\kappa^L$. If all column sums equal $\kappa$, then $\mathbf{1}^{\top}W = \kappa\mathbf{1}^{\top}$ and the probability is again $\kappa^L$. In both cases $\kappa = \tfrac1p\mathbf{1}^{\top}W\mathbf{1} = \bar g$. If $g(s,a) = \gamma(s+a)$, all rows of $W$ are equal, so the row sums are constant; if $g(s,a) = \gamma(s)$, the column sums are constant.

*(c)* Independent uniform inputs succeed independently with probability $\bar g$ each. $\square$

*Example.* For $g(s,a) = 1 - \mathbf{1}[s \in B]\,\mathbf{1}[s+a \in B]$ with $|B| = \beta p$, an eigenvector that is constant on $B$ and on its complement gives $\rho^2 - (1-\beta)\rho - \beta(1-\beta) = 0$, so $\rho(W) = \tfrac12\left((1-\beta) + \sqrt{(1-\beta)(1+3\beta)}\right)$, which is $0.8205$ for $\beta = 15/31$.

# References {.unnumbered #sec-refs}

::: {.references style="overflow-wrap:anywhere"}
- Amireddy, Behera, Paraashar, Srinivasan, Sudan. *Local Correction of Linear Functions over the Boolean Cube.* STOC 2024. arXiv:2403.20305. <https://arxiv.org/abs/2403.20305> Bibliographic data as returned by a search summary; not checked against the source.
- Noga Amit, Shafi Goldwasser, Orr Paradise, Guy N. Rothblum. *Models That Prove Their Own Correctness.* arXiv:2405.15722, 24 May 2024 (later versions through Dec 2025); also ECCC TR24-098. <https://arxiv.org/abs/2405.15722>
- Mihir Bellare, Don Coppersmith, Johan Håstad, Marcos Kiwi, Madhu Sudan. *Linearity testing in characteristic two.* IEEE Transactions on Information Theory 42(6):1781-1795, November 1996. Preliminary version: Proc. 36th IEEE FOCS, pp. 432-441, 1995. <https://doi.org/10.1109/18.556674>
- Michael Ben-Or, Don Coppersmith, Mike Luby, Ronitt Rubinfeld. *Non-abelian homomorphism testing, and distributions close to their self-convolutions.* Random Structures & Algorithms 32 (2008), pp. 49-70. Preliminary version in RANDOM 2004 (LNCS 3122); ECCC TR04-052. <https://doi.org/10.1002/rsa.20182>
- Manuel Blum, Michael Luby, Ronitt Rubinfeld. *Self-testing/correcting with applications to numerical problems.* Journal of Computer and System Sciences 47(3):549-595, 1993. Preliminary version: Proc. 22nd ACM STOC, pp. 73-83, 1990. <https://doi.org/10.1016/0022-0000(93)90044-W>
- Brilliant. *Limits of Self-Correction in LLMs: An Information-Theoretic Analysis of Correlated Errors.* Preprints.org, DOI 10.20944/preprints202601.0892 (not peer-reviewed; v4, April 2026). <https://www.preprints.org/manuscript/202601.0892> Bibliographic data as returned by a search summary; not checked against the source.
- Jeremy Cohen, Elan Rosenfeld, J. Zico Kolter. *Certified Adversarial Robustness via Randomized Smoothing.* Proc. 36th International Conference on Machine Learning (ICML 2019), PMLR 97:1310-1320. arXiv:1902.02918. <https://proceedings.mlr.press/v97/cohen19c.html>
- Cordero-Encinar, Duncan. *Certified Self-Consistency: Statistical Guarantees and Test-Time Training for Reliable Reasoning in LLMs.* arXiv:2510.17472 (Oct 2025). <https://arxiv.org/abs/2510.17472> Bibliographic data as returned by a search summary; not checked against the source.
- Irit Dinur, Elena Grigorescu, Swastik Kopparty, Madhu Sudan. *Decodability of group homomorphisms beyond the Johnson bound.* Proc. 40th Annual ACM Symposium on Theory of Computing (STOC 2008), pp. 275-284. Preprint ECCC TR08-020. <https://doi.org/10.1145/1374376.1374418>
- I. Dinur. Course notes, 2025. <https://www.wisdom.weizmann.ac.il/~dinuri/courses/25-loc2glob/L02.pdf> Bibliographic data as returned by a search summary; not checked against the source.
- Joseph Emerson, Robert Alicki, Karol Życzkowski. *Scalable noise estimation with random unitary operators.* Journal of Optics B: Quantum and Semiclassical Optics 7 (2005) S347-S352. arXiv:quant-ph/0503243. <https://arxiv.org/abs/quant-ph/0503243>
- Ferhat Erata, Orr Paradise, Thanos Typaldos, Timos Antonopoulos, ThanhVu Nguyen, Shafi Goldwasser, Ruzica Piskac. *Learning Randomized Reductions.* Proc. 43rd International Conference on Machine Learning (ICML 2026), PMLR 306, 2026. arXiv:2412.18134 (v1, 24 Dec 2024, under the title 'Learning Randomized Reductions and Program Properties'). <https://proceedings.mlr.press/v306/erata26a.html> Full text not read; described from the abstract.
- Valentino F. Foit, David W. Hogg, Soledad Villar. *Group Averaging for Physics Applications: Accuracy Improvements at Zero Training Cost.* arXiv:2511.09573, 11 Nov 2025; workshop paper, Machine Learning and the Physical Sciences workshop at NeurIPS 2025. <https://arxiv.org/abs/2511.09573>
- Shafi Goldwasser, Jonathan Shafer, Neekon Vafa, Vinod Vaikuntanathan. *Oblivious Defense in ML Models: Backdoor Removal without Detection.* Proc. 57th Annual ACM Symposium on Theory of Computing (STOC '25), pp. 1785-1794, June 2025. arXiv:2411.03279 (5 Nov 2024). <https://doi.org/10.1145/3717823.3718245> Full text not read; described from the abstract and section list.
- Elena Grigorescu, Swastik Kopparty, Madhu Sudan. *Local decoding and testing for homomorphisms.* APPROX-RANDOM 2006, Lecture Notes in Computer Science vol. 4110, pp. 375-385, Springer, 2006. <https://www.springerprofessional.de/local-decoding-and-testing-for-homomorphisms/1236322>
- Shuichi Hirahara, Nobutaka Shimizu. *Optimal Random Self-Reductions for All Linear Problems.* Technical report, Electronic Colloquium on Computational Complexity, TR26-048, 24 March 2026 (revision 1: 16 April 2026). <https://eccc.weizmann.ac.il/report/2026/048>
- Yiding Jiang, Vaishnavh Nagarajan, Christina Baek, J. Zico Kolter. *Assessing Generalization of SGD via Disagreement.* International Conference on Learning Representations (ICLR) 2022 (spotlight). arXiv:2106.13799 (25 Jun 2021). <https://arxiv.org/abs/2106.13799>
- Kimura. *Understanding Test-Time Augmentation.* arXiv:2402.06892. <https://arxiv.org/abs/2402.06892> Bibliographic data as returned by a search summary; not checked against the source.
- Henry Kvinge, Andrew Aguilar, Nayda Farnsworth, Grace O'Brien, Robert Jasper, Sarah Scullen, Helen Jenne. *Can Neural Networks Learn Small Algebraic Worlds? An Investigation Into the Group-theoretic Structures Learned By Narrow Models Trained To Predict Group Operations.* Proceedings of TAG-DS 2025, PMLR 321:302-312, 2026. arXiv:2601.21150 (29 Jan 2026). <https://proceedings.mlr.press/v321/kvinge26a.html> Capitalisation of the subtitle unconfirmed.
- Thomas Kwa, Ben West, Joel Becker, Amy Deng, Katharyn Garcia, Max Hasin, Sami Jawhar, Megan Kinniment, Nate Rush, Sydney Von Arx, Ryan Bloom, Thomas Broadley, Haoxing Du, Brian Goodrich, Nikola Jurkovic, Luke Harold Miles, Seraphina Nix, Tao Lin, Neev Parikh, David Rein, Lucas Jun Koba Sato, Hjalmar Wijk, Daniel M. Ziegler, Elizabeth Barnes, Lawrence Chan. *Measuring AI Ability to Complete Long Tasks.* arXiv:2503.14499, v1, 18 Mar 2025 (the current version, v3 of 25 Feb 2026, is retitled 'Measuring AI Ability to Complete Long Software Tasks'). <https://arxiv.org/abs/2503.14499>
- Balaji Lakshminarayanan, Alexander Pritzel, Charles Blundell. *Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles.* Advances in Neural Information Processing Systems 30 (NIPS 2017), pp. 6402-6413. <https://proceedings.neurips.cc/paper/2017/hash/9ef2ed4b7fd2c810847ffa5fa85bce38-Abstract.html>
- Tao Li, Vivek Gupta, Maitrey Mehta, Vivek Srikumar. *A Logic-Driven Framework for Consistency of Neural Models.* Proc. EMNLP-IJCNLP 2019, pp. 3924-3935. arXiv:1909.00126. <https://doi.org/10.18653/v1/D19-1405>
- Richard J. Lipton. *New directions in testing.* In: Distributed Computing and Cryptography (J. Feigenbaum, M. Merritt, eds.), DIMACS Series in Discrete Mathematics and Theoretical Computer Science, vol. 2, American Mathematical Society, pp. 191-202, 1991 (workshop held October 1989). <https://archive.dimacs.rutgers.edu/Volumes/Vol02.html> Text not consulted; cited for the attribution made by secondary sources.
- Yi Liu. *Two Calls, Two Moments, and the Vote-Accuracy Curve of Repeated LLM Inference.* arXiv:2605.03379, 5 May 2026 (preprint; cs.LG, cs.CL). <https://arxiv.org/abs/2605.03379>
- Aman Mehta. *When Agents Disagree With Themselves: Behavioral Consistency as an Uncertainty Signal for LLM Agents.* arXiv:2602.11619 (v1, Feb 2026, titled 'When Agents Disagree With Themselves: Measuring Behavioral Consistency in LLM-Based Agents'; v2, July 2026, with the title above); ICML 2026 workshop paper. <https://arxiv.org/abs/2602.11619>
- Elliot Meyerson, Giuseppe Paolo, Roberto Dailey, Hormoz Shahrzad, Olivier Francon, Conor F. Hayes, Xin Qiu, Babak Hodjat, Risto Miikkulainen. *Solving a Million-Step LLM Task with Zero Errors.* arXiv:2511.09030, 12 Nov 2025 (preprint; cs.AI). <https://arxiv.org/abs/2511.09030>
- Neel Nanda, Lawrence Chan, Tom Lieberum, Jess Smith, Jacob Steinhardt. *Progress measures for grokking via mechanistic interpretability.* International Conference on Learning Representations (ICLR) 2023 (oral, notable top 25%). arXiv:2301.05217. <https://arxiv.org/abs/2301.05217>
- John von Neumann. *Probabilistic logics and the synthesis of reliable organisms from unreliable components.* In: Automata Studies (C. E. Shannon, J. McCarthy, eds.), Annals of Mathematics Studies no. 34, Princeton University Press, pp. 43-98, 1956. <https://www.degruyterbrill.com/document/doi/10.1515/9781400882618/html> Bibliographic data verified; content not consulted.
- Toby Ord. *Is there a half-life for the success rates of AI agents?* arXiv:2505.05115, 8 May 2025 (preprint; cs.AI). Also posted at tobyord.com/writing/half-life. <https://arxiv.org/abs/2505.05115>
- Alethea Power, Yuri Burda, Harri Edwards, Igor Babuschkin, Vedant Misra. *Grokking: Generalization Beyond Overfitting on Small Algorithmic Datasets.* arXiv:2201.02177, 6 Jan 2022 (preprint). <https://arxiv.org/abs/2201.02177>
- Ronitt Rubinfeld, Madhu Sudan. *Robust characterizations of polynomials with applications to program testing.* SIAM Journal on Computing 25(2):252-271, 1996. <https://dc2.philarchive.org/rec/RUBRCO>
- R. Rubinfeld. Lecture notes on linearity testing, MIT course handout. <https://people.csail.mit.edu/ronitt/COURSE/F24/Handouts/lec20sp24lintest.pdf> Bibliographic data as returned by a search summary; not checked against the source.
- Joel J. Wallman, Joseph Emerson. *Noise tailoring for scalable quantum computation via randomized compiling.* Physical Review A 94, 052325 (18 Nov 2016). arXiv:1512.01098. <https://doi.org/10.1103/PhysRevA.94.052325>
- Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed H. Chi, Sharan Narang, Aakanksha Chowdhery, Denny Zhou. *Self-Consistency Improves Chain of Thought Reasoning in Language Models.* International Conference on Learning Representations (ICLR) 2023. arXiv:2203.11171 (v1 21 Mar 2022, v4 7 Mar 2023). <https://arxiv.org/abs/2203.11171>
:::

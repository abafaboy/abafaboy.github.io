---
title: "Coherence, Not Error Rate, Limits the Self-Correction of Learned Computation"
subtitle: "When does voting over a random self-reduction repair a trained network? An exact criterion, sharp worst-case radii and a depolarizing law, studied at toy scale"
kicker: "Research preprint · November 2026 · not peer reviewed"
author:
  - "<b>Abafa Mukhamedov</b> (commissioned and published this work)"
  - "<b>Claude</b>, an AI research agent built by Anthropic (conceived, implemented, ran and wrote it)"
date: "16 November 2026"
description: "An exact criterion, sharp worst-case radii and a depolarizing law for voting over random self-reductions, with exhaustive measurements on small trained networks."
pdf: "paper.pdf"
abstract: "[[ABSTRACT: to be written last]]"
footer: "Generated from paper.md by build.py. Every number in the text is read from a JSON file in results/, written by a script in code/."
---

# Introduction {#sec-intro}

A trained network is a fixed function. Building reliable computation from unreliable components is an old problem (von Neumann, 1956), but its standard remedy, repeating the computation and taking a vote, does not apply to such a function: asked the same question twice it gives the same answer, so an input it gets wrong, it gets wrong every time. Language models that sample their output do vary between calls, and voting over samples helps them (Wang et al., 2023), but only against the part of the error that changes from call to call (Liu, 2026). Errors that survive compound: if each of $L$ steps fails independently with probability $\varepsilon$, all succeed with probability $(1-\varepsilon)^L$, which falls to one half after about $\ln 2/\varepsilon$ steps.

Program checking has a different remedy. Blum, Luby and Rubinfeld (1993) observed that when the target function $f$ satisfies an algebraic identity, one can randomise the *input* and leave the program alone. If $f$ is a homomorphism, a map with $f(x+y) = f(x)+f(y)$, then $f(x) = f(x+r) - f(r)$ for every $r$. A program $M$ that errs on a fixed set of inputs is queried at $x+r$ and at $r$, two uniformly random points, so its fixed error pattern reaches the vote $M(x+r) - M(r)$ as noise. A plurality over several random $r$ returns $f(x)$ at *every* input, provided $M$ is "not wrong too often". Such an identity is a *random self-reduction*, and the voter is a *self-corrector*.

This paper asks what "not wrong too often" has to mean when $M$ is a trained network. One candidate is the error rate: the classical guarantees hold below a constant error rate. The other is the structure of the errors. We borrow two words from quantum computing, where the same distinction is central (Wallman and Emerson, 2016): errors are *incoherent* when they behave like independent noise with scattered wrong values, and *coherent* when they are aligned so that they reinforce one another under the randomisation. Which of the two decides whether voting can repair a trained network?

We study the question where everything can be computed exactly: small networks trained on exact algebraic tasks, whose complete prediction tables we enumerate. [[RESULT: one sentence on the zoo: number of trained networks and training runs, tasks and moduli, range of error rates covered; state that the run is the unit of analysis]] The contributions are:

1. **An exact criterion.** The errors of all votes at an input $x$ are summarised by one distribution, the *twirled channel* $T_x$, which we compute exactly. Voting succeeds at $x$ if and only if the truth is the strict mode of $T_x$ (Proposition 1).
2. **The worst case.** The two-query plurality corrector is guaranteed at every input below error rate $1/3$ if $|H|$ is odd and below $1/4$ otherwise, and both values are sharp (Theorem 2, Proposition 3). This limits the corrector, not the underlying code.
3. **The incoherent case.** For independent errors with scattered wrong values, a $c$-query vote is correct with probability $1/q + (1-1/q)\lambda^c$, where $\lambda$ is the advantage over chance. The truth then stays the mode at every error rate short of chance, and only finite size limits correction (Theorem 4).
4. **Same error rate, different fates.** Synthetic error families with equal error rates break at $1/4$, at $1/3$, at $0.484$, near $0.78$, or never (Section 4).
5. **Trained networks.** [[RESULT: headline measurement on trained networks: how close their twirled channels are to the depolarizing law (a coherence statistic, per run), the largest error rate at which every input is still correctable, and the smallest error rate at which some input is not, compared with 1/3]]
6. **Which twirl.** Voting over the invariances of the task cannot remove errors that depend only on the answer; the translation vote can (Proposition 6). [[RESULT: comparison on trained networks of the translation twirl, the invariance twirl, the raw model and baselines at equal query budget]]
7. **Other tasks.** [[RESULT: four-query bilinear vote on multiplication networks and two-query vote on the hidden linear map; agreement with the lambda^4 and lambda^2 laws]]
8. **Chains and label-free evaluation.** The survival rate of a chain is the largest eigenvalue of a transfer matrix (Proposition 8), and the pass rate of the linearity test estimates the error rate without labels, exactly for incoherent errors and too low for coherent ones (Proposition 7). [[RESULT: horizons of trained-network chains with and without self-correction; accuracy and bias of the label-free estimate on trained networks]]

**Scope.** The setting is narrow on purpose. The tasks are exact algebraic maps on groups of at most a few thousand elements, and the networks are small. The corrector is *given* the group law: it must add $r$ to an input and subtract outputs. We claim nothing about language models. The mathematics is classical: the corrector and the tester are those of Blum, Luby and Rubinfeld, the incoherent law is Fourier multiplicativity, and the worst-case thresholds coincide with known decoding radii in two cases. The thesis of the title has been stated in other settings, for repeated sampling of language models (Liu, 2026; Brilliant, 2026) and for quantum noise (Wallman and Emerson, 2016); here it concerns voting over a random self-reduction on learned algebraic maps. What we add is the per-input criterion, the sharp plurality thresholds (to our knowledge) and the measurement of the twirled channels of trained networks.

# Setting and notation {#sec-setting}

**Task and model.** $G$ and $H$ are finite abelian groups written additively, $q = |H|$, and the task $f: G \to H$ is a homomorphism. The running example is $G = \mathbb{Z}_p^2$, $H = \mathbb{Z}_p$, $f(a,b) = a + b \bmod p$. A trained network is represented by its table of argmax predictions $M: G \to H$. Its *error field* is $e = M - f$, its error set is $E = \{x : e(x) \neq 0\}$ and its *error rate* is $\varepsilon = |E|/|G|$. A uniformly random guess has error rate $1 - 1/q$, which we call chance. The *advantage*
$$\lambda = 1 - \frac{\varepsilon}{1 - 1/q}$$
is 1 for a perfect model, 0 at chance, and negative for a model that is worse than chance.

**The self-corrector.** For a shift $r \in G$, one *vote* for the value at $x$ is $V_r(x) = M(x+r) - M(r)$; it costs two queries. Because $f$ is a homomorphism,
$$V_r(x) = f(x) + D_x(r), \qquad D_x(r) = e(x+r) - e(r).$$
The self-corrector $\mathrm{SC}_k(x)$ draws $k$ independent uniform shifts and returns the plurality of the $k$ votes. A tie for first place counts as a failure throughout, and $\delta_k(x)$ is the failure probability at $x$. The corrector uses the group operations of $G$ and $H$ but no labels and no knowledge of $f$.

**The twirled channel.** The distribution of the vote offset under a uniform shift,
$$T_x(h) = \Pr_r\left[D_x(r) = h\right], \qquad h \in H,$$
is the *twirled channel* at $x$. In quantum information, to twirl a noise process is to average it over a group of random operations, which reduces it to a few parameters (Emerson, Alicki and Życzkowski, 2005); here the group is the shifts of the input. The counts $N_h(x) = |G|\,T_x(h) = \sum_{a \in H}\sum_{r \in G} \mathbf{1}[e(r) = a]\,\mathbf{1}[e(r+x) = a+h]$ form an autocorrelation on $H \times G$, so one fast Fourier transform of size $|H||G|$ gives $T_x$ exactly for all inputs at once. We call $x$ *correctable* when the truth is the strict mode of the channel, $T_x(0) > \max_{h \neq 0} T_x(h)$, and call $T_x(0) - \max_{h \neq 0} T_x(h)$ the *margin* at $x$.

**Incoherent errors and the depolarizing form.** The reference model for structureless errors is the *incoherent* field: the $e(x)$ are independent, each is non-zero with probability $\varepsilon$, and a non-zero error is uniform on the $q-1$ wrong values. For such a field a vote that combines $c$ distinct queries is correct with probability $1/q + (1-1/q)\lambda^c$ and takes each wrong value with probability $(1-\lambda^c)/q$ (Theorem 4). In words, when $\lambda^c \geq 0$: with probability $\lambda^c$ the vote is the truth, and otherwise it is uniform on $H$. This one-parameter form is the classical counterpart of the depolarizing channel of quantum information. By the *coherence* of a real error field we mean the departure of its twirled channels from this form.

**More than two queries.** The linearity test of Blum, Luby and Rubinfeld checks $M(x) + M(y) = M(x+y)$ and involves $c = 3$ queries. Multiplication $f(a,b) = ab \bmod p$ is bilinear but not a homomorphism of $\mathbb{Z}_p^2$; it is corrected by the four-query vote $M(a+r, b+s) - M(r, b+s) - M(a+r, s) + M(r,s)$, so $c = 4$.

# Theory {#sec-theory}

All statements are proved in the appendix and were checked numerically on synthetic error fields (`code/theory_checks.py`, results in `results/theory_checks.json`). No trained network appears in this section.

## The exact criterion {#sec-criterion}

::: theorem
**Proposition 1 (exact criterion and rate).** Fix an input $x$ and $k \geq 1$ votes with independent uniform shifts.

*(a)* The offsets of the $k$ votes from $f(x)$ are independent draws from $T_x$. Hence $\delta_k(x) = \Pr[N_0 \leq \max_{h \neq 0} N_h]$, where the counts $(N_h)_{h \in H}$ are multinomial with $k$ trials and cell probabilities $T_x$.

*(b)* $\delta_k(x) \to 0$ as $k \to \infty$ if and only if $T_x(0) > \max_{h \neq 0} T_x(h)$. If $T_x(0) = T_x(h)$ for some $h \neq 0$, then $\delta_k(x) \geq 1/2$ for every $k$. If $T_x(0) < T_x(h)$ for some $h$, then $\delta_k(x) \to 1$.

*(c)* If the truth is the strict mode, then
$$\delta_k(x) \leq \sum_{h \neq 0} \left(1 - \left(\sqrt{T_x(0)} - \sqrt{T_x(h)}\right)^2\right)^k .$$

*(d)* If the truth is the strict mode and $h^*$ is a most likely wrong value with $T_x(h^*) > 0$, then $-\tfrac{1}{k}\ln \delta_k(x) \to I_x = -\ln\left(1 - (\sqrt{T_x(0)} - \sqrt{T_x(h^*)})^2\right)$.
:::

Part (a) is the observation of Blum, Luby and Rubinfeld, and (b) to (d) are standard large-deviation facts. Stated together they say that correctability at $x$ is a property of one computable distribution and not of the error rate: Section 4 has fields with $\varepsilon = 0.27$ that have uncorrectable inputs, and fields with $\varepsilon = 0.75$ that have none.

Two cautions apply. Each term of (c) is a valid bound only for a wrong value with $T_x(h) < T_x(0)$. And the rate in (d) is reached slowly: for a depolarizing channel with $q = 31$ and $T(0) = 0.30$ the exact failure probability with 40 votes is $3.4 \times 10^{-3}$ where the bound gives $3.4 \times 10^{-2}$, and for a nearly tied channel $(0.36, 0.34, 0.30)$ the failure probability with 160 votes is still $0.45$. Failure probabilities in this paper are therefore computed as the exact multinomial probability of (a); the routine agrees with brute-force enumeration to $4 \times 10^{-16}$.

## The worst case: one third and one quarter {#sec-worst}

How large can the error rate be before *some* error field defeats the corrector at *some* input?

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

Parts (i) and (ii) are classical: (i) is the two-query bound of Blum, Luby and Rubinfeld, and (ii) follows from it. Part (iii) and Proposition 3 are, to our knowledge, not stated in the literature; the proof is elementary and they may be folklore. The extremal field consists of errors that are *isolated* along the orbit $x, 2x, 3x, \dots$ of the input and carry the *same* wrong value $h$. Each such error spoils two votes, with offsets $+h$ and $-h$. If $h \neq -h$ the two wrong votes disagree, and the truth loses only when $|G| - 2|E| \leq |E|$. If $h = -h$ they agree, and it loses already when $|G| - 2|E| \leq 2|E|$. When $\tau$ does not divide $|G|$ the smallest breaking error rate lies slightly above $1/\tau$, for example $321/961 = 0.334$ on $\mathbb{Z}_{31}^2$.

::: box
**Relation to the unique-decoding radius.** The values $1/4$ and $1/3$ are familiar from coding theory, and the coincidence needs care. The tables of all homomorphisms $G \to H$ form an error-correcting code (Grigorescu, Kopparty and Sudan, 2006; Dinur et al., 2008). Two distinct homomorphisms $f$ and $g$ agree exactly on the kernel of $g - f$, whose index divides both $|G|$ and $|H|$, so they agree on at most a fraction $1/p$ of the inputs, where $p$ is the smallest prime dividing $\gcd(|G|,|H|)$. A table at distance less than $(1 - 1/p)/2$ from a homomorphism therefore has a unique nearest homomorphism. This *unique-decoding radius* is $1/4$ for $p = 2$ and $1/3$ for $p = 3$, as in Theorem 2, but $0.4$ for $p = 5$ and $0.484$ for $p = 31$. Theorem 2 is a statement about one decoder, the two-query plurality vote, and not about the code. For odd $|H|$ with $p \geq 5$ its guarantee stops at $1/3$, inside the unique-decoding radius, and the fields that defeat it contain no competing homomorphism. Conversely the guarantee is $1/4$ whenever $|H|$ is even, whatever $G$ is.
:::

**Verification.** Over every error field on 23 small pairs $(G, H)$, 3,386,884 fields in total, the three inequalities always hold, each with minimal slack exactly 0, and both counts of Proposition 3 are as predicted. A search by number of errors on 70 further pairs with $|G|$ from 10 to 20 (13,246,114 fields) confirmed the first count in 63 pairs and the second in 57; the remaining cases exceeded the search budget and are unresolved.

## Incoherent errors: the depolarizing law {#sec-depol}

The worst case needs errors arranged along the orbit of the input with a common value. The opposite extreme is a field with no arrangement at all.

::: theorem
**Theorem 4 (depolarizing law).** Let the errors $e(x)$, $x \in G$, be independent with $\Pr[e(x) = 0] = 1 - \varepsilon$ and $\Pr[e(x) = h] = \varepsilon/(q-1)$ for every $h \neq 0$, and let $\lambda = 1 - \varepsilon/(1 - 1/q)$. For distinct points $x_1, \dots, x_c$ and signs $s_i = \pm 1$, the sum $S = \sum_i s_i\, e(x_i)$ satisfies
$$\Pr[S = 0] = \frac{1}{q} + \left(1 - \frac{1}{q}\right)\lambda^c, \qquad \Pr[S = h] = \frac{1 - \lambda^c}{q} \quad \text{for every } h \neq 0 .$$
:::

::: theorem
**Corollary 5 (no threshold short of chance).** For even $c$, $\Pr[S = 0] - \Pr[S = h] = \lambda^c > 0$ whenever $\lambda \neq 0$. In expectation over an incoherent field, the truth is therefore the strict mode of the vote at every error rate except exactly chance, including error rates above chance and $\varepsilon = 1$.
:::

This is not new mathematics. The characteristic function of a sum of independent variables is the product of their characteristic functions, and each error contributes a factor $\lambda$; for binary outputs the statement is the piling-up lemma of linear cryptanalysis. We restate it in channel language because it is the reference form against which a trained network can be measured, with $c = 2$ for the vote, $c = 3$ for the linearity test and $c = 4$ for the bilinear vote. It holds in expectation over the field; for one field the frequencies over $r$ fluctuate around it by $O(|G|^{-1/2})$.

Corollary 5 does not contradict coding theory. Against adversarial errors beyond the unique-decoding radius no procedure can single out $f$, and one must accept a list of candidates or use advice (Dinur et al., 2008; Hirahara and Shimizu, 2026). An incoherent field is far from every homomorphism in the same structureless way. A model that is wrong on *every* input illustrates this: with $q = 3$ and $\varepsilon = 1$ the law gives $T_x(0) = 1/2$ against $1/4$ for each wrong value, and in simulation on $|G| = 961$ every input was correctable in all 20 fields.

**Verification.** On $\mathbb{Z}_{31}^2$ with $q \in \{2, 3, 5, 31\}$, five error rates from $0.1$ to $1$ and $c \in \{2,3,4\}$ (60 cells, 20 random fields each, all votes enumerated), the measured frequency is within $9.6 \times 10^{-4}$ of the law evaluated at each field's realised error rate. Against the nominal error rate, three cells deviate by more than three standard errors (largest $|z| = 3.90$). All three come from one set of 20 fields whose realised error rate was $0.908$ for a nominal $0.9$. A replication with 100 new fields again drew a high rate ($|z| = 2.86$), and one with 4000 fields gave $z = -0.03$ for $c = 2$.

**Finite size (heuristic).** On a finite group the truth must beat every wrong value at every input of one realised field. The gap $N_0(x) - N_h(x)$ has mean $|G|\lambda^2$ and, near chance, standard deviation about $\sqrt{2|G|/q}$, and there are about $|G|q$ pairs $(x,h)$. Treating the gaps as independent Gaussians, the first failure is expected at
$$\lambda_c^2 \approx 2\sqrt{\frac{\ln(|G|q)}{|G|q}}, \qquad \varepsilon_c = (1 - \lambda_c)\left(1 - \frac{1}{q}\right).$$
This is not proved. In simulation (Table 1) the estimate is within $0.002$ of the median for $p \geq 17$ and $0.022$ too low at $p = 11$. It also explains why the wrong-everywhere model is not correctable for large $q$: with $q = 31$ and $\varepsilon = 1$, $\lambda^2 = 1/900$ is far below $\lambda_c^2 = 0.037$, and only 4.0% of the inputs were correctable.

| $p$ | group size | simulated median | interquartile range | estimate $\varepsilon_c$ | chance |
|----:|-----:|------:|:-----------:|------:|------:|
| 11 | 121 | 0.583 | 0.560 to 0.587 | 0.561 | 0.909 |
| 17 | 289 | 0.671 | 0.663 to 0.675 | 0.670 | 0.941 |
| 23 | 529 | 0.732 | 0.728 to 0.736 | 0.731 | 0.957 |
| 31 | 961 | 0.779 | 0.774 to 0.786 | 0.781 | 0.968 |
| 47 | 2209 | 0.835 | 0.831 to 0.838 | 0.837 | 0.979 |
| 61 | 3721 | 0.864 | 0.861 to 0.866 | 0.864 | 0.984 |

: **Table 1.** Largest error rate up to which every input of an incoherent field on $\mathbb{Z}_p^2 \to \mathbb{Z}_p$ is correctable: 24 random fields per $p$, exact test of all inputs. The threshold is located on a grid with final step 0.002; failures between coarser grid points below the located window are not excluded.

## Invariance twirl and transitive twirl {#sec-twirls}

Test-time augmentation and group averaging vote over transformations that leave the answer unchanged; for $f(a,b) = a+b$ such a transformation is $(a,b) \mapsto (a+r, b-r)$. We call this an *invariance twirl*: it moves the query within the set of inputs that share its answer. The shift of the self-corrector is a *transitive twirl*: it moves the query to a uniformly random point of the whole domain, at the price of a second query that removes the shift.

::: theorem
**Proposition 6 (invariance twirl versus transitive twirl).** Let $f(a,b) = a+b$ on $G = \mathbb{Z}_p^2$.

*(a)* The invariance vote $M(a+r, b-r)$, with $r$ uniform on $\mathbb{Z}_p$, is the value of $M$ at a uniform point of the level set $\{f = a+b\}$. If the error depends only on the answer, $e = \varphi \circ f$, every vote equals $M(a,b)$, and the output error rate is exactly $\varepsilon$ for any number of votes.

*(b)* For the same error field the translation vote at $x$ has the channel $T_x(h) = \Pr_s[\varphi(f(x)+s) - \varphi(s) = h]$ with $s$ uniform on $\mathbb{Z}_p$, the twirled channel of $\varphi$ on the answer group. It corrects $x$ if and only if the truth is the strict mode of that channel.

*(c)* For an incoherent field an invariance vote is correct with probability $1 - \varepsilon$ on average and costs one query, while a translation vote is correct with probability $1/q + (1-1/q)\lambda^2$ and costs two.
:::

Neither twirl dominates. With $m$ of the 31 answers wrong ($p = 31$, random wrong values, 20 fields per $m$), the invariance vote has error exactly $m/31$ for any number of votes, while under the translation twirl every input is correctable in all fields for $m = 3, 6, 9, 12, 15$, that is, up to $\varepsilon = 0.48$. Convergence is slow when many answers are wrong: the exact mean failure with 5, 15 and 45 votes is $0.264$, $0.027$, $8.4 \times 10^{-5}$ for $m = 9$. On incoherent errors the order reverses. For a mean failure below $10^{-3}$ the invariance twirl needed 9 queries at $\varepsilon = 0.1$ and 17 to 21 at $\varepsilon = 0.3$; the translation twirl needed 14 to 18 and 38 to 46 (three fields each).

## Estimating the error rate without labels {#sec-labelfree}

The linearity test needs no labels: draw $x, y$ and check whether $M(x) + M(y) = M(x+y)$. Blum, Luby and Rubinfeld introduced it as a *self-tester*, a procedure that estimates how often a program is wrong, and the relation between its pass rate and the distance from the nearest homomorphism has been analysed in detail (Bellare et al., 1996; Ben-Or et al., 2008). Using it on a trained network is an application of that tester, not a new estimator.

::: theorem
**Proposition 7 (what the pass rate says).** Let $\pi = \Pr_{x,y}[M(x) + M(y) = M(x+y)]$ for independent uniform $x, y$.

*(a)* (Unconditional.) $1 - \pi \leq 3\,d$, where $d$ is the fraction of inputs on which $M$ differs from any fixed homomorphism. In particular $\varepsilon \geq (1-\pi)/3$.

*(b)* (Incoherent errors.) Under the assumptions of Theorem 4, $\mathbb{E}\,\pi = 1/q + (1-1/q)\lambda^3 + O(1/|G|)$. Inverting, $\hat\lambda = \left((\pi - 1/q)/(1-1/q)\right)^{1/3}$ and $\hat\varepsilon = (1-\hat\lambda)(1-1/q)$.

*(c)* (Blind spot.) $\pi$ depends on $M$ alone. It carries information about the distance of $M$ to the nearest homomorphism, which need not be $f$.
:::

For incoherent fields the inversion is accurate ($\mathbb{Z}_{31}^2 \to \mathbb{Z}_{31}$, 8 error rates, 10 fields each, $\pi$ computed over all pairs): the root-mean-square error of $\hat\varepsilon$ is $1.1 \times 10^{-4}$ at $\varepsilon = 0.1$, $1.5 \times 10^{-3}$ at $0.5$ and $1.1 \times 10^{-2}$ at $0.85$. Feeding $\hat\lambda$ into the depolarizing channel and Proposition 1 predicts, without labels, the number of votes needed for a mean failure of $10^{-3}$. On a grid of odd vote counts the prediction was exact in all 15 fields with $\varepsilon \leq 0.3$ and optimistic at $\varepsilon = 0.5$, where it gave 55 votes and two of three fields needed 63.

For coherent errors the estimate is biased low, and only (a) remains. A constant offset on a random set with $\varepsilon = 0.312$ gives $\hat\varepsilon = 0.231$, and in the 20 coherent fields we examined $\hat\varepsilon$ never exceeded $\varepsilon$. The blind spot is concrete: a table equal to a second homomorphism $g$ on 72.8% of the inputs has error rate $0.706$ with respect to $f$ but $\hat\varepsilon = 0.250$, close to its distance $0.262$ from $g$.

## Chains and horizon {#sec-chains}

::: theorem
**Proposition 8 (survival of a chain).** Let a model compute the running sum $s_{t+1} = s_t + a_t$ on $\mathbb{Z}_p$, with independent uniform $a_t$ and a uniform initial state. Let $g(s,a)$ be the probability that the step on input $(s,a)$ is correct: $g = \mathbf{1}[e(s,a) = 0]$ for the raw model and $g = 1 - \delta_k(s,a)$ for the self-corrector with fresh shifts at every step. Let $W$ be the $p \times p$ matrix $W[s,s'] = g(s, s'-s)/p$, and $\bar g$ the mean of $g$ over all inputs.

*(a)* The probability that all of $L$ steps are correct is $\tfrac{1}{p}\mathbf{1}^{\top} W^L \mathbf{1}$, and its $L$-th root tends to $\rho(W)$, the largest eigenvalue (Perron root) of $W$.

*(b)* If the row sums or the column sums of $W$ are constant, for example when $g$ depends only on the answer or only on the current state, the probability is exactly $\bar g^{\,L}$.

*(c)* If the $L$ inputs were independent and uniform on $G$, the probability would be $\bar g^{\,L}$; the number of steps survived with probability one half is then $\ln 2/(-\ln \bar g) \approx \ln 2/(1 - \bar g)$.
:::

Re-running the raw model on the same input changes nothing, so its chain lasts about $\ln 2/\varepsilon$ steps; the corrector replaces $\varepsilon$ by the mean of $\delta_k$, which falls exponentially in $k$. For an incoherent field with $\varepsilon = 0.190$ on $\mathbb{Z}_{31}^2$ the exact mean failure per step is $0.343$, $0.273$, $0.069$, $7.1 \times 10^{-3}$, $1.5 \times 10^{-4}$ with 1, 3, 5, 9, 15 votes, and the exact survival probability first drops to one half after 2, 3, 10, 98, 4511 steps, against 4 for the raw model. With one or three votes the self-corrector is *worse* than the raw model: a vote combines two queries and so fails about twice as often. For this field the Perron root and $\bar g$ nearly coincide (decay rates within a relative $2 \times 10^{-5}$ for the corrected chains with up to 25 votes).

The formula $\bar g^{\,L}$ is not general. If the raw model errs exactly when the current state and the next state both lie in a set of 15 of the 31 residues, then $1 - \varepsilon = 0.766$ but the exact survival factor per step is $\rho(W) = 0.8205$, and after 20 steps the chain survives with probability $0.0182$, not $0.0048$. A constant failure rate per step is an assumption about the error structure.

# Same error rate, different fates {#sec-fates}

Five synthetic error families make the gap between error rate and correctability concrete. All live on $\mathbb{Z}_{31}^2 \to \mathbb{Z}_{31}$ with $f(a,b) = a+b$, except where a wrong value of order 2 requires an even modulus. For each family and error rate we compute the twirled channel of every input exactly and record the fraction of correctable inputs and the smallest margin (Figure 1, Table 2). Closed forms are in the appendix.

![**Figure 1.** Five synthetic error families behave differently at the same error rate. **a** Fraction of inputs at which the truth is the strict mode of the twirled channel. **b** Smallest margin over inputs, $\min_x [T_x(0) - \max_{h \neq 0} T_x(h)]$; some input is uncorrectable where the curve is at or below zero. Four families are on $\mathbb{Z}_{31}^2 \to \mathbb{Z}_{31}$; the band with $2h = 0$ is on $\mathbb{Z}_{30}^2 \to \mathbb{Z}_{30}$ with $h = 15$. Band curves are exact and deterministic, the random families are means over 8 fields, and every point is an exact enumeration over all votes. Dashed lines mark $1/4$, $1/3$, $1/2$ and chance ($30/31$). The second-homomorphism family breaks at error rate $(1 - 1/q)/2 = 0.484$, and its curve ends at $30/31$ because the two homomorphisms agree on $1/31$ of the inputs.](figures/fig_phase_diagram.svg)

*Scattered wrong values* is the incoherent field of Theorem 4. *Constant offset on a random set* adds the same value $h$ to the output on a random set of inputs. *Second homomorphism* replaces $f$ by another homomorphism $g$ on a random set of density $\rho$ (here $g(a,b) = a + 2b$), which gives error rate $\rho(1 - 1/q)$. The two *band* families add a constant $h$ on a contiguous band of one coordinate, $\{(a,b) : a < \varepsilon p\}$, once with $2h \neq 0$ and once with $2h = 0$.

| Error family | Breaks, predicted | Breaks, measured |
|:-----|:-----|:-----|
| Scattered wrong values (incoherent) | at the finite-size limit $0.781$; not below chance ($0.968$) in expectation | all 8 fields fully correctable up to $0.75$; mean correctable fraction $0.974$ at $0.80$ and $0.123$ at $0.90$ |
| Constant offset on a random set | never: margin $1 - 3\varepsilon + 3\varepsilon^2 \geq 1/4$ | never, at 101 error rates in 8 fields; smallest margin $0.175$ |
| Second homomorphism on a random set | at density $\rho = 1/2$, error rate $0.484$ | fully correctable for $\rho \leq 0.44$; for $\rho \geq 0.56$ the mode is $g$ at every input with $f \neq g$ |
| Band on $\mathbb{Z}_{31}$ with offset $h = 1$, so $2h \neq 0$ | from $11/31 = 0.355$ to $20/31 = 0.645$; $0.677$ of the inputs survive | as predicted at every band width |
| Band on $\mathbb{Z}_{30}$ with offset $h = 15$, so $2h = 0$ | from $8/30 = 0.267$ to $22/30 = 0.733$; half of the inputs survive | as predicted at every band width |
| The same band on $\mathbb{Z}_{30}$ with offset $h = 1$ | from $1/3$ to $2/3$; $0.633$ of the inputs survive | as predicted at every band width |

: **Table 2.** Error rates at which each synthetic family has an uncorrectable input ("breaks"). Band families are deterministic; the others use 8 random fields on an error-rate grid of step 0.01.

Four observations follow. First, the error rate does not determine the outcome: near $\varepsilon = 0.4$ three families are fully correctable, one has lost a third of its inputs and one has lost half. Second, the same offset is harmless on a random set and fatal on a band. On a random set the wrong votes $+h$ and $-h$ each have probability $\varepsilon(1-\varepsilon)$ and never overtake the truth. On a band, an input whose shift exceeds the band width sees every error isolated along its orbit, which is the extremal configuration of Theorem 2. A constant offset on a contiguous region of input space is a plausible failure of a learned model, so the worst case is not exotic. Third, what moves the threshold from $1/3$ to $1/4$ is the order of the wrong value: on the same group and error set, $h = 15$ breaks on $[1/4, 3/4]$ and $h = 1$ only on $[1/3, 2/3]$. Fourth, only the second-homomorphism family is limited by the code. It stays correctable until the table is closer to $g$ than to $f$, and beyond that point the corrector returns $g$: it finds the nearest homomorphism, whatever the labels say.

The incoherent field outlasts every structured family except the random-set offset, up to the finite-size limit of Table 1. Which of these regimes a trained network occupies is an empirical question, taken up next.

# Trained networks: how coherent are their errors? {#sec-trained}

[[SECTION TO BE WRITTEN: the zoo of trained networks, their twirled channels measured exhaustively, a coherence statistic against the depolarizing law, and correctability as a function of error rate, with the training run as the unit of analysis]]

# Twirls and baselines at equal query budget {#sec-baselines}

[[SECTION TO BE WRITTEN: translation twirl, invariance twirl, raw model and other baselines compared at equal numbers of model queries, on organic errors and on answer-dependent errors of trained networks]]

# Other tasks: multiplication without multiplying and a hidden linear map {#sec-other}

[[SECTION TO BE WRITTEN: the four-query bilinear vote on multiplication networks and the two-query vote on networks trained on a hidden linear map, compared with the laws for c = 4 and c = 2]]

# Long chains {#sec-long}

[[SECTION TO BE WRITTEN: horizons of chained computation with trained networks, raw and self-corrected, exact Perron root against the independent-input formula]]

# Label-free evaluation {#sec-eval}

[[SECTION TO BE WRITTEN: the pass rate of the linearity test on trained networks, accuracy and bias of the label-free error estimate, the unconditional bound, and the predicted number of votes]]

# Related work {#sec-related}

**Self-testing, self-correcting and homomorphism codes.** Blum, Luby and Rubinfeld (1993) introduced self-testing and self-correcting programs, including the linearity test and the corrector used here. The random self-reducibility of low-degree polynomials is attributed to Lipton (1991) and to Blum, Luby and Rubinfeld, and Rubinfeld and Sudan (1996) extended testing to polynomials. Bellare et al. (1996) and Ben-Or et al. (2008) relate the pass rate of the linearity test to the distance from the nearest homomorphism. Grigorescu, Kopparty and Sudan (2006) and Dinur et al. (2008) study homomorphisms as codes under adversarial errors, including list decoding. Amireddy et al. (2024) correct linear functions over the Boolean cube up to nearly a $1/4$ fraction of errors, and Hirahara and Shimizu (2026), in a technical report, give random self-reductions for all linear problems when the program is correct on only a small fraction of inputs. These are worst-case analyses. Lecture notes define the corrector by plurality (Rubinfeld, lecture notes; Dinur, lecture notes); we did not find the $1/3$ versus $1/4$ thresholds stated. Our search was limited to web queries, so the absence of a source is weak evidence.

**Random self-reducibility in machine learning.** We are not the first to bring these ideas to learned models. Goldwasser et al. (2025) use techniques inspired by random self-reducibility to remove planted backdoors from a model without detecting them, with guarantees when the ground truth is close to a linear, polynomial or Fourier-heavy function. Their adversary is a malicious trainer and their setting is real-valued regression. To our reading of the abstract and section list (we could not read the full text), they do not characterise correctability through a per-input channel, do not separate coherent from incoherent errors, and do not measure the errors of honestly trained networks. Erata et al. (2026) learn randomized self-reductions automatically for numerical functions; again to our reading of the abstract, that work discovers the identity, whereas we take it as given and ask when voting over it corrects a trained network. Amit et al. (2024) pursue per-input trust by another route, models that output a proof checked by a verifier.

**Voting and its correlated-error limit.** Self-consistency takes the most frequent answer over sampled reasoning paths (Wang et al., 2023), and deep ensembles vote across independently trained models (Lakshminarayanan, Pritzel and Blundell, 2017). Liu (2026) derives bounds on majority-vote accuracy over repeated calls of a language model from the first two moments of per-example correctness; to our reading of the abstract, the same-example correlation, not the one-call accuracy, governs what voting can buy there. Brilliant (2026), in a preprint that is not peer reviewed, argues that correlated errors limit self-correction in language models, and Cordero-Encinar and Duncan (2025) certify that a vote equals the model's modal answer. Meyerson et al. (2025) complete a task of over a million steps by decomposing it and voting at every step, and Mehta (2026) uses agreement across reruns of an agent as an uncertainty signal. In all of these the votes resample the *same* input, so an error that is a stable function of the input cannot be removed. A random self-reduction moves the query across the domain; the limit then shifts from correlation across calls to the coherence of the error field under shifts, which the twirled channel measures exactly.

**Test-time augmentation, group averaging and randomized smoothing.** Averaging predictions over label-preserving transformations of the input (test-time augmentation; Kimura, 2024), over a symmetry group of the task (Foit, Hogg and Villar, 2025) or over noise around the input (Cohen, Rosenfeld and Kolter, 2019) are invariance twirls in our terms. Proposition 6 states what separates them from a transitive twirl.

**Twirling and randomized compiling.** The terms come from quantum information. Twirling a noise process over random unitaries reduces it to a channel with one fidelity parameter (Emerson, Alicki and Życzkowski, 2005), and randomized compiling inserts random gates into a circuit so that coherent and correlated noise becomes stochastic noise (Wallman and Emerson, 2016). We use the vocabulary and the analogy; nothing here is quantum.

**Label-free accuracy estimation.** Jiang et al. (2022) estimate test error from the disagreement of two independently trained networks, and Li et al. (2019) use consistency under known logical relations as a training signal. The linearity test needs one model and an algebraic identity, and it comes with the unconditional bound and the blind spot of Proposition 7.

**Grokking.** Our tasks follow the modular-arithmetic setting of Power et al. (2022), in which small networks generalise long after they fit the training set; Nanda et al. (2023) reverse-engineered the algorithm that small transformers learn for modular addition, and Kvinge et al. (2026) probe which group-theoretic structures such networks capture. These works study how the correct algorithm forms; we study the errors that remain.

**Long-horizon reliability.** Kwa et al. (2025) measure the length of tasks that agents complete with 50% success, and Ord (2025) models such data with a constant failure rate per unit of task length. Ord's later analysis reports that failure rates probably decline over a task, so the constant-rate model should not be taken literally. Proposition 8 gives the corresponding caution in our setting: a constant rate holds only for particular error structures.

# Discussion {#sec-discussion}

[[SECTION TO BE WRITTEN: what the results mean, what would have to be true for them to matter beyond toy algebraic tasks, and open questions]]

# Limitations and what is not shown {#sec-limits}

[[SECTION TO BE WRITTEN: toy scale, the corrector is given the group law, snapshots within a run are correlated, the finite-size estimate is heuristic, unsearched group pairs, limits of the literature search, and every negative result]]

# Reproducibility {#sec-repro}

[[SECTION TO BE WRITTEN: one command per result file, seeds, runtimes, software versions, and the map from every number in the text to a key in results/]]

# Proofs {.unnumbered #sec-proofs}

Throughout, $N_h(x) = |G|\,T_x(h)$ is the number of shifts $r$ with $D_x(r) = h$.

## Proof of Proposition 1 {.unnumbered}

*(a)* Since $f$ is a homomorphism, $V_r(x) = f(x+r) + e(x+r) - f(r) - e(r) = f(x) + D_x(r)$. For uniform $r$ the offset $D_x(r)$ has distribution $T_x$ by definition, and independent shifts give independent offsets, so the counts are multinomial. The plurality returns $f(x)$ exactly when $N_0 > N_h$ for all $h \neq 0$.

*(b)* By the law of large numbers $N_h/k \to T_x(h)$ almost surely for every $h$. If $T_x(0) > T_x(h)$ for all $h \neq 0$, then almost surely $N_0 > \max_{h \neq 0} N_h$ for all large $k$, so $\delta_k(x) \to 0$. If $T_x(0) < T_x(h)$ for some $h$, then $\Pr[N_h > N_0] \to 1$ and $\delta_k(x) \to 1$. If $T_x(0) = T_x(h)$ for some $h \neq 0$, the pair $(N_0, N_h)$ is exchangeable, so $\Pr[N_h \geq N_0] = \Pr[N_0 \geq N_h]$. The two events cover the sample space, so each has probability at least $1/2$, and the first implies failure.

*(c)* Write $t_0 = T_x(0)$ and $t_h = T_x(h) < t_0$. Failure implies $N_h \geq N_0$ for some $h \neq 0$. The difference $N_h - N_0$ is a sum of $k$ independent steps equal to $+1$, $-1$, $0$ with probabilities $t_h$, $t_0$, $1 - t_0 - t_h$. For every $s \geq 1$, Markov's inequality gives
$$\Pr[N_h \geq N_0] \leq \mathbb{E}\left[s^{N_h - N_0}\right] = \left(1 - t_0 - t_h + s\,t_h + t_0/s\right)^k .$$
If $t_h > 0$, the choice $s = \sqrt{t_0/t_h} > 1$ turns the right-hand side into $(1 - (\sqrt{t_0} - \sqrt{t_h})^2)^k$. If $t_h = 0$ the event is $\{N_0 = 0\}$, of probability $(1-t_0)^k$, which is the same expression. Summing over $h \neq 0$ gives the bound. The requirement $s \geq 1$ is where $t_h < t_0$ is used.

*(d)* Let $\mu_h = 1 - (\sqrt{t_0} - \sqrt{t_h})^2$, which increases with $t_h$ on $[0, t_0]$, and $\mu = \mu_{h^*}$. By (c), $\delta_k(x) \leq (q-1)\mu^k$, so $\liminf -\tfrac1k \ln\delta_k(x) \geq -\ln\mu = I_x$. For the other direction, $\delta_k(x) \geq \Pr[S_k \geq 0]$ with $S_k = N_{h^*} - N_0$. Let $s = \sqrt{t_0/t_{h^*}}$ and define a new probability $\tilde{\Pr}$ by the density $s^{S_k}/\mu^k$. Under $\tilde{\Pr}$ the steps of $S_k$ are still independent and equal $+1$ and $-1$ with the same probability $a = \sqrt{t_0 t_{h^*}}/\mu > 0$ each. Therefore
$$\Pr[S_k \geq 0] = \mu^k \sum_{j \geq 0} \tilde{\Pr}[S_k = j]\, s^{-j} \;\geq\; \mu^k\, s^{-1}\, \tilde{\Pr}\left[S_k \in \{0, 1\}\right].$$
For a symmetric walk with steps in $\{-1, 0, 1\}$ the local limit theorem gives $\tilde{\Pr}[S_k \in \{0,1\}] \geq c/\sqrt{k}$ for some $c > 0$ and all $k \geq 1$. (Two values are used so that the argument also covers $a = 1/2$, where $S_k$ has the parity of $k$.) Hence $\delta_k(x) \geq c\, s^{-1} k^{-1/2} \mu^k$ and $\limsup -\tfrac1k\ln\delta_k(x) \leq I_x$. $\square$

## Proof of Theorem 2 {.unnumbered}

For $x = 0$ all offsets are zero and the claims are trivial. Let $x \neq 0$ have order $m \geq 2$. Translation by $x$ partitions $G$ into $|G|/m$ orbits, each a cycle $r, r+x, \dots, r+(m-1)x$. Fix one cycle, write $e_i = e(r + ix)$ for $i \in \mathbb{Z}_m$ and $d_i = e_{i+1} - e_i$; the $d_i$ are the $m$ values of $D_x$ on this orbit. Let $a$ be the number of error points on the cycle, and let $n_0$ and $n_h$ be the numbers of $i$ with $d_i = 0$ and with $d_i = h$. We show
$$n_0 \geq m - 2a, \qquad n_0 - n_h \geq m - 4a, \qquad n_0 - n_h \geq m - 3a \ \text{ if } 2h \neq 0 .$$
Summing over the orbits gives (i), (ii) and (iii).

If $a = 0$ then $n_0 = m$ and $n_h = 0$. If $a = m$ then $n_0 \geq 0 \geq m - 2a$ and $n_0 - n_h \geq -m \geq m - 3a$.

Let $0 < a < m$. The error points split into $R \geq 1$ maximal runs of cyclically consecutive error points, of lengths $L_1, \dots, L_R$ with $\sum_j L_j = a$. Call the difference $d_i$ *touched* if $e_i \neq 0$ or $e_{i+1} \neq 0$. A run of length $L$ touches exactly $L+1$ differences, the $L-1$ inside it and the two at its ends, and no difference is touched by two runs, because two adjacent error points lie in the same run. So $m - a - R$ differences are untouched, and each of them equals 0. Since $R \leq a$, this gives $n_0 \geq m - a - R \geq m - 2a$.

Now consider the $L+1$ differences touched by one run, and let $z$ and $g$ be the numbers of them equal to $0$ and to $h$. Always $g - z \leq L + 1 \leq 3L - 1$. If $L \geq 2$, then $g - z \leq L+1 \leq 2L - 1$. If $L = 1$ and the error value is $u \neq 0$, the two touched differences are $u$ and $-u$; both equal $h$ only if $u = h = -h$, so $g - z \leq 1 = 2L - 1$ whenever $2h \neq 0$. Since only touched differences can equal $h \neq 0$,
$$n_0 - n_h = (m - a - R) + \sum_{\text{runs}} (z - g) \;\geq\; m - a - R - \sum_{j} (3L_j - 1) = m - 4a ,$$
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
$$\mathbb{E}\,\chi(e(x)) = (1 - \varepsilon) + \frac{\varepsilon}{q-1}\sum_{h \neq 0}\chi(h) = 1 - \varepsilon - \frac{\varepsilon}{q-1} = \lambda .$$
The distribution of $e(x)$ is invariant under $h \mapsto -h$, so $\mathbb{E}\,\chi(-e(x)) = \lambda$ as well. The points are distinct, so the errors are independent and $\mathbb{E}\,\chi(S) = \lambda^c$, while the trivial character gives 1. By Fourier inversion on $H$,
$$\Pr[S = h] = \frac1q \sum_{\chi} \overline{\chi(h)}\; \mathbb{E}\,\chi(S) = \frac1q\left(1 + \lambda^c\left(q\,\mathbf{1}[h = 0] - 1\right)\right),$$
which is the claim. The difference of the two probabilities is $\lambda^c$, positive for even $c$ and $\lambda \neq 0$. The queries of the vote, $x + r$ and $r$, are distinct when $x \neq 0$; those of the linearity test, $x$, $y$, $x+y$, when $x \neq 0$, $y \neq 0$ and $x \neq y$; those of the bilinear vote when $a \neq 0$ and $b \neq 0$. $\square$

*The finite-size estimate (heuristic).* For fixed $x \neq 0$ and $h \neq 0$, $N_0(x) - N_h(x) = \sum_r (\mathbf{1}[D_x(r) = 0] - \mathbf{1}[D_x(r) = h])$. Each term has mean $\lambda^2$ and variance $p_0 + p_h - (p_0 - p_h)^2 \approx 2/q$ near chance, where $p_0 \approx p_h \approx 1/q$, and the terms are nearly uncorrelated. The gap is thus approximately Gaussian with mean $|G|\lambda^2$ and standard deviation $\sqrt{2|G|/q}$. The smallest of $n \approx |G|q$ such gaps is about $\sqrt{2\ln n}$ standard deviations below the mean, and setting it to zero gives the estimate in the text. The independence and Gaussian assumptions are not justified here.

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

::: references
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

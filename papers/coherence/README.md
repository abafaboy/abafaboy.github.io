# Beyond the Error Rate: Error Coherence and Voting-Based Self-Correction of Small Networks Trained on Modular Arithmetic

This directory holds the source, code, data and results of a research preprint, published as `index.html` (and `paper.pdf`). The paper asks when voting over a random self-reduction, the self-corrector of Blum, Luby and Rubinfeld, repairs a trained network. It proves an exact per-input criterion and sharp worst-case thresholds for the two-query plurality vote, and it computes exactly the vote channels of 1,373 snapshots from 86 training runs of small networks on modular arithmetic. The finding, for the two-query plurality vote: below the classical worst-case radius the error rate guarantees correction; above it, the worst-input correctability of addition and linear-map networks is limited by the coherence of their errors (for addition networks, mainly output collapse onto a few classes), while multiplication networks break where independent errors of the same rate would. The linear-map result rests on 3 runs.

The paper was conceived, implemented, run and written by AI agents (instances of Claude, built by Anthropic), coordinated by a workflow script in a single session at the request of Abafa Mukhamedov. Verification consisted of the exhaustive and synthetic checks in `code/theory_checks.py`, and, in the same session, a referee pass over the proofs, an audit of the numbers against `results/`, and a rerun of the whole pipeline from a clean checkout, all by AI agents of the same model (see the paper's Limitations). It is not peer reviewed, and no human has verified the proofs, the code or the text.

## Rebuilding everything

Requirements: Python 3 with NumPy, SciPy and Matplotlib (used: Python 3.13.18, NumPy 2.5.3, SciPy 1.18.1, Matplotlib 3.11.2); pandoc for the page (used: 3.1.3); Node with Playwright for the PDF. Everything runs on a CPU. The runtimes below were measured on a 4-core machine, about 27 minutes in total.

From this directory, in this order:

```
python3 code/core.py --selftest                    # library self-tests, about 6 s
python3 code/make_zoo.py                           # trains the zoo: zoo/ and cache/, 136 s, 2 processes
python3 code/zoo_summary.py                        # results/zoo_summary.json, 11 s
python3 code/theory_checks.py                      # paper Sections 3-4 and Figure 1, 47 s, 2 processes
OMP_NUM_THREADS=1 python3 code/exp_channels.py     # Section 5, Figures 2-4, 310 s
OMP_NUM_THREADS=1 python3 code/exp_twirls.py       # Section 7, Figure 6, 199 s
OMP_NUM_THREADS=1 python3 code/exp_tasks.py        # Section 8, Figure 7, 38 s
OMP_NUM_THREADS=1 python3 code/exp_labelfree.py    # Section 10, Figure 9, 273 s
OMP_NUM_THREADS=1 python3 code/exp_horizon.py      # Section 9, Figure 8, 116 s
OMP_NUM_THREADS=1 python3 code/exp_debias.py       # Section 6, Figure 5, 464 s (one process)
python3 build.py                                   # index.html and paper.pdf (python3 build.py --no-pdf: page only)
```

Dependencies between the steps:

- The prediction tables in `zoo/` are committed, so the analysis scripts run without retraining. The logits in `cache/` are not committed (see `.gitignore`), and `exp_twirls.py` needs them, so run `make_zoo.py` first. It rewrites `zoo/` with identical array contents on the same NumPy and BLAS build.
- `exp_channels.py` reads the incoherent-field reference values from `results/theory_checks.json`, and `exp_debias.py` reads the results of `theory_checks.py`, `exp_channels.py` and `exp_tasks.py`.
- `exp_tasks.py` imports the exact plurality routine from `exp_twirls.py`, and `exp_horizon.py` imports helper code from `exp_labelfree.py`. They need the other script's code, not its results.
- Each script that draws figures can redraw them from its saved JSON without recomputing: `--figs-only` for `exp_channels.py` and `exp_debias.py`, `--figure-only` for `theory_checks.py` and the other experiment scripts.
- SVG figures differ between reruns only in matplotlib's random element identifiers and the date; the PNGs are byte-identical.

All seeds are fixed and recorded in the JSON files.

## File map

| Path | Content |
|:--|:--|
| `paper.md` | Source of the paper: Markdown with TeX math, pandoc front matter |
| `build.py`, `template.html` | Build `paper.md` into `index.html` (MathML, no JavaScript) and `paper.pdf` (headless Chromium) |
| `index.html` | The built page |
| `code/core.py` | Library: exact twirled channels (FFT and enumeration), bilinear and invariance channels, exact plurality failure probabilities, linearity-test pass rate, depolarizing law, real voting, zoo loaders; `--selftest` |
| `code/make_zoo.py` | Trains the 86 runs (one-hidden-layer networks, full-batch Adam) and writes `zoo/` and `cache/` |
| `code/zoo_summary.py` | Coverage of the zoo: models per family, error-rate distribution, correctability counts |
| `code/theory_checks.py` | Checks of the statements of Section 3 on synthetic error fields; Figure 1 (`--figure-only` redraws it from the JSON) |
| `code/exp_channels.py` | Trained networks: the mean-vote identity, coherence ratios, correctability per run, failure against votes, the zero-vote mechanism; Figures 2 to 4 |
| `code/exp_twirls.py` | Invariance, translation and concatenated twirls against sampling and an ensemble at equal query budget; Figure 6 |
| `code/exp_tasks.py` | Multiplication with the four-query vote, the hidden linear map and extraction of its secret; Figure 7 |
| `code/exp_horizon.py` | Horizons of chained computation, raw and self-corrected; adaptive stopping; Figure 8 |
| `code/exp_debias.py` | Bias-subtracted voting: subtracting the label-free background predicted by the output histogram from the vote counts; exact asymptotic criterion for all 1,373 models, finite vote counts for six networks, estimated histograms, synthetic and constructed failure cases; Figure 5 |
| `code/exp_labelfree.py` | Label-free error estimate from the linearity test, vote prediction, confidence from the vote margin, nearest homomorphisms, two-network disagreement; Figure 9 |
| `code/paperstyle.py` | Shared figure style |
| `zoo/` | One `.npz` file per training run (argmax prediction table of every snapshot over the whole input group, training mask) and `index.json` (one record per model) |
| `cache/` | Not committed: float16 logits of the memorising networks, written by `make_zoo.py` |
| `results/` | One JSON file per script; every number in the paper is read from these |
| `figures/` | The figures, as SVG (used by the page) and PNG |
| `fonts/` | STIX Two Math (SIL Open Font License, `fonts/OFL.txt`), so equations render the same in every browser and in the PDF |

## What is tested and what is not

Tested:

- Theorem 2 and Proposition 3 (the 1/3 and 1/4 thresholds): every error field on 23 small group pairs with at most 9 elements, and a search by number of errors on 70 more pairs with 10 to 20 elements, of which 7 (ties) and 13 (strict wins) exceeded the search budget.
- The depolarizing law, the finite-size estimate, the twirl comparison, the label-free estimate and the chain formula: simulation on synthetic error fields (`results/theory_checks.json`).
- The exact computations: FFT channels against integer enumeration and brute force (`core.py --selftest`); the exact plurality routine against enumeration and Monte Carlo; the faster evaluators in `exp_twirls.py` and `exp_labelfree.py` against the core routine.
- Exact failure probabilities against real voting, and exact chain survival against simulated chains (the z-scores are stored in the JSON files).
- `exp_debias.py` recomputes the plain criterion and reproduces `exp_channels.json` (1,223 models) and `exp_tasks.json` (150 models) with no mismatch, and the synthetic and i.i.d. thresholds of `theory_checks.json` exactly; its exact recursion for the bias-subtracted rule matches brute-force enumeration (largest difference 4e-15) and, without the shift, the core plurality routine.
- Determinism: during the work, the zoo was built twice with identical array contents, and `theory_checks.py`, `exp_channels.py`, `exp_twirls.py`, `exp_horizon.py` and `exp_debias.py` were each run twice with identical results apart from timings. A final rerun of the whole pipeline above from a clean checkout on the same machine reproduced all nine results files with no differing value apart from timing fields, all `zoo/` files byte for byte and all PNG figures byte for byte; each step took at most about 22% longer than listed. Afterwards, Figures 1, 2 and 6 were redrawn from the JSON with relabelled legends (Figure 1 also resized, with the band curves drawn at their grid points).

Not tested:

- No proof has been checked by a human or by a proof assistant; the exhaustive checks cover small groups only.
- Reproducibility was checked only on the same machine and software versions; identical tables are expected only on the same NumPy and BLAS build.
- Nothing at scale: groups have at most 2,809 elements, there is one architecture family, one optimiser and one weight-decay value (1) where weight decay is used, and nothing about language models.
- The finite-size estimate of the incoherent limit is a heuristic; only a much weaker rigorous bound is proved. The bias-subtracted rule was devised after the zero-vote mechanism was found and evaluated on the same networks, with no held-out runs. Failure probabilities below 1e-10 are bounds, not exact values. Horizons above 1e4 steps were computed, not simulated.
- The search for prior work used web search only; arXiv and the main bibliographic services were unreachable from the build machine, and no cited work was read in full text.

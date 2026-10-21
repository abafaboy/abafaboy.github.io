# Clarity pass: chapters 29–32

Completed 21 October 2026. Read SCRIPT_CLARITY_BRIEF.md, SCRIPT_FORMAT.md including Letterer features, CODEX_SCRIPT_BRIEF.md section 3, the complete STORY_BIBLE.md and its foreshadowing ledger, all four assigned scripts, and chapter 28's final ten story panels and end card. Checked the relevant chapter beats and continuity rulings.

All panels in these four chapters were **unlocked**: no matching `chapters/chNNN/art/<id>.png` existed during the initial and final checks. No images were generated.

## Change counts

“Rewritten” counts final dialogue/narration text entries with changed wording, including one entry formed by combining two bubbles. Metadata-only changes do not count as rewrites. “Moved” counts entries transferred to another existing panel; a moved entry can also be rewritten. “Off-panel” counts final entries newly marked `offpanel:<id>`. “Side” compares each entry with its original source, including moved entries. Counts overlap.

| Chapter | Rewritten | Moved | Marked off-panel | Corrected side | Reshaped panels |
|---|---:|---:|---:|---:|---:|
| 29 | 34 | 0 | 3 | 1 | 24 |
| 30 | 27 | 0 | 9 | 0 | 19 |
| 31 | 40 | 5 | 13 | 1 | 18 |
| 32 | 24 | 1 | 9 | 1 | 17 |

No panels were added, split, merged or renumbered. Every existing ID remains in its original reading order.

## Chapter 29 — Paperwork

Named the two arrival cards, Orrin, the rice ball, the laundry errand, the mineral deposit and the proposed load path. Kept Dami's wall, the last van's seizure, the pocket gag and Taeo's apology beats. Moon still mends in silence, refuses money, permits the fresh carving and freezes at Kett's mark; PAYOFF P04 notes remain intact.

No lines moved between panels. Combined the office's two phone bubbles in P16 into one off-panel line, so the detail shot has only one unseen voice. Marked Nib in P07 and Taeo in P47 off-panel. Corrected Minho's P06 side to the right, beside the southeast van. Added explicit speaker positions and expanded object-only frames where dialogue needs visible faces.

Reshaped:
- wide → tall: P01, P04, P08, P12, P15, P17, P21, P23, P28, P39, P42, P46, P48, P55.
- wide → full: P10, P35, P43, P50.
- inset-l → full: P18, P24.
- narrow-r → tall: P29, P34.
- inset-l → wide: P44.
- strip → tall: P45.

**NEEDS REDRAW:** None. No locked panels.

## Chapter 30 — The Rim

Clarified Orrin's shell rim, the foreleg load path, the padded brace, the fee and whose licence is being used. Preserved “YOU MEASURED ME. YOU DIDN'T ASK ME.”, the voluntary ₩300,000/₩1,700,000 contributions, the ₩2,000,000 total, Minho's central award and Seonhee's authorization. Nib now says he will keep the receipt, matching the following action.

No lines moved between panels. Marked unseen close-up speakers and call voices off-panel. Expanded P49 into a visible two-shot. Grandpa's concern, Taeo's genuine pause before “IT'S FINE,” and the complete threshold exchange remain. No additional load test, percentage gain or injury was introduced.

Reshaped:
- wide → tall: P02, P08, P10, P14, P17, P19, P21, P23, P25, P29, P31, P32, P46, P48, P50.
- wide → full: P06.
- inset-l → full: P11.
- inset-r → full: P45.
- inset-l → wide: P49.

**NEEDS REDRAW:** None. No locked panels.

## Chapter 31 — Two Pulses

Clarified the approach, mineral collection, private rest conversation, link permissions and unfinished brace. Preserved both exact dreams, Kett's ledge mark, two filled cases collected while the boss lives, the intact survey line and the early-charge hook. Taeo still cannot hear the private dreams or see through the links.

Moved five entries:
- Orrin's link permission: P08 → P06, where he is visible and Nib holds the keyed relay handset toward him. Changed its delivery to local speech and its side from left to right.
- Nib's fifty-metre report: P14 → P13.
- Nib's packed-deposit report: P26 → P25, before Taeo asks how they are.
- Sejin's blood-pressure/link-release instruction: P41 → P42.
- Taeo's brace question: P52 → P51, as a call through Nib's radio.

Combined Nib's two binocular-view lines in P12 into one off-panel line. Preserved every existing silent panel, including Orrin's return-mark detail in P07.

Reshaped:
- wide → tall: P03, P04, P10, P18, P24, P26, P41, P43, P47, P50.
- wide → full: P12, P14, P20, P21, P27, P46.
- narrow-l → tall: P15.
- inset-r → full: P16.

**NEEDS REDRAW:** None. No locked panels.

## Chapter 32 — Change the Angle

Named the forefoot, brace angle, consent to share the load, return marks and new horn fragment. Kept the prepared glancing turn, cliff collision, boss falling into the void, 21% load share and Taeo's recoil. Orrin's shell remains intact. The horn remains window 4's first new kind, consumed for +34%; the deposit stays separate sale cargo.

Moved Nib's consent from P10 → P09, where his face and keyed radio are visible; P10 now has Orrin's remote consent and Taeo's reply. Added Haein to P48's foreground so her central-return announcement has a visible speaker. Corrected Sejin's P46 side to the centre. The handshake, Minho's successful central run and final “EAST TERRACE. CLEAN.” remain.

Reshaped:
- wide → tall: P03, P07, P14, P17, P19, P23, P31, P35, P37, P40, P46.
- wide → full: P10, P50, P53.
- inset-r → wide: P36.
- inset-l → full: P38.
- vignette → tall: P47.

**NEEDS REDRAW:** None. No locked panels.

## Validation and final checks

Each chapter passed `tools/validate_script.py` before revision began on the next chapter. Each final file reports **OK, zero errors, zero warnings**. Used the bundled Python executable because the shell's `python` resolves to the Windows Store alias; the validator imports the existing `tools/yaml` package.

| Chapter | Panels | Silent | Chibi | Tall/bleed | Taeo float lines |
|---|---:|---:|---:|---:|---:|
| 29 | 57 | 17 | 1 | 20 | 3 |
| 30 | 53 | 10 | 2 | 18 | 3 |
| 31 | 54 | 12 | 1 | 15 | 5 |
| 32 | 56 | 7 | 1 | 18 | 6 |

Tall/bleed coverage exceeds one quarter in every chapter. Reviewed all three-speaker panels for visible faces and matching positions, checked close-up/off-panel limits, and retained the chapter hooks, prices, percentages, return rules, props, silent beats, comedy and plant/payoff notes. Changes made by this pass are limited to ch029.yaml, ch030.yaml, ch031.yaml, ch032.yaml and this report.


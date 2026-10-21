# Clarity pass: chapters 075–078

Applied SCRIPT_CLARITY_BRIEF.md to scripts/ch075.yaml through scripts/ch078.yaml. No images generated. All panels were unlocked when checked. No panels were added, split, merged, removed or renumbered; three pairs of dialogue bubbles were combined.

Counts track individual source `lines` entries whose text was rewritten, including float narration, tags and footnotes. A source line counts once even if revised again; combining two source bubbles counts as two rewritten lines. Off-panel counts track resulting line entries newly marked `offpanel:<id>`. Movement, attribution and side changes are separate counts and can overlap with rewrites.

| Chapter | Lines rewritten | Lines moved | Lines marked off-panel | Side corrections | Panels reshaped | Tall/bleed |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 075 | 34 | 1 | 8 | 3 | 13 | 13 / 52 |
| 076 | 18 | 0 | 3 | 0 | 13 | 13 / 50 |
| 077 | 64 | 2 | 10 | 4 | 18 | 15 / 60 |
| 078 | 22 | 0 | 4 | 2 | 15 | 17 / 54 |

## Chapter 075 — Sorry Properly

Named Channel B and the predator in Sera's account, made the shared stop rule explicit, and clarified the flute, draft and diagram exchanges. Preserved the required apology and response verbatim, the visitor-tax joke, Sera's continuing anger, and Kesh's exact loop hook.

- Moved Taeo's offer to help from the P44 pencil detail to P43. P43 now shows Kesh left, Taeo centre and Haein right.
- Combined P01's repeated hook into one phone bubble, retaining every word. Both P01 and P03 mark Nib's radio voice off-panel.
- Other off-panel lines: P10 Sera; P30, P33, P35 and P45 Taeo; P44 Kesh.
- Side corrections: P33 Sera left to right and Taeo right to left; the moved Taeo line right to centre at P43.
- Reframed P22 and P48 as medium two-shots with both speaking faces visible. Specified speaker positions and waist-up crops elsewhere.
- Added/split panels: none.
- Reshaped to tall: P04, P06, P10, P11, P13, P18, P20, P25, P32, P41, P47.
- Reshaped to full: P34, P46.

### NEEDS REDRAW

None. No art exists for these panel IDs.

Validation: **OK**, no warnings. 52 panels, 10 silent panels, 2 chibi panels, 6 float lines.

## Chapter 076 — One Word

Clarified the shorts repair, folded backing, payment refusal and counter-mark observations. Kept the opening repair misunderstanding, pocket jokes, private changing, existing thigh repair and new knee patch. Moon still speaks only “THAR.” Nib's shocked question and the older fork reveal remain unchanged.

- Combined P11's two lines into one off-panel bubble over the repair detail.
- Other off-panel lines: P04 and P20 Nib.
- No lines moved; no side values changed.
- Added explicit staging for the two different adult heights and full seated bodies. Tightened P08 to Nib's face, hands and bag handle.
- Added/split panels: none.
- Reshaped to tall: P01, P10, P14, P16, P19, P27, P28, P31, P45, P48.
- Reshaped to full: P03, P09, P25.

### NEEDS REDRAW

None. No art exists for these panel IDs.

Validation: **OK**, no warnings. 50 panels, 24 silent panels, 2 chibi panels, no float narration.

## Chapter 077 — The Loop

Explained the echo as sound taking a physical route, with the existing twelve-second delay and open/closed-branch controls intact. Clarified the collector, finite reservoir, timing contacts, supported bow, medical conditions and everyone's stop authority. Preserved the timing values, PAYOFF P15, Moon's unresolved history, gradual recovery/testing interval, complete Channel B record and exact gate-side hook.

- Moved Kesh's first P17 line to P16, leaving one off-panel line over the contact detail.
- Moved Taeo's P49 reply to the beginning of P51, after Haein's record-retention statement and the silent tapping-plate detail. The reply remains about retaining the whole Channel B failure.
- Combined P46's two explanation bubbles into one off-panel line over the plan.
- Off-panel lines: P07 Taeo; P09, P11 and P17 Kesh; P25 Haein; P35 and P36 Taeo; P37 Sera; P46 Taeo; P49 Haein.
- Side corrections: P42 Taeo right to centre; P45 Nib right to centre; P47 Taeo right to centre; the moved record reply from left at P49 to right at P51.
- P42, P45 and P47 explicitly show all three speakers. Reframed P27 and P52 so their speakers' faces are visible.
- Added/split panels: none.
- Reshaped to tall: P03, P04, P06, P13, P16, P19, P20, P21, P22, P28, P37, P42, P45, P54.
- Reshaped to full: P12, P26, P47, P48.

### NEEDS REDRAW

None. No art exists for these panel IDs.

Validation: **OK**, no warnings. 60 panels, 12 silent panels, 2 chibi panels, 4 float lines.

## Chapter 078 — The Shot

Named the wave, target opening, dump deadline and return marks so the battle reads as a sequence of visible decisions. Kept the staggered contacts, bounded wave impulse, 0.8-second storage limit, supported injured LEFT arm, shot and boss death, five-person return order, 22-second completion, concealed recovery-net contents and exact final hook.

- Off-panel lines: P09 Haein; P21 the predator's copied radio voice; P38 Sejin; P42 Minho.
- No lines moved or combined.
- Side corrections: P02 Sejin right to centre; P10 Taeo right to centre. Both panels explicitly show all three speakers.
- Made Minho and Haein visible during the final return count. Clarified medium framing at the controls and retained Taeo's RIGHT forearm wrap/support and LEFT-hand knock.
- Added/split panels: none.
- Reshaped to tall: P07, P10, P12, P13, P16, P21, P26, P39, P41, P42, P44, P45.
- Reshaped to full: P02, P06, P48.

### NEEDS REDRAW

None. No art exists for these panel IDs.

Validation: **OK**, no warnings. 54 panels, 10 silent panels, 1 chibi panel, 3 float lines.

## Final checks

Each chapter passed `python tools/validate_script.py scripts/chNNN.yaml` before editing began on the next chapter; the final refinements were validated again in chapter order. Validation used the bundled Python 3.12 interpreter and the validator's bundled YAML module.

All four scripts retain their original panel IDs, story events, plant/payoff notes, UI entries, title/end cards and hooks. Dialogue remains in CAPS and within the 18-word limit; inset/narrow lettering stays within 12 words. Panels have at most three spoken lines; three-speaker panels draw all three people. Close-ups have at most one off-panel line. At least a quarter of each chapter's panels are tall or bleed.


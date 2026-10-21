# Clarity pass: chapters 33, 39, 40 and 42

Completed against `SCRIPT_CLARITY_BRIEF.md`, `bible/SCRIPT_FORMAT.md`, `CODEX_SCRIPT_BRIEF.md` section 3, and the cast, motifs and foreshadowing in `bible/STORY_BIBLE.md`. Read chapter 32's closing panels for the opening continuity.

Only the four assigned YAML scripts and this report were edited in the project. No images were generated. None of the assigned panels had an existing `chapters/chNNN/art/<id>.png` at the checks before editing or at the final audit. Existing panel IDs, story events, monetary amounts, plants, payoffs and hooks were preserved.

Counts refer to existing dialogue/narration entries: a rewritten line has changed text; a moved line changes panels; an off-panel count means a newly added `offpanel:` prefix; a side correction changes an existing `side` value. Categories can overlap. The one additional bridging line is listed separately.

| Chapter | Lines rewritten | Lines moved | Newly marked off-panel | Sides corrected | Panels | Tall / bleed |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 33 | 28 | 0 | 4 | 4 | 53 | 18 |
| 39 | 32 | 0 | 0 | 1 | 50 | 21 |
| 40 | 31 | 2 | 9 | 0 | 52 | 17 |
| 42 | 22 | 1 | 3 | 4 | 50 | 20 |

## Chapter 33 — Surplus

- Clarified the crew settlement, equal ownership, lease contributions, monthly rent, separate doors and dinner exchanges. Preserved the soil joke, Eunchae's second-attempt pass, sponsor change and emergency dispatch hook.
- Marked Seonhee at P19, Taeo at P23, and both dispatch lines at P52 off-panel. Corrected Seonhee's side at P14, Eunchae's at P45, and both dispatch lines to the central phone at P52. Added explicit positions for drawn speakers.
- Reshaped to `tall`: P03, P04, P06, P08, P09, P14, P15, P18, P20, P22, P29, P33, P39, P51.
- Reshaped to `full`: P13, P37, P42. Reframed P36 to show Taeo's face during Eunchae's news and P43 as a medium two-shot.
- Panels added, split or merged: none. Dialogue lines added: none.

### NEEDS REDRAW

None. No locked panels were present.

## Chapter 39 — Good Work

- Made the insult, offered blanket, evacuation lane, stair supports, Side Passage F and old door design explicit. Kept Nib's contained hurt and pride, Seoryun's exact recognition line, and the exact patch hook.
- Corrected Sejin's P28 side to the centre and specified where each speaker appears. Preserved the existing off-panel lines at P21 and P40; no new off-panel markings were needed.
- Reshaped to `tall`: P02, P03, P07, P09, P11, P14, P16, P17, P20, P23, P25, P26, P28, P32, P34, P38, P41, P43.
- Reshaped P01 to `full`. Reframed conversation shots so speaking faces remain visible, including the three speakers at P28.
- Panels added, split or merged: none. Dialogue lines added: none.

### NEEDS REDRAW

None. No locked panels were present.

## Chapter 40 — Why the Patch

- Distinguished present-day voices from the Seogang portraits, contract insert, childhood TV scene and Kang memory. Clarified the rescue delay, Kang's loss and the proposed rescue network without changing the separate incidents or the bill's pending status.
- Moved the shared-site line from P10 to P08 and the line about keeping the patch visible from P25 to P24. Each close-up/insert now has at most one off-panel spoken line.
- Newly marked Taeo off-panel at P09, P10, P11, P16, both P17 lines and P25; Seoryun at P28; dispatch at P44. Preserved the existing reporter voice at P18 and Seoryun's off-panel reply at P37.
- Added one short line at P22 identifying Taeo's father immediately before the unchanged required line, “YOU WENT BACK FOR PEOPLE LIKE HIM. NOBODY WENT BACK FOR HIM.” This gives both instances of “HIM” an immediate referent.
- Reshaped to `tall`: P02, P03, P20, P21, P24, P26, P27, P28, P30, P34, P36, P38, P40, P48. Reshaped P18 to `full` for the boy holding baby Haru.
- Panels added, split or merged: none. The Thursday invitation and its deliberate pause before “BRING NIB” remain intact.

### NEEDS REDRAW

None. No locked panels were present.

## Chapter 42 — The Plaque

- Clarified the routine appointment, memorial silence, rescue knot, casualty question, consenting pressure test and final bruise observation. Preserved the four-hundred-gate history, the exact `ANOMALOUS ENTITIES: 0` labels, Moon's single flower and eye contact, and the unanswered mystery.
- Moved Orrin's consent from the P37 hand insert to P36, where Sejin, Taeo and Orrin are all visibly drawn. P37 retains one off-panel consent line from Nib.
- Newly marked Nib off-panel at P10 and P37, and Grandpa inside the office at P35. Corrected Ara's two P12 lines to the centre, Nib's P40 line to the centre, and Orrin's moved consent to the centre at P36.
- Reshaped to `tall`: P01, P02, P05, P06, P08, P12, P13, P14, P17, P18, P26, P29, P32, P36, P40, P44, P47, P48.
- Reshaped to `full`: P09, P19, P28, P35. Kept Moon's P27 portrait cropped to face and shoulders and made the final standing figures spacious.
- Panels added, split or merged: none. Dialogue lines added: none.

### NEEDS REDRAW

None. No locked panels were present.

## Validation

Each chapter reported **OK**, with no warnings, from `tools/validate_script.py` before work began on the next assigned chapter. After the final framing audit, the validator was rerun on all four scripts and again reported **OK** with no warnings.

| Script | Silent panels | Chibi story panels | Taeo float lines |
| --- | ---: | ---: | ---: |
| `ch033.yaml` | 7 | 2 | 3 |
| `ch039.yaml` | 9 | 2 | 5 |
| `ch040.yaml` | 10 | 1 | 6 |
| `ch042.yaml` | 16 | 1 | 3 |

The final audit also checked spoken-line sides, speaker references in art briefs, the three-line limit, off-panel limits in close-ups/inserts, and the quarter-chapter minimum for tall/bleed panels. No issues remained. Existing silent beats, chibi gags, UI kinds, plant/payoff notes and end cards were retained.

# Clarity pass: chapters 21, 22, 23 and 26

Revised only `ch021.yaml`, `ch022.yaml`, `ch023.yaml` and `ch026.yaml` in the repository, plus this report. No images generated. None of the assigned chapters had an art directory at either the opening or final check; all revised panel compositions were unlocked. Existing panel IDs remain unchanged.

Counts below refer to `lines` entries. Rewritten means an existing entry's text changed, including shortened or merged bubbles. Moved entries also count as rewritten when their text changed. Off-panel and side counts describe changes to attribution and placement, so the columns overlap. Art staging was also made explicit wherever a speaking character's position needed clarification.

| Chapter | Rewritten | Moved to another panel | Newly marked off-panel | Corrected `side` | Final panels | Tall/bleed |
|---|---:|---:|---:|---:|---:|---:|
| 21 | 25 | 2 | 5 | 1 | 61 | 19 |
| 22 | 42 | 1 | 16 | 10 | 61 | 21 |
| 23 | 26 | 4 | 7 | 1 | 59 | 18 |
| 26 | 23 | 0 | 8 | 2 | 56 | 15 |

## Chapter 21 — Not Requested

- Split P26's bumper insert and replies across P26 and new **P26a**. The insert keeps Haein's single off-panel question; Nib's answer and Haein's Bluebird joke move into a visible two-shot.
- Added one spoken entry at **P37**: Taeo reads the return-route result aloud before Chae responds. She still cannot see his interface.
- Clarified the draw button, summon circle, watch spot, return request and neighbour's watch over the open door. Marked absent video-call speakers, Taeo outside Nib's close-up, and Nib outside the coffee hand insert. The apology, open door, cup, Kett mark, permitted amber pulse, coffee welcome and housing-notice hook remain.
- Reshaped to **tall**: P01, P02, P07, P08, P12, P18, P19, P20, P21, P23, P29, P39, P42, P49, P51.
- Reshaped to **full**: P48.
- Taeo float narration: **4** entries.

### NEEDS REDRAW

None. No locked panels.

## Chapter 22 — The Zone

- Split P08's call across P08 and new **P08a**, moving the landlord's final deflection and hang-up into the new reaction close-up. Each close-up now has at most one unseen line.
- Clarified the deposit promise, building sale, room size, window surcharge, exam, property listing, link permission and invitation. Present-day Eunchae's account is explicitly off-panel over the memory images.
- Reframed P39 to show Nib's face and hands, with Minho's single off-panel warning. All three-speaker compositions have the speakers visible; absent phone and close-up voices are marked.
- Preserved the exact housing figures, salt-iron integration, winged candidate, **PLANT P10** refusal, reset to 0%, and final expensive-manners exchange. The price conversion below P29 remains a footnote beneath its three main entries.
- Reshaped to **tall**: P02, P06, P09, P12, P19, P20, P26, P28, P31, P45, P53, P58.
- Reshaped to **full**: P14, P55.
- Reshaped to **wide**: P39, P43.
- Taeo float narration: **6** entries.

### NEEDS REDRAW

None. No locked panels.

## Chapter 23 — Same Kind

- Moved Taeo's archive observation from **P11 to P12**, Dami's doorway reply from **P29 to new P29a**, Taeo's tin reply from **P41 to P42**, and his ownership reminder from **P45 to P44**. The object inserts each retain only one off-panel voice.
- Removed P12's redundant float observation to keep the visible three-person exchange to three entries. Clarified what sells, what raises alignment, the new material types, the collection fee, the blocked doorway and the candidate's unknown size.
- Added **P29a** as a waist-up doorway two-shot; no new story event. Reframed P42 to show the walking speakers' faces, and P55 to give standing Nib room.
- Corrected the opening roof description to the established workshop roof from chapters 21–22. Preserved both **PLANT P11** zero gains, the archive rule, van seizure, Seonhee's collapse, collector confrontation, terrace-clay and copper-moss order, and Orrin's anonymous **[ACCEPTED]** hook.
- Reshaped to **tall**: P04, P07, P14, P16, P17, P18, P23, P24, P25, P27, P30, P39, P42, P43, P55.
- Reshaped to **full**: P09, P28.
- Taeo float narration: **5** entries.

### NEEDS REDRAW

None. No locked panels.

## Chapter 26 — Fair and Square

- Marked the absent opening speaker, assessor, radio respondent, collector and map speaker off-panel. Clarified the scaffold exchange, practical instructions, benchmark, debt offer, housing refusal and container terms.
- Merged Chae's two briefing bubbles at **P07** into one off-panel entry; merged Minho's two map-insert bubbles at **P50** into one off-panel entry. No bubbles moved between panels and no panels added.
- **P16 intentionally retains a bad practical order:** four rushed commands leave the recipient and direction unspecified. P17 immediately identifies the confusion; P19 supplies named, explicit orders. This preserves the reason Taeo loses while making the reader understand the mistake. The dummy is named, and Orrin's later advice names the missing instruction.
- Preserved the identical courses, sixty-second closure, 120-second limit, Taeo's 123 seconds, Minho's 94 seconds, ₩310,000,000 debt, half-forgiveness offer and refusal, original thirty-day notice, container agreement, Friday routes and Orrin's off-panel hook. No LOAD SHARE name or effect added.
- Reshaped to **tall**: P02, P04, P06, P10, P14, P15, P20, P22, P24, P30, P37, P45.
- Reshaped to **full**: P09, P17, P25, P41.
- Taeo float narration: **4** entries.

### NEEDS REDRAW

None. No locked panels.

## Validation

Ran `python tools/validate_script.py scripts/chNNN.yaml` after each chapter and obtained **OK before starting the next chapter**. Rechecked the final versions after the final staging edits. The bundled Python runtime was used; the validator imports its existing `tools/yaml` package.

| File | Result | Panels | Silent | Chibi | Warnings |
|---|---|---:|---:|---:|---:|
| `ch021.yaml` | OK | 61 | 12 | 2 | 0 |
| `ch022.yaml` | OK | 61 | 5 | 2 | 0 |
| `ch023.yaml` | OK | 59 | 7 | 2 | 0 |
| `ch026.yaml` | OK | 56 | 7 | 1 | 0 |

Additional script review checked visible speaker staging, off-panel sides, close-ups with at most one off-panel entry, three-speaker visibility, room for full figures, the quarter-tall/bleed target, stable original IDs, bubble limits, CAPS, float limits and preservation of the chapter hooks and foreshadowing notes.

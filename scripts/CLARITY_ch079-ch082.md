# Clarity pass: chapters 79–82

Followed `SCRIPT_CLARITY_BRIEF.md`, the script format and letterer rules, section 3 of `CODEX_SCRIPT_BRIEF.md`, the cast voices and foreshadowing ledger, and chapter 78's final ten panels and end card. Changed only the four assigned scripts and this report. No images generated.

Counts below compare the delivered scripts with their starting versions. “Rewritten” counts changed `lines[].text` entries, including Taeo's float narration. Counts overlap when one line received both a rewrite and a speaker correction. Art directions and UI text are excluded from line counts.

| Chapter | Lines rewritten | Lines moved | Newly marked off-panel | Lines with corrected `side` | Panels | Tall/bleed |
|---|---:|---:|---:|---:|---:|---:|
| 79 | 43 | 0 | 4 | 2 | 49 | 15 |
| 80 | 34 | 0 | 5 | 0 | 52 | 13 |
| 81 | 46 | 0 | 12 | 2 | 52 | 13 |
| 82 | 36 | 0 | 6 | 0 | 50 | 13 |
| **Total** | **159** | **0** | **27** | **4** | **203** | **54** |

No panels were added, split, merged or renumbered. No lines needed to move between panels: off-panel attribution and roomier compositions resolved the staging problems. All four chapters have at least one quarter of their panels tall or bleed. Every speaking composition now specifies speaker positions; wide conversation panels use waist-up framing. Detail panels retain their close framing and identify unseen speakers as off-panel.

## Chapter 79 — Aftermath

Made the test-record discussion explicit about Channel B, the original order, witness corrections, the supported shot and the 0.8-second force-storage limit. Clarified what cooperative ownership could change while keeping the route untested. Named the cylinder, cable sleeve, settlement mark and Ilan where vague pronouns slowed the reveal. Preserved Sera's injury, consent over her statement, Seoryun's `GOOD.`, and the sealed-cylinder hook.

- **Reshaped to tall:** P01, P05, P10, P12, P19, P22, P24, P26, P28, P36, P39, P41, P43, P47.
- **Reshaped to full:** P09, P35.
- **New off-panel lines:** Chae in P23, P25 and P32; Taeo in P38.
- **Corrected sides:** Taeo in P35 to centre; Sera in P45 to centre.
- Added explicit positions throughout the speaking panels and waist-up framing to the remaining wide conversations.

### NEEDS REDRAW

None. No assigned panel had existing art when checked before editing or during the final audit.

## Chapter 80 — Responsibilities

Clarified that the handwriting is Ilan's, the letter is from River Year 306, and its evidence is a year old. Preserved the original letter passages and all four `PLANT P18` notes. Kept Sera's relief, anger and pride, her ownership of the letter, and the distinction between finding Ilan and assuming he needs rescue. Clarified the declined booking, shared control of relay work, medical stop authority and Nib's right to leave. The charter hook remains unchanged.

- **Reshaped to tall:** P08, P09, P21, P22, P24, P25, P29, P32, P35, P39, P40.
- **Reshaped to full:** P30, P41.
- **New off-panel lines:** Sera in P15 and P16; Chae in P23; Haein in P36; Taeo in P42.
- Added explicit speaker positions and waist-up framing to wide conversations; standing departures, Kesh's seated height and ensemble scenes have vertical room.

### NEEDS REDRAW

None. No assigned panel had existing art when checked before editing or during the final audit.

## Chapter 81 — The Paperwork Is the Door

Named the charter, membership form, permit law and voting rules directly. Kept all five licence requirements, including the exact ₩300,000,000 capital requirement, separate from the proposed cooperative structure. Clarified wages, ownership shares, exit terms and legal review without granting approval. Kept the paperwork jokes and the gold-edged invitation hook.

- **Reshaped to tall:** P02, P18, P19, P21, P23, P24, P28, P30, P32, P35, P36, P42.
- **Reshaped to full:** P09, P31.
- **P34:** changed from a hand-detail strip to a waist-up wide two-shot of Sera and Taeo, so both speakers are visible.
- **P21:** changed the camera to show Sejin, Haein and Taeo together, with all three faces visible.
- **New off-panel lines:** Nib in P03; Chae in P08, P11, P15 and P16; Taeo in P20, P25, P30 and P35; Sera in P26 and P29; the messenger in P43.
- **Corrected sides:** Haein in P21 and P23 to centre.
- Added explicit positions and suitable body framing throughout the other speaking panels.

### NEEDS REDRAW

None. No assigned panel had existing art when checked before editing or during the final audit.

## Chapter 82 — Meridian

Made Meridian's financing, recovery pay, board control of jobs and control of the remote method explicit. Clarified the leave discussion and Channel B argument while preserving Baek's reasonable appeal and his idealism line. Kept the offer unsigned, the crew review pending and Minho undecided. Minho's final two hook lines remain verbatim.

- **Reshaped to tall:** P02, P06, P09, P10, P11, P25, P36, P37, P40, P43, P44.
- **Reshaped to full:** P08, P42.
- **P14:** changed the camera to a medium two-shot with Baek's and Taeo's speaking faces visible.
- **New off-panel lines:** Nib in P03, P38 and P39; Baek in P23 and P29; Taeo in P34.
- Added explicit positions and waist-up framing to meeting-room conversations. Tower arrivals, corridor scenes, departures and the roof approach now give bodies vertical room.

### NEEDS REDRAW

None. No assigned panel had existing art when checked before editing or during the final audit.

## Validation

Ran `python tools/validate_script.py scripts/chNNN.yaml` after each chapter and obtained `OK` before editing the next. The final run across all four scripts also reports `OK` with no errors or warnings:

| Script | Result | Silent panels | Chibi panels | Float lines |
|---|---|---:|---:|---:|
| `ch079.yaml` | OK | 8 | 2 | 5 |
| `ch080.yaml` | OK | 8 | 2 | 2 |
| `ch081.yaml` | OK | 7 | 2 | 3 |
| `ch082.yaml` | OK | 9 | 2 | 5 |

Also checked that every panel has at most three lines, every spoken line has a side, and no close-up or detail panel contains more than one off-panel line. Existing IDs, silent beats, chibi beats, plant notes, continuity facts and chapter hooks are retained.

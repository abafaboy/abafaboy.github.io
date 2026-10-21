# Clarity pass: ch096

Read `SCRIPT_CLARITY_BRIEF.md`, `bible/SCRIPT_FORMAT.md` including Letterer features, `CODEX_SCRIPT_BRIEF.md` section 3, the complete story bible including voices and foreshadowing, chapter 96 in full, and chapter 95's last ten panels and end card. Checked the adjacent chapter beats and continuity rulings.

## Chapter 96: The Re-run

All panels were unlocked: no `chapters/ch096/art/<id>.png` files existed during the pass. Existing panel IDs, events, continuity facts, title, end card and final hook are preserved. No images were generated.

### Line changes

| Change | Count | Details |
|---|---:|---|
| Existing lines rewritten | 29 | 24 spoken lines and 5 Taeo float lines. Named Taeo in the jump instruction, anchor fragments in scoring, the force transfer and irregular heartbeat in the medical conversation, and the presentation and contest in family dialogue. Preserved the dinosaur jokes and Haru's mistaken T. rex arms. |
| Lines moved between panels | 0 | Clear framing and off-panel attribution kept every line in its original panel. |
| Lines marked off-panel | 3 | Taeo's replies in P20, P40 and P49 now use `offpanel:taeo`, all with `side: r`. Each close-up shows the other speaker and contains exactly one off-panel line. |
| Existing `side` values corrected | 1 | P10: Sejin changes from `l` to `c`; Dara is left, Sejin middle, Taeo right, all drawn. |
| UI message entries edited, counted separately | 7 | P11: 2; P16: 3; P44: 2. Applied CAPS, specified Haru's 2:00 PM start, and made Sejin's return examination explicit. |

Added explicit screen positions for drawn speakers. Reframed P08 as a two-shot and P42 as a shot showing both faces and hands. Kept phone-hand kit panels, the 5:00 AM departure, 16:40 return coach, injuries, no-transfer rest day, and examination before final-day work.

### Panel changes

No panels added, split, merged or removed. The chapter remains 52 panels.

17 existing panels reshaped:

| New shape | Panels and previous shape |
|---|---|
| `tall` | P01 (`wide`), P04 (`wide`), P07 (`wide`), P08 (`inset-r`), P09 (`vignette`), P14 (`wide`), P26 (`wide`), P28 (`wide`), P33 (`wide`), P38 (`wide`), P43 (`wide`), P48 (`wide`) |
| `full` | P10 (`wide`), P19 (`wide`), P34 (`inset-l`), P36 (`wide`), P42 (`strip`) |

P03 and P51 remain tall, giving 14 tall panels out of 52 (26.9%). Standing groups and full figures have vertical room or a full panel; remaining wide conversations specify waist-up framing. P22 keeps its inset chibi gag with the seated characters cropped at the waist; P34's full chibi tableau has room for both figures.

### NEEDS REDRAW

None. No existing chapter 96 art locks required a redraw.

### Validation

Ran the bundled Python executable with `tools/validate_script.py scripts/ch096.yaml`: **OK**, no errors or warnings. Final counts: 52 panels, 8 silent panels, 2 chibi panels and 7 float narration lines. The hook remains `YOU WENT.` / `I WENT.` / `GOOD. NOW WIN.` with P51 tall.

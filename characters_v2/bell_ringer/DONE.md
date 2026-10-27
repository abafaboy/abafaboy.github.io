# M7 DONE — The Drowned Bell-Ringer

Finished 27 October 2026. All requested M7 deliverables are present. Ready for Claude's review; this file does not claim review-board approval.

## Files and tries

| File | Kept try | Contents |
|---|---:|---|
| `front.png` | 2 of 2 | Checked full-body front, used as first reference for all subsequent sheets/scenes. |
| `turnaround.png` | 1 of 1 | Front, three-quarter, left profile and back; same scale and baseline. |
| `details.png` | 1 of 1 | Cracked bell and Hush split, full clapper hammer, five-digit hand. |
| `toll.png` | 5 of 5 | Force annulus beyond reach, calm inner safe pocket, adult scale witness. |
| `card.json` | — | Design, palette, height, side/prop continuity and remaining limits. |
| `prompts.json` | — | Exact prompts and reference paths for all nine image calls, source/save paths, free-space checks, verdicts and reject reasons. |

All four kept images are native 1536×1024 PNGs from the built-in `image_gen.imagegen` tool. The sheets have no scale silhouette; the toll scene keeps one generic adult witness as required by the 27 October override. No expressions or chibi sheet was requested for M7.

## Remaining limitations for review

- `toll.png` is the best permitted fifth try. Its witness is approximately 254 px high against about 810 px for the posed giant, a projected ratio around 0.31 versus the ideal 1.78/6 = 0.297. Their feet are at almost the same depth and the witness reaches the knee area. This remains an approximate scene scale, near the 27 October tolerance, rather than a calibrated scale card.
- The final toll scene has much simpler architecture than the other tries, but its water still carries more reflection marks than requested. The robe hem has more small notches than ideal. No further image calls were made after the fifth toll try.
- Sheets have a faint background tone variation; the 27 October changes explicitly allow it.
- The bell crack was consistently placed on the anatomical LEFT side, and the clapper in the anatomical RIGHT hand. The source design leaves these sides open; these are continuity choices for later panels.

## Rejects

Five native PNGs are saved as ordinary files in `characters_v2/_rejects/`:

- `bell_ringer_front_try01_rendered_texture_and_shredded_hem.png`
- `bell_ringer_toll_try01_scale_witness_too_small_busy_water.png`
- `bell_ringer_toll_try02_scale_witness_undersized.png`
- `bell_ringer_toll_try03_scale_witness_oversized.png`
- `bell_ringer_toll_try04_busy_reflections_soft_foreground.png`

No reject was used as a reference. The initial front was generated without image references; later calls used only this entry's checked front and, where useful, its checked turnaround (maximum two images).

## Verification and disk limit

Read the 27 October README overrides first and the reading-order files, plus the model-sheet sections 1–3, panel-brief 4b, style-test report, review status, and applicable art-bible rules. Used the imagegen skill and the built-in image tool.

Checked the kept images at native size and 200 px wide, with enlarged hand/edge inspection in memory. All nine kept/rejected PNGs have the correct PNG signature, are 1536×1024, and SHA-256-match their generator originals byte for byte. `fsutil hardlink list` returns exactly one name per saved PNG; none is a reparse point. No resizing, re-encoding, hard links or shortcuts were used for delivery. No previews or temporary images were written into the project.

Ran `Get-PSDrive C` before every image call. The recorded free space ranged from 36.843 to 42.271 GiB, always above 3 GiB; no disk-limit stop was triggered. Final verification found 45,216,227,328 free bytes (about 42.1 GiB).

Project writes were confined to `characters_v2/bell_ringer/` and M7-prefixed rejects in `characters_v2/_rejects/`. No other chat's folder or shared brief/review was edited. No publication or upload was performed.

Nothing left to draw within M7's five-try rule. Stopped after writing this file.

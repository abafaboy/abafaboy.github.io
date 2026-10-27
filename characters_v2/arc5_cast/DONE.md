# S27 DONE — Arc 5 supporting cast

27 October 2026. Completed by chat S27. **Best of five retained with faults; awaiting Claude's review.** Drawing stopped at the five-try limit in README_START_HERE.md's 27 October changes.

Files in this entry:
- `lineup.png` — attempt 4, native 1536×1024 PNG, 1,745,917 bytes.
- `card.json` — roster, colours, design locks, reference, and outstanding faults.
- `prompts.json` — exact prompts and reference paths for all five calls, outcomes, original generator paths, and free-space readings.
- `DONE.md` — this report.

The single row contains all 18 requested people: Branch Chief Yang; three market aunties; old and younger fishermen; the PC bang owner with his broom; the PR pair and photographer; the tourist couple; the fishmonger father, mother, toddler in stroller and standing child; the Marine engineer and trooper. All standing feet and stroller wheels share one baseline. No 178 cm silhouette, following the 27 October override. S27 requests this front-view lineup only, so no separate front, turnaround, expression or detail PNG was added.

## Remaining faults and uncertainties

- **Both Marine chest badges have star-like centre motifs.** They should show Kanghan's plain nested silver hexagons. Yang's separate Association star-and-shield is appropriate.
- **The PC owner's unlit cigarette is not clearly legible.**
- The stroller partly occludes the mother's lower legs.
- The PR pins are silver, but their tiny hexagon geometry is simplified. The older aunties' head/body ratios merit Claude's review; they read shorter than the intended approximately seven heads.
- A faint background tone variation remains. The 27 October rule explicitly says this alone is not a reason to redo.
- The long, single-baseline roster fills the width rather than the full canvas height so that the complete cast can fit without being horizontally compressed.

The fifth try did not resolve the badge problem and had less consistent emblem shapes. Attempt 4 was kept for its complete roster, clear props, silver PR pins, legible neck respirator, and coherent baseline. This report does not declare the asset approved. Review/fix candidates are the badge centres, cigarette, visibility of the mother's legs, and older-auntie proportions. No requested deliverable file remains missing.

## Rejects saved as ordinary PNG files

In `characters_v2/_rejects/`:
- `arc5_cast_try01_wrong_canvas_badges.png` — wrong 1983×793 canvas; wrong/extra badges; textile mottling.
- `arc5_cast_try02_badges_ear_prop_respirator.png` — ambiguous badges; pencil-like ear prop; unclear/missing respirator.
- `arc5_cast_try03_gold_pr_pins.png` — gold rather than silver PR pins; tiny auntie's necklace insufficiently distinct.
- `arc5_cast_try05_marine_badges.png` — incorrect Marine badge symbols remained; less consistent pin geometry.

## Verification and limits

Used built-in `image_gen.imagegen`. Each call used one approved house-style anchor, `style_test_v2/acting/B3_P29.png`, covered by the APPROVED style-test entry in `reviews/STATUS.md`. No outside, retired, unapproved external, or reject images were used as inputs.

Checked the kept sheet at native size, with in-memory detail crops, at 200% for ink/colour edges, and at 200 pixels wide for silhouettes. No obvious JPEG blocks, ringing or optical blur were seen. Occluded fingers and tiny emblems cannot all be certified from this crowded lineup.

Every saved PNG was copied directly with `System.IO.File.Copy`, without re-encoding or resizing. SHA-256 comparisons confirmed that all five saved PNGs are byte-identical to their generator originals. All five have one filesystem link path and no reparse-point attribute: ordinary files, no hard links or shortcuts. No preview, crop or temporary image files were saved in the project.

`Get-PSDrive C` ran immediately before each image call. Free bytes by attempt: 44,392,685,568; 44,105,879,552; 43,653,951,488; 42,608,697,344; 42,171,957,248. Every check exceeded 3 GB. Final verification found 41,243,856,896 bytes free.

Project writes were confined to `characters_v2/arc5_cast/` and these four S27 rejects in `characters_v2/_rejects/`. No other chat's folders, briefs, scripts, or review board were edited. No publication or external upload was performed.

Stopped after writing this DONE file.


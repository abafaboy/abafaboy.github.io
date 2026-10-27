# S16-B — Borro
Completed 27 October 2026.

All four requested remaining sheets are delivered. No drawing work remains for this chat. The new sheets await Claude's review; this handoff does not change the review board.

## Files
- `front.png` — existing Claude-approved reference, unchanged, including Claude's scale silhouette.
- `turnaround.png` — front, three-quarter, side and back, one scale and baseline; shell depth, same-edge shield hinges and rear strap shown.
- `expressions.png` — eight heads/shoulders in a 4×2 grid: calm, slow smile, dry deadpan, protective frown, straining under weight, sleepy, offended at being called equipment, quiet sadness.
- `details.png` — moss/flower/slate close-up; Borro's blunt-fingered hand beside Jaeha's smaller gloved hand; shield front/back with hinges, rear strap and grip; satchel/trowel/seed pouch; white oval mask worn and held, each with two round eye-holes.
- `chibi.png` — eight gag poses in a 4×2 layout with approximately 2.5-head proportions.
- `prompts.json` — exact prompts, ordered reference paths, disk checks, native source paths and kept/rejected decisions for all six image calls.
- `card.json` — existing palette and design locks retained; stale cloud failure status updated to reflect the approved front and new sheets awaiting review.

## References and continuity
Used the built-in image_gen.imagegen tool. Approved `borro/front.png` was the FIRST reference for every call. Only the details sheet additionally used approved `kang_jaeha/front.png`, for the small hand/glove. No rejected or unreviewed image was used as a reference.

All four new sheets exclude silhouettes and text. The shell follows the approved roof-slate construction and moss seams: high white flower at Borro's anatomical right nape, yellow flower on his right shoulder, white flower on his left shoulder. Far-side flowers are hidden when occluded. The shield keeps its riveted door construction, below-centre boss and two hinges on one physical edge: outer face picture-right, reverse face picture-left. Satchel remains on his right hip.

Uncertainty for review: the approved front does not expose the full rear shell. Its unseen plates and moss are a coherent continuation; exact hidden rear plate geometry cannot be verified from that reference. Chibi simplifies the design at the requested gag proportions.

## Rejects
Ordinary full-resolution PNGs saved at:
- `../_rejects/borro_turnaround_a1_shield_too_short.png` — shield shortened to about waist height; front hand at canvas edge.
- `../_rejects/borro_chibi_a1_sleep_letters_and_tall_proportions.png` — forbidden sleep letters and bodies too tall for the chibi brief.

Turnaround attempt 2 and chibi attempt 2 were kept; expressions and details each used one attempt.

## Verification and disk rule
Every delivered sheet is a native 1536×1024 PNG copied directly from the generator without resizing or re-encoding. Kept files and rejects are ordinary copies, not hard links, shortcuts or reparse points. No extra previews or temporary images were saved in the project folder.

Ran `Get-PSDrive C` before every image call. Free space remained above 3 GB throughout (41.27–42.39 GiB at the six call checks), so the low-space stop condition was never reached.

Approved front SHA-256, unchanged:
`B983A70E6515E0CAEE3DC760B5AF6776B6143403E8D9EACEB866474808D5C5EB`

Writes confined to `characters_v2/borro/` and the two authorized Borro reject files. No brief, review-board or other character file was changed.

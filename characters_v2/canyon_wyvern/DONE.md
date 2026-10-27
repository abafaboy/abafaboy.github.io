# M8 — Canyon wyvern — DONE

Date: 27 October 2026. Chapter: 24. Drawing complete; no deliverables left to draw. Pending Claude's independent review.

Files in this folder:
- `front.png` — required front reference, kept attempt 2.
- `turnaround.png` — side, front and dorsal top with spread wings, kept attempt 3.
- `details.png` — beaky head/needle teeth, hooked tail barb, wing-bone ash cracks, kept attempt 1.
- `flock.png` — twelve diving wyverns, counted as three staggered bands of four, with one generic adult worker on a canyon walkway for scale; kept attempt 4.
- `card.json` — dimensions, palette, design locks, scale notes, file hashes and review notes.
- `prompts.json` — exact built-in image_gen.imagegen prompts, references, all ten attempts, disk preflights and rejection reasons.
- `DONE.md` — this handoff.

Every kept image and reject is a native 1536×1024 PNG copied as an ordinary file. All ten copies matched the generator originals by SHA-256, each had one NTFS hard link, and none was a reparse point. No resizing or re-encoding was applied to saved art. No extra previews or temporary images were saved in the project; thumbnail and 200% pixel inspections were made in memory.

Six rejects are preserved in `characters_v2/_rejects/`:
- `canyon_wyvern_front_attempt01_fragmented_shading.png`
- `canyon_wyvern_turnaround_attempt01_unequal_wing_scale.png`
- `canyon_wyvern_turnaround_attempt02_top_wings_bent.png`
- `canyon_wyvern_flock_attempt01_count_and_blurred_pipe.png`
- `canyon_wyvern_flock_attempt02_ten_wyverns.png`
- `canyon_wyvern_flock_attempt03_nine_wyverns.png`

Review notes:
- The side turnaround's far hind leg is occluded by the near leg.
- Front/top turnaround spans approximately match within the 27 October tolerance of about 5%.
- The flock's spacing is relatively orderly because three visible bands of four were used to secure the requested dozen.
- Faint background tone variation is retained under the 27 October override.

Applied the 27 October changes first: no human silhouette on sheets, front-first reference workflow, at most two references in any call, and no asset exceeded five attempts. Only this entry's passed new images were used as references. The canyon scene was drawn from the canonical written design; no unreviewed concurrent location key, old artwork, outside artwork or reject was used.

C: free space was checked with `Get-PSDrive C` before every image call; every preflight passed the 3 GB stop threshold. Final validation found about 37.346 GiB free. The first flock call timed out at the host after saving its PNG; that output was recovered, inspected and preserved as a reject. No call was blindly duplicated.

Project writes were confined to `characters_v2/canyon_wyvern/` and this entry's six reject files. No shared briefs, review files, other entry folders or chapter panels were changed. Nothing was published or uploaded. Stopping here.


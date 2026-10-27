# M2 — The drowned hound — DONE

27 October 2026. Drawing finished under the 27 October README overrides. Pending Claude review; this is not an approval verdict.

## Files

- `front.png` — required first reference, kept attempt 3.
- `turnaround.png` — side, front and back; attempt 4 retained as the best of five.
- `details.png` — head/jaw, brow Hush crack, barnacles/weed in fur, four-toed forepaw; attempt 1.
- `action.png` — lunging out of dark water in the approved flooded car park, with a generic adult silhouette for scale; attempt 1.
- `card.json` — measurements, palette, locks, design choices and image-specific QA.
- `prompts.json` — exact built-in imagegen arguments for all 10 calls, references, disk preflight values, source/saved paths, outcomes, rejection reasons and SHA256 audits.
- `DONE.md` — this report.

All four kept images are native **1536×1024 PNGs**, copied byte-for-byte from the generator. No resampling, sharpening, compositing or re-encoding was applied to delivered art.

## Remaining faults and review notes

**Turnaround is not a strict proportions pass.** After five attempts, attempt 4 was retained under the normal filename as README rule 3 requires. Its side-view horizontal length relative to withers-to-ground height is approximately **1.7**, versus the design target **3.5 / 1.7 = 2.06**. The side view's head is also slightly taller than the front/back, so exact view scale is not certified. Organic barnacle/weed details vary slightly between views. This sheet was **not used as a reference** for the later images; they use the passing front.

The details sheet has very sparse violet ash around the crack. In the action scene the splash partly hides the rear propulsion, and wet reflections/splash retain local detail. The front, details and action passed local inspection with these caveats. Faint sheet background tone variation was accepted under the 27 October override.

No additional images remain to draw under this entry's five-attempt rule. Claude should review the turnaround faults before approving the set for later chapter work.

## Rejects

Six ordinary PNGs saved in `characters_v2/_rejects/`:

- `drowned_hound_front_a01_wrong_angle.png` — three-quarter rather than strict front.
- `drowned_hound_front_a02_paws_and_large_crack.png` — paws read five-toed; oversized brow crack.
- `drowned_hound_turnaround_a01_short_body.png` — compressed side torso.
- `drowned_hound_turnaround_a02_length_ratio.png` — short side length and view-scale drift.
- `drowned_hound_turnaround_a03_short_ribcage.png` — profile length/height ratio still short.
- `drowned_hound_turnaround_a05_ratio_persists.png` — ratio still short; less distinct foreleg overlap than kept attempt 4.

Attempt 4 is the kept turnaround, so it is not also duplicated in the rejects folder.

## Checks and scope

- Read the README and its required story, naming, style, art-direction, design and entry references, plus model-sheet sections 1–3, panel proportions section 4b, applicable art-bible rules, the style-test report and review board.
- Built-in `image_gen.imagegen` used throughout. Exact V2 style, cleanup, drowned-hound snippet and negative blocks verified in all 10 archived prompts.
- References: passing new `front.png`; for the action only, `locations_v2/carpark_gate/key.png`, approved in `reviews/STATUS.md` and `reviews/L7.md`. Maximum two references per call. No rejected, retired or outside images were passed.
- No people or scale silhouettes on sheets. The action retains its human scale figure.
- Inspected full-size results, 200 px-wide views and in-memory 200% crops. No preview/crop image files were saved in the project.
- All 10 saved PNGs have valid PNG headers, native dimensions and SHA256 hashes identical to their generated originals. NTFS hard-link enumeration confirms **one file path each**: no hard links, shortcuts or reparse points.
- `Get-PSDrive C` checked immediately before every image call. Every call was above 3 GB free; lowest preflight free space was about **39.7 GiB**. Final check: about **38.7 GiB** free. The disk-stop condition was never reached.
- Project writes were confined to `characters_v2/drowned_hound/` and this entry's named reject PNGs. No other chat's folder, shared guide or review verdict was edited. Nothing was published or uploaded.

Stopped after writing this file.

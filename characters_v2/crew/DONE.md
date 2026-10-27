# S23 — DONE

Completed 27 October 2026. Arc 4 crew and Kanghan staff, chapters 23–33.
Built-in image_gen.imagegen; V2 cinematic cel. Ready for Claude's review; this file does not grant review-board approval.

## Delivered

| File | Contents | Tries |
|---|---|---:|
| lineup_kit.png | Pyo, Dami, Woo, Jaeha, Ho; full-face smoky visors, twin filters, yellow hard hats and lamps | 1 |
| lineup_faces.png | Same five in the same order and scale; respirators down, hard hats off; front identity master | 2 |
| kanghan_lineup.png | Foreman Gu, engineer, grey-haired duty chief, tactical trooper with round shield and core carbine | 1 |
| dami_daughter.png | Six-year-old girl in an oversized yellow raincoat; missing front tooth | 1 |
| card.json | Ids, ages, heights, palette, layout, side locks and open design choices | — |
| prompts.json | Exact prompts and tool arguments, reference paths, all attempts, disk checks and PNG hashes | — |

Every PNG is 1536×1024, copied byte for byte from its generator original. No resizing, retouching, sharpening, recompression, hard links or shortcuts. All five files (including the reject) have exactly one filesystem name according to fsutil hardlink list. Generator originals remain in the application's generated_images directory. No previews or temporary images were saved in the project.

## Reject retained

`characters_v2/_rejects/crew_lineup_faces_try1_dark_jaeha_trousers.png` — first unmasked lineup: Jaeha retained dark navy trousers instead of grey coveralls; clothing shadows were also too fragmented. This image was never used as a reference. The second attempt corrected the uniform.

## Continuity and lettering

- Crew order, left to right: **Pyo 1, Dami 2, Woo 3, Jaeha 4, Ho 5**. Tabards deliberately contain **no drawn numbers**, following the README and style guide's no-text rule. Add the identifiers during lettering.
- Pyo's brace is on his anatomical **LEFT** knee, picture-right within his front figure. Jaeha retains the approved anatomical-left fringe and right-ear pencil where uncovered; notebook is hidden inside the tabard.
- `lineup_faces.png` was generated and checked first and serves as the requested front-view reference for this lineup entry. No duplicate, unrequested `front.png` was kept.
- The only existing external image reference was the approved `kang_jaeha/front.png`, covered by `reviews/STATUS.md` (S1–S15 approved). The other reference was this entry's checked front master, as allowed by MODEL_SHEETS_BRIEF section 2.
- Canon specifies Pyo 160 cm and Jaeha 178 cm. Unspecified heights were resolved as Dami 164, Woo 184, Ho 181; Gu 168, engineer 176, duty chief 172, trooper 183; daughter about 112 cm. These are S23 design choices, not new source-bible canon.
- Dami's phone and staff tablets face inward/backward; there is no exposed screen needing a generated photo or lettering.

## Checks and review caveats

Checked the required cast, equipment, proportions, relative heights, common baselines, side locks, attached props, hands, lack of text, lack of scale silhouettes, native size and ordinary-file status. Inspected all kept sheets at full view, as 200 px thumbnails, and sampled native pixels at 200% using in-memory previews only. Source and delivery SHA-256 hashes match.

A few angular workwear folds remain, especially near the ankles; Claude may prefer simpler shapes. The daughter has a larger child head in the simple manhwa treatment. Respirator forms are compact at the neck in the unmasked sheet and cover the whole face in the masked sheet. Faint background tone variation is retained under the 27 October rule; it was not a reason to redraw.

## Disk and scope

Ran **Get-PSDrive C before every one of the five image calls**. Every reading exceeded the 3 GB stop threshold. Last integrity-check reading: **42,835,939,328 bytes free (about 39.9 GiB)**.

Project writes were confined to `characters_v2/crew/` and the one S23 reject above. No other chat's folder, brief, bible, review board or chapter art was changed. Nothing was published or uploaded to a public destination.

No drawing remains for S23. Stopping after this DONE file.


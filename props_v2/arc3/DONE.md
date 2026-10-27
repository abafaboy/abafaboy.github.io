# P1 — Arcs 3–4 props — DONE

27 October 2026 · Asia/Tashkent

Completed entry P1 of `ASSETS_ARC3_BRIEF.md`. Kept attempt **5 of 5** as `props.png`, following the 27 October instruction to retain the best complete image after five tries and record its faults. This is delivered for Claude's review; it is not marked APPROVED.

## Deliverables

- `props.png` — native **1536 × 1024 PNG**, seven prop groups: the Kanghan sealing stake with blank glowing timer; Sora's original brass compass and wrist chain; Minseok's cracked orange phone with yellow thumbs-up sticker; his rusted hard-hat lamp with orange vest cloth; the factory-steel link with incised diamond stamp; Choi's foil-lined kimbap box with silver USB-A drive; Geum's long-handled steel ladle.
- `card.json` — prop locks, layout, palette, image metadata, QA, disk checks and remaining caveats.
- `prompts.json` — exact built-in image_gen arguments for all five attempts, references, source paths, decisions and rejection reasons.
- `_rejects/props_attempt01_rendered_texture.png`
- `_rejects/props_attempt02_lens_facets.png`
- `_rejects/props_attempt03_mottled_steel.png`
- `_rejects/props_attempt04_emblem_and_cloth.png`

## Review notes / remaining faults

- Attempt 5 is the strongest complete result. Some fine mottled rust/steel treatment remains, and foil still has several highlight shapes. It is not a flawless strict pass for the surface-rendering checks in 11b.1/6. All four earlier native PNGs are retained as rejects with reasons in the prompt archive.
- Timer is blank and green with no digits. A central pixel is **#05F812**, rather than the requested exact **#00FF00**. The letterer should cover the blank display. No pixels were recoloured or re-saved.
- Background is visually plain light grey with faint variation; corner samples are #DEE0E3, #DEE0E2, #DDDDE2 and #DDDEE1, rather than exact #E9E9EC. Retained under the 27 October background-tone exception.
- The seven groups are independently enlarged detail studies, not a shared-scale arrangement. The stake is canonically 1 m; later panels must size each prop to its user's body. Sora's chain belongs on her RIGHT wrist and Geum's ladle in her RIGHT hand. No people or scale silhouettes were drawn.
- No further images remain to draw for P1. Further changes belong to Claude's review after this five-attempt delivery.

## Verification

All five images are 1536 × 1024 ordinary PNG files, each with **one filesystem hard link** and no shortcut/reparse link. The kept file is byte-identical to the generator output: SHA-256 `246CC3A5E98278C2B81DD29B07D7F19B328F9C546561443A3B7C560CDB432921`.

Inspected the native full-size result, an in-memory 200 px-wide thumbnail, and an in-memory 200% crop of the phone/sticker/ink edge. All seven object silhouettes read at thumbnail size; no obvious compression blocks, ringing halos or enlarged-source softness observed. No preview or temporary image files were written in the project. Prompt JSON and card JSON parse correctly; every recorded image exists.

The approved `characters_v2/knight_commander/details.png` was inspected for the established small diamond-outline factory stamp and was the sole attached reference on attempts 1–2. Attempts 3–5 used text only. Approval was checked against `reviews/STATUS.md` (S1–S15 / S6 approved). No rejected, retired or outside image was used as a reference.

Read `README_START_HERE.md` with its 27 October overrides first, then its relevant reading sequence: story bible v4, Arcs 3–4 beats, name sheet, style guide, art direction, character designs and the Arc 3 assets brief. Also read the model-sheet rules, panel brief sections 2/4b and the existing style-test report.

## Disk checks and scope

Ran **Get-PSDrive C before every image-generation call**. Free space before attempts 1–5 was **41.979, 41.847, 41.632, 41.279 and 41.055 GiB**, respectively; all exceeded 3 GiB. No disk-space stop was triggered.

Every project write was confined to `props_v2/arc3/`, including rejects in its `_rejects/` subfolder. Automatic generator originals remain in the application-managed generated_images directory. Other chats' folders were only read where an approved reference was needed and were never modified. Nothing was published or uploaded.

Stopped after this DONE file.

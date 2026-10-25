# DONE — S9 · Yoo Bomi

Round 2 outfit restyle completed 25 October 2026. Round 1 was approved by the owner and is preserved as history.

## Round 2 restyle

Read the updated Fan service block, section 2.7 and Bomi's section 8 snippet in CHARACTER_DESIGNS_v2.md, plus the current style rules and checks 11 and 11b.

The whole set now uses the approved outfit:
- cropped neon-yellow bomber worn open, sleeves pushed up;
- black crop top with bare midriff;
- high-waisted blue denim shorts with a functional black belt;
- opaque black thigh-high socks;
- the same plain black trainers with grey soles, no stripes or logo.

Retained Bomi's original adult face, two-tone high ponytail, big grin, approved compact recurve and nearby white camera drone with red recording light. Posing is neutral and confident for the reference views, with ordinary comedy gestures in the gag sheet. No nudity, explicit content, sexual pose or intimate camera angle.

## Current files

- `source_front.png` — new outfit front master, completed and checked first.
- `turnaround.png` — front, three-quarter, side and back, same scale and common baseline.
- `expressions.png` — eight head-and-shoulders expressions in a 4×2 grid: neutral, smile, anger, shock, sadness, fear, determination, laughing.
- `details.png` — six studies: drone; compact bow; grinning face and ponytail; cropped bomber/crop top; denim shorts and belt; thigh-high socks and trainers. Clothing details are clothes-only reference objects.
- `chibi.png` — eight comedy poses with the new outfit, the same two bow gags and a nearby drone in every cell.
- `card.json` — updated outfit locks, denim/sock palette, continuity details and selected prompt IDs.
- `prompts.json` — exact historical and Round 2 prompts, tool arguments, reference images, archive paths and selections.
- `QA.json` — dimensions, opacity, exact background audit, hashes and review results.
- `DONE.md` — this completion record.

Supporting files: the five `sources/*_alpha.png` files, `sources/qa_thumbnails.png`, `export_sheets.ps1` and `validate_sheets.ps1`.

## Method and verification

Used the built-in image-generation tool. The front was an outfit-only edit of the owner-approved Round 1 front. Every other sheet references the new front; previous own images supply only continuity, acting and layout. No outside images or retired story references were used.

All seven Round 2 prompts contain the exact V2 STYLE BLOCK, CLEAN-UP LINE, sheet description, updated Yoo Bomi snippet and NEGATIVE BLOCK in the required order. The prompt log retains all historical versions and archived image-reference paths.

Viewed each final image at full size and at 200 pixels wide. Checked outfit continuity, original identity and gear, expression/gag counts, hands and joints, functional pockets/belt/string, plain shoes, clean opaque fold shading, matte drawn surfaces, no lettering or brand marks, and suitable adult reference posing.

All five final PNGs are **1536×1024**, opaque, with exact **#E9E9EC** empty backgrounds. The image tool supplied transparent cutouts; the export script composites them onto the required grey without resizing or repainting the foreground. The pixel audit found zero background mismatches and zero nonopaque final pixels. All 30 historical/current prompt records and reference paths validate.

## Archives and retries

Moved each replaced old-outfit file to the requested name:
- `characters_v2/_rejects/yoo_bomi_r2_old_outfit_source_front.png`
- `characters_v2/_rejects/yoo_bomi_r2_old_outfit_turnaround.png`
- `characters_v2/_rejects/yoo_bomi_r2_old_outfit_expressions.png`
- `characters_v2/_rejects/yoo_bomi_r2_old_outfit_details.png`
- `characters_v2/_rejects/yoo_bomi_r2_old_outfit_chibi.png`

Their replaced alpha sources and the previous thumbnail strip use the same prefix. Additional Round 2 rejects and their alpha sources are also preserved: the first expression attempt included an unwanted full-body figure; the first detail attempt used too many small denim-shadow streaks. Both were corrected on attempt 2.

Selected attempts: front 1, turnaround 1, expressions 2, details 2, chibi 1. Earlier Round 1 and initial-generation history remains in the prompt log and rejects archive.

No unresolved required outfit or identity locks were found in final review. The compact bow remains the previously approved drawn reference, nominally about 90 cm.

All project writes stayed in `characters_v2/yoo_bomi/` and Yoo Bomi files in `characters_v2/_rejects/`. Other chats' folders were not modified. Nothing was published.


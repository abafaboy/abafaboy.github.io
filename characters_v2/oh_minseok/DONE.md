# S22 — Oh Minseok — DONE

Completed 27 October 2026 (Asia/Tashkent), ready for Claude review. All requested S22 deliverables are present. Nothing remains to draw.

| File | Contents | Attempts |
|---|---|---:|
| front.png | Minseok full-body identity anchor | 1 |
| turnaround.png | Front, three-quarter, left profile, back | 1 |
| expressions.png | All five S22 expressions, plus neutral, fear and determination to complete the standard eight-portrait 4×2 sheet | 1 |
| young_cast.png | Jaeha at 20, Choi at 30, Mok at 34, side by side | 2 |
| card.json | Palette, locks, design decisions, ages and review notes | — |
| prompts.json | Exact built-in image_gen.imagegen arguments, references and QA for all five calls, including the reject | — |

All four kept images are native 1536×1024 PNGs, copied byte-for-byte from generator originals. SHA-256 comparisons passed for every kept image and the reject. Windows hard-link enumeration returned exactly one path per saved PNG: these are ordinary independent files, not hard links or shortcuts. No resizing, recompression, retouching or compositing was applied to delivered art.

## Checks

Read README_START_HERE.md with its 27 October overrides first, then STORY_BIBLE_v4.md, ARC3_4_BEATS.md, NAME_SHEET.md, MANHWA_STYLE_GUIDE.md, MANHWA_ART_DIRECTION.md, CHARACTER_DESIGNS_v2.md and ASSETS_ARC3_BRIEF.md. Also read the required MODEL_SHEETS_BRIEF sections 1–3, PANEL_BRIEF_v2 section 4b, style test report and the art-bible chibi reference.

Minseok's front passed this chat's checks before it became the first reference for the remaining calls. Existing Jaeha, Choi and Mok fronts were checked against reviews/STATUS.md (S1–S15 APPROVED) and visually inspected before use. No old art, outside images, unapproved other-chat art or rejects were used as references. Maximum references in one call: four.

Visual review covered native full-size images, 200-pixel-wide thumbnails and selected 200% detail crops. Inspection images existed only in memory. Checked adult head counts and leg length, same-baseline height relationships, anatomical sides, scar, grey hair, vest repairs, hands, expressions, matte cel rendering, and crisp PNG edges. No scale silhouettes. No text except young Jaeha's chest T.

Young Jaeha has a clean new vest, visibly shorter left-biased fringe and bare hands. Young Choi has reduced under-eye shading without his older deep bags. Young Mok keeps the dark undercut, black guild jacket, crimson hound emblem and gold chain.

## Reject

characters_v2/_rejects/oh_minseok_young_cast_try1_choi_under_eye_shading.png — ordinary native PNG, preserved without alteration. The first lineup retained shading beneath young Choi's lower lids that could read as eye bags. The second attempt was kept.

## Decisions and minor uncertainties

- Minseok's exact height and scar side were unspecified. This set establishes 176 cm and an anatomical RIGHT eyebrow scar; card.json records these as production choices.
- Model sheets use local colours. Story flashbacks must be desaturated except for the orange vest.
- The turnaround's three-quarter view faces picture-right; the profile faces picture-left. Both satisfy the requested view set.
- The generated light-grey background approximates #E9E9EC with slight tone variation, allowed by the 27 October override.
- This is a completed drawing entry awaiting Claude's review; no claim of approval in reviews/STATUS.md is made.

## Disk and scope

Get-PSDrive C was checked before every image call. Free bytes were 40,530,649,088; 40,452,489,216; 40,300,163,072; 39,926,820,864; and 39,717,347,328. Every check exceeded the conservative 3 GiB cutoff of 3,221,225,472 bytes. The low-space stop condition never triggered.

Project writes were confined to characters_v2/oh_minseok/ and the single named reject in characters_v2/_rejects/. No other chat's folder was changed. No extra previews or temporary images remain in the project. Nothing was published or uploaded.

S22 finished. Stop.

# ch003-R1 — completed, 27 October 2026

Only P33.png, P45.png and P49.png were replaced. Built-in image_gen was used for every image call. Work stops here at the requested attempt cap.

| Panel | Tries | Kept | Result |
|---|---:|---:|---|
| P33 | 1 | 1 | Near anatomical RIGHT pauldron repaired to intact plain dark iron with bronze trim; far LEFT cracked pauldron remains occluded. Original impact, portcullis, rust cloud, small Jaeha, composition and light preserved. |
| P45 | 1 | 1 | Near anatomical RIGHT pauldron repaired; original Nib foreground, pinned knight, small Jaeha by bars, green shafts and red light preserved. |
| P49 | 5 | 4 | Best of five retained. Nib is much smaller beside heel-seated Yerin, his skull is smaller than hers, and their crowns are close. Residual issues below require review. |

## P49 remaining uncertainties

The selected image is the closest result after five tries, not a claim of exact approval. Its approximate projected floor-to-crown ratio is 1.21, compared with 105/82 = 1.28; Nib is about 6 percent low by this simple image-space measurement. The crown gap is about 0.8 of Yerin's head rather than one full head. Both contact the same floor at the same depth, Yerin sits back on her heels, and Nib's head is smaller. Some stone detail at the extreme foreground and far arches remains softened. Attempt 5 enlarged Nib too much and also changed Yerin's size, so it was rejected. No sixth try was made.

## Files and provenance

- Kept PNGs: P33.png (1024×1536), P45.png (1536×1024), P49.png (1024×1536). Every kept PNG is byte-identical to its full native generator output; no resizing or pixel retouching.
- Exact prompts, ordered references, all seven calls, disk checks, source paths, rejects and verification: PROMPTS_R1.json.
- Normalized head boxes for every visible character and per-panel verdicts: REVIEW_R1.json.
- Per-panel completion notes: PROGRESS_R1.md.
- Original files were moved before replacement, byte-for-byte, to:
  - _rejects/P33_v2_wrong_near_right_pauldron_cracked.png
  - _rejects/P45_v2_wrong_near_right_pauldron_cracked.png
  - _rejects/P49_v2_nib_oversized_beside_kneeling_yerin.png
- P49 discarded candidates 1, 2, 3 and 5 are ordinary PNG files under _rejects/, with reasons in their names and the prompt log.

P33 and P45 used the current panel as reference 1 and knight_commander/turnaround.png as reference 2. Every P49 call used scale_chart_v2.png, nib/turnaround_mask.png, song_yerin/front.png and approved P50.png in that order. Attempts 4 and 5 used the current working P49 as the fifth reference for a targeted size edit, as allowed by PANEL_BRIEF_v2 section 5; no rejected image was passed from _rejects/.

## Verification

All three kept files, all three archived originals and all four new rejects have exactly one filesystem link and are ordinary files. Original archive hashes match the original panels. SHA-256 checks confirm the other 59 approved chapter PNGs are unchanged. Both JSON logs parse successfully. Full-size and 200-pixel-wide reviews were completed for the selected files. No previews or temporary images were saved in the project; the one inspection preview outside it was removed.

C: free space was checked with Get-PSDrive C before all seven image calls and stayed above 3 GB (lowest pre-call reading: 32.18 GiB). Final reading: 31.42 GiB. The space stop rule was not triggered.

No other chapter art, scripts, sheets, briefs or review-board files were edited. No pending generation remains. P49's stated residuals remain for Claude's review; no more drawing is authorized past five tries.

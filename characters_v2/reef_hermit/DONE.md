# M11 — The Reef Hermit — DONE

27 October 2026, Asia/Tashkent. Generation complete; awaiting Claude's approval. Chapter 35, ASSETS_ARC5_BRIEF.md entry M11.

## Delivered

| File | Kept attempt | Contents |
|---|---:|---|
| front.png | 1 of 1 | Checked design master: full front view, shrine shell, larger anatomical RIGHT claw, bell, violet eye-stalks and carapace Hush crack. |
| turnaround.png | 2 of 2 | Front, front three-quarter, anatomical right profile facing picture-right, back. |
| details.png | 1 of 1 | Bell hanging inside doorway; larger RIGHT claw beside the smaller claw; dull violet eye-stalks; Hush fissure and ash; cracked dome shedding chips. |
| out_of_shell.png | 3 of 3 | Reaching forward, intact soft pale pink-grey curled abdomen halfway outside and visibly continuous into the shrine doorway. |
| card.json | — | Height, palette, locks, view orientation, layout and self-check status. |
| prompts.json | — | Exact built-in imagegen prompts, ordered references, all seven attempts, sources, decisions and pre-call C: free-space checks. |

Every kept image is a native 1536×1024 PNG, copied byte-for-byte from the generator. Built-in image_gen.imagegen was used throughout.

## Rejects saved as ordinary PNG files

- ../_rejects/reef_hermit_turnaround_try01_compressed_crowded_views.png — single-row layout squeezed the wide body and crowded/cropped outer legs.
- ../_rejects/reef_hermit_out_of_shell_try01_streaked_abdomen_clipped_shell.png — streaked soft-body highlights and left shrine-edge crop.
- ../_rejects/reef_hermit_out_of_shell_try02_left_edge_crop.png — matte abdomen corrected; shrine still clipped at left.

No attempt limit exceeded. No required image remains undrawn.

## Checks and review notes

- Read README_START_HERE.md with the 27 October overrides first, then the applicable reading-order files. Also consulted MODEL_SHEETS_BRIEF.md sections 1–3, PANEL_BRIEF_v2.md sections 2 and 4b, the existing style reports, reviews/STATUS.md, and chapter 35 continuity/action.
- Initial style reference: approved style_test_v2/acting/A3_P23.png. Once front.png passed self-check, it was the first reference for every subsequent image. Own generated images were used as edit targets only for the two targeted out-of-shell corrections; no file from a _rejects folder was attached. No retired or external art used.
- No human scale silhouettes, labels or lettering in any delivered sheet. Grey background and neutral upper-left light retained.
- Larger anatomical RIGHT claw checked across views. Bell stays inside the shrine doorway; rear and profile views occlude it where appropriate. Abdomen is hidden in front/turnaround and exposed in out_of_shell.png.
- Turnaround layout note for Claude: four views are arranged 2×2, with one common foot baseline per row. A single-row attempt compressed this broad crab; two rows preserve its natural leg/claw span and fill the canvas height.
- Eyes retain restrained catchlights and dull violet local colour, with no emissive eye glow. Slight grey-background tone variation is allowed by the 27 October override.
- All kept images reviewed full size, at 200 px wide, and in 200% inspection crops. Inspection derivatives existed only in memory; none were saved in the project.
- SHA-256 comparisons confirm that all four kept PNGs and all three rejects exactly match their generator originals. File metadata shows no links/reparse points; fsutil hardlink list returned only one path for each PNG. They are ordinary files, never shortcuts or extra hard links.
- Get-PSDrive C was checked immediately before every image generation call. Free space ranged from 41.340 GiB before the first call to 39.154 GiB before the last, always above the 3 GiB stop threshold.
- One image call's response timed out after the complete output had been saved automatically; that PNG was recovered from this chat's generated-images directory and inspected. No duplicate generation was issued for that completed call.
- Intentional project writes were confined to characters_v2/reef_hermit/ and this entry's three files in characters_v2/_rejects/. Other chats' folders and shared review/brief files were not edited.

Stopped after writing this DONE file.

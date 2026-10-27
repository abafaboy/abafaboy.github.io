# ch002-R1 — DONE

27 October 2026, Asia/Tashkent. Built-in image_gen only. Drawing stopped.

Read README_START_HERE.md with its 27 October overrides, the applicable reading-order files, all of PANEL_BRIEF_v2.md, reviews/ch002.md and STATUS.md, script format, acting-test lessons, and the assigned script entries with their neighbouring panels. Only R1's assigned art and R1 logs were changed.

| Panel | Tries used | Kept try | Result |
|---|---:|---:|---|
| P04 | 4 | 4 | Redrawn. Two distinct connected fists pull Yerin's collar and Jaeha's vest shoulder. Nib's skull is smaller than Jaeha's; T patch visible. |
| P14 | 3 | 3 | Low launch from pillar, red/green speed streaks, both knives held back; extra sheathed handles removed. |
| P20 | 1 | 1 | Exactly nine round towers: four left, taller central tower, four right. P20 and approved P57 supplied as references. |
| P21 | 2 | 2 | High view past cracked left pauldron; backhand contact, arched airborne Nib, both knives still gripped. Extra back hilt removed. |
| P22 | 1 | 1 | Nib strikes low on a massive pillar; green shafts, crater debris, dark upper-quarter window space. |
| P24 | 5 | 2 | Best full-size version kept at the limit. Crouch, left palm on ribs, reverse-gripped right knife, spitting, mask/notch and quiet aftermath. **An extra dark cylindrical handle above the left palm remains.** |

16 image calls total. No panel exceeded five tries. All six normal panel files are present; no assigned panel is left undrawn.

## Review concerns

- **P24 is best effort, not a strict pass.** A dark cylindrical grip remains inside the left elbow above the rib palm, in addition to the knife in his right hand and the brown stowed grip at the far hip. Repeated local removal requests did not erase it. Try 5 used a native 1024×1024 target crop but returned 1254×1254 with the object still present; it was saved unchanged as a reject and was not resized or composited. Try 2 is the best full-size image.
- P14's cloak hem is more ragged than ideal; the brown shapes at the back in the final are empty sheaths rather than additional exposed knife handles.
- P04's small distant knight uses softer simplified detail than the foreground. Both drag grips, skull scale and T were the priorities of the review fix.
- These are this chat's visual-review verdicts. The shared approval board was not edited.

## P20 preservation

The generator edited the nine-tower sigil using original P20 and approved P57. Its replacement was composited **unscaled at original pixel size** into the interior of the original badge, as permitted by PANEL_BRIEF_v2.md section 5. The surrounding original pixels were retained. Pixel comparison against the archived original found **0 changed pixels outside the sigil mask** (188,218 changed inside). The mask polygon and exact prompt are recorded in PROMPTS_R1.json. No sharpening or resizing was used.

## Files and verification

- Kept: P04.png, P14.png, P20.png, P21.png, P22.png, P24.png.
- All are PNGs with valid signatures. P14/P21 are 1024×1536; the other four are 1536×1024.
- Original P04 moved before replacement to _rejects/P04_v1_review_missing_grip_oversized_head.png; original P20 to _rejects/P20_v1_seven_tower_sigil.png. Their original bytes were preserved.
- Every discarded generated try is saved as a normal PNG in _rejects/; exact prompts, ordered input files, sources, archive paths and rejection reasons are in PROMPTS_R1.json.
- The original P04 had pre-existing hard links. Its new archive entry was detached into a verified byte-identical ordinary copy. All 18 R1 kept/reject/original PNG files have one hard-link entry each; none is a shortcut or reparse point.
- All 38 explicitly listed approved chapter-2 panel PNGs were hash-checked and are unchanged.
- Full-size review, 200-pixel-wide thumbnail review and 200% edge inspection completed. No compression blocks, JPEG ringing or resized final art introduced.
- Fractional head boxes for every visible character are in REVIEW_R1.json. Final dimensions and SHA-256 hashes are included.
- C: was checked with Get-PSDrive C immediately before every image call. The lowest pre-call free space was 38.055 GiB, above the 3 GiB stop threshold. Final verification saw 37.878 GiB free.
- No extra previews or temporary images were placed in the project. Temporary inspection derivatives outside the project were removed. The native input crop remains beside generator outputs outside the project as prompt provenance.
- No scripts, briefs, shared sheets, approval files or other parts' logs were edited. Nothing published.

Finished and stopped.


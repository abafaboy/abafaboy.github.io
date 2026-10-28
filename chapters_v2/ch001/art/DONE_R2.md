# ch001-R2 — complete

28 October 2026, Asia/Tashkent. Built-in image_gen only.

All eight requested panels were completed in the required order and saved under their normal names in chapters_v2/ch001/art/. Nothing remains to draw for this job.

| Panel | Tries | Completed change |
|---|---:|---|
| P03 | 1 | Sixth summon's long-handled, heavy flared mace rests on his shoulder. Other panel content retained. |
| P06 | 4 | Same mace held upright, without a spear point or halberd blade. Original low gripping arm preserved in the kept attempt. |
| P07 | 2 | Same long-handled flared mace swung during the leap. Other figures and original hand/arm paths retained. |
| P09 | 1 | One tiny white-jacketed Yerin with pink bag added among the seven hunters on the pit floor. |
| P14 | 1 | Small Yerin added at the back of the hunters' group, head at their shoulders, white jacket and pink bag visible. |
| P44 | 2 | Redrawn from behind the knight's RIGHT shoulder; Yerin directly ahead inside his sword arc; RIGHT hand holds sword. |
| P50 | 2 | Redrawn with RIGHT-hand sword at picture-left and LEFT gauntlet reaching around the pillar at picture-right. LEFT pauldron cracked; nine chest-sigil towers countable. |
| P52 | 2 | LEFT gauntlet visibly grips Yerin's pink bag strap after dragging her out; RIGHT hand raises sword; Jaeha braces at pillar base. LEFT pauldron cracked; nine chest-sigil towers countable. |

## Hands, references and review

Hands and arms were checked first. Every visible hand was inspected in an individual or paired 2x in-memory crop before its panel was kept; crop boxes, hand jobs and inspection notes are in REVIEW_R2.json. Full panels were also reviewed at full size and 200 pixels wide. Tiny figures and solid silhouettes naturally hide individual digits; those occluded digits are not falsely claimed to be separately visible.

The current scripts_v2/ch001.yaml has no hands: or hand_ref: fields. Prompts supplied explicit side-specific hand jobs and used the matching approved H1 grip, strap, notebook, reaching and bracing references as applicable. P50 and P52 both explicitly passed characters_v2/hands/grip_hilt_one_hand.png.

The three redraws first passed all five user-specified references in order: knight turnaround, Yerin front, Jaeha front, scale chart, approved P45. A subsequent localized hand-reference pass kept each call within the five-input cap and counted toward that panel's tries. P44's chest badge stays on the front breastplate and is naturally hidden by its rear camera; it was not relocated onto the helm, back or cloak.

All exact prompts, ordered reference files, generator source paths, free-space checks, original backups, discarded candidates and final hashes are recorded in PROMPTS_R2.json. Head boxes for every visible character are normalized to 0–1 in REVIEW_R2.json. No unresolved visual faults are recorded in this chat's kept-panel review.

## Preservation and file verification

- 15 image calls total; no panel exceeded five tries.
- Eight original-panel backups were copied before each panel's first change to _rejects/<id>_v2_<reason>.png. Their SHA-256 hashes match the initial files.
- Seven discarded/intermediate generated candidates are ordinary PNG copies in _rejects/ and are linked to their exact prompts in the log.
- All eight kept PNGs and all fifteen backup/reject PNGs have filesystem link count 1. No shortcut or hard link is used for delivery.
- Every kept PNG is byte-identical to its generator output. P03, P06, P09, P14 and P44 are 1536x1024; P07, P50 and P52 are 1024x1536. No kept panel was resized, recompressed or re-saved through an image editor.
- The final audit found a pre-existing hard link on the old P09 pointing to an earlier generated image outside the project. P09 was detached and recreated as an ordinary copy; the earlier linked source was restored byte-for-byte from the original-panel backup. Both restorations were verified by hash.
- All 53 non-target chapter PNGs, including P45, retain their starting SHA-256 hashes. Scripts, briefs, sheets and other parts' logs were not edited. The hands_fix/ folder was never accessed or changed.
- All inspection crops and thumbnails stayed in memory. No preview or temporary image was saved in the project.
- C: was checked with Get-PSDrive C before every image call and stayed above the 3 GB stop threshold. Final observed free space was 10,051,489,792 bytes (about 9.36 GiB).
- No HTTP 429 usage-limit response occurred. No publication or upload was performed.

Completed: P03, P06, P07, P09, P14, P44, P50, P52.
Remaining: none.

STOP.

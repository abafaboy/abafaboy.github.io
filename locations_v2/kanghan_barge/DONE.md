# L24 DONE — 27 October 2026

Entry L24 is finished. All six requested PNGs are delivered. Prepared for Claude review; this does not mark the images approved.

## Deliverables

- kanghan_barge/key.png — best of five tries; limitations below.
- kanghan_barge/far.png — one try, barge seen offshore from the breakwater.
- fishing_boat/key.png — second try kept.
- pc_bang/key.png — third try kept.
- pim_tower/key.png — first try kept.
- pim_tower/through_rift.png — second try kept.

Each of the four assigned folders contains notes.md, prompts.json and DONE.md. There are 14 generated PNGs in total: 6 kept and 8 rejects. Rejects are ordinary PNG files in the corresponding location's _rejects/ folder. Nothing remains undrawn.

## Barge key retained at the five-try limit

The fifth key is the best overall vessel/deck view and is saved under the normal key.png filename, following README_START_HERE.md's 27 October rule. Its remaining faults are:

- Harpoon barbs, shackle pins and the exact chain gauge are too small to verify precisely in the wide image. The brief's 2 m harpoons and arm-thick chains remain the specification for close views.
- Marine surfaces remain more densely rendered than the preferred broad cel planes.

Four earlier keys were rejected for oversized harpoons, large scale figures and/or a render-like finish. Their reasons are recorded in prompts.json. No sixth barge-key call was made.

## Verification and disk checks

All 14 kept/rejected files are native 1536×1024 PNGs, byte-identical to their generator outputs by SHA-256. Every project PNG has one filesystem link; none is a hard link, shortcut or re-encoded image. PNGs total 32697730 bytes. Full-size, 200-pixel thumbnail and 200% detail checks were performed. QA previews existed only in memory; no preview or temporary image files were saved in the project.

Get-PSDrive C was checked before every image-generation call. Lowest pre-call free space: 35.781 GB using PowerShell's 1GB unit. Free space at the final file audit: 35.163 GB. The 3 GB stop condition was never reached.

## References and scope

Only review-board-approved inputs were used: style_test_v2/acting/A1_P11.png for rendering, and locations_v2/call_void/key.png for the rift view (reviews/STATUS.md and reviews/L8.md). No unapproved character sheet, rejected image, old art or outside image was used as a reference.

All project writes stayed inside locations_v2/kanghan_barge/, fishing_boat/, pc_bang/ and pim_tower/. No other chat's folder or review-board file was modified. No upload or publication was performed. Work stops with these DONE files.

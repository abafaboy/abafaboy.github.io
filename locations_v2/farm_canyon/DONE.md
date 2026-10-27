# L18 — DONE

Completed 27 October 2026. Drawing complete; ready for Claude's review. This file does not grant review-board approval.

All seven required location views are finished:

| File | Kept try | Content |
|---|---:|---|
| `key.png` | 3 | Deep canyon from beside the inner rim; zig-zag walkways, descending giant pipes, distant river and one scale worker |
| `walkway.png` | 1 | Guardrails, spiral trap stone flush in a rock landing, adjacent giant pipe |
| `relief.png` | 1 | Monumental carved coral giant holding back a wave |
| `pipe_gallery.png` | 2 | Wave-carved vaulted tunnel, three separate pipes on cradles |
| `junction.png` | 1 | Round junction chamber, supported branching pipes, one violet leak |
| `glass_wall.png` | 2 | Fogged curved glass barrier, pipe feed, nested-hexagon and crescent plaque |
| `rim_ledge.png` | 2 | White elliptical inner rim in an open mechanical steel iris, missing crossing and walkway stumps |

`notes.md` records layout, route, scale and lighting. `prompts.json` records the final prompt set, approved input references, attempt verdicts, SHA-256 hashes and file checks. Built-in image_gen was used. Twelve image calls total; no image exceeded five tries.

Five rejected PNG originals are saved in this folder's `_rejects/`: two extra-worker canyon keys, one gallery with only one legible pipe, one glass-wall view with undersized feeds, and one rim view with unclear iris blades. No reject was used as an input reference.

Verification: every kept and rejected image is a native 1536×1024 PNG copied byte-for-byte from its generated original. All twelve files have one NTFS path each, no hard links, symbolic links or shortcuts. Full views, 200 px thumbnails and 200% detail crops were inspected. Inspection previews existed only in memory; no extra preview or temporary image files were saved in the project.

C: free space was checked with `Get-PSDrive C` before every image call and stayed above 3 GB. Lowest pre-call reading: 38.626 GiB. Final verification reading: 37.588 GiB; the low-space stop condition was never reached.

Known kept-image notes: the canyon key includes a second small incidental service hut as well as the main engineers' cabin; it does not alter the route. No outstanding required images or blocking visual faults found. Formal review remains for Claude.

Only `locations_v2/farm_canyon/` was written in the project. Other chats' folders and shared briefs were not edited. Remaining work for L18: none.

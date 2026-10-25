# Part A — chapter 1

Completed the permitted drawing and review cycle on 25 October 2026 (Asia/Tashkent). Built-in image_gen; 17 image calls. This is a partial quality pass: three panels accepted, four retained for review after the three-try cap.

| Panel | Tries | Native PNG | Verdict | Remaining issue |
|---|---:|---|---|---|
| P01 | 1 | 1024x1536 | Accepted | None found; anonymous tiny crowd head boxes are approximate. |
| P02 | 1 | 1536x1024 | Accepted | None found. |
| P03 | 3 | 1536x1024 | Review only | Archer free hand returns to hip, low-bow pose/depth remain weak; Nib hem has repeated pointed wear. |
| P04 | 3 | 1254x1254 | Review only | Generator returned 1254 square on all three calls, despite required 1024 square; final rim is warm rather than pale gate light, near-side tooth remains ambiguous. |
| P05 | 3 | 1536x1024 | Accepted | Visible art y~366-625 is inside the middle third; closed mouth is outside eye-only crop as scripted. |
| P06 | 3 | 1536x1024 | Review only | Nib hem still has repeated small triangular teeth after long tatters were reduced. |
| P07 | 3 | 1024x1536 | Review only | Dark red remains in Nib scarf tail despite final black-fill edit; scene requires solid-black summon silhouettes. |

All seven named panel files are present. Review-only files are the final native candidates, also archived under explicit failure names in _rejects; they are not approved chapter art. No P08 image was made because it is a caption.

Checks 11, 11b.1-11 and 11c.1-11 were reviewed at full/native size, 200 px width and 200% detail. REVIEW_A.json contains normalized head boxes, selected verdicts, issues and per-attempt checks. PROMPTS_A.json contains every exact prompt, ordered reference path and hash, generated source, archive/final path and SHA-256 provenance. P03/P06/P07 each have all seven summons plus Jaeha; P04 has only Nib head visible.

All final PNGs and reject copies are byte-identical to their generated sources. Nothing was resized, sharpened, pixel-painted or re-encoded. P04 therefore remains the generator native 1254x1254 and explicitly fails the requested size. At most five reference images per call; at most three total tries per panel. Inspection thumbnails/crops existed only in memory.

Project writes were limited to P01-P07.png, this part's rejects, PROMPTS_A.json, REVIEW_A.json, PROGRESS_A.md and DONE_A.md. Other parts, scripts, briefs, sheets and location keys were not edited. No retired or outside art references used; nothing published or uploaded.

Part A stops here under the brief's attempt cap.

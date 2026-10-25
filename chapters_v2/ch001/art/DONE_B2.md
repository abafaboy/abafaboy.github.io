# B2 — chapter 1 finished

25 October 2026, Asia/Tashkent. Built-in image_gen only. This part stops at the brief’s three-total-tries limit.

| Panel | Tries | Native PNG size | Result |
|---|---:|---|---|
| P15 | 3 | 1536×1024 | Kept: pressure-plate strip |
| P16 | 3 | 1024×1536 | Kept: husk impact |
| P17 | 2 | 1536×1024 | Kept: hunters laughing |
| P18 | 3 | 1536×1024 | Kept: Jaeha name-card |
| P19 | 3 | 1536×1024 | **Review-only, failed 11b.11** |
| P20 | 3 | 1536×1024 | Kept: first stone lizards |

Five panels pass this visual review. P19.png is the final candidate for inspection, **not approved chapter art**: its cropped foreground sleeve/vest boundary still reads soft relative to the notebook and hands. It is also archived byte-for-byte as _rejects/P19_03_review_only_soft_foreground.png. No fourth try was made.

Checks 11, 11b.1–11 and 11c.1–11 were run at native/full size, 200px width and 200% detail crops. REVIEW_B2.json records every final panel’s check results and normalized head boxes: nine visible heads total; P15 and P19 have none. Nonapplicable checks are marked. P18 is inner narration with the scripted closed-mouth public smile.

Production notes: P15’s foot/contact, dust and inner engraved border fit the middle-third crop; the extreme lower outer plate lip extends slightly beyond it. P17’s axeman has shut laughing eyes, so his toward-spearman eyeline is expressed by his head direction. These remain available for owner review.

Prompt audit: all 17 transmitted prompts retain the exact V2 STYLE BLOCK, CLEAN-UP LINE, final NEGATIVE BLOCK, and verbatim script acting/eyeline/foreground in the required order. The reference sentence has one documented assembly typo in every call: “showonly” instead of “show only”. Its design-only/scene-pose instruction is otherwise unchanged. PROMPTS_B2.json preserves the exact transmitted prompts and records this deviation rather than silently correcting history. Character snippet prop changes are the required scene overrides: Jaeha’s book is held and his left chest pocket empty; the writing pencil moves into his right hand in P19.

Every image call used at most five inputs. All references came from characters_v2 or locations_v2, plus this part’s own draft edit targets. No retired, real webtoon or outside reference images were used.

All six final/review-only files and every reject are byte-identical copies of native generator PNGs. No art was resized, re-saved, sharpened, converted, composited or shrink-enlarged. Inspection thumbnails/crops existed in memory only. Native dimensions, PNG decode, SHA-256 source equality, all 17 candidate archives and all head coordinates passed mechanical verification. PROMPTS_B2.json contains source paths, reference paths, exact prompts, hashes and metrics.

Written files: P15.png–P20.png, PROMPTS_B2.json, REVIEW_B2.json, PROGRESS_B2.md, DONE_B2.md and this part’s twelve reject PNGs under _rejects/. No other part’s files, scripts, sheets or briefs were edited. Nothing published or uploaded.

B2 is finished under the try cap and stops here; the P19 visual failure and reference-sentence spacing deviation remain explicitly documented.

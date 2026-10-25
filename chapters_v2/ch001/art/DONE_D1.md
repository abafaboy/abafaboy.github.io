# D1 finished: chapter 1, P33-P38

All six assigned panels are delivered. Four pass; two are explicitly review-only after the maximum three tries. No fourth try was made.

| Panel | Tries | Native PNG size | Result |
|---|---:|---|---|
| P33 | 1 | 1024x1536 | OK: dormant kneeling knight and boss-room reveal |
| P34 | 1 | 1536x1024 | OK: industrial wrist cuff, stamped shape and snapped link |
| P35 | 3 | 1536x1024 | OK: boot step within middle third |
| P36 | 3 | 1536x1024 | REVIEW ONLY: top 15 pixels of the image band exceed the strict middle-third boundary |
| P37 | 3 | 1024x1536 | OK: rising knight; red face-hole, green shafts, cracked LEFT pauldron; Jaeha back T restored |
| P38 | 3 | 1536x1024 | REVIEW ONLY: calling hand remains near ear/neck rather than clearly cupped at mouth |

## Remaining flags

- **P36:** final art band starts at y327; the strict middle third begins at y342. The red hollow remains readable in the central crop, but this is recorded as a delivery-rule failure. Final candidate is also archived in `_rejects/P36_3_15px_above_middle_third.png`. It was neither cropped nor resaved to hide the issue.
- **P38:** final shield has a visible left forearm support, rear strap/cuff and fist around the rear handle; foreground blur and continuous floor chains are corrected. Mok's right calling hand still reads as an ear/neck touch, so 11c.2 remains failed. Final candidate is also archived in `_rejects/P38_3_calling_hand_near_neck_not_cupped_mouth.png`.

## Checks and provenance

- Sections 11, 11b.1-11 and 11c.1-11 were checked for every attempt, at full native size, 200 px wide, and 200% detail views. Failures are retained explicitly; no blanket all-pass claim is made.
- Fourteen built-in imagegen calls total, at most five images per call. Every exact prompt and ordered reference path is in `PROMPTS_D1.json`, including all rejects and edit targets.
- All six delivered panels and all reject PNGs match their generator source bytes and SHA-256 hashes. Exact native dimensions and PNG signatures were verified. No resize, sharpening, screenshot, JPEG/WebP conversion or art resave occurred. QA derivatives stayed in memory.
- Prompt audit confirms the exact V2 STYLE BLOCK, CLEAN-UP LINE and NEGATIVE BLOCK in order, plus verbatim script camera, light, art, acting, eyeline and foreground fields where present. Character snippets retain approved designs; Jaeha's held-notebook scene overrides his pocket snippet.
- `REVIEW_D1.json` records normalized head boxes for every visible head, final status, all 33 checks and attempt history. Inserts without heads have empty head maps.
- Intentional project writes are limited to P33.png-P38.png, D1's four reports and D1 rejects. No other chat's panels, scripts, sheets or briefs were changed. Nothing was published.

D1 has reached its requested stopping point. STOP.

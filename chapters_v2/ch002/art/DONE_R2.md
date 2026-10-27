# ch002-R2 — complete

27 October 2026, Asia/Tashkent. Built-in image_gen. Drew only P35, P36, P40, P41, P42 and P43 from scripts_v2/ch002.yaml.

| Panel | Tries | Kept PNG | Local review |
|---|---:|---|---|
| P35 | 5/5 | P35.png — 1536×1024 | Best at cap; faults below |
| P36 | 4/5 | P36.png — 1536×1024 | Kept after scale/window-space corrections |
| P40 | 1/5 | P40.png — 1536×1024 | Full-canvas strip source; eyes inside middle half, no bars |
| P41 | 2/5 | P41.png — 1536×1024 | Pommel on crossed knives; amber contact ring; spare hilt removed |
| P42 | 2/5 | P42.png — 1024×1536 | Kneeling CARRY collapse, right palm down, notebook in left fist, dark window field |
| P43 | 2/5 | P43.png — native 1254×1254 | Yerin reaches without touching, horrified open mouth, simplified background |

## Faults and uncertainties

P35 reached the five-try limit. The fifth candidate is the best overall and is kept under the normal filename as instructed. The visible bronze breastplate badge still has TEN towers instead of nine; Nib's anatomical LEFT ear is connected again, but its V-notch remains indistinct. This panel needs Claude's review and is NOT claimed to pass those locks. Earlier candidates had a wrong-side wound, spare knife hilts or a detached ear tip. The kept candidate has the correct LEFT armpit wound at picture-right, two held knives with empty sheaths, white impact field and violet ash.

No other material uncertainty was found in the local review. These are local visual verdicts; external approval remains with Claude. P36's tiny Nib facial details are limited by wide-shot scale. P41's knight head is outside the crop; P43 includes only Jaeha's shoulder, so neither has an additional head box.

## Records and verification

- PROMPTS_R2.json contains all 16 exact prompts, ordered references, source script entries, every pre-call C: free-space check, generator sources, saved candidates, rejection reasons and file metadata.
- REVIEW_R2.json contains fractional head boxes for every visible head, local checks and explicit P35 faults.
- PROGRESS_R2.md records each finished panel.
- Ten rejected candidates are ordinary PNG files in _rejects/. No existing assigned panel file was present when drawing began; no approved panel was replaced.
- All 38 panels explicitly listed as approved in reviews/ch002.md retain their initial SHA-256 hashes. The review text says 39, but its explicit list contains 38; all listed files were checked.
- All 16 saved candidate files match their generator source bytes exactly. No resizing, re-encoding, sharpening, hard links or shortcuts. Each file has one filesystem hard-link name and no reparse/link type.
- Native images, relevant detail crops and 200-pixel thumbnails were reviewed. All QA crops/thumbnails stayed in memory; no extra previews or temporary images were saved in the project.
- No image call used more than five inputs. Own rejected candidates were used only as edit targets; character/location/continuity references were approved sheets, location keys and approved chapter-2 panels.
- Get-PSDrive C was checked immediately before every image call. Lowest pre-call free space: 41405485056 bytes (about 38.56 GiB), above the 3 GiB stop threshold. Final verification free space: 40880078848 bytes.

All six assigned panels are saved. Nothing remains undrawn in R2. No scripts, briefs, sheets or other jobs' files were edited. No publishing or upload. Stopped after this report.

# ch002-R6 — P52 complete

27 October 2026, Asia/Tashkent. Five built-in image_gen attempts; selected try 4. Stopped at the five-try limit.

P52.png is 1536×1024, with only Nib and the small area uncovered by his reduction edited. The original is preserved byte-for-byte as _rejects/P52_v3_nib_still_big.png. All PNGs are ordinary independent files (link count 1).

| Try | Nib hair-to-soles | Nib head | Crown y | Soles y | Result |
|---|---:|---:|---:|---:|---|
| 1 | 301 px | 65 px | 639 | 940 | candidate |
| 2 | 293 px | 71 px | 628 | 921 | reject |
| 3 | 268 px | 66 px | 647 | 915 | reject |
| 4 | 277 px | 67 px | 660 | 937 | Selected |
| 5 | 316 px | 74 px | 625 | 941 | reject |

Target: about 285 px body, 65 px head, crown 650 and soles 935. Selected try 4 is 277 px/67 px, both within about 3% of target and README 27 October about 5% tolerance. It has the lowest combined relative body/head error. The crown is about 10 px low; soles about 2 px low. These are the remaining small size deviations.

Yerin was measured on every attempt. Her native outer hair silhouette, including lifted locks, is about 119 px to the chin; the denser crown-to-chin span is about 101 px. This differs from the brief approximate 90 px. Her original pixels were preserved, and the explicit Nib 65 px head target governed the edit. See REVIEW_R6.json for the landmarks, measurements and ratios.

Nib retains the crouch, upward look back, left-eye mask, scarf, binoculars, cloak, bare feet and exactly two knives held low. His far-side left ear notch and single left fang remain partly occluded at this original head angle; their visibility is not newly certified. The old larger silhouette is removed and the floor, rubble and arches continue through the revealed space.

To preserve the rest exactly, the selected generated local patch was composited onto the untouched original at native pixel size. No art was resized or sharpened. Pixel comparison: zero changed pixels outside the local Nib repair mask; zero changes to Jaeha, Yerin and the right pillar; zero changes in the upper hall. Diff bounds: x 244–572, y 543–959. Every other chapter 2 PNG hash is unchanged. Full-size and 200 px phone-size visual QA completed in memory, with no project previews or temporary images.

C: free space was checked with Get-PSDrive C immediately before each image call: 34.29, 34.05, 33.76, 33.23 and 32.74 GiB. Every check exceeded 3 GB. Exact prompts, ordered references, input states, generated paths/hashes and archives are in PROMPTS_R6.json; measurements, head boxes, selection and pixel verification are in REVIEW_R6.json.

Delivered: P52.png, PROMPTS_R6.json, REVIEW_R6.json, DONE_R6.md, original archive and all five native generated candidates in _rejects/. No scripts, briefs, character sheets or shared review-board files changed. No further drawing remains for this job. Claude approval remains external to this chat. STOP.

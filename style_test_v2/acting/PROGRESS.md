# Acting test progress

References frozen; exact prompts prepared for P11, P28 and P23.
P11 attempt 1 rejected: busy background, sawtooth wear, wrong visible pencil side, left hand in pocket. P11 attempt 2 saved for thumbnail review.
P28 attempt 1 rejected: wrong mage identity, missing T patch, Mok not smiling.
P28 attempt 2 rejected: unsupported shield/idle pocket hand, wrong arm path; P23 attempt 1 rejected: warm light, depth blur, detailed right zone.
P11 attempt 2 rejected after close-up: thumb at hip rather than hooked in belt.
P23 attempt 2 rejected after close-up: source still too golden.
P11 attempt 3 done: accepted after full-size, 200 px and hand-crop review.
P28 attempt 3 rejected: unsupported shield arm, wrong gaze and daylight.
P28 attempt 4 saved for review only: shield grip/arm connection and lamp eyeline still fail; third and final redo used.
P23 attempt 3 done: accepted after green-light correction, full-size and 200 px review.
PROMPTS.json, REPORT.md and REVIEW_art.json complete. Three 1536x1024 primary PNGs saved; no further drawing.

## Round 2

Claude's strict review supersedes the round 1 P11 pass claim. A3 is locked unchanged. P28 restaged, six unique images requested; B2 will be byte-identical to new A2. Up to three total tries per unique image.
R2_A1_P11_attempt01: kept; Three scoped fixes applied: flat opaque vest and sleeve, visible right-shoulder to left-hip shield sling, belt-hung black scabbard with steel chape. Approved poses, faces and crop preserved.
R2_B1_P27_attempt01: rejected; Right hand reads as vertical thumbs-up rather than thumb jab back at door; grounded shield bottom is outside crop.
R2_A2_B2_P28_attempt01: rejected; Mage became bearded axeman, T patch lacks glyph, near right arm and far left arm jobs reversed, garment shards persist.
R2_B1_P27_attempt02: kept; Open mid-line fake smile, cold down-left eyes, horizontal thumb jab toward right-hand door, left-arm shield support and visible floor contact; left third calm.
R2_A2_B2_P28_attempt02: kept; Near right arm clamps shoulder, far left hand rests shield top, correct male mage and T restored, Jaeha right eye up and closed strained listening smile, Mok open mid-line. A2 and B2 copied identically.
R2_B3_P29_attempt01: rejected; Vest and hoodie contain diagonal shard shading; face and speaking mouth retained for edit. Native 1254 square requires output normalization.
R2_B3_P29_attempt02: kept; Clothing repainted to broad opaque shapes; asymmetric open warning mouth, right eye up, right-ear pencil and reacting palms preserved; normalized from native square to required 1024 square.
R2_B4_P31_attempt01: rejected; Shield does not touch Jaeha back and near right arm holds it; notebook duplicated in pocket and wrong near hand; Mok face angry rather than dead flat.
R2_B4_P31_attempt02: rejected; Duplicate tower shields, wrong near-arm support, closed speaking mouth, residual shard clothing and foreground blur.
R2_B5_P32_attempt01: kept; Single visible right eye in profile, level doorward calculating gaze, low brow and raised lower lid, mouth excluded, attached right-ear pencil; native 3-to-1 strip normalized to 1536 by 512.
R2_B4_P31_attempt03: review_only_failed_checks; Final try: back contact and open mouth improved, but duplicate notebook, ambiguous near-right shield arm, angry brows, shard sleeve shadows and blurred foreground plate remain.
B_sequence.png stacked B1/B2/B3/B4/B5 at 800x2826 with exact 40 px white gaps. A3 hash unchanged; A2/B2 identical.
Round 2 full-size, 200 px and scroll review complete. B4/P31 remains failed after three total tries; all required files saved, report/manifest/review updated. STOP.

## Final targeted B4 correction

Claude passed A1, A2=B2, B1, B3 and B5 and the scroll rhythm. Current P31 explicitly permits the existing right-arm shield shove. Old B4 moved to _rejects/B4_P31_r2_angry_face_duplicate_notebook.png. One scoped edit prepared: cold flat face and empty left chest pocket only.
Final B4 edit done in one imagegen call: cold flat face and empty orange left pocket; right-arm shield and all other staging retained. Old B4 preserved under requested reject name.
B_sequence rebuilt at 800x2826 with four 40 px white gaps. Seven approved PNG hashes unchanged; A2=B2 still identical. PROMPTS.json, REPORT.md, REVIEW_art.json and verification metrics updated. STOP.

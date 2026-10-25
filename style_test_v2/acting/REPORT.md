> **Latest: Round 2 is complete. A3 is unchanged; A1 and the restaged P28 are replaced; B1–B5 and B_sequence are saved. B4/P31 still fails after three tries. The Round 2 section below supersedes the earlier pass claims.**

# A1 acting test — chapter 1

25 October 2026, Asia/Tashkent. Built-in `image_gen` only. Read the README reading order, `ACTING_TEST_BRIEF.md`, the updated acting study including 5b, style guide 6b/10/11/11b/11c, script format and source panels P11, P28 and P23. Jaeha's `DONE.md` contains the required Round 1 fixes section.

**Result: P11 and P23 pass this visual review. P28 remains a failed test after the initial candidate and three redos.** Its last candidate is saved as `A2_P28.png` for review and duplicated in `_rejects/`; it is not represented as accepted chapter art. No further drawing follows this report.

## Delivered files

| File | Selected candidate | Status |
|---|---|---|
| `A1_P11.png` | attempt 03 | Accepted in this visual review |
| `A2_P28.png` | attempt 04 | Review only; 11c.2 and 11c.3 fail |
| `A3_P23.png` | attempt 03 | Accepted in this visual review |
| `PROMPTS.json` | Ten generated candidates | Exact prompts, ordered input files, source panel fields, imagegen source files, rejects and final verdicts |

All three main PNGs are **1536×1024**. They are direct copies of their generated sources, without pixel retouching or resizing. The `_qa/` thumbnails and crops are inspection derivatives only. `_references/` holds byte-identical snapshots of the current approved character/location inputs so other chats' subsequent edits cannot alter this test's provenance.

## Acting checks on the selected images

“Pass” below means the prohibited condition in style guide 11c was not found. The failed P28 candidate is included for an explicit comparison.

| 11c check | A1 / P11 | A2 / P28, review only | A3 / P23 |
|---|---|---|---|
| 1. No mannequin stance | Pass: Mok's loaded leg and loose opposite knee contrast with Jaeha's bow | Pass: Mok leans forward; Jaeha braces and recoils backward | Pass: wall compression, raised shoulders and bent, joined knees |
| 2. Hands follow acting | Pass: two-finger shoo, belt-hooked thumb, busy hunters; Jaeha's hands are occluded at his chest | **Fail:** the visible grip reads like a second sword hilt; its attachment to the shield and specified arm paths remain unclear | Pass: both closed hands grip one bag strap; sleeves and joints remain coherent |
| 3. Correct eyelines | Pass: Mok looks toward the bowed foreground listener; hunters attend to gear | **Fail:** Jaeha's pupils turn sideways/back instead of clearly up-right to the red lamp | Pass: eyes turn off-panel right across the corridor |
| 4. Emotion reads | Pass: lazy asymmetric grin with unsmiling eyes; subordinate bow | Pass for the broad contrast: Mok's coercive grin against Jaeha's sweating, strained placation; incorrect eye direction is counted above | Pass: wide eyes, open questioning mouth, sweat and whole-body fear |
| 5. Framing has depth/crop | Pass: foreground back/head/T patch crop, speaker beyond | Pass: side two-shot and cropped iron door | Pass: cropped crater lip at left, off-centre figure and calm right third |
| 6. Camera changes | Pass: P10 object insert → P11 over-the-shoulder | Pass: P27 low portrait → P28 side two-shot | Pass: P22 low tilted impact → P23 three-quarter half-body reaction |
| 7. No lineup | Pass: two smaller hunters at different depths behind Mok | Pass: hunters overlap at a farther depth behind the pushing pair | Pass: one character only; lineup condition inapplicable |
| 8. No copied standing-sheet pose | Pass | Pass for the full pose; residual hand/gear bias remains under check 2 | Pass |

## P11: kept attempt 03

The cold upper-left LED source, cool pit planes and orange foreground vest separate clearly at 200 px width. Background detail is reduced to broad steel-pile shapes; the upper region is usable for lettering. The foreground head/right shoulder/back patch crop remains, with Jaeha's notebook and hands hidden against his chest rather than duplicated in a pocket. His pencil is occluded on the far right side, not moved to the visible left ear. The only glyph is the back T.

Mok's two-finger flick, belt contact, lazy grin and weight shift carry the dismissive exchange. The spearman works a glove strap at his teeth and the bearded axeman yawns with the axe across his shoulders. Full-size hand inspection found no extra digits, disconnected limbs or unsupported props. Large opaque clothing shadows and smooth vest edges replace the first candidate's distressed, shard-like treatment. Sections 11 and the applicable 11b checks pass; sheet-background check 11b.8 does not apply to panels.

**Standing-pose drift:** no literal front-sheet stance was copied. There was a recurring default hand placement: attempt 01 put Mok's left hand in a pocket; attempt 02 moved it outside but left the thumb at the hip. The targeted third edit raised the hand and hooked the thumb at the belt while preserving the scene's bow, shoo and weight shift.

## P28: selected attempt 04 is still rejected

The final edit improves the red-lamp key, removes the unwanted warm daylight, reduces the background and changes the idle hip hand to a grip. The shield visibly presses against Jaeha's back, his heels brace, both palms rise in placation, and the ponytailed swordsman and male mage share a look behind them. The T patch and the correct mage identity were restored after attempt 01.

The close-up remains a failure: the new vertical grip has the appearance of a sword hilt, with no unambiguous mechanical connection to the shield. The prescribed anatomical left shield arm/right pointing arm paths are still not convincing. Jaeha's pupils also miss the up-right lamp target. These fail 11c.2/11c.3, functional-gear/anatomical clarity in 11b.4/11b.7, and the corresponding design/acting checks in section 11. A full strict pass is not claimed.

**Standing-pose drift:** the complete neutral model-sheet stance was avoided, but repeated generations returned a default hip/pocket hand while the shield floated beside the body. The last targeted edit changed the hand and retained the forward push/backward brace, but did not resolve the grip and eye-direction problems. The brief's three-redo limit has been reached, so the last candidate is retained for inspection, with the same bytes archived under its failure name.

## P23: kept attempt 03

Yerin's back presses into the wall beside the cropped fresh crater; shoulders rise, elbows tuck, both hands lock on the strap and her bent knees press together. Her round freckled face, low ponytail, loose cheek strand, off-white jacket, anatomical-left sleeve cross and single pink bag stay on model. The face turns three-quarters toward off-panel right, with widened eyes, an open question and sweat. The right third contains only quiet, lower-contrast wall; no card or text is drawn.

The final targeted edit replaces yellow-gold light with sickly green on the crater, hair edge, cheek edge and jacket, preserving cool violet shadows and natural local skin colour. The earlier depth blur is gone. Figures, hands and foreground chips have drawn edges; the simplified wall does not rely on depth-of-field blur. Full-size and 200 px review pass sections 11, applicable 11b checks and all applicable 11c checks. Closed gripping fingers are partly occluded by the strap, with no duplicated digits or broken joints.

**Standing-pose drift:** none toward the neutral front sheet. The strap-gripping vocabulary is also on the fear expression sheet because it is required by the script; the compressed wall pose, bent knees, torso/head angle and off-panel gaze come from this scene. The retries corrected rendering and light, not a mannequin stance.

## Reject ledger

Every filename below is in `_rejects/`. Each candidate's exact prompt and inputs are recorded under its matching attempt id in `PROMPTS.json`.

| Candidate / archived file | Rejection reason |
|---|---|
| `A1_P11_attempt01_busy_background_sawtooth_wrong_pencil_thumb.png` | Establishing-level background and cluttered calm band; shard-like vest streaks and sawtooth armhole; pencil at the visible wrong ear in back view; left hand in pocket |
| `A1_P11_attempt02_thumb_at_hip_not_hooked_in_belt.png` | Pocket fixed, but close-up shows thumb at the hip/belt edge instead of clearly hooked into the belt |
| `A2_P28_attempt01_wrong_mage_missing_T_Mok_no_smile.png` | Mage drifts toward the bob-haired crossbow woman; chest T omitted; Mok's stern mouth misses camera smile |
| `A2_P28_attempt02_floating_shield_idle_hand_wrong_arm.png` | Idle pocket hand, unsupported shield and unconvincing arm assignment; Jaeha's mouth reads more as a grimace |
| `A2_P28_attempt03_unconnected_shield_arm_wrong_eyeline_daylight.png` | Hip/sword hand still does not connect to shield; wrong Jaeha eye direction; added warm daylight and busy ruined architecture |
| `A2_P28_attempt04_review_only_ambiguous_shield_grip_wrong_gaze.png` | Grip/arm connection remains ambiguous and sword-like; Jaeha's gaze still misses lamp; same image also delivered as review-only `A2_P28.png` |
| `A3_P23_attempt01_warm_light_depth_blur_busy_right.png` | Yellow-gold source, foreground/background depth blur and receding architecture in the calm zone |
| `A3_P23_attempt02_key_still_yellow_green.png` | Blur and calm zone fixed, but lit hair/stone still read too golden in the close-up |

## Verification and scope

- Ten successful built-in image-generation calls: P11 three candidates, P28 four candidates, P23 three candidates. P28 uses the initial candidate plus three redos; P11/P23 use two redos each.
- One preflight P11 call with six inputs was rejected by the tool before producing an image. Its exact request is preserved in `_qa/PROMPTS_preflight_six_refs.json`; every successful call uses at most five inputs. Redundant expression/location inputs were omitted where required by that cap; all visible character designs remain represented, including the hunters' lineup. Targeted edits use this chat's own archived candidate as the edit target.
- JSON parses; every recorded output/reference exists. `_qa/image_metrics.json` records dimensions, source-copy equality and reference hashes. Exact V2 style/cleanup/negative/reference blocks and verbatim source acting, eyeline and foreground text were checked.
- `_qa/contact_200px.png`, individual 200 px thumbnails and hand/face crops support the full-size visual review. `PROGRESS.md` and `REVIEW_art.json` record the final panel outcomes.
- Intentional project writes are confined to `style_test_v2/acting/`. No shared briefs, research, scripts, character folders or location folders were changed. No retired or external webtoon art was used. Nothing was published.

The acting test is finished with two accepted panels and one documented failure. This report does not approve proceeding to chapter production.


## Round 2 — strict review, restaged P28 and five-panel dialogue run

**Current result:** the targeted A1 edit and B1/P27, new A2=B2/P28, B3/P29 and B5/P32 are kept after visual review. **B4/P31 is review-only and still fails after its three total tries.** It is included in the requested sequence and also archived as a reject. A3/P23 is retained byte-for-byte as Claude instructed. No full strict-test pass is claimed.

Claude's Round 2 findings supersede this report's earlier P11 acceptance: that image had translucent shard shading, an unsupported back shield and an exposed blade. The original kept image is archived as `_rejects/R1_A1_P11_Claude_shards_floating_shield_bare_sword.png`; the old report/manifest/progress/review are preserved under `_qa/round1_archive/`.

### Files, dimensions and tries

| File | Final size | Round 2 tries | Result |
|---|---|---|---|
| `A1_P11.png` | 1536×1024 | 1 | Three requested changes only; kept |
| `A2_P28.png`, `B2_P28.png` | 1536×1024 | 2, shared image | Restaged shoulder steering; byte-identical files; kept |
| `A3_P23.png` | 1536×1024 | 0 | Claude's accepted image, unchanged |
| `B1_P27.png` | 1536×1024 | 2 | Low portrait, open fake smile and backward thumb jab; kept |
| `B3_P29.png` | 1024×1024 | 2 | Open warning mouth and raised right eye; kept |
| `B4_P31.png` | 1536×1024 | 3 | Last candidate, review-only; remaining failures below |
| `B5_P32.png` | 1536×512 | 1 | Right-eye profile calculation; kept |
| `B_sequence.png` | 800×2826 | Deterministic stack | B1→B2→B3→B4→B5; four white 40 px gaps |

Eleven successful built-in imagegen calls produced six unique Round 2 assets. Three is a **total-try cap**, not three additional redos. No asset exceeded it. A2 and B2 share one generation history.

### Per-panel acting checks

P = pass on the selected image; F = failure; — = outside the visible crop or not applicable. A3 remains under Claude's explicit keep instruction, rather than being redrawn or newly certified here.

| 11c check | A1/P11 | B1/P27 | A2=B2/P28 | B3/P29 | B4/P31, review only | B5/P32 |
|---|---|---|---|---|---|---|
| 1. No mannequin stance | P | P | P | P, lean in crop | P | — |
| 2. Hands follow acting | P, original gestures retained | P | P | P | **F: shield arm assignment** | — |
| 3. Eyelines | P | P, off-left/down | P, door/up/shared look | P, up-right | P, back/floor | P, level doorward |
| 4. Named emotion | P | P | P | P | **F: anger instead of dead flat** | P |
| 5. Depth/crop | P | P | P | P | P | P |
| 6. Camera changes | P | P | P | P | P | P |
| 7. No lineup | P | — | P | — | — | — |
| 8. No copied sheet stance | P | P | P | P | P | — |
| 9. Speaker/listener mouths | Scoped original grin retained | P, open speech | P, Mok open; listeners closed | P, open speech | P, small speech gap; listener closed | —, inner thought/eye crop |
| 10. Face/head moves across lines | Separate earlier scene | P | P | P | P, though exact mood fails 4 | P |
| 11. Supported props | P, sling/scabbard | P, shield strap/grip/floor | P, hand and floor support | P | **F/unclear foreground plate** | P, attached pencil |

**A1/P11 — targeted edit.** The kept image itself was passed as the edit target. Jaeha's visible vest and hoodie sleeve were repainted into flat local colour and a few broad opaque shadow shapes, without the translucent diagonal mosaic. Mok's shield now has a thick black sling visibly crossing from his anatomical right shoulder to left hip, with the shield top behind the right shoulder. His one sword is inside the belt-hung matte-black scabbard with steel chape from `mok_hangyu/details.png`. The bow, crop, shooing fingers, belt thumb, grin, hunters, lighting and set were preserved. The original approved grin was not reposed because the user expressly limited this edit to three changes; hidden Jaeha mouth remains hidden. No model-sheet stance drift was introduced.

**B1/P27 — kept attempt 02.** Mok turns his head back-left toward off-panel Jaeha, chin lifted, cold down-left eyes contrasting with the open white-toothed camera smile. His right thumb now jabs horizontally backward at the picture-right door; the first attempt's vertical thumbs-up was rejected. The left-arm shield has a rear grip/strap and lower floor contact; the sword is sheathed at the belt. The left third remains dark and available for the name card. Large cropped low-angle staging differs from P28. No copied neutral sheet stance.

**A2=B2/P28 — kept attempt 02.** This started as a fresh drawing of the restaged script, using the current design/prop/location references rather than the failed round 1 shield-nudge image. The second attempt corrects the arm jobs: Mok's near right sleeve/forearm reaches across to clamp Jaeha's near right shoulder; the far left hand rests on the top of the grounded shield. His open mouth carries the line while his chin and eyes turn toward the door. Jaeha leans backward, palms out, head tipped back, right pupil rolled toward the lamp, with a closed strained listening smile and sweat. The right-ear pencil is visible and the far left eye stays behind its fringe. The swordsman and clean-shaven male mage share a closed-mouth look at staggered depths. The first candidate's bearded axeman/mage mix-up and missing T were fixed. No literal sheet stance; the initial arm-side bias needed a targeted correction. No shield touches Jaeha's back in P28.

**B3/P29 — kept attempt 02.** The camera closes to a tighter three-quarter view on the same side. Jaeha's chin is less tipped back than P28, the brows tighten unevenly, and the closed listening smile opens into an asymmetric nervous warning mouth. His right eye stays high under the upper eyelid, pencil remains behind the near right ear, and both cropped palms continue placation. The far-left notebook remains in its pocket in this panel. The clothing-only edit simplifies the orange/grey shadows while preserving the face and hands. His changed mouth/head angle follows the scene, not the front-sheet pose.

**B4/P31 — attempt 03 remains failed.** The last fresh composition improves the edge-to-back contact and shows an attached rear shield strap/handle. Mok's smile is gone and his lips have a small opening on the short line; Jaeha pitches down and stumbles right with a closed reacting mouth. Those broad acting changes are visible. However, a second notebook remains in the chest pocket while another is held forward, failing 11b.4. The shield arm still reads as the near/right arm rather than the specified left-arm path, failing 11c.2/anatomical-side clarity. Mok's knitted brows read anger rather than the scripted flat dead affect, failing 11c.4. The hoodie retains overly broken fold-shadow shapes, failing the strict 11b.1 standard, and the blurred plate at the left edge reads like an additional shield with unclear support, failing the drawn/no-depth-blur and prop-clarity checks. The final candidate is therefore not accepted. No fourth try was made.

**B5/P32 — kept attempt 01.** The close-up is the visible right eye in profile, facing picture-right. The upward public warning has changed to level, narrowed calculation: low brow, raised lower lid, no smile or mouth in frame. The pencil is attached behind the right ear; the long fringe belongs to the far left eye. This is inner thought, so 11c.9 does not call for a talking mouth. No extra eye, system glow, floating prop or neutral standing pose appears.

### Dialogue rhythm and continuous staging

| Beat | Face/head/mouth change | Listener/body response |
|---|---|---|
| P27 | Mok back-left head turn, lifted chin, open false smile | Thumb invites toward the right-hand door |
| P28 | Mok leans down/right, chin jerks toward door, open speech | Jaeha tips back, pupil up, closed strained smile, palms out; hunters share a look |
| P29 | Jaeha turns into tighter three-quarter, uneven brow, open warning mouth | Sweat and half-raised palms retain the pressure of the prior beat |
| P31 | Mok pitches down, smile drops, small speech gap | Jaeha pitches forward, gaze down, reacting mouth closed; precise props/mood still fail |
| P32 | Jaeha levels his head/gaze, lowers brow and narrows eye | Public mask gone; mouth outside the extreme crop |

The action axis is retained: the door is always picture-right, including off-panel in the close-ups. The shot ladder changes low portrait → side two-shot → square close-up → low action two-shot → extreme profile strip. The sequence was reviewed as one scroll as well as at full panel size and 200 px width. The P31 failure remains visible and documented inside the strip; stacking does not turn it into an accepted panel.

### Round 2 rejects

All exact prompts and ordered reference paths are in `PROMPTS.json`, including every reject and the review-only final P31.

| File in `_rejects/` | Reason |
|---|---|
| `R2_B1_P27_attempt01_right_hand_reads_as_vertical_thumbs_up_rather_than_thumb_jab_back_at_door_grounded_shield_bottom_is_outsi.png` | Right hand reads as vertical thumbs-up rather than thumb jab back at door; grounded shield bottom is outside crop. |
| `R2_A2_B2_P28_attempt01_mage_became_bearded_axeman_t_patch_lacks_glyph_near_right_arm_and_far_left_arm_jobs_reversed_garment_shar.png` | Mage became bearded axeman, T patch lacks glyph, near right arm and far left arm jobs reversed, garment shards persist. |
| `R2_B3_P29_attempt01_vest_and_hoodie_contain_diagonal_shard_shading_face_and_speaking_mouth_retained_for_edit_native_1254_squa.png` | Vest and hoodie contain diagonal shard shading; face and speaking mouth retained for edit. Native 1254 square requires output normalization. |
| `R2_B4_P31_attempt01_shield_does_not_touch_jaeha_back_and_near_right_arm_holds_it_notebook_duplicated_in_pocket_and_wrong_near.png` | Shield does not touch Jaeha back and near right arm holds it; notebook duplicated in pocket and wrong near hand; Mok face angry rather than dead flat. |
| `R2_B4_P31_attempt02_duplicate_tower_shields_wrong_near_arm_support_closed_speaking_mouth_residual_shard_clothing_and_foregrou.png` | Duplicate tower shields, wrong near-arm support, closed speaking mouth, residual shard clothing and foreground blur. |
| `R2_B4_P31_attempt03_final_try_back_contact_and_open_mouth_improved_but_duplicate_notebook_ambiguous_near_right_shield_arm_ang.png` | Final try: back contact and open mouth improved, but duplicate notebook, ambiguous near-right shield arm, angry brows, shard sleeve shadows and blurred foreground plate remain. |

### Final verification

- A3 SHA-256 remains `650c38f0f60f7ef39fcddb440d2fc6abe6cb574e717ee47ab97c5ec5e5ee6c8f` before and after Round 2. No A3 generation or write occurred.
- A2 and B2 are byte-identical: `44d771a6d0847a1c8835235288bf596b9b786fa9171a35805ef022af0a131b41`.
- Required final PNG sizes decode correctly. The generator returned native 1254×1254 for B3 and 2172×724 for B5; these were mechanically resized with Lanczos to the specifically requested 1024×1024 and 1536×512. Native originals are retained under `_qa/round2/native/`. Content corrections used imagegen, not pixel retouching.
- The strip is 800×2826: panel heights 533, 533, 800, 533 and 267, with four exact 40 px pure-white gaps. No title, panel label, speech bubble or SFX was composited into it.
- Exact V2 style/cleanup/negative blocks and verbatim acting/eyeline/foreground text were validated for all Round 2 candidates. Inputs are current approved snapshots or this chat's own drafts; ordered input hashes are checked. No successful request exceeded five reference images.
- `_qa/round2/metrics.json` records candidate counts, final/native sizes, hashes and deterministic resize provenance. `_qa/round2/contact_200px.png` and individual thumbnails support visual inspection. Root `PROMPTS.json`, `PROGRESS.md` and `REVIEW_art.json` are updated.
- Intentional writes stayed within `style_test_v2/acting/`. No shared character, location, research, script or brief files were changed. Nothing was published.

Round 2 is finished and stops here, with B4/P31 explicitly review-only after the permitted three tries.

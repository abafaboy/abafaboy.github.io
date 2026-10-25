# S14 Lyra — completed set, strict QA record

25 October 2026. The owner approved the revised `front.png` ("lyra is good"). That exact file was the first design reference for all nine new calls and remains byte-for-byte unchanged.

**All requested files are generated. The new sheets are not a clean strict QA pass after three tries each.** Their residual failures and uncertainties are recorded below. No fourth tries were made. Completion means the authorized S14 generation and handoff are finished; it does not invent owner approval of the new sheets.

## Deliverables

| File | Content | Selection |
|---|---|---|
| front.png | Approved adult Lyra in cropped plunging halter, bare midriff, short hip-slit skirt over short dark shorts and thigh-high boots | Existing approved file unchanged |
| turnaround.png | Front, three-quarter, side and back; four bows; approximately same scale/baseline | Attempt 3 of 3 |
| expressions.png | Eight heads/shoulders in the exact requested 4x2 reading order | Attempt 3 of 3 |
| details.png | Bow, flute, braid/beads, left chest guard, left bracer, right glove, boots, with useful construction crops | Attempt 3 of 3 |
| card.json | Identity, height, complete hex palette, anatomical locks, expression order, files and QA status | Updated |
| prompts.json | All historical and current exact prompts/tool arguments, references/hashes, reject reasons and per-attempt checks | Updated |
| DONE.md | File list and material uncertainties | Written |

All four PNGs are native 1536 x 1024. Kept outputs were copied byte-for-byte from the generator. No resizing, compositing, background replacement, manual alignment or retouching of delivered art. Only QA thumbnails/crops were derived with Pillow. No old cast art, external imagery, real webtoon inputs or real title/artist/studio names were used in prompts. Project writes stayed in `characters_v2/lyra/` and allowed `characters_v2/_rejects/lyra_*` paths. The image tool created its own managed originals. Nothing was published.

## Prompt/source audit

Current design 2.10, section 8 Lyra snippet and S14 brief were read again. Every one of the nine new prompts starts with the exact V2 STYLE BLOCK immediately followed by the exact CLEAN-UP LINE, includes the current Lyra snippet word for word, and ends with the exact NEGATIVE BLOCK. The source blocks were rechecked at completion. All first references match the approved front SHA-256 in `card.json`; all native output hashes were verified. Original front-generation prompt history was retained.

## Material limits

- All new backgrounds are quiet light-grey fields, but their pixel values vary and do not satisfy exact flat #E9E9EC. Corner samples are in the per-attempt `_qa/*_pixel_check.json` files. Left-edge strips in expression sheets include some artwork and should not be treated as wholly empty patches.
- Ink, hard clothing shapes and some skin shadow edges improved, but residual smoothly modelled skin/garment surfaces remain. Turnaround ankle folds still have more angular fragments than desired.
- In the turnaround side view, the quiver is not clearly visible; its completeness cannot be certified through the profile occlusion. The three-quarter angle is modest. Four views and bows are present.
- Turnaround sole ink bottoms are {'front': 976, 'three_quarter': 976, 'side': 972, 'back': 970}, spread 6 px on the 1024px canvas. They read as one baseline at thumbnail size, but are not numerically exact. See `_qa/turnaround_alignment.json`.
- Occluded fingers/toes are not certified by guesswork. Expressions have no hands. Details hand crops show one thumb and four fingers on each hand. Silver metal highlights are allowed; bare skin stays cool and matte, with soft-modelling limitations above.

## turnaround.png — selected attempt 3

Inspected the complete generated image, full-detail crops where relevant, and a 200px-wide preview. Chapter-only acting checks 11c do not apply to these sheets.

| Section 11 | Result |
|---|---|
| 1. Key light | pass |
| 2. 200px separation | pass |
| 3. Background contrast/density | pass contrast, fail exact background |
| 4. Crop/foreground | sheet exempt |
| 5. Camera/layout | pass four views; three-quarter angle modest |
| 6. Facial emotion | pass neutral confidence |
| 7. Reserved colours | pass |
| 8. Design/locks | partial, profile quiver occluded or absent |
| 9. Calm space | pass |
| 10. Text/anatomy | pass plausible joints/grips, hidden digits |
| 11. Drawn/cel appearance | fail residual soft modelling |

| Section 11b | Result |
|---|---|
| 1. Shard shadows | fail ankle crease clusters |
| 2. Sawtooth wear | pass |
| 3. Brand marks | pass |
| 4. Gear construction | partial, profile quiver not readable |
| 5. Face identity | pass identity |
| 6. Plastic/3D look | fail |
| 7. Anatomy | pass within visibility |
| 8. Exact sheet background | fail |
| 9. Adult wardrobe | pass adult approved clothes |

Residual strict issues: 11.11 / 11b.6: soft face/torso modelling and shiny garment highlights persist; 11b.1: several angular ankle folds remain; 11b.8: nonuniform grey background; 11.8: side-view quiver is not clearly visible; side-lock completeness cannot be certified.

## expressions.png — selected attempt 3

Inspected the complete generated image, full-detail crops where relevant, and a 200px-wide preview. Chapter-only acting checks 11c do not apply to these sheets.

| Section 11 | Result |
|---|---|
| 1. Key light | pass |
| 2. 200px separation | pass, all eight emotions distinguishable at 200px |
| 3. Background contrast/density | pass contrast, fail exact background |
| 4. Crop/foreground | pass heads/shoulders crop |
| 5. Camera/layout | pass 4x2 |
| 6. Facial emotion | pass requested eight |
| 7. Reserved colours | pass |
| 8. Design/locks | pass visible locks |
| 9. Calm space | pass small gutters |
| 10. Text/anatomy | pass no text, face anatomy plausible |
| 11. Drawn/cel appearance | partial, residual soft chest/face |

| Section 11b | Result |
|---|---|
| 1. Shard shadows | pass broad garment shadows |
| 2. Sawtooth wear | pass |
| 3. Brand marks | pass |
| 4. Gear construction | pass |
| 5. Face identity | pass same oval face, freckles, blue almond eyes and lips |
| 6. Plastic/3D look | partial residual softness |
| 7. Anatomy | pass visible anatomy |
| 8. Exact sheet background | fail |
| 9. Adult wardrobe | pass adult exact neckline |

Residual strict issues: 11b.8: background remains nonuniform #E9E9EC approximation after third attempt; 11.11 / 11b.6: residual smooth chest and face modelling remains alongside clear hard neck/shoulder shadows.

## details.png — selected attempt 3

Inspected the complete generated image, full-detail crops where relevant, and a 200px-wide preview. Chapter-only acting checks 11c do not apply to these sheets.

| Section 11 | Result |
|---|---|
| 1. Key light | pass |
| 2. 200px separation | pass named groups separable at 200px; fine holes/fingers checked full size |
| 3. Background contrast/density | pass contrast, fail exact uniform fill |
| 4. Crop/foreground | pass purposeful object/torso crops |
| 5. Camera/layout | pass seven distinct groups, complete bow/boot pair |
| 6. Facial emotion | not applicable no face |
| 7. Reserved colours | pass no glow |
| 8. Design/locks | pass required props; small hardware extrapolation noted |
| 9. Calm space | pass clear gaps |
| 10. Text/anatomy | pass no text; one thumb/four fingers on each hand |
| 11. Drawn/cel appearance | partial residual smooth skin/cloth |

| Section 11b | Result |
|---|---|
| 1. Shard shadows | pass with caveat few larger joint folds, some angularity |
| 2. Sawtooth wear | pass |
| 3. Brand marks | pass |
| 4. Gear construction | pass choker solid pearl, flute plain, functional fittings |
| 5. Face identity | not applicable no face |
| 6. Plastic/3D look | partial residual soft modelling |
| 7. Anatomy | pass five-digit bare left hand/right glove |
| 8. Exact sheet background | fail |
| 9. Adult wardrobe | pass adult covered torso crop |

Residual strict issues: 11.11 / 11b.6: torso skin and some garment/glove treatment retain smooth modelling; 11b.8: background remains a nonuniform approximation of #E9E9EC.

## All new attempts

| Sheet / attempt | Outcome and reasons |
|---|---|
| turnaround / 1 | Reject; 11.5: three-quarter rotation too shallow; 11.8 and 11b.4: profile figure missing its own bow/grip; third/fourth view gear reads conflated; 11.11 / 11b.6: softly modelled skin rather than hard cel shading; 11b.1: repeated ankle crease clusters persist; 11b.8: nonuniform grey background |
| turnaround / 2 | Reject; 11.5: second view remains a shallow three-quarter; 11.8 / 11b.4: third profile still lacks its own bow and left hand grip; 11.11 / 11b.6: soft skin and cloth sheen persist; 11b.1: ankle wrinkle clusters remain; 11b.8: nonuniform background |
| turnaround / 3 | Selected diagnostic; 11.11 / 11b.6: soft face/torso modelling and shiny garment highlights persist; 11b.1: several angular ankle folds remain; 11b.8: nonuniform grey background; 11.8: side-view quiver is not clearly visible; side-lock completeness cannot be certified |
| expressions / 1 | Reject; 11.11 / 11b.6: soft skin/hair modelling and shiny halter remain; 11b.8: grey background varies rather than exact #E9E9EC |
| expressions / 2 | Reject; 11b.8: background remains nonuniform and not exact #E9E9EC; 11.11 / 11b.6: residual soft chest/face modelling despite sharper neck/shoulder cel shadows |
| expressions / 3 | Selected diagnostic; 11b.8: background remains nonuniform #E9E9EC approximation after third attempt; 11.11 / 11b.6: residual smooth chest and face modelling remains alongside clear hard neck/shoulder shadows |
| details / 1 | Reject; 11.8 / 11b.4: choker in torso crop has empty ring instead of the approved single pearl; 11.8 / 11b.4: flute has added silver wrap/coils beyond reference; 11b.1: repeated angular ankle creases reappear in boot studies; 11.11 / 11b.6: glove texture/cloth/skin retains rendered surface treatment; 11b.8: nonuniform grey background |
| details / 2 | Reject; 11b.1: angular ankle and knee crease clusters persist on boot pair/inset; 11.11 / 11b.6: soft skin/cloth modelling remains despite flatter glove; 11b.8: nonuniform grey background |
| details / 3 | Selected diagnostic; 11.11 / 11b.6: torso skin and some garment/glove treatment retain smooth modelling; 11b.8: background remains a nonuniform approximation of #E9E9EC |

Every failed output, including the three selected diagnostics, is also preserved at its permitted reject archive. Exact paths are in `prompts.json`. Prior front reports remain in `QA_REPORT_v1_long_skirt.md` and `QA_REPORT_v2_front.md`.

## Finish

Completed the requested turnaround, expressions and details in order, three tries per image, with card, prompts and DONE. The original approved front is unchanged. Stopped.

# L12-B complete — 27 October 2026

Four remaining L12 views drawn with the built-in image_gen tool and saved for review. The already approved rooftop_room/stairs_night.png was outside this job.

## Kept images

| File | Size | Kept attempt | Continuity |
|---|---|---|---|
| survey_gate/exit_dusk.png | 1536×1024 PNG | 1 | Modern arcade concrete, shutters, terrazzo and cold fluorescent light; warm dusk above the exit stairs; one tiny street figure. |
| survey_gate/trap_chamber.png | 1536×1024 PNG | 1 | Round grey granary masonry, amber slit-window light, two square ceiling chutes, nominal 10 m ceiling and 5 m wall-stair lever landing; two small adult figures. |
| mangwon_market/fish_lane.png | 1536×1024 PNG | 1 | Approved blue arcade roof, awnings and warm bulbs; tanks, fish on ice trays, violet-lit cold-storage stairwell; two small adults. |
| hanriver_gate/bank_dusk.png | 1536×1024 PNG | 4 | Blue-hour park from behind crisp wooden pallets, continuous riverbank path, approved tarped enclosure, containers, generator, cables and pier-side slit; orange bridge lamps, two tiny guards. |

All paths above are relative to locations_v2/. References were survey_gate/outside.png and key.png, mangwon_market/key.png, and hanriver_gate/key.png and wide.png, confirmed APPROVED by reviews/STATUS.md and the L6, L7 and L9 verdicts. Old caveats in location notes were superseded by those verdicts.

## Prompt logs

- survey_gate/prompts_L12.json
- mangwon_market/prompts_L12.json
- hanriver_gate/prompts_L12.json

Logs contain exact prompts for every call, approved reference paths, pre-call free bytes, kept/rejected decisions and file verification.

## Rejects

All saved unchanged as ordinary PNG files:

- hanriver_gate/_rejects/bank_dusk_attempt01_soft_foreground.png — depth-of-field blur on foreground pallets.
- hanriver_gate/_rejects/bank_dusk_attempt02_added_water_channel.png — added a water channel between park and enclosure; nearest pallet edges still soft.
- hanriver_gate/_rejects/bank_dusk_attempt03_soft_pallets.png — bank layout corrected, but pallets still blurred.

No survey_gate or mangwon_market rejects were generated.

## Verification and disk guard

All four kept images and all three rejects are native 1536×1024 PNGs. SHA-256 hashes match the generator originals byte for byte. Every saved image has exactly one hard-link name and no reparse-point attribute: ordinary files, no hard links or shortcuts. No resizing, sharpening, recompression or other image modification was applied to saved art.

Reviewed full images and representative details at 200%. The temporary detail inspection sheet was outside the project and removed. No extra previews or temporary images were saved in the project.

Get-PSDrive C was checked before every one of the seven image calls. Free space never approached the 3 GiB stopping threshold:

| Image | Attempt | C: free GiB before call |
|---|---|---|
| survey_gate/exit_dusk.png | 1 | 41.280 |
| survey_gate/trap_chamber.png | 1 | 41.093 |
| mangwon_market/fish_lane.png | 1 | 40.865 |
| hanriver_gate/bank_dusk.png | 1 | 40.627 |
| hanriver_gate/bank_dusk.png | 2 | 40.325 |
| hanriver_gate/bank_dusk.png | 3 | 39.867 |
| hanriver_gate/bank_dusk.png | 4 | 39.486 |

Final C: free space: 38.755 GiB.

## Remaining

None for L12-B. All four requested views are saved for Claude's review. No review-board approval was changed. Drawing stopped.

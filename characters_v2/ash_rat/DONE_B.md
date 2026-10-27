# M1-B — Swarm scale correction

Completed 27 October 2026. Replacement ready for Claude review. Stopped after four image-generation attempts, within the five-try limit.

## Delivered

- `swarm.png` — kept attempt B4, native 1536 × 1024 PNG. Two dozen ash rats pour along the approved brick sewer around one clothed hunter standing in shallow ankle-deep water. The nearest rats have high hunched backs approximately level with the visible knees, with a clear side-view animal and human boots supporting the 70 cm body-plus-tail scale. Grey knee patches make the comparison visible. Foreground contours stay sharp; water uses flatter reflection shapes.
- `prompts.json` — appended all four exact built-in imagegen prompts, reference arguments, disk readings, local verdicts, saved paths, generator sources and file verification. The old swarm record is now marked rejected by Claude, with its new archive path; its original prompt remains historical.
- `card.json` — corrected only the normal-rat height description from the old ankle-height interpretation to knee-high (about 48 cm), and appended the M1-B review note.
- `DONE_B.md` — this completion record.

The approved `front.png`, `turnaround.png`, `details.png`, `swarm_mother.png` and Claude's `scale_card.png` were not changed. Review-board files were not changed.

## References

Every call passed exactly these four images, in this order:

1. `characters_v2/ash_rat/front.png` — approved species design.
2. `characters_v2/ash_rat/turnaround.png` — anatomy, long crooked limbs and high hunch.
3. `characters_v2/ash_rat/scale_card.png` — the SMALL normal rat beside the 178 cm man. The larger mother was explicitly excluded from the scene.
4. `locations_v2/sewer_gate/key.png` — approved L6 sewer architecture and white-blue caged lamps.

No rejects, old art or outside images were passed to generation. Used built-in `image_gen.imagegen`, with the V2 style block, clean-up line, species snippet and negative block. The review's knee-height requirement overrides the old prompt and original DONE file's ankle-height notes.

## Ordinary-file reject archive

- `../_rejects/ash_rat_swarm_rats_half_size.png` — original scene moved as requested; SHA-256 `E0F376E1E498DC3EB35892C54DDBDDD010734A3B8DF89F567399EC29E880E7E0` unchanged.
- `../_rejects/ash_rat_swarm_short_of_knee_soft_foreground_b1.png` — rat backs below knees, optically blurred foreground rats, overly detailed water.
- `../_rejects/ash_rat_swarm_soft_foreground_busy_water_b2.png` — improved side-view size, but remaining blur, busy reflections and inconsistent knee comparison.
- `../_rejects/ash_rat_swarm_below_knees_excess_count_b3.png` — sharper and flatter, but rats below knee patches and excessive distant crowd.

## Verification

The kept B4 and all three new rejects are native 1536 × 1024 PNGs, byte-identical to their generator originals. Copy-Item created independent ordinary files. The original archive and all four new files each have one hard-link path; no reparse points, shortcuts or hard links were used. Kept B4: 2,763,010 bytes; SHA-256 `7534299ABDE9BB929079C753F9C89009EA5279D784005A9F56BF2530089A0738`.

Inspected the native image, a 200 px thumbnail and a 200% diagnostic crop. No block compression, edge ringing, upscaling or foreground optical blur seen in the kept file. All diagnostics existed only in memory. No temporary images or preview files were saved in the project. Saved art was never resized, re-encoded or retouched.

## Disk checks

Get-PSDrive C was checked immediately before every generation call. The stop threshold was 3 GiB (3,221,225,472 bytes).

| Attempt | Free bytes before call | Free GiB |
|---|---:|---:|
| B1 | 40,637,513,728 | 37.847 |
| B2 | 40,321,388,544 | 37.552 |
| B3 | 40,180,457,472 | 37.421 |
| B4 | 39,827,550,208 | 37.092 |

Final verification reading: 39,569,764,352 bytes free. The low-space stop condition was never reached.

## Remaining review limits

- Claude's final approval is pending. Local visual review finds the nearest rats approximately knee-high; a perspective scene does not provide an exact physical measurement.
- Distant rats overlap, so an exact count of 24 and every hidden limb cannot be certified. The kept scene reads as a dense two-dozen swarm.
- Some fine ink and wet-reflection detail remains, while B4 is sharper and flatter than the rejected early attempts.

No required M1-B deliverable remains unwritten. Nothing was published. Stopped after saving the replacement, archive, prompts, scale metadata correction and this DONE file.
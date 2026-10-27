# L11-B — Bomi's streaming-room interior

27 October 2026. Generation finished at the five-attempt limit; best candidate retained for review, with the screen-colour fault below.

- Kept: `interior.png`, native 1536 × 1024 PNG, 2,031,984 bytes, attempt 1.
- Built-in `image_gen` used; the approved `outside.png` was passed in every call. No character or family-photo reference was needed.
- Exact prompts, inputs, disk checks, candidate results and selection are recorded in `prompts_interior.json`.
- One dated layout/light line was appended to `notes.md`, superseding the old interior hold.
- Rejected attempts 2–5 are ordinary PNG files in `_rejects/`. The first candidate was promoted to `interior.png`; its duplicate reject copy was removed.

## Content and review

The cramped upstairs room is empty at night: two blank green monitors, a microphone and pop filter on a clamped boom arm, a ring light, one white four-rotor camera drone resting on its charging dock, unlettered sky posters, and a small generic family photo on the shelf. The desk is at picture-left, the cropped bed at picture-right, and the dark sliding window, cream curtains, plant and warm shaded lamp match the exterior. Warm lamp light falls against navy night shadows.

Checked full size, at 200 px wide, and a 200% detail: clear drawn ink and cel shadows, coherent furniture perspective, supported equipment, no room occupants, no readable lettering, and no visible compression blocking or ringing. The family photo is incidental, with no identifiable likeness. Authoritative review status was not changed.

## Remaining fault

The monitor faces are visually blank green but are **not mathematically uniform #00FF00**. Sample pixels in the kept image are RGB (6,254,2), (6,254,1), (6,253,2), (6,253,1) and (7,254,2). New generations and targeted screen edits did not produce an exact flat fill. Per README_START_HERE.md's 27 October rule 3, stopped after five tries and kept the strongest room image. Exact RGB (0,255,0) screen fill remains to be resolved; no further drawing was attempted.

## File and disk checks

C: was checked with `Get-PSDrive C` immediately before every generation: 42.11, 41.86, 41.38, 41.22 and 41.03 GiB free. All exceeded the 3 GiB cutoff. Final check: 40.405 GiB free.

The kept PNG is a byte-for-byte copy of the original generator PNG, without resizing, re-encoding, sharpening, hard links or shortcuts. SHA-256: `20AF12B901D5478400CA5ADF7952D8404AA8F7BE6E1699D772DFDB5AF9173C48`. `fsutil hardlink list` showed one pathname for each kept/rejected file; all have null LinkType/Target. QA previews were made outside the project and removed. No extra previews or temporary images remain in the project. The existing exterior was not changed.

Stopped after this DONE file.

# ch001-FIX-B — completed 27 October 2026

Scope: P21 and P22 only. P09 was already approved and was not changed.

| Panel | Saved PNG | Tries | Result |
|---|---|---:|---|
| P21 | `P21.png`, 1024×1536 | 2 | Kept attempt 2; passes this chat's visual review. |
| P22 | `P22.png`, 1536×1024 | 5 | Kept attempt 5 as the best available at the five-try limit; remaining faults below. |

## P21

Jaeha stands on the corridor floor in a separate distant lane, roughly half Yerin's image height. Both boots and floor contact are visible below the horizon, clear of the foreground lizard. His single notebook is held in his left hand, his pencil is stopped in his right hand, and the left chest pocket is empty. His head was reduced in the second candidate to restore the adult proportions.

Yerin's shoulders, two-handed bag-strap grip, frightened tailward gaze, long legs and wall contact remain. The foreground lizard winds its club tail back while biting the cropped shield. Approved P23 was passed for the fortress, green-dusk light, violet/slate shadows and character continuity.

## P22 — best of five, requires reviewer attention

The fifth candidate has the most compact lizard body. Its back is near Yerin's mid-thigh rather than her chest; both subjects share the floor. The raised club tail is connected, Yerin flinches with closed eyes and a flying ponytail after a small sidestep, and the impact uses a hot orange field, sharp graphic strokes and slate-violet wall debris.

Remaining faults/uncertainties:
- Total nose-to-club length still reads longer than the specified 1.5 m. Shoulder/back height is improved, but a full strict scale pass is **not** claimed.
- The club-to-face gap reads wider than one finger. The near miss is clear, but does not precisely meet that spacing.

The five-try limit has been reached. No further drawing was done.

## Files and provenance

- `PROMPTS_FIX_B.json`: exact prompts, ordered reference paths, source PNG paths, per-call C: free-space readings and verdicts for all seven attempts.
- `REVIEW_FIX_B.json`: normalized head boxes for both humans and the visible lizard in P21, and Yerin and the lizard in P22; P22's remaining faults are explicit.
- Five new rejects are ordinary PNG files under `_rejects/`, with `FIX_B_try` in their names. Existing v1 rejects were preserved.
- Built-in imagegen was used for all seven calls. Each call passed approved character sheets and P23, or this chat's own draft as an edit target, with at most five inputs. No retired art or external images were used.
- All seven output PNGs decode at the required native sizes and are byte-identical to their generator sources. No final or reject was resized, re-encoded, sharpened, hard-linked or made into a shortcut. `fsutil hardlink list` confirms a single path for every new PNG.
- Final SHA-256 P21: `ba8bfff51532b5542e7355db4775a913ea93d7c0090f69e1560752ddb2492df7`.
- Final SHA-256 P22: `373c314a450642c70f9d20cc54d0502adfa0be98244d59bebd5d3a39996f6d3c`.
- Full-size, 200 px-wide and 200% detail inspection completed. Both JSON files parse, and all head boxes are ordered fractions within 0–1.
- No previews or temporary images were created in the project. Small inspection images were made outside the project and removed.

## Disk-space rule

`Get-PSDrive C` was run immediately before each image call. The lowest pre-call reading was 40.340 GiB, above the 3 GB stop threshold. The final check reported 39.480 GiB free. No space stop was triggered.

Only this job's two final panels, its five rejects, its prompt/head-box logs and this DONE file were written in the project. No other chapter panels, scripts, briefs, sheets or review-board files were edited. Nothing was published or uploaded.

STOP.

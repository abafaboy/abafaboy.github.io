# E1 — finished; P45 continuity correction completed

2026-10-25, Asia/Tashkent. P44–P49 and the four requested E1 records are saved. Built-in image_gen only: 15 initial production calls plus 2 calls for the newly authorized P45 correction. No image or replacement patch was resampled.

## Current P45 correction

The airborne black notebook at the upper right has been removed. Its former footprint now contains the same orange speed-line field, faint ruined masonry and a few inked debris chips. The approved panel was cropped for the edit; the accepted replacement was extracted on the original 1024×1536 coordinate grid and composited back at 1:1 pixel size.

Only the rectangle `[775,352,924,476]` was eligible for replacement (149×124 pixels), with a four-pixel blend confined inside it. Actual changed pixels occupy `[776,353,923,475]`. Every pixel outside the replacement rectangle is identical to the preceding kept P45. All characters, faces, hands, clothing, pockets, weapons, head boxes and the remaining background are therefore unchanged. No pocket alteration was made.

The first correction output removed the notebook but enlarged its padded crop; it was rejected instead of being resized. The second output retained the native panel grid, and only its repaired local background patch was used. The final P45 is a lossless PNG composite at 1024×1536, not a byte-identical copy of the full generated correction image. The pre-correction panel and rejected crop output are archived in `_rejects/` with provenance in `PROMPTS_E1.json`.

Claude's earlier praise of the dropped notebook is superseded by the user's correction: the airborne notebook broke continuity with P54, P55, P57 and P63. All other P45 content remains passed.

| Panel | Initial tries | Additional correction calls | Size | Current result |
|---|---:|---:|---|---|
| P44 | 3 | 0 | 1536×1024 | Kept; Claude pass; unchanged |
| P45 | 3 | 2 | 1024×1536 | Kept; airborne notebook removed by scoped lossless crop composite |
| P46 | 3 | 0 | 1536×1024 | Kept; unchanged |
| P47 | 3 | 0 | 1536×1024 | REVIEW ONLY: prior concern about Mok's angry brow remains; unchanged |
| P48 | 1 | 0 | 1536×1024 | Kept; unchanged |
| P49 | 2 | 0 | 1254×1254 | Kept at accepted native square size; unchanged |

## Records and verification

- `PROMPTS_E1.json` preserves every original prompt and candidate and adds both exact correction prompts, input hashes, generator sources, crop geometry, composite recipe and current audit. No image call used more than five references.
- `REVIEW_E1.json` retains all head boxes and the full 11/11b/11c checks, updates the P45 notebook findings, and records the crop correction and pixel comparison. Corrected P45 was inspected full size, at 200 px width and in a 200% detail crop; no seam, notebook remnant, softness or compression artifact was observed.
- `PROGRESS_E1.md` appends the correction; historical dropped-notebook praise is explicitly superseded.
- Final P45 SHA-256: `d5e519a4e56c84c140632268b327ecf6f7ea9aa2a0bd1a729c835374705d2f97`.
- Other five E1 panel hashes are unchanged. P45 dimensions and PNG decoding verify. Its heads are unchanged and no pixels outside the replacement box differ.
- Project writes for this correction were confined to P45, its own archive/crop/reject files and the four requested E1 records. No other part's panel, source, script, brief or reference was edited.

The P45 correction is complete. STOP.

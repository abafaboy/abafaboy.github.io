# M12 DONE — The Deep Lantern / Oriel

Completed 27 October 2026 by chat M12. Candidate sheets are ready for Claude review; this does not change the shared approval board.

## Kept files

| File | Contents | Tries |
|---|---|---:|
| `front.png` | Checked front design anchor, corrected smaller pendant lantern; whole creature | 2 |
| `side.png` | Complete long side view, dorsal lid plates, relaxed edge-on webbed hand | 4 |
| `head.png` | Frontal and three-quarter head, whole crest and violet lantern | 1 |
| `hand.png` | Same left hand, palm and back; four long fingers plus one opposing thumb each | 1 |
| `lantern.png` | Intact violet, intact pure white, and violet with exactly three clearly shattered front bars | 2 |
| `freed.png` | Lifted noble head, gentle sea-grey eyes, white lighthouse light, broken cage bars | 1 |

Also saved `card.json` and `prompts.json`. The latter records every exact tool prompt and input path, all eleven image calls, the five rejects, reference revision notes, and pre-call free-space readings. Built-in `image_gen.imagegen` was used.

## Checks and interpretation

- Read README's 27 October changes first and the applicable reading sequence; used V2, its exact clean-up and negative blocks, and the Deep Lantern identity snippet.
- Applied the newer sheet rule: no 178 cm silhouettes, ruler, or 80 m barge outline in these sheets. Canonical dimensions remain 150 m body length, 15 m hand span, 30 m crest rise, 12 m lantern height, recorded in `card.json`.
- Added `front.png` as required by MODEL_SHEETS_BRIEF sections 1–3. Its first version was corrected after comparison with the side, then preserved as a reject. Every later sheet used the checked front as its first reference.
- Initial reference was the approved acting-style anchor `style_test_v2/acting/A3_P23.png`; later references were this entry's own checked designs. No retired, outside, or rejected-folder image was an input.
- All six kept files and five rejects are native 1536×1024 PNGs, copied byte-for-byte as ordinary files. SHA-256 checks match all eleven generator originals; no hard links, shortcuts, reparse points, resizing, recompression, or retouching.
- Inspected kept images full-size, as 200 px thumbnails and in 200% crops. Inspection previews existed only in memory; none were saved in the project.
- Head generation returned a host timeout after saving its original. Recovered and inspected that exact PNG; no duplicate generation was requested.
- Free C: space was checked with Get-PSDrive C before each image call and stayed above 3 GB. Final verification: 40,357,474,304 bytes free (37.586 GiB). No disk-space stop was needed.

## Rejects

Saved as ordinary native PNGs in `characters_v2/_rejects/`:

- `deep_lantern_front_try1_oversized_lantern.png`
- `deep_lantern_side_try1_oversized_hand.png`
- `deep_lantern_side_try2_hand_and_crest_ratios.png`
- `deep_lantern_side_try3_lantern_too_tall.png`
- `deep_lantern_lantern_try1_ambiguous_broken_bar_count.png`

## Limits and remaining work

The sheets are design views, not calibrated metric scale cards; the numerical dimensions above remain authoritative. The front has a head-on face with the body receding slightly toward picture-right; `head.png` supplies the straight frontal head. The side's hand is edge-on, so use `hand.png` for the full spread and finger construction. Tiny coral and barnacle placement varies between views; preserve the main crusting regions, crest, brow crack and dorsal plate silhouette in panels.

No requested asset is left undrawn. Claude review remains. No other chat's folders, shared briefs or review status were modified. Stopping after this DONE file.


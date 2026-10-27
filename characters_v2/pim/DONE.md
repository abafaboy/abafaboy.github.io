# S29 — Pim — stopped at the five-try front limit

Date: 27 October 2026. Chat: S29. Entry is **incomplete; front has not passed**.

README_START_HERE.md, Changes on 27 October, rule 3: "Only a sheet entry whose `front.png` fails stops there (everything else in it is drawn from the front)." Five front attempts were made. Attempt 5 is the best and is retained as `front.png`, with its remaining faults below. No sixth attempt was made. The remaining sheets must wait for a passing front.

## Saved in this folder

- `front.png` — fifth attempt, best retained, 1536×1024 native PNG; **not approved**.
- `card.json` — canon heights, palette, locks, practical placement choices, forms, unresolved faults and remaining files.
- `prompts.json` — exact built-in image_gen.imagegen prompts and reference paths for all six calls, outcomes, source paths, disk checks and file validation.
- `DONE.md` — this report.

## Faults in the retained front

- The upper wings end near the knees, but the lower wing pair extends into the upper calves instead of ending at the backs of the knees.
- Close inspection of the face reveals two small nose-like marks above a separate mouth. Pim must have no visible nose.
- Four separated digits per hand, tall feathery antennae, long adult chitin limbs, lilac vest, brass mirror badge, wire bracelets, tuning-fork satchel and unlit cracked headset are present. The front is still unsuitable as the foundation for the remaining sheets because of the two faults above.

## Attempts and rejects

All rejects are ordinary native PNG files in `characters_v2/_rejects/`:

1. `pim_front_try1_wings_too_long_antennae_short.png` — wings below knees; antennae too short vertically. Small hands also required further inspection.
2. `pim_front_try2_antennae_vertical_scale.png` — wing length improved, antennae still short; hands not accepted as final.
3. `pim_front_try3_missing_finger.png` — enlarged hand inspection showed two long fingers plus a thumb, rather than three plus a thumb.
4. `pim_front_try4_short_antennae.png` — four clear digits achieved, but antennae shortened again; unnecessary blush and excess eye gloss.
5. `pim_turnaround_try1_inherited_missing_finger.png` — initially drawn from front attempt 3, then rejected when its source front failed the enlarged digit check. No subsequent sheet used either rejected image.

Front attempt 5 is retained under the normal filename rather than duplicated in rejects.

## Left to draw

- A corrected, passing `front.png` is needed before the rest of S29 can proceed.
- `turnaround.png` — front, three-quarter, side and back with four wings folded to the backs of the knees.
- `turnaround_field.png` — wings open to 2.6 m, glowing lilac eye-spots, blazing antennae and faint signal rings.
- `expressions.png` — the seven S29 expressions plus neutral for the standard eight-cell sheet.
- `details.png` — all antenna states, wing scales and eye-spots, vest and badge, bracelets, tuning forks, cracked dead-ring headset, and Geum's floral bonnet over the antennae.
- `chibi.png` — eight gag poses at 2.5 heads tall.

## Verification and scope

Read README's 27 October changes first, then the required story/design/style reading order and applicable sheet, proportion and chibi rules. Used the built-in image generator. The approved acting image `style_test_v2/acting/A3_P23.png` was used only as the style anchor; the failed turnaround call additionally used the then-selected own front as its first reference. No old art, outside images or reject inputs were used. Every call used at most two references. No scale silhouette or lettering was requested or drawn.

Checked C: using `Get-PSDrive C` immediately before each image call; all checks were above the 3 GB stop threshold. Final free space was 41,482,514,432 bytes (about 38.6 GiB); disk space did not cause the stop.

All six saved PNGs are 1536×1024, byte-identical to their generator originals by SHA-256. Each has one hard link and no reparse-point attribute: no hard-link copies or shortcuts. Inspected full native art, enlarged hands/face and the retained front at 200 px wide. No extra previews or temporary images were saved in the project. Project writes were confined to `characters_v2/pim/` and this chat's `pim_` files in `characters_v2/_rejects/`. No other chat's folder was changed. Nothing was published or uploaded.

Stopped as required after recording the failed front and remaining work.

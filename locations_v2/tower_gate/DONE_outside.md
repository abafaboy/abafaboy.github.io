# L8-B — tower exterior

27 October 2026. Stopped after five built-in imagegen attempts, as required by README_START_HERE.md's 27 October rule: "If it still fails, keep your best try under the normal file name, list its faults in your DONE file, and go on with the rest of the job."

**Result: best attempt retained; exterior still needs review/redraw. Not approved.**

- Kept attempt 3 as `outside.png`, an ordinary 1536×1024 PNG copied byte-for-byte from the generator.
- Kept the other four attempts as ordinary PNG files in `_rejects/`.
- Recorded every exact prompt, the two reference paths, pre-call C: free space, source files and reviews in `prompts_outside.json`.
- Added the exterior status/layout line to `notes.md`.
- Used only the approved `tower_gate/key.png` and `sewer_gate/outside.png` as image inputs, in that order, for every call. No rejected image was used as an input.
- No other entry was drawn. No extra previews or temporary images were left in the project.

## Remaining faults / what is left

1. The retained image has **eleven storeys, not twelve**: ten full opening bands plus the partly obscured lowest band behind the hoarding.
2. Counting ground as floor 1, the jagged gate slit is on **floor 6, not floor 7**. There are five storeys above its row and five below; the required arrangement is five above and six below.
3. The pedestrians remain somewhat too large against nominal 3 m floor spacing; some exposed roof rebar reaches the canvas edge.
4. A passing exterior still needs exactly twelve countable bare storeys and the slit on the seventh, with correct pedestrian scale. Do not treat this retained exterior as an approved continuity reference.

The retained image otherwise has the across-street view, bare concrete structure, exposed rebar, right-side scaffolding with green mesh and loose plastic, blank pavement hoarding, ordinary surrounding buildings/street lights, orange dusk and a narrow jagged black-violet slit with a pale rim.

## Disk and file verification

C: was checked with `Get-PSDrive C` immediately before every generation call. Free GiB for attempts 1–5: **42.1406, 41.8942, 41.3889, 41.1840, 40.8987**. The 3 GiB stop threshold was never reached. The post-save check had 40.6642 GiB free.

All five saved images have PNG signatures and native dimensions **1536×1024**, with no conversion, resizing, sharpening or re-encoding. File/link inspection confirms ordinary files with no extra hard links or shortcuts. The final file's SHA-256 matches the original generated PNG:

`CFE03BCAF19B93622970620A750A44BF6755CD65E1CA193373DF59C4371BC7AE`

Final saved files:

- `outside.png`
- `prompts_outside.json`
- `notes.md` (appended line)
- `DONE_outside.md`
- `_rejects/outside_L8B_try01_floor_count_gate_scale.png`
- `_rejects/outside_L8B_try02_floor_count_hidden_ground.png`
- `_rejects/outside_L8B_try04_ten_storeys.png`
- `_rejects/outside_L8B_try05_floor_count.png`

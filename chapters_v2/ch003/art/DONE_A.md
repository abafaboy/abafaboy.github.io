# DONE — ch003-A

27 October 2026 · Asia/Tashkent

Part A is finished: P01–P08 of scripts_v2/ch003.yaml, following PANEL_BRIEF_v2.md section 9, Chapter 3. P09 is a caption and has no art. No assigned panel remains undrawn.

| Panel | Tries | Native PNG | Result / uncertainty |
|---|---:|---|---|
| P01 | 1 | 1536×1024 | Kept. Nine-tower siege; two smoking towers; grey memory with violet ash. |
| P02 | 5 | 1536×1024 | Best try retained at the five-try cap. See faults below. |
| P03 | 2 | 1536×1024 | Kept. Single message tube; Kett holds the tube and clutches the sleeveless cloak at its armhole edge; mustard scarf is the only warm colour. |
| P04 | 2 | 1024×1536 | Kept. High view of Kett running down the six-storey stair and looking back. |
| P05 | 1 | 1536×1024 | Kept. Distant fortress bell, drawn sound rings, cropped near tower/banner. |
| P06 | 3 | 1024×1536 | Kept. Two held knives, grey-white impact, violet ash; spare hilts removed; left-ear notch and scorched hem corrected. |
| P07 | 2 | 1536×1024 | Kept. Exactly nine single physical scratches; knife finishes the ninth. |
| P08 | 4 | 1536×1024 | Kept. Small rear figure about one fifth of frame height; empty pass; two lowered knives and empty crossed sheaths. |

## P02 retained faults
- Nib is about 0.26 of the commander’s drawn height against the intended 105/450 = 0.233, roughly 12% too tall.
- The background remains denser than the talk recipe asks.
- Faint local warmth remains on Nib’s skin/gear.
- Background soldiers face away up the visible stair instead of filing down it.
- Nib’s feet are apart instead of heels together.
- At this small scale his speaking mouth and tiny costume details are less readable than in the closer panels.

P02 is explicitly kept for review after five tries, not represented as a strict pass. Its best composition preserves the intact closed-visored commander, salute and opposing eyelines. No sixth try was made.

## Files and verification
- Eight kept panels, twelve rejects, twenty built-in image_gen calls. Every successful image is saved under its kept name or _rejects/P0N_<try>_<reason>.png.
- PROMPTS_A.json contains each exact call prompt, ordered reference paths, generated source path, try number, disk-space check, dimensions, SHA-256 and verdict. Its plan/source fields preserve the script camera, light, art, acting, eyeline and foreground.
- REVIEW_A.json contains normalized head boxes for every readable character, including the seven anonymous background soldiers in P02, plus checks and explicit P02 failures. Scenery, tiny siege silhouettes and the hand-only insert have no dialogue head target.
- PROGRESS_A.md records every completed panel and the final P02 audit.
- All twenty PNG files decode at their required native dimensions, have one filesystem link, are ordinary files, and match the generator source SHA-256. No PNG was resized, re-encoded, sharpened or composited.
- Full-size and 200px-wide visual checks completed; enlarged hand/face/gear inspections were made in memory. No previews or temporary images were saved in the project.
- C: was checked with Get-PSDrive C before every image call. The lowest recorded pre-call free space was 37.65 GiB, above the 3 GB stop threshold. Last verification: 41,253,519,360 free bytes (about 38.42 GiB). No disk stop was triggered.

## References and scope
Read README_START_HERE.md with its 27 October overrides; the applicable reading order; PANEL_BRIEF_v2.md all the way through; SCRIPT_FORMAT_v2.md; the assigned script panels and adjacent P09/P10 continuity; acting-test Round 2 and REPORT; reviews/STATUS.md and S2b.md; and the applicable ART_BIBLE rules.

Used only current approved design/location references, plus this chat’s own candidates as scoped edit targets. Flashback Nib uses front_seal2_nomask.png, turnaround_seal2.png where his back matters, details_seal2.png and base expressions.png for the face. All flashback costume colours were directed into greys; no mask. Commander was rebuilt as unhushed with intact armour, whole cloak, closed visor and no face-hole.

Intentional project writes were limited to P01–P08.png, this part’s reject PNGs, PROMPTS_A.json, REVIEW_A.json, PROGRESS_A.md and DONE_A.md in chapters_v2/ch003/art/. No other part’s files, scripts, briefs, sheets or review-board files were edited. Nothing was published.

STOP — part A complete.

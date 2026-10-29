# S37: the romance trial (29 October 2026)

**Why.** The owner, 29 October: "make a reference with the mc with the love interest. whichever one fits the story. do like a trial mini comic", to see how close to romance the series can go. Claude chose **Moon Ahin**: the story already builds it (ch 29 "Why are you carrying my husks?" "Because they're carrying us."; ch 33 "I was passing"; ch 40 "Ahin. They're yours. Hold them.").

**The line (fixed):** romance as far as regular, not adult-rated, manhwa go: flirting, a real kiss, embraces, two silhouettes embracing behind blinds, a fade to black, the morning after. Never nudity, never a sexual pose or act, nothing explicit, no angle up the skirt or at the chest or crotch. Both are adults: Kang Jaeha is 24 (178 cm), Moon Ahin is 22 (170 cm). If the image tool refuses an image, do **not** reword the prompt to get around the refusal: write the panel, the exact prompt and the exact error into `DONE.md`, keep any earlier try, and go on with the next image. Claude reports refusals to the owner.

**Read first:** `README_START_HERE.md` (its 29, 28 and 27 October changes come first); `PANEL_BRIEF_v2.md` all the way through (it is the rulebook for every panel here: sizes by shape, no text in the art, hands first, legs second, the try limits); `S36_GUILD_MASTER_AND_REAL_LEGS.md` section 1 (the leg checklist and the pose sketch); `S33_FAN_SERVICE_NOTES.md` "Rules for every sheet"; `CHARACTER_DESIGNS_v2.md` 2.1 (Jaeha, look `coat`) and 2.11 / 2.20 (Moon Ahin, look `summer`).

**References** (at most 5 per image call, approved files only):
- Jaeha, look coat: `characters_v2/kang_jaeha/turnaround_coat.png` (the black field coat with the orange lining, dark grey shirt, navy cargo trousers with grey knee patches, black boots, black fingerless gloves; the pencil behind his RIGHT ear, the fringe over his LEFT eye); his face from `kang_jaeha/expressions.png`.
- Moon Ahin, look summer: `characters_v2/moon_ahin/front_summer.png`, `turnaround_summer.png`, `details_summer.png` (no sun hat at night; the silver ribbon bow at the back of her loose hair; white lace gloves; the high slit on her LEFT side; the baton in its slim holster at her RIGHT hip); her face from `moon_ahin/expressions.png`.
- For the gags at P09 and P15: `lyra/front.png`, `pim/front.png`, `borro/front.png`, `nib/turnaround_seal3.png` (masked).
- Scale: `characters_v2/scale_chart_v2.png` whenever two or more characters share a panel (her head top at his eyebrows).
- Hand references from `characters_v2/hands/` only where `reviews/STATUS.md` and `hands/INDEX.md` list them as approved; if a script's `hand_ref` is not approved, use the nearest approved one.

## Part A: the couple reference sheet
`characters_v2/_couples/jaeha_ahin/couple_ref.png` (1536×1024, flat light grey #E9E9EC, no text), three poses of the two together in their side-story looks, left to right:
1. **Standing side by side,** facing the viewer, full figures on one floor line at true heights (her head top at his eyebrows), her shoulder just touching his arm; his coat on, her summer dress.
2. **The standing kiss, in profile:** she has pulled him down by his shirt collar with her bare RIGHT hand and risen a little onto the balls of her feet (heels lifted, knees soft); he bends his neck and upper back to her, his RIGHT hand on her back; eyes closed. His coat is round her shoulders, so he is in his dark grey shirt.
3. **Sitting on a concrete step:** she sits on his LEFT with his coat round her shoulders, her head resting on his shoulder; his forearms on his knees; both pairs of feet on the step below.

Draw the pose sketch first (S36 1b): two plain mid-grey wooden mannequins, each in a plain grey full-body leotard (never nude), the taller one 178 cm and the shorter 170 cm, in exactly these three poses, saved as `characters_v2/_couples/jaeha_ahin/_pose/couple_ref_pose.png`. Check it against the leg checklist (S36 1c), then draw the sheet with the pose sketch as reference 1. Up to 3 tries for the sketch and 5 for the sheet. Crop every hand at 2x before you keep it.

## Part B: the trial mini comic
Draw every panel with art in `scripts_v2/side01.yaml` (P01, P03-P17, and END.png for the chibi end card), exactly as the script says, into `chapters_v2/side01/art/` (P02 is the title card and has no art).
- Sizes, rules and checks as `PANEL_BRIEF_v2.md` (sections 2-4c and 13): `wide` 1536×1024, `tall` 1024×1536, `inset-l`/`inset-r` and END square at the native 1254×1254; flat-coloured, no text, letters or numbers anywhere in the art (no room numbers, no writing on the key card, no floor numbers in the lift).
- No location keys exist for the beach or the hotel: draw them generic from the script's continuity, consistent from panel to panel (the same sea wall steps, the same bridge, the same hotel tower).
- Pose sketches first (S36 1e) for P03, P07, P08, P11 and P13, saved as `chapters_v2/side01/art/_pose/<panel>_pose.png`, two grey leotard mannequins at true heights.
- P13 is silhouettes only: soft dark shapes behind the slats of half-closed blinds, lit warm from inside, an embrace and a kiss, her hand drawing the ribbon from her hair. No detail inside the silhouettes.
- Side locks every panel: Jaeha's pencil behind his RIGHT ear and fringe over his LEFT eye; Ahin's slit on her LEFT side, her RIGHT glove off from P05 (it lies on the step in P05 and in the corridor at P12), her ribbon gone from P13 and tied round Jaeha's RIGHT wrist at P17.
- Up to 5 tries per panel. Files: `PROMPTS.json` (every exact prompt and its references), `REVIEW.json` (for each panel: the 2x hand crops, the eight leg-checklist answers where legs show, the verdict), `PROGRESS.md` (one line per kept panel), and `DONE.md` at the end (what was drawn, the tries, any refusals with their exact messages).

**Order:** Part A, then Part B in panel order. Disk floor: before each image call check the free space on C: (Get-PSDrive C); below 1.5 GB, stop and write `DONE.md`. If the image tool reports a usage limit (HTTP 429), stop and write `DONE.md`. Ordinary files only (never hard links or shortcuts), no extra previews in the project folder, rejects into `chapters_v2/side01/art/_rejects/` (moved, never deleted). Do not touch any other chat's files. Do not stop to ask anything; finish the job.

# Chapter 1 fixes: proportions, scale and perspective (25 October)

**Why.** After chapter 1 went out, the owner and a reader found the same faults: "the body poses are weird", "the proportions", and in P09 the people were far too big for the scaffolding ("they look way too small", said of the scaffolding). The owner: "be more strict about the proportions. the bodies sometimes look small and compressed when they shouldn't. also judge harshly on how things should look from a certain camera angle." Claude went through all 60 panels against the new rules in `PANEL_BRIEF_v2.md` section 4b. Three panels fail and are redrawn here; the rest pass.

**How.** Follow `PANEL_BRIEF_v2.md` (all of it, section 4b above all) and the panel's entry in `scripts_v2/ch001.yaml`: same recipe, shape, size, light, acting, calm zone and story content. Only the faults below change.
- Before you overwrite a panel, move the old file to `chapters_v2/ch001/art/_rejects/<id>_v1_<fault>.png`.
- Keep the new image at the same pixel size as the old one.
- Update that panel's head boxes in a NEW file, `chapters_v2/ch001/art/REVIEW_FIX.json` (same format as the other REVIEW files).
- Log each prompt in `PROMPTS_FIX.json`, and write `DONE_FIX.md` when all three are done (with tries and anything you're unsure of).
- Write nothing else: other chats are drawing chapter 2 at the same time.

## P09 (full, 1536×1024): Gate 0912 from the street edge
**Faults.** Jaeha, at the pit's edge, is drawn taller than the Association tent and the van behind him, and taller than two flights of the scaffold stair. The pit and its scaffolding read far too small for the people in it. The camera looks down into the pit, but the hunters at the bottom are drawn straight on, as if from eye level.

**Redraw with these sizes and this camera:**
- **Camera:** high, at the street edge about 4 m above the street, looking steeply down into the pit. Everything below is seen from above: the tops of heads and shoulders, bodies foreshortened toward the feet, and the pit's vertical piles converging downward.
- **The pit:** about 18 m deep, roughly ten people stacked. The scaffold stair tower runs down the near wall in flights, 2 m from landing to landing (each landing a little more than a person's height above the next), with a 1.1 m guard rail. Two cross struts span the pit high up. Floodlight poles on the street are 8 m tall.
- **On the street, at the top left:** the Association's pop-up tent (3 m to the roof peak) and Black Hound's black van (2 m tall). Jaeha stands alone at the pit's edge beside the tent: a small figure, about the van's height and well short of the tent's peak, seen from above and behind, hugging his notebook. He is small in the frame.
- **At the bottom of the pit:** seven hunters in black guild jackets in two loose clusters beside the gate. Each is tiny, about a tenth of the pit wall's height, seen from above, and still correctly proportioned (7.5–8 heads). The gate is a door-height slit, 2 m: a little taller than a hunter.
- **Keep:** the night, the cold white LED floodlights, the blue tarps, the puddles, the yellow-and-black barriers, and the calm area at the top for the location tag.

## P21 (tall, 1024×1536): the tail coils toward Yerin
**Fault.** Jaeha, in the background, floats: his feet are hidden behind the lizard's back, high in the frame, so he seems to stand on the lizard.

**Redraw:** the same moment and composition, but Jaeha stands on the corridor floor, about six metres behind the lizard. His boots are visible on the floor, below the horizon line, and he is about half Yerin's height in the frame because he is farther away. He is a full figure, correctly proportioned, pencil stopped, head snapping up toward her. The lizard is 60 cm at the shoulder and 1.5 m long with the tail. It is nearer the camera than Yerin, so it looks bigger, but only by the same perspective as the floor tiles: at her depth its back would reach her mid-thigh. The camera is at chest height (about 1.3 m), so the horizon runs at Yerin's chest.

## P22 (wide, 1536×1024): the tail misses her face
**Fault.** The lizard is drawn about twice its design size: its back reaches Yerin's chest, although she stands closer to the camera than it does.

**Redraw:** the same moment and composition, with the lizard at its real size: 60 cm at the shoulder (its back at Yerin's mid-thigh, since she is at the same depth), 1.5 m long with the tail. The club tail is the size of a large melon, about 35 cm across. Yerin keeps her full proportions (about 7 heads, long legs in the black leggings). The camera is low (knee height), tilted for the impact, so we look slightly up at her and the swinging tail.

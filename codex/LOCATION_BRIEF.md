# LOCATION BRIEF: location keys for Arc I (method B)

Chapter sessions will pass these keys as reference images, so every panel set in a place shows the same room. Draw them in **method B** (the TECHNIQUE BLOCK in `PANEL_BRIEF.md` section 7, plus `style_test/abcd/STUDY_NOTES.md`). Read `bible/ART_BIBLE.md` (A4 colour script, Part C) first.

## Layout source, in order of authority
1. `world/floorplans/<id>.png` and `world/LOCATIONS.md`. **Check for them right before you start each location**: they are being written now and may appear while you work. When a plan exists, put every door, window and piece of furniture where it says.
2. Otherwise, the descriptions in `scripts/ch001.yaml` (panels P01–P55), `bible/PART_ONE_BEATS.md` (chapters 1–9) and `bible/STORY_BIBLE.md`.

Whatever you decide, write it down in `locations/<id>/notes.md`: the layout (which wall has the door, the window, the bed and so on), the palette hex values, and the props that must recur.

## Deliverables per location
In `locations/<id>/`:
- `key_wide.png` (1536×1024): the establishing view from the main camera position the scripts use.
- `key_reverse.png` (1536×1024): the reverse angle, so both directions of every room are defined.
- `key_detail.png` (1536×1024), only where listed: the recurring corner or props in close-up.
- `notes.md`, as above.

No people (one small scale silhouette at most, no face). No text: signs, posters, menus and screens stay blank or abstract shapes. Screens are dark unless the notes say otherwise. Use the ART_BIBLE A4 colour script for the time of day named.

## Order (do the first two before anything else)
1. **taeo_flat**: Taeo's 18 m² studio in Mangwon-dong, night with a warm lamp. Bed against a wall, small desk, kitchenette strip, a window, the door. Leave open floor in front of the bed for the summon circle. Detail: the desk corner and lamp.
2. **hanbit_mart**: the interior at night under pale fluorescent green-white light. Wide = the counter, till, cigarette shelves behind it and a small TV mounted high; reverse = the aisles toward the glass front. Detail = the counter top.
   Also do **hanbit_mart_ext** (the street corner at night, glass front glowing, a green sign panel with a white circle logo and no letters, a scooter, crates, a potted plant) and **hanbit_breakroom** (tiny: lockers, a microwave on a fridge, a folding table, a plastic stool, the rota whiteboard as squiggles).
3. **night_bus**: a Seoul city bus interior at night, looking down the aisle; reverse from the back row.
4. **mangwon_street**: the walk home: a narrow residential street and alley at night (sodium orange), a bus-stop advertising screen (dark), the street door of Taeo's building.
5. **aao_office**: the Ability Assessment Office: an assessor's desk (Chae Yuri), monitors (dark), filing shelves, a waiting bench.
6. **pyo_cafe**: an upscale café where Dr. Pyo meets Taeo.
7. **ryu_practice_yard**: Ryu Survey's west practice yard: an outdoor training yard with targets and equipment.
8. **haeseong_port**: a small coastal fishing town, three hours from Seoul. Idle fishing boats, buoys, the black-violet sea-gate slit in the water offshore, the bus stop. Also **grandparents_house**: a modest old house with a small yard, the TV, the kitchen table.
9. **gma_hearing_room**: the GMA hearing room for Nib's review.
10. **moon_laundromat**: Granny Moon's laundromat in Mangwon: washers, folding table, warm light at night.

When taeo_flat and hanbit_mart (with ext and breakroom) are done, write `locations/READY_ARC1_CORE.md` listing those files, then carry on. At the end, write `locations/REPORT.md` listing everything.

Do not modify any file outside `locations/`. Do not stop to ask; keep going until the list is done.

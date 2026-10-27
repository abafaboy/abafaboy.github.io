# LOCATION KEYS BRIEF: Arc 1 places in style V2 (one Codex chat per entry)

**What a location key is.** A reference image of a place that every later panel set there must match: its layout, its light and its colour. Several chats run at the same time. Each draws only its own entry, in its own folders.

**Read first:**
- `README_START_HERE.md`;
- `MANHWA_STYLE_GUIDE.md`: the V2 STYLE BLOCK, the NEGATIVE BLOCK, table 5.3 (colour keys) and section 8 (backgrounds);
- `CHARACTER_DESIGNS_v2.md` section 5 (what each place looks like).

## Rules
- **Size.** Every key is 1536×1024 and drawn in V2. Use the location's key light from table 5.3. A location key is the one place a background is drawn at full detail.
- **No people,** except where an entry asks for tiny figures to show scale.
- **No text:** signs and screens stay blank, and screens are flat #00FF00.
- **Files:**
  - `locations_v2/<id>/key.png` and the extra views the entry lists;
  - `locations_v2/<id>/notes.md`: the layout in a few lines (where the gate stands, where the doors are, where the light comes from), for later panels;
  - `locations_v2/<id>/prompts.json`.
- **Redo** an image (up to 5 times) if it fails the checks in `MANHWA_STYLE_GUIDE.md` section 11 that apply to a place.
- **Finish.** When your entry is done, write `locations_v2/<id>/DONE.md`. Do not stop to ask.

## Entries (one chat each)

| # | Ids | Draw |
|---|---|---|
| L1 | `gate0912_site`, `gate_exit` | **`gate0912_site`:**<br>- `key.png`: from street level looking down into the subway construction pit at night, with floodlights, scaffold stairs and the gate (a door-height black-violet slit with a pale rim) at the bottom between the steel struts;<br>- `reverse.png`: from the pit floor looking up at the floodlights and the street;<br>- `gate.png`: a close view of the gate slit.<br>**`gate_exit`:**<br>- `key.png`: the same street at night with rescue vehicles, red and blue strobes on wet asphalt, and a giant #00FF00 billboard across the street. |
| L2 | `gate0912_fortress`, `boss_room` | **`gate0912_fortress`:**<br>- `key.png`: a ruined fortress corridor of pale limestone under a sickly green-dusk sky seen through cracks;<br>- `details.png`: a pressure plate, spike holes in a wall, a portcullis.<br>**`boss_room`:**<br>- `door.png`: the tall iron door with the red lamp above it, from the corridor;<br>- `key.png`: the vast pillared hall from the doorway, with green-dusk shafts from the broken roof. Leave the knight out, but show the steel anchor plates and snapped chains where he kneels at the far end;<br>- `details.png`: the floor pressure plates and an anchor plate. |
| L3 | `rooftop_room` | `key_night.png`: the green-painted rooftop at night, with the water tank, laundry lines, plastic chairs, warm light from the room's door and the Mapo skyline with distant Han River bridges. `key_day.png`: the same view in the morning. `interior.png`: the one room and tiny kitchen, old wallpaper, a fold-out table, Seoa's desk with a laptop (#00FF00 screen). |
| L4 | `gwanghwamun`, `ninth_wall` | **`gwanghwamun`:**<br>- `key.png`: Gwanghwamun Square at night under a red sky, the palace gate and the ridge behind it as dark shapes, cracked pavement and abandoned cars. The S-grade gate is a vertical tear in the sky many storeys tall, black-violet inside with a pale rim. Tiny figures in the square for scale.<br>**`ninth_wall`:**<br>- `key.png`: drawn in grey for a flashback. A great limestone wall across a mountain pass with nine round towers and banners, under siege by Hush-spawn (black shapes leaking ash). A distant fortress with a great bell. |
| L5 | `memorial_hall`, `kanghan_monitor` | **`memorial_hall`:**<br>- `key.png`: a guild hall lobby set up for a memorial press event: a black backdrop with no text, a framed portrait on an easel with black ribbons and white chrysanthemums (leave the photo as a plain grey placeholder), and press cameras on tripods.<br>**`kanghan_monitor`:**<br>- `key.png`: a dark glass-walled room high in a corporate tower at night, with a wall of #00FF00 monitors and the city lights far below. |

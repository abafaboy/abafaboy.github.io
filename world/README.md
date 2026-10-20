# world/ · the MSGF location bible

Everything about **where** *My Summons Go First* Part One happens (chapters 1–100). The story itself is in `STORY_BIBLE.md` and `PART_ONE_BEATS.md`; the general look is in `ART_BIBLE.md`.

## What is here

| File | What it is |
|---|---|
| `LOCATIONS.md` | The location bible: an index of every location id, the aliases, one entry per place (where it is, chapters, exterior and interior, looks, colours, travel, continuity locks), the other side and the pockets, the route-alignment windows, a travel table, the gate sites, every contradiction found with its ruling, the decisions writers must follow, the script lines to correct, and the web sources. **Start here.** |
| `city_map.svg` / `.png` | Seoul, about 11 × 12 km round Mapo: the Han and its bridges, main roads, subway Lines 1, 2, 5, 6 and 9 with the stations the story uses, district and neighbourhood names, 24 numbered story pins with a legend, 12 gate incident sites (violet diamonds) with chapters, the ch1 bus route and walk home, the Hapjeong gate zone, and an inset of the home turf at 2.6 × scale. Arrows point to Haeseong, Chungju, Yeoju and Daegu. |
| `otherside_map.svg` / `.png` | The other side (stylised): the watch country with the old line, Nib's post, Kett's post and **the white bit**; Sera's river settlement and the shared region; Orrin's uplands, the far cliffs, Kesh's signal halls, Dara's field country. Below it the borderland pockets with their skies and fragment kinds, the Seoul gate slits, the summon seams (cyan) and the clue links (amber); the route-alignment window table; and four insets: the Guro basin, the Terrace Gate east connection, the Chungju river, the Yeoju field. |
| `floorplans/` | Eleven plan sheets, each `.svg` with a `.png` beside it (below). |
| `keys/<id>/` | Codex's visual keys for the 13 Arc I locations (`key_wide.jpg`, `key_reverse.jpg`, sometimes `key_detail.jpg`, and `notes.md`). **The keys are canonical for how a place looks.** |

### Floor plans

| Sheet | Covers |
|---|---|
| `taeo_flat` | Unit 402 (drawn to the key), the 4F corridor, the site (bus street, corner stop, alley, rear lane) and a section of the five-storey block |
| `hanbit_mart` | Shop floor (drawn to the key), stockroom corridor, back store, break-room inset (to its key) and the street corner |
| `moon_laundromat` | The laundromat (to the key), the north counter's lip with Kett's mark, the back room, the street |
| `aao_office` | Chae's assessment room (to the key) and the AAO lobby inset |
| `grandparents_house` | The house and courtyard (to the key), the ch8 seating lock, and a site sketch of Haeseong harbour, the breakwater and the sea gate |
| `ryu_practice_yard` | The Ryu Survey compound: the keyed practice yard plus the west strip, workshop, service bay and cage, with insets of the office container, the container home and the workshop roof |
| `guro_pit` | The Guro foundation pit, its street and hoarding, and the side-gallery inset |
| `sinjeong_arcade` | The Sinjeong surge: street level and the underground (F stair, landing, corridor F, pharmacy, stockrooms, food court, seven gates) |
| `exhibition_arena` | The exhibition at Seoul World Cup Stadium (local frame): the course, operator boxes, service corridor, draw stage, archery range, stage, press pit, VIP enclosure |
| `mapo_tyre_base` | The crew's first base: forecourt, two-storey block (1F and 2F plans), the three-bay shed with the featured bay |
| `go_first` | The GO FIRST building, four floors: Eunchae's and the guild hall, the clinic, the crew floor, the roof garden |

## Conventions

- **Ids** are snake_case and match the scripts' `locations:` fields. Aliases are listed in `LOCATIONS.md` section 2.
- **Precedence** (LOCATIONS.md, "How to use"): story facts the beats need; then locked script text (ch001–ch013); then the keys for looks; then the continuity pass and later scripts; then this folder's own decisions, marked **(decided here)**.
- **Compass.** Plans and maps use the real compass, north up, except the exhibition sheet and the side-gallery inset (local frames, labelled). The `taeo_flat` and `mangwon_street` keys use their own local frames; LOCATIONS.md section 2 shows how to turn them.
- **No readable signs** in any drawing; signs are shapes and colours. No real address is given for any fictional place.
- **Plan colours.** Blue dots and wedges: script panel cameras (chapter·panel). Teal squares and wedges: Codex key cameras. Violet diamonds and black slits with a cyan rim: gates. Cyan: summon seams. Amber: anchor deposits and clues. Numbered white circles: the key on each sheet.
- **Maps.** The city map uses district boundaries from KOSTAT 2013 / JUSO 2015 (southkorea/seoul-maps on GitHub) in an equirectangular projection; the river, roads and lines are simplified, and pins are good to about 100 m. Real places named on the maps were checked on the web (LOCATIONS.md section 14).

## Still to do

- Keys for the unkeyed sets the scripts use most: `ryu_office`, the container home, `ryu_yard_roof`, `mapo_tyre_base`, `sinjeong_*`, `exhibition_arena`, `guro_pit`, `metro_maintenance_tunnel`, `camping_store`, `aao_lobby`, `gma_building`, `mangwon_riverside`, `porters_lodging`, `go_first` (ledger/CONTINUITY_TODO.md:22 lists the first ones).
- Skies for the Yeoju pockets and the film-crew gate: set by the first script that enters, then record them in LOCATIONS.md section 8.
- The script lines listed in LOCATIONS.md section 13 are outside this folder and still need their owners' edits.

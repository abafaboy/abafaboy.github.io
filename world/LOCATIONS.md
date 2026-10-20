# My Summons Go First: location bible (Part One, chapters 1–100)

This file fixes every place the story uses in Part One, so scripts and art stay consistent for 100 chapters. `STORY_BIBLE.md` decides what happens, `ART_BIBLE.md` how it looks in general, and this file **where** it happens and what each place looks like.

## How to use this file

- **Script writers.** Put the `id` in `locations:` (SCRIPT_FORMAT.md). Use the travel table (section 9) for `when:` lines and time tags. Follow every continuity lock.
- **Artists.** Attach the Codex key images (`world/keys/<id>/`) and the floor plan (`world/floorplans/`) to every establishing shot. Furniture never moves unless a panel moves it (ART_BIBLE A10).
- **No readable signs.** Every sign here is described by shape and colour only (ART_BIBLE A6, A9). The letterer adds words only where a script names them.
- **"(decided here)"** marks a choice this file makes because the bible files and scripts are silent. Writers must treat it as canon.
- **Precedence.** When sources disagree, this file rules in this order:
  1. **Story facts the beats need** (PART_ONE_BEATS.md), for example the balcony Orrin leaves by in ch24.
  2. **Locked script text** in ch001–ch013. Their lettered words cannot change; art notes that clash with a key are listed in section 11.
  3. **The Codex keys** (`world/keys/`) for how a place looks. A key beats a floor plan, and beats a script's art note on looks.
  4. **The continuity pass** (ledger/REPORT_continuity_14-22.md) and the later scripts (ch023–ch093).
  5. The rest of this file.
- **Contradictions** are listed in section 11, each with file and line and the ruling. Script lines that should be corrected are in section 13.
- **Real geography.** The city is the real Seoul with fictional businesses. Every real neighbourhood, road, bridge, station and line named here was checked on the web (section 14). Fictional premises sit on real streets or real street types. No real address is given for any fictional place or private person.
- **Compass.** All directions in this file are the real compass. The Codex keys for `taeo_flat` and `mangwon_street` describe their rooms in their own local frames; section 2 shows how to turn them.
- **Season.** Chapter 1 is a Tuesday in early spring (ch001 `when:`). Part One covers about fourteen months.
- **Maps.** `world/city_map.png` (Seoul pins and gate sites), `world/otherside_map.png` (the other side, the pockets and the seams). Pin numbers on the city map are in the index below.

## 1. Index

Chapters in **bold** come from a script's `locations:` field; the others come from the beats. "m" means mentioned, not shown.

| id | Name | Where | Chapters | Key | Plan | Map |
|---|---|---|---|---|---|---|
| `taeo_flat` | Taeo's studio flat, unit 402 | Mangwon 2-dong, Mapo-gu | **1–3, 5, 6, 9–12, 18–21, 23**, 24, 28; m 15, 17, 22, 26 | keys/taeo_flat | taeo_flat | pin 2 |
| `taeo_building` | Taeo's building: stairs, corridors, piloti | same | **2, 3, 21, 22**, 24, 28 | (mangwon_street, materials only) | taeo_flat (site, section) | pin 2 |
| `taeo_street` | The bus street and the corner stop | same | **2, 3, 20–22**, 24, 28 | (mangwon_street) | taeo_flat (site) | pin 2 |
| `mangwon_street` | The walk-home alley | Mangwon-dong, from the Hapjeong-dong lanes | **1, 5, 21, 29** | keys/mangwon_street | taeo_flat (site) | inset |
| `night_bus` | The green branch bus | corner stop to Yanghwa-ro | **1** | keys/night_bus | — | inset route |
| `seogyo_gate` | The Seogyo-dong corner gate | World Cup-ro, Seogyo-dong | **1** (alert; m 21) | — | — | G1 |
| `hanbit_mart` | Hanbit Mart, shop floor | western Hapjeong-dong | **1, 5, 9, 18, 22**, 6; m 99 | keys/hanbit_mart | hanbit_mart | pin 1 |
| `hanbit_stockroom` | Stockroom corridor and back store | same | **5, 6, 9** | (hanbit_mart reverse) | hanbit_mart | pin 1 |
| `hanbit_breakroom` | Staff break room | same | **1, 5, 6, 9, 18** | keys/hanbit_breakroom | hanbit_mart (inset) | pin 1 |
| `hanbit_mart_ext` | The mart's street corner | same | **1, 5, 18** | keys/hanbit_mart_ext | hanbit_mart (street) | pin 1 |
| `moon_laundromat` | Granny Moon's laundromat | Mangwon 1-dong | **5, 29**, 76 | keys/moon_laundromat | moon_laundromat | pin 5 |
| `pyo_cafe` | The café in the tower by Hapjeong Station | Seogyo-dong side of Hapjeong stn | **6** | keys/pyo_cafe | — | pin 6 |
| `hapjeong_side_street` | Side street beside the tower | same | **6** | — | — | pin 6 |
| `mangwon_riverside` | The embankment in Mangwon Hangang Park | Mangwon-dong riverside | **6, 19, 21** | — | — | pin 7 |
| `world_cup_ro` | World Cup-ro at Mangwon station | Mangwon / Seogyo | **3**, 33, 61 | — | — | pin 4 |
| `camping_store` | The camping shop | taeo_street, 3 min north | **19**, 43 | — | — | pin 12 |
| `noodle_shop` | Noodle shop and its crossing | Mangwon-dong, four-lane road | **7** | — | — | pin 9 |
| `eunchae_gosiwon` | Eunchae's gosiwon room | near Hapjeong stn | **22** | — | — | pin 13 |
| `porters_lodging` | Porters' lodging over a tool shop | Mangwon 1-dong | **23**, 61, 64 | — | — | pin 14 |
| `ryu_practice_yard` | Ryu Survey compound and container home | Mangwon 2-dong | **7, 9, 20–23, 26, 29, 30, 41, 48, 52, 93**, 24, 25, 27, 28, 43–45, 47, 53, 84, 86, 89 | keys/ryu_practice_yard | ryu_practice_yard (+ container-home inset) | pin 8 |
| `ryu_yard_street` | Pavement outside the yard | same | **7, 12, 20** | — | ryu_practice_yard | pin 8 |
| `ryu_office` | The office container | same | **10**, 26 | (ryu_practice_yard) | ryu_practice_yard (inset) | pin 8 |
| `ryu_yard_roof` | The workshop roof | same | **20, 22, 23**, 82 | — | ryu_practice_yard (inset) | pin 8 |
| `ryu_training_gate` | Training-gate cage and hollow | same | **12** | — | ryu_practice_yard | G4 |
| `ryu_van` | Ryu Survey's white van | on the road | **10, 34**, many | — | — | — |
| `mapo_tyre_base` | The crew's first base | Hapjeong-dong | **63**, 33–98 | — | mapo_tyre_base | pin 15 |
| `go_first` | The GO FIRST building | Hapjeong-dong | 99, 100 | — | go_first | pin 24 |
| `hapjeong_gate_zone` | The gate advisory zone | Hapjeong, Seogyo, Mangwon | declared 21; **22** sign | — | — | city map |
| `aao_office` | Ability Assessment Office, Mapo branch | off World Cup-ro, Seongsan-dong | **3, 4, 21, 23**, 25, 46; m 92 | keys/aao_office | aao_office | pin 3 |
| `aao_exam_hall` | AAO written-exam hall | same building | **48** | — | — | pin 3 |
| `aao_practical_hall` | AAO practical gym | same building | **48**, 49 | — | — | pin 3 |
| `awakened_cram_academy` | Cram academy for the awakened | Noryangjin-dong, Dongjak-gu | **48** | — | — | pin 20 |
| `gma_building` | Gate Management Agency, Seoul office | near Gongdeok, Mapo-gu | **9** | — | — | pin 10 |
| `gma_hearing_room` | GMA hearing room | same | **9** | keys/gma_hearing_room | — | pin 10 |
| `metro_maintenance_tunnel` | Line 6 maintenance spur | Seongsan-dong (under) | **10, 11** | — | — | G3 |
| `gate_stone_gallery` | Inside: the stone gallery (E) | pocket | **11** | — | — | otherside |
| `guro_pit` | The Guro foundation pit | Guro-dong, Guro-gu | **13–17**; m 18 | — | guro_pit | G5 |
| `guro_gate_inside` | Inside: the Guro basin (C) | pocket | **13–17** | — | guro_pit (side gallery inset) | otherside |
| `guro_hospital_er` | Kwak's emergency department | Guro-gu | **18** | — | — | pin 11 |
| `seoul_line2` | Line 2 over the Dangsan Railway Bridge | Han River | **18** | — | — | city map |
| `seongsan_redevelopment` | Emptied villa block, salt-iron gate | Seongsan-dong | **22** | — | — | G6 |
| `stone_survey_rim` | Two paid stone-survey jobs | unstated | **23** | — | — | not pinned |
| `terrace_gate_rim` | Terrace Gate staging, freight hardstanding | Mullae-dong, Yeongdeungpo-gu | **23, 30–32**, 29 | — | — | G7 |
| `terrace_gate_east` | Inside: the east terrace (C+) | pocket | **31, 32** | — | — | otherside |
| `sewer_gate_rim` | Mapo maintenance chamber, sewer gate | Mangwon 1-dong (under) | **23** | — | — | G8 |
| `sinjeong_arcade` | The Sinjeong arcade surge | Sinjeong-dong, Yangcheon-gu | **34–38**, 33 hook, 39, 40 | — | sinjeong_arcade | G9 |
| `sinjeong_street` | The road above, tent, press line, kerb | same | **34–38, 41**, 39, 40 | — | sinjeong_arcade | G9 |
| `seoryun_base` | Seoryun's rescue depot | Tojeong-dong riverside, Mapo-gu | **41** | — | — | pin 16, G10 |
| `long_night_memorial` | Long Night memorial plaque | Seonyudo Park, Yeongdeungpo-gu | 42 | — | — | pin 17 |
| `seogang_camp` | Seogang camp site (nine years ago) | Seogang riverside, Mapo-gu | 40, 43 | — | — | pin 18, G12 |
| `yoon_family_flat` | The Yoon family flat (nine years ago) | Sangsu-dong side, Mapo-gu | 43 | — | — | pin 19 |
| `film_crew_gate` | Film-crew D-grade gate | DMC backlot, Sangam-dong | 47 | — | — | G11 |
| `exhibition_arena` | The exhibition at Seoul World Cup Stadium | Seongsan-dong, Mapo-gu | **52, 56**, 49–61 | — | exhibition_arena | pin 21 |
| `national_assembly` | National Assembly (TV only) | Yeouido | 47, 66, 70 | — | — | pin 22 |
| `meridian_tower` | Meridian Tower | Yeouido | 81, 82 | — | — | pin 23 |
| `haeseong_port` | Haeseong harbour, quay, breakwater, sea gate | Haeseong (fictional) | **8, 9**, 43, 62, 96 | keys/haeseong_port | grandparents_house (site) | off map |
| `haeseong_bus` | The intercity coach | Seoul to Haeseong | **8, 9**, 96 | — | — | off map |
| `grandparents_house` | The grandparents' house | Haeseong | **7, 8, 21, 30**, 43, 62, 96 | keys/grandparents_house | grandparents_house | off map |
| `haeseong_school` | Haru's school | Haeseong | 59 (video), 96 | — | — | off map |
| `chungju_river_gate` | Chungju underground river (A) | Chungju, North Chungcheong | **63, 71**, 64–79 | — | — | otherside inset |
| `chungju_gate_site` | Chungju staging cutting | Chungju | **63, 71** | — | — | off map |
| `sera_hospital` | Sera's hospital | Chungju (decided here) | 72, 75 | — | — | off map |
| `yeoju_anchor_field` | Yeoju anchor field, gates A–E | Yeoju, Gyeonggi | **93**, 84, 92, 94–98 | — | — | otherside inset |
| `yeoju_demo_ring` | Public demo ring by the depot | same | **93**, 92 | — | — | otherside inset |
| `provincial_clinic` | The provincial dialysis clinic | Yeoju (decided here) | 87; m 100 | — | — | off map |
| `nib_post` | Nib's watch post (other side) | the watch country | **21** (flashback); m 4, 46 | — | — | otherside |
| video only | `doyun_lecture` (ch12), `guro_site_news` (ch11), `archive_rescue_site` (ch36) | — | **11, 12, 36** | — | — | — |

## 2. Aliases and sub-ids

Use the canonical id in new scripts. Older scripts may use an alias; it means exactly the same place.

| Alias (used in) | Canonical id | Note |
|---|---|---|
| `hanbit_mart_breakroom` (ch001, ch005, ch009) | `hanbit_breakroom` | Codex key name |
| `hanbit_mart_stockroom` (ch005, ch009) | `hanbit_stockroom` | |
| `mart_street` (ch001, ch005, ch018) | `hanbit_mart_ext` | Codex key name |
| `hapjeong_alley` (ch001) | `mangwon_street` | Codex key name; the walk starts in Hapjeong-dong lanes and ends in Mangwon-dong |
| `ryu_yard` (ch010, ch012) | `ryu_practice_yard` | the whole compound; CODEX_SCRIPT_BRIEF.md:44 |
| `tyre_yard` (older world files) | `mapo_tyre_base` | script name from ch063 |
| `exhibition_stadium` (older world files) | `exhibition_arena` | script name from ch056 |
| `noryangjin_exam` (older world files) | `awakened_cram_academy` + `aao_exam_hall` + `aao_practical_hall` | ch048 moved the exam into the AAO building |
| `mangwon_storm_drain` (older world files) | `sewer_gate_rim` / `sewer_gate_inside` | ch023 |
| `sinjeong_stairwell` (ch038) | `sinjeong_f_stair` | |
| `sinjeong_arcade_f` (ch038) | `sinjeong_f_landing` | |
| `guro_gate`, `guro_gate_gallery` (older notes) | `guro_gate_inside` | |
| `terrace_gate_inside` (older world files) | `terrace_gate_outer` (outer edge, ch23) / `terrace_gate_east` (east connection, ch31–32) | |

Sub-ids, each covered inside its parent entry: `aao_ext`, `aao_lobby` (aao_office); `pyo_cafe_ext` (pyo_cafe); `gosiwon_street` (eunchae_gosiwon); `noodle_shop_crossing` (noodle_shop); `ryu_training_gate_inside` (ryu_training_gate); `guro_pit_rim`, `guro_pit_street`, `guro_side_gallery` (guro_pit); `salt_iron_cave` (seongsan_redevelopment); `stone_survey_inside`; `sewer_gate_inside`; `terrace_gate_outer`; `sinjeong_command`, `sinjeong_f_stair`, `sinjeong_f_landing`, `sinjeong_pharmacy`, `sinjeong_stockrooms` (sinjeong_arcade); `exchange_gate_inside` (seoryun_base); `exhibition_service_corridor`, `exhibition_draw_stage` (exhibition_arena); `haeseong_breakwater` (haeseong_port); `chungju_gate_staging` (chungju_gate_site).

**Turning the Codex key frames into the real compass.**
- `taeo_flat` key: its "north" (the window wall) is real **east**. Its "west" (kitchenette) is real north, its "east" (bed) real south, its "south" (entrance) real west. So the key's "northwest desk" is in the real north-east corner, under the window at the far LEFT as you look in. Scripts that say "north window" or "northwest desk" (ch018–ch021) use the key frame; both mean the same room.
- `mangwon_street` key: its "north" (up the alley) is real **east**. Its "east-west main road" is the real north–south bus street; its "southwest corner" bus stop is the real north corner of the alley mouth, on the east kerb of the bus street.
- Every other key uses the real compass.

## 3. Home turf: Mangwon-dong and Hapjeong-dong, Mapo-gu

### taeo_flat · Taeo's studio flat, unit 402

- **Keys.** `world/keys/taeo_flat/`: `key_wide.jpg` (from the entry), `key_reverse.jpg` (from the bed head), `key_detail.jpg` (the desk corner), `notes.md`. **Plan:** `world/floorplans/taeo_flat.svg` / `.png` (plan, site sketch, section).
- **Sub-ids.** `taeo_building` (stairs, open-air corridors, ground-floor piloti) and `taeo_street` (the bus street and the corner stop), both below.
- **Where.** Mangwon 2-dong, Mapo-gu. A fictional five-storey studio block on the east side of a two-lane bus street that runs south from World Cup-ro near Mangwon station. No real address. **(decided here)**
  - Mangwon station (Line 6, under World Cup-ro) is 7 minutes' walk north (ch003).
  - Mangwon-dong is low-lying riverside ground that flooded badly in the past (Wikipedia, Mangwon-dong), so its housing is older and cheaper than Hapjeong-dong's. That is how Taeo pays ₩450,000 a month on a ₩5,000,000 deposit (ch5, ch15).
- **Chapters.** 1 (the draw; Nib arrives), 2 (the whole chapter), 3 (the morning call; the street door and the bus), 5 (hook: the knife on the table), 6 (the sleepless night; Nib sleeps sitting by the door), 9 (montage), 10–12 (mornings before the yard), 18 (Chae's call; the shard glows at the entry step), 19 (the interface; integration), 20 (P01–P05, 3:56 AM), 21 (Nib's rage; the open door; "1. ASK FIRST."; the notice), 23 (copper moss integrated before 9 PM; the moss window), 24 (Orrin; the ladder truck), 28 (packing; the empty room). Mentioned, not shown: 15, 17 (the deposit), 22 (rezoning; landlord selling), 26 (the deadline).
- **Interior** (looking IN from the door, which is in the west wall; follow the key):
  - **Vestibule and entry.** A tiled shoe area one step down, a tall shoe cabinet on the north side, a coat hook, an intercom panel. The door is a flat slate-grey steel slab with a lever handle and a blank brass number plate.
  - **Left foreground (north wall):** the kitchenette from the key: sink, two-ring hob, white under-counter fridge, washer under the counter, wall cabinets and a hood above. The folding table stands stowed against this wall past the fridge.
  - **Far left, by the window:** the pale wood desk with the orange cone lamp, a plain mug and a closed notebook; on the short shelf above, THE FRAMED PHOTO (parents, Taeo at 14, baby Haru; abstract shapes, no faces in the key) and a small plant. The photo lives on this shelf above the DESK, never above the bed (ruling C25).
  - **Far wall (east):** the ONE window, two sliding panes centred on the wall, sill at about 0.75 m, a narrow balcony outside it with a metal rail. A grey-blue blackout roller blind sits in the box above the window (rolled up in the key). Scripts that say "curtain" mean this blind **(decided here)**.
  - **Right (south wall):** the single bed along the wall, head at the window end, grey duvet, three storage drawers facing the room.
  - **Right foreground:** the black metal clothes rack (two plain jackets, boxes below); the olive backpack (patch out) hangs on its end hook.
  - **Only other room:** the windowless wet room off the vestibule (shower, toilet, basin). It is not in the key.
  - **Clear floor** about 1.7 m wide west of the bed holds the summon circle (1.4 m across, ch1 and ch24) and the folding table when it is set out.
- **Balcony** (0.95 m deep): the AC outdoor unit, a folded drying rack, the rail. View: the rear lane, the backs of low villas, lit windows at night. The ladder truck docks here from the rear lane in ch24.
- **Key props.** THE CUP (ch2, packed ch28): a plain white ceramic mug with one thin green band **(decided here)**. From ch21 P41 a sheet of printer paper reading "1. ASK FIRST." is taped on the wet room's outside wall, facing the bed (ch021, ch023). The original drawing of Nib's post is folded PAPER, kept with the pebble (continuity report). Kwak's marked knee pads are stacked at the entry step from ch19.
- **Time-of-day looks.** Night: the desk lamp only, warm orange on the desk side, deep blue-grey elsewhere, phone screen cold white. Morning: cool grey-blue daylight, one yellow band of sun at the blind's edge (the window faces east). Day with the blind down: dim blue-grey with one yellow line. Summon: cyan #3FE3F2 takes the whole room.
- **Colour script.**

  | Look | Key light | Shadows | Accent |
  |---|---|---|---|
  | Night | lamp orange #D5A06A, desk side | blue-grey #303C50 | phone-screen white |
  | Morning | cool grey-blue daylight | soft blue | one yellow band at the blind |
  | Summon | interface cyan #3FE3F2 | navy #0B1530 | the arrival's own colour (Nib's amber eyes, Orrin's slate-green) |

  Walls #C9BBA7, timber floor #9C8066, duvet #777E88 (key notes). Night and morning rows are ART_BIBLE A4.
- **Travel.** Mangwon station 7 min walk. Hanbit Mart 20 min walk (laundromat at 7 min). Ryu yard 12 min. AAO 20 min walk, or Line 6 Mangwon to Mapo-gu Office (one stop) plus 5 min. Camping store 3 min. The riverside about 12 min south-west.
- **Continuity locks.**
  - Main room 5.00 × 3.60 m (18.0 m²), ceiling 2.30 m; unit 402 on 4F; no lift.
  - Screen geography: looking IN, kitchenette LEFT, bed RIGHT, window centred far. Looking OUT, the kitchenette is RIGHT and the bed LEFT. Never mirror the room.
  - The door opens OUT into the corridor and hinges on its north jamb (from inside: handle LEFT, hinges RIGHT).
  - Nib's sleeping spot: the floor at the edge of the shoe step, back against the wet-room wall beside the door (ch006 P01, ch020).
  - The desk lamp is on the desk's west end, about 2 m from the bed. In ch1 P52 Taeo knocks it by catching its cord.
  - Orrin (ch24) pins the bed and cracks the window; both panes come out; he leaves over the sill and the balcony onto the ladder truck and bends the rail. The rail stays bent and the glass taped until the move (ch28).
  - The block is inside `hapjeong_gate_zone` from ch21.
- **Contradictions.** C01, C02, C03, C05, C06 (section 11).

### taeo_building · stairs, corridors and piloti

- **Plan:** `taeo_flat` site sketch and section. No key: the `mangwon_street` key gives the street materials only.
- **The block.** Five storeys of dark red brick with a grey parapet: a ground-floor piloti, then twelve studios, three to a floor on 2F–5F (ch021, ch022). On 4F, 401 is the south neighbour, 402 Taeo (the middle door), 403 the north neighbour toward the stairs.
- **Piloti.** Open ground floor under the brick overhang: the glass street door a step back from the pavement, a bank of twelve mailboxes, the foot of the stairs, a little parking. The street door faces the bus street (west).
- **Corridors.** Open-air access corridors on the west face, 1.30 m wide, under the slab above, with a waist-high metal rail on the street side and cold white tube lights. The stairs are at the north end, so they are on the RIGHT as you come out of 402 (ch003). From the 4F corridor Nib sees "a scooter below, too many lights" (ch2).
- **Rear.** The east face has the balconies over a narrow rear lane; the ladder truck parks there in ch24.
- **Section.** Piloti 3.0 m, then 2.8 m a floor: the 4F floor is about 8.6 m above the street.
- **Locks.** No lift. 402's door, held open, swings out across the corridor with its outer face toward the stairs (ch021). The landlord's notice (ch21) is taped on the outer face of 402's door and every other door.

### taeo_street · the bus street and the corner stop

- **Plan:** `taeo_flat` site sketch. Key: `world/keys/mangwon_street/` shows the corner (see that entry).
- **The street.** A two-lane bus street running north–south: low red-brick blocks, gas meters, tangled overhead wires, a convenience-store sign far off, a parked delivery scooter (ch020). North: World Cup-ro and Mangwon station, 7 min.
- **The corner stop.** 30 m south of the street door, where the alley (`mangwon_street`) meets the street (ch021, ch022): a bus shelter with a tall portrait advertising screen (dark in the key; lit green in ch1 P45), a utility pole and a lamp post. This is ch1 P45's "corner before his building".
- **GMA zone sign** from ch22 P01: bolted to the lamp post by the stop, a yellow field with a black-and-yellow hazard border and a violet pictogram of a door-shaped slit, no letters. Keep it in every later shot of the corner (ch022).
- **The streetlight of ch20.** The hook happens under the last streetlight on the block before the building, about five minutes from his door; keep the corner stop and its screen out of frame (ch020).
- **Locks.** Buses at the corner stop run NORTH past the street door toward Mangwon station (ruling C04). The camping store is 3 minutes north on the east side (ch019).

### mangwon_street · the walk-home alley (alias hapjeong_alley)

- **Keys.** `world/keys/mangwon_street/`: `key_wide.jpg` (from the bus street looking up the alley), `key_reverse.jpg` (from farther up the alley looking back), `notes.md`.
- **Where.** The walk home from Hanbit Mart starts in the Hapjeong-dong villa lanes, follows Poeun-ro and lanes west into Mangwon-dong, passes Granny Moon's laundromat and reaches the bus street at the corner stop by this alley (ch005, ruling C07).
- **The alley (key).** A narrow residential lane running east from the bus street. At its mouth: the bus shelter with the tall dark ad screen and the utility pole on the north corner; on the south side just inside, a three-storey red-brick villa with a recessed grey steel door, three shallow concrete risers, a blank intercom, a shallow concrete canopy, a drainpipe and a sodium lamp above the door. Opposite: a low brick boundary wall, exposed gas meters and pipes. Overhead wires, a small blank shop sign far off.
  - The key's villa is a NEIGHBOUR, not Taeo's building (ruling C01; ch029 calls it obsolete as his home).
- **Chapters.** 1 (as `hapjeong_alley`: the walk home and the floating window, P42–P46), 5 (the walk home past the laundromat), 21 (the lane at night), 29 (daylight: the walk to Moon's).
- **Looks.** Night: sodium #BE8754 on brick #78574D, shadows #2D3B54, sky #1D2B43, the ad screen #17202C (key). Day (ch29): flat warm daylight on the same brick, meters and wires.
- **Travel.** Laundromat to the corner about 6 min; corner to the street door 30 m.
- **Locks.** The ad screen is dark unless a script lights it. No police, gate or people in the base key.

### night_bus · the green branch bus

- **Keys.** `world/keys/night_bus/`: `key_wide.jpg` (front looking aft), `key_reverse.jpg` (from the rear bench), `notes.md`.
- **Route (decided here).** A green branch bus (Seoul's green buses are the local branch routes; Wikipedia, Buses in Seoul) from the corner stop north up the bus street, east along World Cup-ro past Mangwon station and the Seogyo-dong corner (G1), down to Hapjeong station and on to a Yanghwa-ro stop near the mart: about 10 minutes. ch1's cold open is the ride TO work at 7:50 PM.
- **Interior (key).** A modern low-floor city bus; front is the driver's end. Two closed doors on the right side (front by the driver, middle exit), driver at front left, central aisle, blue moulded paired seats in the rear half, a few single and priority seats forward, a raised five-seat back bench. Muted ochre poles and straps, dark blank route display and fare screen, narrow cool ceiling strips.
- **Lock.** Taeo's seat is the rear bench, left window. Phone glow only for scripted passengers.
- **Colour script.** Navy #28364F, seats #4D6480, shadow #1D293E, rails #B8A56F, city-light rectangles #B38A5C (key); cold white phone glow, one red banner shape per phone in ch1 (ch001 palette).
- **Chapters.** 1.

### seogyo_gate · the Seogyo-dong corner gate (G1)

- **What.** The gate behind ch1's Emergency Alert ("Gate advisory: Seogyo-dong, Mapo-gu", ch001 P01; beats 19). The bus passes it: a night street corner in Mapo, a small door-height black-violet slit with a cold white-cyan rim and lavender light, inside a ring of orange barriers and police tape on the pavement; pedestrians walk past without looking (ch001).
- **Where (decided here).** A corner on World Cup-ro in Seogyo-dong, between Hapjeong and Mangwon stations, on the bus route. It and the Hanbit Mart gate (G2) are the two centres of `hapjeong_gate_zone`. Still on the TV ticker in ch21.
- **Chapters.** 1; mentioned 21.

### hanbit_mart · Hanbit Mart, Hapjeong store

- **Keys.** `world/keys/hanbit_mart/`: `key_wide.jpg` (customer side looking north to the counter), `key_reverse.jpg` (behind the counter looking south), `key_detail.jpg` (the counter), `notes.md`. **Plan:** `world/floorplans/hanbit_mart.svg` / `.png` (shop, stockroom corridor, back store, break-room inset, the street corner).
- **Sub-ids.** `hanbit_stockroom`, `hanbit_breakroom`, `hanbit_mart_ext` (entries below).
- **Where.** Western Hapjeong-dong, Mapo-gu (STORY_BIBLE.md:182), just south of Yanghwa-ro and west of Hapjeong station. The ground floor of a modest three-storey brick villa on the north-east corner of a junction of two residential streets (streets on its west and south sides; key: "southwest street junction"). No real address. **(decided here)**
- **Chapters.** 1 (the shift, the courier, the gate in aisle 2), 5 (the construct stocker; Eunchae meets Nib), 6 (night: the hook in the back), 9 (montage: Eunchae teaches Nib Hangul at the break-room table **(decided here)**), 18 (Dokgo's apology; the kiosk; Taeo's last weeknight), 22 (Eunchae's first morning shift). Mentioned: 99 (the guild building is "two streets from the old Hanbit Mart"; "old" means his old workplace, the store is still open).
- **Shop floor (key).** 6 m east–west by 9 m north–south. The south glass front wraps onto the west wall; the glass entrance is in the west return near the south-west corner, opening in, with a bell above it (the JINGLE).
  - **Counter** across the north-west rear, facing south; the staff passage behind it, the cigarette grid on the north wall, a small dark TV high above the north end of the cigarettes. Counter, west to east: scanner in its cradle, dark till, receipt printer, Taeo's white coffee cup.
  - **Stockroom door** in the north wall immediately east of the counter.
  - **Two low gondolas** running north–south in the centre and east, with a clear front cross-aisle. Aisle 1 = the west face of the centre gondola; aisle 2 = between the gondolas. The promo end cap on the centre gondola's north end faces the counter and carries the one red two-for-one tag.
  - **Drinks fridges** along the east wall.
  - **Front strip:** the low window shelf, a security pillar, the basket stack, the low drinks display by the door (ch18 vitamin-drink gift boxes) and, from ch18, the self-checkout kiosk just east of the door (ruling C09).
- **Opening hours (decided here).** A 24-hour chain store. From ch5 the construct stocker works nights; from the ch18 Friday the store is unstaffed 22:00–06:00 (kiosk and stocker, entry by bank card) (ch018).
- **Time-of-day looks.** Night: pale fluorescent green-white #E1EBDD throughout, grey-green shadows #87998B, the glass a black mirror. Day: daylight cream through the south glass, fluorescent behind (ch022).
- **Colour script.** Walls #C4CEC0, counter #B9C3B6, shelf ochre #B8A17A, dark screens #222D33; the red sale tag #B94B48 is the only saturated note (key notes; ART_BIBLE A4).
- **Travel.** Hapjeong station 6 min walk. Taeo's flat 20 min walk, or the bus (10 min) plus a short walk. Eunchae's gosiwon 8 min. The tyre base 6 min. GO FIRST 2 min (two streets).
- **Continuity locks.**
  - TWO aisles. Looking SOUTH down aisle 2 from the stockroom door: packet noodles LEFT, snacks RIGHT, the black glass front at the far end.
  - **The gate (ch1)** opens mid-aisle 2, 3.4 m from the south glass: a chest-height crack, then a door-height slit across the aisle (G2 on the city map). The gondolas are low (1.5 m), so the slit shows over them from the door and through the glass from the street.
  - Keep aisle 2 unobstructed in every non-gate shot (key notes).
- **Contradictions.** C08, C09 (section 11).

### hanbit_stockroom · stockroom corridor and back store (alias hanbit_mart_stockroom)

- **Plan:** `hanbit_mart` (items 6, 22–26).
- **Layout.** Through the north-wall door beside the counter: the stockroom corridor (racks of cartons, a hand truck) leading east to the steel back door onto the side passage, west to the break room; north of it the back store (manager's small desk with a dark CCTV monitor, racks) and the staff WC.
- **The stocker's box (ch5):** a square of white floor tape about 80 × 80 cm on the concrete just inside the back door, where the construct stocker stands between tasks (ch005).
- **Chapters.** 5 (stockroom maths; Nib listens), 6 (the hook: Taeo on an upturned crate against the corridor's north wall, the wall it shares with the break room; Nib on the other side; the amber thread runs through the wall, ch006 P51–P55; ruling C05), 9.

### hanbit_breakroom · staff break room (alias hanbit_mart_breakroom)

- **Keys.** `world/keys/hanbit_breakroom/`: `key_wide.jpg`, `key_reverse.jpg`, `notes.md`. **Plan:** `hanbit_mart`, break-room inset.
- **Layout (key).** A windowless room 2.2 m east–west by 2.8 m north–south off the stockroom corridor. One grey door in the south wall at its south-west, opening OUT. Two tall narrow grey-green lockers side by side on the west wall. A compact off-white fridge in the north-east corner with the microwave on top. A narrow pale folding table along the east wall south of the fridge, one round blue-grey stool. The rota whiteboard directly above the table: grey squiggle strokes and one small red outlined rectangle, no legible glyphs. A white mug, a food tub, a propped phone (dark). One warm fluorescent tube.
- **Screen geography.** From the door: lockers LEFT, table and whiteboard RIGHT. From the appliance corner looking back: table LEFT, lockers RIGHT (key).
- **Colour script.** Fluorescent cream #D8D2B4, shadows #8F998C, lockers #929D90, table #BDAD8B, stool #647784, rota box #B94B48 (key).
- **Chapters.** 1 (Haru's video call), 5, 6 (the hook: Nib kneels with his palm on the south wall, the wall shared with the stockroom corridor), 9 (Hangul flashcards), 18 (Eunchae: "FROM TONIGHT IT'S THE KIOSK AND THE HAT").
- **Contradiction.** C10 (three lockers and a sink in ch005/ch009 notes; the key wins).

### hanbit_mart_ext · the mart's street corner (alias mart_street)

- **Keys.** `world/keys/hanbit_mart_ext/`: `key_wide.jpg` (from across the junction, south-west, looking north-east), `key_reverse.jpg` (beside the storefront looking south-west across the junction), `notes.md`. **Plan:** street strip on `hanbit_mart`.
- **Look (key).** The corner shop under a modest three-storey brick villa at a south-west junction. A dark green fascia #466B52 wraps the south and west faces, with one plain white disc logo on each face and no letters. Pale green-white interior seen through the glass. A grey delivery scooter parked along the south kerb east of the shop corner, three stacked green crates by the east end of the south window, a terracotta potted plant beside the west entrance, a plain bicycle chained to the pole at the south-west kerb, overhead wires, deep navy residential surroundings, sodium-orange lamps.
- **Back.** The steel back door opens onto the 3 m side passage along the east wall, beside the recycling bins (ch005 P01).
- **Chapters.** 1 (police tape, the crowd, the gate glow through the glass), 5 (the side passage; the front from across the road), 18 (the kiosk visible through the glass).
- **Colour script.** Night #202C40, sodium #BC8453, glass #D9E6D5, crates #667B60, brick #70544D (key).

### moon_laundromat · Granny Moon's laundromat

- **Keys.** `world/keys/moon_laundromat/`: `key_wide.jpg` (from the south-east door), `key_reverse.jpg` (from the back counter), `notes.md`. **Plan:** `world/floorplans/moon_laundromat.svg` / `.png`.
- **Where.** A quiet side street off Poeun-ro, Mangwon 1-dong, Mapo-gu (ch005). Fictional, no real address. 7 minutes' walk from Taeo's flat, about 13 from Hanbit Mart.
- **Chapters.** 5 (first sight at night; she lowers the blind), 29 (she mends Nib's shorts; he carves Kett's mark), 76 (one word in his language; she closes the shop; the older mark). Granny Moon herself appears at the memorial (ch42) and at the GO FIRST party (ch100).
- **Layout (key).** 4.8 m east–west by 8 m north–south. South glass storefront: the glass entry at the south-east; the wide front window at the south-west returns onto the west wall, with a plain pale roller blind half lowered over that corner window. A long folding counter under the window (folded cream and grey laundry, a muted teal basket, a small closed sewing tin). Four front-loading stainless washers along the west wall, doors closed. Two stacked dryer units on the east wall's north half (four round portholes). A plastic chair. North wall: the service counter with a sink at the north-west and a plain staff door at the north-east (to the back room where she lives, decided here). Clear centre aisle, warm dome pendants, old cream tiles with a dull teal lower trim.
- **Kett's mark.** Carved by Nib in ch29 on the projecting wooden lip of the NORTH service counter, as payment. Beside it is an older, faded copy of the same three-line fork, never shown before ch76 (ch029; ruling C16).
- **Looks.** Night: warm cream light #CFAD7E on tiles #D6CBB3, the only lit shopfront on the street, the glass #25364D. Day (ch29): late-morning daylight through the south glass. No amber anywhere (ch005).
- **Locks.** The window wraps the south-west corner; keep the return in every view. Machine controls are dark and unlettered. Granny Moon stands at the folding counter facing the street, her head nearly at the top of the window frame (190 cm).

### pyo_cafe · the café in the glass tower by Hapjeong Station (+ pyo_cafe_ext)

- **Keys.** `world/keys/pyo_cafe/`: `key_wide.jpg` (from the south-east entrance), `key_reverse.jpg` (from the window table), `notes.md`. No plan.
- **Where.** The ground floor of a glass office tower on the corner by Hapjeong Station, Seogyo-dong side (ch006; Hapjeong station is on Yanghwa-ro, Lines 2 and 6). Fictional tower and café, no real address.
- **Chapters.** 6 (Dr. Pyo's offer, late morning: 10:29 to about 11:10 AM).
- **Exterior (`pyo_cafe_ext`).** A glass office tower with a revolving door at its foot; flat spring daylight (ch006).
- **Interior (key).** An upscale, restrained café, 7 m east–west by 9 m north–south. Tall glazing along the west wall onto the street; the main glass door at the south-east. The meeting table by the west window in the south-west half: a rectangular walnut table with three beige upholstered chairs (two on the long sides, Nib's on the north end). Two white cups and saucers, one tall pale juice glass, one blank business card. Espresso and service counter at the north-east with a dark till and blank menu panels. A continuous taupe banquette along the east wall with two small round tables. Pale stone tile, dark walnut trim, a potted ficus by the entrance, brass pendants.
- **Colour script.** Cool late-morning daylight from the west; cream #D6CDC0, walnut #86674E, taupe #B1A495, blue-grey shadows #9EA5A6, the pale juice #CAA37B is the one accent, never Nib's amber (key; ch006 palette).
- **Contradiction.** C19 (ch006's pale oak floor and grey stone tables; the key wins).

### hapjeong_side_street · the side street beside the tower

- **Where.** Beside the café tower by Hapjeong Station (ch006). No key.
- **Look.** Flat late-morning spring daylight, warm grey pavement, blue-grey shadows, a small loading bay (ch006).
- **Chapters.** 6 (about 11:15 AM, after the café).

### mangwon_riverside · the embankment in Mangwon Hangang Park

- **Where.** Mangwon Hangang Park on the Han's north bank, Mangwon-dong. The scenes sit on the stretch between Seongsan Bridge (west, downstream) and Yanghwa Bridge (east) (ch019). The official park is longer: 7.4 km of north bank from the north end of Wonhyo Bridge to the Hongjecheon Bridge in Sangam-dong (Hangang Park official site; ruling C21).
- **The spot (ch019, ch021).** The top of a stepped concrete embankment below the riverside path, with a low concrete parapet about 75 cm high (chest-high on Nib, seat-high for Taeo). Below: grass, the cycle path, the water; across the river, the far bank's embankment road and apartment towers as simple shapes. Downstream to the right (facing the river), the long steel deck-arch of Seongsan Bridge with its row of arches. Facing the river (south), Nib stands on the right (west), Taeo sits on his left.
- **Chapters.** 6 (11:40 AM, the river path), 19 (spring green), 21 (Nib alone at the river, then the lane).
- **Looks.** Day: fresh spring green, open sky; the park is known for its sunset toward Seongsan Bridge (ch019).
- **Travel.** About 12 minutes' walk south-west of Taeo's flat; about 8 from the Ryu yard.

### world_cup_ro · World Cup-ro at Mangwon station

- **Where.** World Cup-ro, the six-lane avenue above Line 6, at Mangwon station, on the edge of Mangwon-dong and Seogyo-dong (ch003; Wikipedia, Special Metropolitan City roads of Seoul).
- **Look (ch003).** Wide pavements, plane trees just budding, a low forsythia hedge, the Line 6 entrance canopy, a bus shelter with a tall portrait ad screen, shops with blank signs (a phone shop, a bakery, a bank, a SumEx draw-ticket shop with a purple-to-pink panel). On the north side a seven-storey mid-rise carries a huge vinyl banner across its top three floors: Sunline for Haneul Air.
- **Chapters.** 3 (P23–P28: the walk to the AAO; the banner, P22 plant); the same banner frame is re-skinned in 33 and 61 as her sponsors change (ch003; CODEX_SCRIPT_BRIEF.md:58).
- **Lock.** Keep the building and the banner frame fixed; only the banner art changes.

### camping_store · the camping shop on the bus street

- **Where.** The east side of the bus street, about 3 minutes' walk north of Taeo's building toward Mangwon station (ch019). Fictional, no real address.
- **Look (ch019).** A narrow old independent camping-and-hiking shop: a faded dark-green blank canvas awning, a glass door on the left, a crammed display window on the right (a small dome tent, a mannequin in a hiking jacket, lanterns, folding chairs, coiled rope; one pair of plain black binoculars on a little wooden stand with a blank price card). Inside, deep and narrow (about 3.5 × 9 m): a slanted wall of hiking boots on the LEFT from the door, racks of jackets and fleeces on the right, a barrel of trekking poles, rolled mats, lanterns and carabiners from the ceiling, a pyramid of gas canisters, a glass counter at the back with the till at its right end and a small dark TV above. Khaki, canvas tan, warm wood; the owner's cobalt-blue jacket is the one saturated note.
- **Chapters.** 19 (the ₩89,000 binoculars), 43 (Nib buys boots, his first shoes, from the same boot wall **(decided here)**).

### noodle_shop · the noodle shop and its crossing (+ noodle_shop_crossing)

- **Where.** Western Mangwon-dong, on a four-lane road (decided here; the road is not named in any script). On the city map near pin 9.
- **Look (ch007).** A small cheap street-facing noodle shop: a glass door onto the pavement, an order counter with menu photos (photos only), then a raised wooden floor about 30 cm high with low tables, floor cushions and a shoe ledge; pendant lamps; a steamed-up front window. Seats: Nib on the far side toward the back wall, Taeo on the near side toward the door.
- **The crossing.** The shop's kerb is the head of a wide zebra crossing over the four-lane road, with a small concrete refuge island in the middle; a bus stop and its stop line just up the road. A stopped bus hides the road behind it from the shop door while the view straight across stays clear (ch007, the ~1:05 PM crossing).
- **Chapters.** 7.

### eunchae_gosiwon · Eunchae's gosiwon room (+ gosiwon_street)

- **Where.** The third floor above a PC bang on a commercial side street near Hapjeong station, Hapjeong-dong: 5 minutes' walk from the station, 8 from Hanbit Mart (ch022). Fictional, no real address.
- **Street (`gosiwon_street`).** A small real-estate agency with listing cards, a fried-chicken shop, a PC-bang sign above, plane trees, a bus route, overhead wires (ch022).
- **Inside (ch022).** A shoe rack at the head of a long narrow corridor; beige plywood doors close together with blank number plates; grey-green linoleum; an LED strip; ducting overhead; a shared kitchen nook at the far end (big rice cooker, kimchi tub, noodle packs, one laminated rules sheet). Her room: about 1.8 × 2.8 m (5 m²), NO window; a raised single bed along the left wall with a grey quilt and a shelf above (folded clothes, a small rice cooker, a small photo with her parents); a built-in desk at the bed's foot with a stool, a mini-fridge under it, a small wall fan, one LED panel. Every wall is papered with handwritten food-hygiene flashcards and pale-yellow sticky notes except one bare square above the pillow, where Nib's drawing hangs from ch22 P26.
- **Chapters.** 22. ₩350,000 a month, no deposit (ch022; continuity report).

### porters_lodging · the porters' lodging

- **Where.** Rented rooms over a shuttered tool shop in Mangwon 1-dong, Mapo-gu (ch023 says Mapo; the neighbourhood is decided here). Fictional, no real address. About 8 minutes' walk from the Ryu yard, 14 from Hanbit Mart.
- **Look (ch023).** An exterior steel stair up to a narrow shared landing outside the rooms; dented grey doors, drying towels, a boot tray, a cold tube light above a doorway.
- **Chapters.** 23 (Bluebird's collectors harass Dami; Nib's stare), 61 (Dami watches BangBang's apology and writes MY SUMMONS GO FIRST on her helmet), 64 (the porters' mutual fund).
- **Lock.** Dami's room is one of the rented rooms; the landing is shared and outside them.

### ryu_practice_yard · the Ryu Survey compound (alias ryu_yard)

- **Keys.** `world/keys/ryu_practice_yard/`: `key_wide.jpg` (from the south gate looking north, 10 a.m.), `key_reverse.jpg` (from the targets looking south), `notes.md`. **Plan:** `world/floorplans/ryu_practice_yard.svg` / `.png` (site plan with the office-container, container-home and roof insets).
- **Sub-ids.** `ryu_yard_street`, `ryu_office`, `ryu_yard_roof`, `ryu_training_gate` (+ `_inside`), the container home (no separate id; scripts call it the container or Taeo's container home).
- **Where.** Western Mangwon-dong (Mangwon 2-dong), Mapo-gu, 12 minutes' walk from Taeo's flat (ch010). Fictional, no real address.
- **Chapters.** 7 (the first visit; the maze), 9, 10 (6:52 AM; the office), 12 (the training gate; the tow), 20 (the roof party), 21, 22 (the roof at dusk), 23 (opens on the roof; the van seized at P19), 24 (Seonhee lets Orrin stay), 25 (the collapsing scaffold; [LINK: 2]), 26 (the AAO practical here; the spare container offered), 27 (sandbag experiments), 28 (moving day; the container home; the dawn tow truck), 29 (the standoff; the last van towed), 30, 41 (Friday morning), 43–45 (Grandpa at the container door; the yard walk; the crew rules), 47 (Minho's cake; the poster on the yard fence), 48, 52 (night work at the trestle), 53 (drills), 82 (Minho on the yard roof), 84 (the co-op meeting in the yard), 86 (Iron Vow at the yard gate), 89 (relay tests), 93 (relay test frames).
- **The keyed practice yard (key).** 18 m east–west by 26 m north–south, chain-link all round, dusty ochre packed ground.
  - **South fence:** the double vehicle gate in the middle. The pedestrian gate is a chain-link wicket in its west leaf **(decided here)**.
  - **South-west:** the grey corrugated office container (`ryu_office`), door in the middle of its east wall, the one window just south of the door, the keyed concrete step, and beside it a removable wheelchair ramp for Dongsik (ch010, ch012, ch020).
  - **South-east:** the van stand, nose west (key). The key's van carries a plain blue rectangular repossession sticker on its side.
  - **Centre:** the plywood radio maze, waist to head high: three staggered parallel east–west walls with offset gaps and short north–south returns, one zigzag corridor, entrance south-centre, exit north-east. Never rebuilt or widened (ch026).
  - **North fence:** three freestanding round practice targets, plain concentric rings.
  - **West of the maze:** Haein's equipment trestle (two handheld radios, one in pieces, coiled cable, a toolbox); the orange safety vest on the west fence.
  - **East fence:** a blue drum, leaning boards, an olive crate.
- **Outside the key (decided here, from ch020–ch030).**
  - **West strip** behind the office: the container home (below), a path along the yard fence, a chain-link door to the street in its orange-meshed frontage, a 3.5 m panel gate in the yard's west fence for Orrin, and open ground with Orrin's tarp awning (his bed ch24–33; ch026 P45 "the adjoining open yard").
  - **Haein's workshop:** one storey, 8 × 6 m, just beyond the yard's north-west corner, roller door on its south face; an outside steel stair climbs its WEST wall to the roof (`ryu_yard_roof`) (ch020).
  - **North service bay:** an open-sided shed north of the yard with three van spaces and a sliding vehicle gate onto the back lane: ch012's "three white vans along the far fence" and "sliding vehicle gate in the far fence" (ruling C11).
  - **Training-gate cage** (`ryu_training_gate`) in the compound's back-right (north-east) corner, beyond the yard's north fence, through a chain-link door.
- **The container home.** A 20-ft spare container behind the office in the west strip, its door facing east (ch026). Taeo and Nib live here from ch28 until ch99; Haein's workshop is the next building north. The crew writes its three rules on blank paper on the wall facing the door (ch45; seen through the open doorway in close crops, ch048). The door stays propped open all evening in ch47. Inside **(decided here; plan inset)**: the rules on the west wall facing the door; Taeo's low bed at the south end under one small window; Nib's mat and the blue fleece in the north-east corner, facing the door; the folding table from the flat in the middle; a shelf with the framed photo, THE CUP, the pebble and the folded drawing; the clothes rack; a small heater.
- **Vans (fleet lock).** Three white vans with a plain shield logo until ch12's tow. Two from ch12: the older on the SE stand, the second in the north service bay (ch020–ch022); the older gets Nib's Kett mark on its bumper (ch21) and a Bluebird strip (ch22) and is seized at ch23 P19. One from ch23: the last van moves to the SE stand with a blank blue sticker (ch026) and is towed in ch29. None from ch29 to ch33 (ch030, ch031). One again from ch34: Ryu redeems it after ch33's deposit pays down the Bluebird debt **(decided here; ruling C15)**; it stands on the SE stand with no sticker (ch041, ch048, ch052, ch093).
- **Time-of-day looks.** Morning (key, 10 a.m.): sun from the south-east, shadows north-west, ground #C5A171, plywood #B59568, shadow #8A6A49, sky #A8C8DB, container #8D9697, vest #C6864B. Dusk (ch12): low golden-orange sun, long brown shadows. Night (ch52): a portable work lamp over the trestle.
- **Locks.** The office is grey, never white (ch023). The party roof is the workshop roof, never the office (ch020). Never move the office or the maze; frame tightly rather than inventing new buildings (ch029, ch030).
- **Contradictions.** C11–C15 (section 11).

#### ryu_yard_street · the pavement outside

- The pavement along the yard's south side: chain-link with orange safety mesh (the west-strip frontage), a plane tree, parked scooters, low buildings, overhead wires (ch007, ch012, ch020). A taxi pulls in at the kerb in ch20 P50 (Dami helps Kwak in).
- **Chapters.** 7, 12, 20.

#### ryu_office · the office container

- **Plan:** `ryu_practice_yard`, office inset. 6.0 × 2.4 m, long axis north–south, ceiling 2.3 m (ch010).
- **Inside (ch010).** Door in the middle of the east wall, the one window just south of it (key). Looking in: a padded bench along the back (west) wall where Minho sleeps, a small fridge, kettle and a jug of barley tea, a shelf of files above; LEFT (south) end, Seonhee's desk facing the south wall (ledger, roll calculator, cash box, lamp) under a corkboard of notices with a small blue bird logo and red stamps; RIGHT (north) end, Dongsik's corner: the radio base at wheelchair height, a wall map with coloured pins, a framed photo of a younger Dongsik with a boy of about eight and a toddler girl. Middle: a folding table with a battered laptop, stools, crates, a gas heater. One fluorescent tube. No readable text.
- **Chapters.** 10 (7:01 to about 8:45 AM), 26.
- **Contradiction.** C12 (window side).

#### ryu_yard_roof · the workshop roof

- **Plan:** `ryu_practice_yard`, roof inset.
- **Look (ch020).** The flat concrete roof of Haein's workshop, about 8 × 6 m, green waterproof paint, a knee-high parapet with a galvanised pipe rail. The outside steel stair arrives at the north-west corner. A blue plastic water tank on a stand in the north-east corner; white styrofoam planters of lettuce and chilli along the east parapet (Seonhee's); two poles carrying a string of bare bulbs. The south parapet overlooks the compound, low Mapo roofs, lit towers and, far to the south-west, the lit span of a Han River bridge (Seongsan Bridge); the south-east corner looks down into the keyed yard.
- **Seating lock (ch20 P13–P49).** A low folding table, long axis east–west, gas burner and grill plate in the middle. East head: Kwak in the only plastic armchair, Dami on a stool at his north-east corner. North side, west to east: Haein, Minho (grill, tongs, phone), Sejin (medic bag). South side, backs to the parapet, west to east: Nib on an upturned blue crate, Taeo on a stool (backpack at his feet, patch out), Eunchae.
- **ch22:** the same roof, the party cleared: four upturned crates, a camping lantern, cup noodles; Taeo, Nib, Minho, Haein. The window-2 invitation opens here and is declined.
- **Chapters.** 20, 22, 23 (opening), 82 (Minho: "HE MADE US THE SAME OFFER") **(decided here: the same roof)**.

#### ryu_training_gate · the training-gate cage (+ ryu_training_gate_inside)

- **Cage (ch012).** 3 × 3 m of chain-link with a padlocked mesh door, in the compound's back-right corner. Inside, near the back fence and facing the door: a squat black-violet slit about 1.3 m tall and 40 cm wide, a few centimetres above the dirt, cold white-cyan rim, a thin green spill. Nib-sized: an adult must crouch. It stays open because nobody kills its boss. Ryu Survey holds a GMA training licence for it and rents it to an academy by the hour. ch12 props: two upturned blue crates inside the door about 2.5 m from the slit, a white chalk line 2 m from the slit.
- **Inside (ch012).** A stone hollow about 4 m across like the bottom of a dry well, open to a GREEN DUSK sky with no sun; grey stone streaked with pale lichen; violet shadows. Haein's rig against the far wall: a scaffold plank with three grey sandbags held up at about 1.2 m by THREE IDENTICAL pale timber beams on steel foot blocks, chalk tallies of one, two and three strokes. The boss: a harmless pale lavender-grey snail the size of a loaf, on the floor by the rig's right end.
- **Chapters.** 12. City map: G4.

### ryu_van · Ryu Survey's van

- A white long-wheelbase passenger-cargo van with a plain shield logo: the driver's row, one rear bench, the cargo area behind where the construct mule rides with the packs (ch010). From ch34 an equipment trailer carries Orrin (with his consent; restraints on the trailer ramp, never his neck or shell) (ch034).
- **Chapters.** 10, 13 (to Guro), 22, 34, and the other jobs. See the fleet lock above.

### mapo_tyre_base · the crew's first base (alias tyre_yard)

- **Plan:** `world/floorplans/mapo_tyre_base.svg` / `.png`. No key.
- **Where.** Hapjeong-dong, Mapo-gu, on a service road just south of Yanghwa-ro, inside `hapjeong_gate_zone` **(decided here)**; about 6 minutes' walk from Hanbit Mart. The beats put it "in a Mapo gate zone" (PART_ONE_BEATS.md:398). Fictional, no real address.
- **Chapters.** 33 (leased with the ₩38,000,000 share), 63 (the featured bay), 65 (Kesh's invitation **(decided here)**), 85 (Dara's invitation **(decided here)**), and the crew's working days through 98.
- **Layout (decided here).** A 30 × 24 m concrete forecourt with oil stains behind a block wall and a 7 m sliding gate on the service road. West: a two-storey block (ground floor common room and kitchen, WC and shower, Sejin's medical corner; upstairs the "separate rooms" of the beats for Sera, Kesh and Dara, a duty room and a spare). East: a three-bay tyre shed under a 3 m canopy.
  - **Bay 1, the featured bay (ch063):** a raised roller shutter, the scarred worktable ("the Mapo worktable"), tyre racks and a plain pegboard.
  - **Bay 2:** gear, relays, charging; the crew's own van bought with the ch62 grants **(decided here)**.
  - **Bay 3:** Orrin sleeps here under the shed roof, not yet his garden (PART_ONE_BEATS.md:398).
  - The broad forecourt admits Orrin without a door gag during serious scenes (ch063).
- **Locks.** Taeo and Nib keep sleeping in the Ryu container home until ch99 (ch041, ch048, ch052, ch063; CODEX_SCRIPT_BRIEF.md:44). The rules wall, Grandpa at the container door, Minho's cake, the yard-fence poster, the co-op meeting and Iron Vow at the gate all belong to the Ryu yard (ruling C23).

### go_first · the GO FIRST building

- **Plan:** `world/floorplans/go_first.svg` / `.png` (four floors). No key, no script yet.
- **Where.** A four-storey building in the Hapjeong gate zone, two streets from Hanbit Mart (PART_ONE_BEATS.md:798): a former print works on a corner in Hapjeong-dong, about 150 m (2–3 minutes) from the mart **(decided here)**. Fictional, no real address.
- **Floors (beats ch99).** Ground: Eunchae's (fair rent), with its own street door, and the guild hall door. 2F: Sejin and Dara's clinic. 3F: rooms and offices (the crew room carries the three rules). Roof: Orrin's garden.
- **Decided here.** An external goods hoist on the east side (2.6 × 3.0 m deck) is Orrin's way to every floor and the roof. The ch100 party (the welcome cup, Granny Moon's cloth) is on the roof garden under a pergola with a long table.
- **The sign (ch100).** GO FIRST over the guild door: an open door with one footprint stepping out and three dots. Painted inside the door: "ANYONE CAN LEAVE. EVERYONE COMES BACK." Lettering is the letterer's.
- **Chapters.** 99 (Dr. Pyo at the door with a plant), 100 (the sign, the cup, the party, the last panel: the open door at night with the sign glowing).

### hapjeong_gate_zone · the gate advisory zone

- **What.** The GMA advisory zone declared in ch21 after the Hanbit Mart gate (G2) and the Seogyo-dong gate (G1) of ch1. Drawn on the city map as everything within 1 km of G1 or G2 **(decided here)**. Insurers drop buildings and rents fall (ch22).
- **Inside it:** Taeo's block, Hanbit Mart, Granny Moon's laundromat, the café by Hapjeong Station, Eunchae's gosiwon, the tyre base and the GO FIRST building ("in the Hapjeong gate zone", ch99). The Ryu yard and the AAO building are just outside it.
- **Sign.** From ch22 a GMA zone sign on the lamp post by Taeo's corner stop (see `taeo_street`).

## 4. Seoul: offices, gate sites and the wider city

### aao_office · Ability Assessment Office, Mapo branch (+ aao_ext, aao_lobby, aao_exam_hall, aao_practical_hall)

- **Keys.** `world/keys/aao_office/`: `key_wide.jpg` (from the south-east door), `key_reverse.jpg` (from Chae's chair), `notes.md`. **Plan:** `world/floorplans/aao_office.svg` / `.png` (Chae's room and the lobby inset).
- **Where.** The ground floor of a plain five-storey civic block (pale grey stone panels, blue-tinted glass) on a quiet side street off World Cup-ro in Seongsan 2-dong, Mapo-gu, 5 minutes' walk from Mapo-gu Office station (Line 6) (ch003). Fictional, no real address.
- **Exterior (`aao_ext`, ch003).** A flat concrete canopy over a four-wing revolving door of glass and brushed steel with a plain glass push door beside it; a bicycle rack; a planter of clipped boxwood; a pale blue blank sign panel above the canopy.
- **Lobby (`aao_lobby`, ch003–004).** A glass front with the revolving door and a side swing door; blue-white ceiling light; a low pale-wood reception counter with a blank number display; a ticket machine on a post; rows of linked blue-grey seats facing the counter; a TV high on the right-hand side wall (KNN 24 in ch4); a leaflet rack, a water dispenser, a potted ficus, green exit signs; the corridor to the assessment rooms at the back. A goods door for Orrin's registration (ch25) and a photo booth (Orrin's ID photo gag, ch25) are on the plan **(decided here)**.
- **Chae's room (key).** 5 m east–west by 7 m north–south. The south wall is a glass partition onto the corridor with the glass door at the south-east corner and a blank green exit plaque above it. A three-seat navy waiting bench along the west wall in the south-west alcove. Chae's pale-grey desk centred in the north half, her rolling chair behind it, two visitor chairs facing north. On the desk: two dark monitors, keyboard, plain files, the small flat silver hand-assessment plate on the visitor's right (east) side, two sensor wrist fobs in a tray. Tall filing shelves along the north-west wall. One broad east window with horizontal blinds.
- **Exam rooms (ch048).** `aao_exam_hall`: a new room in the same building: a north-wall clock, high east windows, spaced single grey desks, south double doors, a front collection table, navy seats, blank green exit plaques. `aao_practical_hall`: a ground-floor gym: south double entrance, an operator rail along the east wall, grey padded floor with a central lane, north equipment doors, blue-white strips, high west daylight. No gate.
- **Chapters.** 3, 4 (the assessment; the blind test), 21 (weekend duty; the ASK FIRST ruling), 23 (the archive of fragment kinds), 25 (Orrin's registration), 46 (Sera's registration; Pyo lobbying), 48 (written exam), 49 (Doyun's practical). Mentioned: 92 (Chae's promotion).
- **Colour script.** Blue-white #DCE6EB, slate shadows #A9B7C4, desk #B6C2CA, navy bench #40536A, exit plaque #5E806A (key).
- **Travel.** From Taeo's flat 20 min walk, or Line 6 Mangwon to Mapo-gu Office plus 5 min. From Hanbit Mart: Line 6 from Hapjeong two stops to Mapo-gu Office plus 5 min (about 15 min).
- **Contradiction.** C18 (ch021's "analogue gauge on a stand, two stools").

### awakened_cram_academy · the cram academy for the awakened

- **Where.** Noryangjin-dong, Dongjak-gu, Seoul's cram-school district (Korea JoongAng Daily) **(decided here)**. Fictional academy, no real address.
- **Look (ch048).** An upstairs classroom: west street windows, an east projection board, two ranks of folding desks either side of a central aisle, a vending alcove by the rear south stair door. Candidates queue to pay at a small table by the south exit. The narrow pavement below has blank academy placards.
- **Chapters.** 48. The written exam and the practical then happen at the AAO building (above).

### gma_building · Gate Management Agency, Seoul office (+ gma_hearing_room)

- **Keys.** `world/keys/gma_hearing_room/`: `key_wide.jpg`, `key_reverse.jpg`, `notes.md`. No plan.
- **Where.** Near Gongdeok station, Gongdeok-dong, Mapo-gu **(decided here)**. Fictional building, no real address.
- **Building (ch009).** An eight-storey grey stone-and-glass block above a broad plaza; about twelve wide granite steps to a glass front, a revolving door between two glass side doors; three flagpoles with plain colour-block flags; a blank stone name panel. A pale stone lobby with a security point (walk-through arch, X-ray belt, grey trays), a registration counter with a small photo corner, lifts to the upstairs corridor. The GMA works weekends.
- **Hearing room (key).** 8 m east–west by 11 m north–south. A one-step dais on the north wall with a long plain panel desk, exactly three high-backed chairs, three dark gooseneck microphones, blank name plates. A witness table and one small chair facing north. Two counsel tables farther south: Chae's at the west, Pyo's at the east, two chairs and a file stack each. A large dark presentation screen centred on the east wall. Two short public rows at the south end with a central aisle. The public double door at the south-west of the south wall and a staff double door at the north-west beside the dais, both with blank green plaques. High narrow west windows with blinds, pale blue-grey walls, muted oak dado.
- **Chapters.** 9 (the hearing; the ruling; Chae's open-gate list).
- **Colour script.** Walls #CED9E0, key #E0E8EC, shadow #98A8B6, oak #967F65, navy chairs #43576B, screen #25323E (key).
- **Contradiction.** C17 (ch009's 12 × 9 m room with one back door; the key wins).

### metro_maintenance_tunnel · the Line 6 maintenance spur (+ gate_stone_gallery)

- **Where.** An out-of-service maintenance spur off Line 6, under Seongsan-dong near Mapo-gu Office station **(decided here)**; the access stair is about 30 m back along the walkway from the staging area. G3 on the city map.
- **The tunnel (ch010, ch011).** A single concrete horseshoe tunnel about 5 m wide. From the staging end: old rails in a concrete track bed on the RIGHT; a raised walkway about 1.2 m wide along the LEFT wall, its kerb about 80 cm above the track bed. Cable trays and conduit both sides; a de-energised overhead line tied back. In the left wall ahead, the steel frame of a cross-passage, its door off and leaning beside it: the gate (E-grade) stands exactly inside that frame and spills a wedge of lavender light. A strip of yellow-and-black tape crosses the walkway 2 m in front of the frame. Behind the tape the staging area: a folding table with the base radio, Haein's second radio with a whip antenna, a stopwatch, a clipboard log, a thermos, Taeo's backpack; Haein's stool; two tripod work lamps; Sejin's upturned crate. The GMA warden's post at the stair foot. Trains run in the next tunnel about every five minutes; their rumble comes through the right wall.
- **Inside (`gate_stone_gallery`, ch011).** An open-sided ledge road about 3 m wide cut into a pale grey cliff: the cliff on the LEFT walking in; on the RIGHT a row of squat, very old squared stone struts holding up an overhanging rock roof, then a sheer drop to a valley of grey stone stacks under a LAVENDER NOON sky with a small hard white sun. About 150 m in the gallery bends left; beyond the bend a broad band of chalk-white stone runs through the cliff: the white stone (Nib: "IT'S THE SAME KIND", P07). The cracked strut before the white stone comes down in P30.
- **Chapters.** 10, 11.

### guro_pit · the Guro foundation pit (+ guro_pit_rim, guro_pit_street, guro_gate_inside, guro_side_gallery)

- **Plan:** `world/floorplans/guro_pit.svg` / `.png` (site plan, the street and hoarding, the side-gallery inset). The basin inside is the inset on `otherside_map.png`.
- **Where.** Guro-dong, Guro-gu, among older four-storey factory blocks and new glass office towers: the old Guro industrial district that became the Guro Digital Complex (ch013). Fictional site, no real address. G5 on the city map.
- **The pit (ch013, locked).** About 60 × 40 m and 12 m deep. Walls of rusty steel H-piles with timber lagging; two levels of steel struts and corner braces wall to wall at about 4 m and 8 m; an idle tower crane in the north-west corner; a gravel truck ramp down the south wall (Dokgo's flatbed at its top, the white Ryu van at its foot). Grey gravel and mud, puddles, rebar bundles, formwork. **The gate** (C-grade) near the middle of the north wall: a door-height slit inside a square frame of scaffold tubes on four concrete blocks, inside a 10 m ring of orange safety mesh open on its south side. Outside the ring, left to right from the ramp: Ryu's white canopy and table (base station, cable drum, charging rack; Taeo's chair faces the gate, 8 m from it) with the white cable entering at the frame's lower left; Dokgo's table 4 m to its right; the porters' staging area with a jacket rack made of a scaffold tube on two trestles; Sejin's small white first-aid tent with a plain green cross near the ramp.
- **Rim (`guro_pit_rim`, ch013).** The general contractor's site office on the south-east rim: three white containers stacked two high, the top one glass-fronted to the pit.
- **Street (`guro_pit_street`, ch017).** The street along the site's south side, east–west: the tall steel hoarding with a sliding mesh gate at the top of the ramp near its west end; the hoarding's street face carries a huge glossy render of the apartment tower being built and a smiling family on a balcony (the developer's logo a blank block). Taeo and Nib sit on the kerb a few metres east of the gate, facing south, Nib on Taeo's left.
- **Inside (`guro_gate_inside`, ch013–017).** THE LANDING, a broad ledge of pale slate-grey slab with the first relay post; THE BASIN beyond, a vast quarry of stacked grey slab terraces cut with low black galleries; every surface slopes about 10° down to the LEFT looking in. GREEN DUSK sky, violet shadows. The survey line: white cable with a blue band every metre, a relay post every 50 m (a short grey tripod with a box, a speaker grille, a coiled handset, a white status lamp). The staging shelf 80 m in; the lower gallery's arch on its left (unsurveyed, 40 m shorter); the upper run; the forward camp about 300 m in; stake 14 with Kett's mark; the rubble wall at stake 20. See the inset on `otherside_map.png`.
- **Side gallery (`guro_side_gallery`, ch015–017).** A low chamber about 6 × 4 m, ceiling 1.8–2.2 m, fractured pale grey stone, lit by hard bars of green-dusk light from ceiling fissures and by headlamps; the slab that pinned Kwak's shins; the side-wall fissure the eyeless scuttler uses.
- **Chapters.** 13–17. Hoarding seen again in 18 P01.
- **Locks.** Eight numbered Dokgo porters; Dami 07 outside, Kwak 08 missing (continuity report). Relay radio works because the cable is whole; supplemental survey stations are 40 m apart.
- **Note.** ch017's earlier pit description was reconciled to the locked ch013 geometry by the continuity pass (ch017 `_status`).

### guro_site_news · the ch11 news clip

- Seen only as a KNN 24 clip (ch011): a different Guro construction site at night, a corrugated hoarding with blank sign blocks, a chained gate, violet gate glow in the pit, sodium site lights and one harsh white work light. Not the ch13–17 pit.

### guro_hospital_er · Kwak's emergency department

- **Where.** A general hospital in Guro-gu, a short walk from a Line 2 station (ch018). Fictional hospital, no real address; pin 11 in Guro-dong.
- **Look (ch018).** A waiting area of linked pale-blue plastic chairs, a wall TV high in a corner, a reception window, wide double doors; a treatment corridor of curtained bays (pale mint curtains on ceiling tracks), each with a bed, a monitor on an arm, a wall oxygen outlet.
- **Chapters.** 18 (19:12 arrival). Kwak is discharged Saturday at 14:00 with a cane (continuity report).

### seoul_line2 · Line 2 over the Han

- A Line 2 car crossing the Han on the Dangsan Railway Bridge between Dangsan and Hapjeong at night: long bench seats, grab poles and straps, big windows full of black river and the lit far bank. Line 2 runs above ground over the river here; Sindorim to Hapjeong is four stops (ch018; Wikipedia, Dangsan Railway Bridge).
- **Chapters.** 18.

### seongsan_redevelopment · the emptied villa block (+ salt_iron_cave)

- **Where.** A fictional redevelopment block in Seongsan 2-dong, Mapo-gu (ch022). G6 on the city map.
- **Street (ch022).** A short street of emptied four-storey red-brick villas due for demolition: windows taped or boarded, abandoned furniture in a car park, one red spray-painted circle-and-cross on the nearest wall, a blue hoarding and a parked excavator at the far end. The gate (D-grade) opened in the basement storeroom of the middle villa: steps behind orange GMA barriers, a bare concrete corridor with pipes, the storeroom's steel door open and the slit inside its frame. Child-height pencil marks climb the frame. Haein's radio table against the corridor's left wall. No survey cable on this short job: radios do not cross, the two/three knock is the fallback.
- **Inside (`salt_iron_cave`).** A vast cave of white and pale-grey salt crystal veined with rust-red iron, black-green brine pools, orange-flagged survey pins; a sinkhole high overhead opens on a saturated ACID LIME-YELLOW NOON sky with a small hard white sun; violet shadows. The boss territory is a field of iron spikes in the salt.
- **Chapters.** 22 (salt-iron; window 2; the invitation declined that night on the roof).

### stone_survey_rim · two paid stone-survey jobs (+ stone_survey_inside)

- **Where.** Not given in any script. Two separate paid jobs on successive working days (ch023); not pinned on the city map.
- **Job one.** A tiled service basement with pipe racks; inside, broken limestone steps under a LAVENDER NOON sky.
- **Job two.** A disused loading shed with a ribbed steel wall and a concrete dock; inside, grey stone shelves under ROSE-PURPLE CLOUD.
- Each has a framed door-height gate, a Ryu radio table and intact white cable with blue bands. Both yield ordinary stone: +0%, +0% (P11). Only the landing areas are shown.
- **Chapters.** 23.

### sewer_gate_rim · the sewer gate (+ sewer_gate_inside)

- **Where.** A Mapo maintenance chamber (ch023), under Mangwon 1-dong near the riverside **(neighbourhood decided here)**. G8 on the city map. (Older world files called it `mangwon_storm_drain`.)
- **Rim (ch023).** Damp grey concrete, a fixed ladder, portable white work lamps, a survey table beside the framed gate. Taeo stays on the dry human-side staging platform.
- **Inside.** Low bricklike mineral vaults, shallow dark water, copper-coloured moss rooted round an exposed anchor seam; through broken vaults a wrong-colour LAVENDER sky. No sewage monster, no boss fight.
- **Chapters.** 23 (copper moss, window 3).

### terrace_gate_rim · Terrace Gate (+ terrace_gate_outer, terrace_gate_east)

- **Where.** A fenced, disused freight hardstanding with low warehouses, on the site of a former clay-storage yard, in the quasi-industrial blocks of Mullae-dong, Yeongdeungpo-gu **(district decided here)**. Fictional lot, no real address. G7 on the city map.
- **Staging (ch023, ch030–032).** Dusty ochre gravel; a grey contracts cabin at the west with a ramp and an outside table. The **east connection**: the near door-height slit in a bolted scaffold-tube frame on concrete feet, facing west, with an orange cordon; the raid canopy and medic station to its left (south-west), the white cable with blue bands feeding its lower south-west corner; a clear return landing in front. The **central connection** is a separately licensed frame farther across the same apron, its own pocket; each local connection closes on its own boss (STORY_BIBLE F17; ch030). A route board with abstract contour lines (ch023).
- **Outer edge (`terrace_gate_outer`, ch023).** A broad outer landing toward clay terraces stacked round a void under a GREEN DUSK sky; narrow climbing shelves near the landing; the main central deposit far off. Sampling only (terrace clay).
- **East terrace (`terrace_gate_east`, ch031–032).** Rust-red clay terraces with grey cap stone over a dark violet void, GREEN DUSK sky. The threshold landing is broad and firm; the shelves are locally level. Advancing, the cliff is on the RIGHT and the open drop on the LEFT. Low stair shelves rise to the 150 m mineral shelf; the deposit is a pale seam on a higher side shelf reached before the ram's run-up. At 200 m a sheltered ledge-rest recess in the right cliff (the dreams; Nib carves Kett's mark on a ledge stone, ch31) opens onto the inside end of a narrow straight stone bridge; the boss (the stone ram) patrols beyond a square clay buttress at the far end and charges straight down the bridge. Orrin braces on a broad stable shelf beside an oblique projecting cliff face; Nib's outboard escape pocket is behind his shoulder; the cable follows the inland edge with relays every 50 m (ch032). See the inset on `otherside_map.png`.
- **Chapters.** 23 (outer edge), 29 (planning), 30 (contracts; the rim brace; "KNOCK WHEN YOU WANT ME BACK"), 31, 32.

### sinjeong_arcade · the Sinjeong underground arcade surge (+ sinjeong_street, sinjeong_command, sinjeong_f_stair, sinjeong_f_landing, sinjeong_pharmacy, sinjeong_stockrooms)

- **Plan:** `world/floorplans/sinjeong_arcade.svg` / `.png` (street level and underground). No key.
- **Where.** A fictional underground shopping arcade by Sinjeong station (Line 5), Sinjeong-dong, Yangcheon-gu (ch034; Wikipedia, Sinjeong station). Not a real station plan; never invent a station exit number (ch038). G9 on the city map.
- **Street (`sinjeong_street`).** A broad road running east–west. On the NORTH pavement: the F stair, the GMA command tent and casualty bay 8 m WEST of it, Seoryun's van farther west, and the main descent (Seoryun's sector stairhead) farther west again. The SOUTH kerb is the press line. A collapsed lightwell EAST of F, where one of the seven gates' expanded mouths breaks out (ch36) and three hounds come from the east (ch37). Concrete barriers protect Haein and Sejin (ch037). Work lamps cold white; red only for incident warnings.
- **Command (`sinjeong_command`, ch034).** A white pop-up tent, a folding map table, two speakerphones, rugged tablets, clipboards, cable drums; the public map is paper.
- **F stair (`sinjeong_f_stair`, alias `sinjeong_stairwell`).** A rectangular concrete hood on the north pavement, opening north; 14 steps down to the SOUTH, railings both sides. Taeo's radio base on a narrow trestle by the WEST railing at the street top; the white cable with blue metre bands runs down the west edge. A small blue child's slip-on trainer with a white heel lies on step 9 until ch35 P24, then sits on the trestle. At the foot, a 3 m square stair-side apron; then the steel fire door, hinged EAST, opening south into the landing and wedged against its east wall (a steel hold-open wedge beside the jamb). Taeo's lowest point is the apron (ch37 P32a); he never goes past the door.
- **F landing (`sinjeong_f_landing`, alias `sinjeong_arcade_f`).** 3 m square, south of the door: an overhead concrete lintel, an east pipe chase, a low crawl strip on the west. A crack in the displaced east partition exposes the gate-side anchor cluster two steps away ("LEAVE IT", ch37). Orrin holds the collapsing ceiling here facing south; to retreat he backs north through the door and up the stairs (ch037–038).
- **Corridor F (`sinjeong_arcade`).** From the door, service corridor F runs SOUTH 20 m to a T: the pharmacy WEST, the food court EAST. Grey tile, cream upper walls, exposed overhead pipes, low red emergency lamps. In ch35 the expansion of food-court Gate 3 drives gate-side stone across F's north arm just above the T; the cable survives in a floor recess under it.
- **Pharmacy (`sinjeong_pharmacy`, ch035).** The T's west branch: a wide public doorway facing EAST under a bent security shutter held 1.7 m up; the counter along the NORTH wall with blank medicine shelves behind; a low waiting bench on the SOUTH wall; a narrow WEST rear door to its stockroom. No street window. Eighteen civilians.
- **Stockrooms (`sinjeong_stockrooms`, ch036).** The pharmacy stockroom (blank cartons on north shelves); its NORTH shared service door to the clothing stockroom (wheeled rails of bagged coats; six more civilians); at the clothing room's EAST end a push-bar exit onto a narrow dogleg, NORTH then EAST round a cream concrete pier, back into F north of the stone wall. Smoke drawn toward that exit is Nib's clue.
- **Gates.** Seven, all deeper than F's first landing: three in the food court, four in the shopping corridors; vertical black-violet slits with cold rims, never portals filling doorways (ch034). Only Gate 3 (food court) is numbered in a script; the plan's other numbers are decided here. Inside a food-court rim the sky is a wrong LAVENDER (ch035 P30).
- **Chapters.** 33 (the alert, hook), 34–38, 39–40 (dawn on the north kerb between F and the tent), 41 (opens on the same kerb).
- **Locks.** All rescue work stays on the Earth side of the thresholds: no return marks in ch34–38. The radio works because the Ryu cable stays whole (grey relay tripods every 50 m; the bypass loop through the stockrooms from ch36). Knocks through the steel door: two outside = come back, three inside = coming.

### seoryun_base · Seoryun's rescue depot (+ exchange_gate_inside)

- **Where.** On the riverside in Tojeong-dong, Mapo-gu, about 600 m west of Mapo station (Line 5) **(decided here)**. Fictional depot, no real address. Pin 16 and G10 on the city map.
- **Depot (ch041).** A modest rescue depot: a concrete drill court in front of a low grey equipment shed; a hose rack west, a shaded rope trestle north, a padded barrier lane east, a briefing table beside the south exit; a fenced gate exercise bay adjoining the shed. No sponsor backdrop, stage or audience.
- **Inside (`exchange_gate_inside`).** Supervised exercise territory through the fenced bay: chalky pale ridges, low rust-brown mineral shelves, LAVENDER NOON sky, violet shadows; white cable with blue bands and grey relays every 50 m. The boss stays alive; it is an approach sweep. Source of the exchange-gate sample (window 4).
- **Chapters.** 41 (the Thursday exchange, 9 AM to late afternoon).

### long_night_memorial · the Long Night memorial plaque

- **Where.** Seonyudo Park, the island park in the Han at Yanghwa Bridge, Yanghwa-dong, Yeongdeungpo-gu (Wikipedia, Seonyudo) **(the memorial's site is decided here)**. Pin 17.
- **Look (decided here).** A low granite wall with a bronze plaque among the park's old concrete water-tank walls; the plaque lists the Long Night's losses, including "ANOMALOUS ENTITIES: 0 casualties" (STORY_BIBLE P13). Granny Moon lays a flower.
- **Chapters.** 42.

### seogang_camp · the Seogang camp site (nine years ago)

- **Where.** The riverside below Seogang-dong, Mapo-gu, near the north end of Seogang Bridge **(decided here)**. Pin 18 and G12.
- **What.** The gate-site camp where Taeo's father (a contracted porter) and mother (a camp cook) died in the Seogang camp collapse, a job subcontracted three times down to the cheapest bidder (STORY_BIBLE.md:74). Seen in the ch43 flashback (muted palette) and in the TV ticker "NEGOTIATIONS ONGOING". Today an ordinary riverside path with no marker **(decided here)**.
- **Chapters.** 40 (the porter story), 43 (flashback); the father's porter ID comes back in 44.

### yoon_family_flat · the Yoon family flat (nine years ago)

- **Where.** A small flat in Sangsu-dong, Mapo-gu **(decided here)**. Pin 19. Flashback only, muted palette.
- **Chapters.** 43 (Father leaves for the camp; Taeo, 14, minds baby Haru).

### film_crew_gate · the film-crew D-grade gate

- **Where.** A studio backlot in the Digital Media City area of Sangam-dong, Mapo-gu **(decided here)**. G11.
- **What.** A film crew ignored the warnings inside a D-grade gate; Sera's first job, done at a paid emergency rate (beats ch47).
- **Chapters.** 47.

### exhibition_arena · the National Gate Skills Exhibition (+ exhibition_service_corridor, exhibition_draw_stage)

- **Plan:** `world/floorplans/exhibition_arena.svg` / `.png` (local frame). No key.
- **Where.** Seoul World Cup Stadium, Seongsan-dong, Mapo-gu, by World Cup Stadium station (Line 6) (Wikipedia, Seoul World Cup Stadium) **(venue decided here; beats ch58: "the stadium erupts")**. A real venue; the event and every installation are fictional. Pin 21.
- **The arena (ch056).** A grey padded course floor on a protective deck over the pitch, below tiered stands. The operator boxes stand behind the near clear safety barrier with the service exit behind them; competitors run AWAY from the boxes toward the far targets. The VIP enclosure is high on the opposite side. Semifinal set: two parallel identical lanes, each with a pivot bridge, a pendulum and a weighted exit shutter. Other installations: Sera's archery range at end A, Sunline's aerial rig and the stage, big screen and press pit (with the lighting-rig truss) at end B, BangBang's fan block in the opposite stand **(placements decided here)**.
- **Service corridor (`exhibition_service_corridor`, ch052, ch056).** An under-stand corridor adjoining the operator box: cream concrete, off-white walls, exposed grey conduit, fluorescent strips, an equipment trestle, wide service doors, a waist-high queue barrier; daylight from the open loading door at the far end.
- **Draw stage (`exhibition_draw_stage`, ch056).** A small arena-side platform with a broad access ramp for Orrin, a blank bracket board at the rear, the officials' desk at stage right.
- **Chapters.** 49 (the bracket draw), 50–61. 51: Taeo in the operator box; 54: Baek in the VIP box; 57: the chant and "NIB. LEFT WALL. TAKE THE HIT."; 58: Haru's missed calls in the operator box; 59–61: the stage, the mic, the rig, the photo.
- **Locks.** Taeo never runs the course. No real sponsor, team or stadium signage; every board is blank.

### national_assembly · the National Assembly (TV only)

- **Where.** The National Assembly in Yeouido, Yeongdeungpo-gu (real; National Assembly station, Line 9). Seen on TV: the bill fails in committee (ch47), Pyo's lobbying (ch66), Pyo smiling on the steps after the first reading (ch70). Pin 22.

### meridian_tower · Meridian Tower

- **Where.** A fictional glass tower in Yeouido, Yeongdeungpo-gu, the Seoul Meridian Guild's headquarters **(decided here)**. Pin 23.
- **What.** Baek's office: the gold-edged invitation (ch81 hook), the absorption offer (ch82). Navy and silver, efficient, expensive (Baek's palette, ch035).
- **Chapters.** 81, 82.

### Video-only places

- `doyun_lecture` (ch012): a dark lecture hall with a low stage, one cool white spot, a large screen with a plain grid of pale lines and one circle.
- `archive_rescue_site` (ch036): last year's tablet footage, an anonymous grey gate-site underpass with concrete columns, an olive rescue crew and barriers, desaturated cool palette with olive as the remembered colour. No real location.

## 5. Haeseong (fictional port town, 3 hours from Seoul)

Haeseong is fictional (STORY_BIBLE.md:183): "the grandparents' small port town, 3 hours away by bus. Its fishing grounds are fenced off by a sea gate that never closes." It is not on the city map; an arrow on `city_map.png` points to it.

### haeseong_port · the harbour, the quay, the breakwater and the sea gate (+ haeseong_breakwater)

- **Keys.** `world/keys/haeseong_port/`: `key_wide.jpg` (from the bus-stop kerb looking south-east to the water and the gate), `key_reverse.jpg` (from the breakwater looking north-west), `notes.md`. **Plan:** the Haeseong site sketch on `world/floorplans/grandparents_house.png`.
- **Layout (key, ch008).** Land to the north, water to the south. An east–west shoreline road behind a low concrete quay. The bus shelter with a dark blank timetable panel and a wooden bench on the quay-side pavement at the north-west, where Grandpa parks his cardboard cart. THREE idle small white-and-navy boats moored along the quay with ropes and floats; a blank pale warning board on the quay; low weathered houses and closed fishery sheds along the north side of the road, a wooded hill behind. A scrap dealer's yard in one of the closed sheds a few minutes east along the road (corrugated iron, strapped bales of cardboard, a steel platform scale with a small red digital readout on a post). The stepped lane climbs the hill from the road to the grandparents' house: about 8 minutes with the cart (ch008).
- **The breakwater (`haeseong_breakwater`, ch008).** Runs south from the west end of the quay: concrete, grey tetrapods on the seaward side, a parapet along the outer edge (chest-high on Grandpa) with a flat walkway inside, a small white light tower at its tip. Grandpa's place is about two-thirds of the way out, where a corner of the parapet is chipped. Locals call it "the wall".
- **The sea gate.** Offshore SOUTH of the harbour mouth: a narrow upright black-violet slit, its base at the waterline, about door-height against the boats, a thin cold white-cyan rim, no fog, inside a ring of SIX muted orange buoys. Never inside the harbour; never entered in Part One. The co-op asks for a survey within two years (ch84).
- **Chapters.** 8 (Sunday noon; the wall), 9 (P01, the departure light), 43 (flashback), 62 (Taeo visits Haru), 96 (the re-run day).
- **Colour script.** Sky #CADCE2, sea #6C8B97 / #486773, concrete #ACA99B, boat white #D4D8D2, boat navy #3C5366, buoys #B86D50, gate #1A1026 with rim #D7F2F3 (key). Cool clear sea light at noon.

### haeseong_bus · the intercity coach

- A white intercity coach with one plain teal stripe and no lettering; high-backed blue-grey fabric seats with white headrest covers, curtains tied back, two-and-two seating; at night the reading lights off and the window a black mirror (ch008, ch009). Four coaches a day to Seoul; the last leaves at 16:40 (ch008 P53). About 3 hours.
- **Seoul end (decided here):** Dong Seoul Bus Terminal by Gangbyeon station on Line 2 (about 40 minutes from Hapjeong by Line 2).
- **Chapters.** 8, 9, 96 (the 5 a.m. bus to Haeseong from Yeoju on the contest's rest day, and back at night; the timings are decided here: about 3 hours each way).

### grandparents_house · the grandparents' house

- **Keys.** `world/keys/grandparents_house/`: `key_wide.jpg` (from the courtyard threshold looking north), `key_reverse.jpg` (from the kitchen looking south), `notes.md`. **Plan:** `world/floorplans/grandparents_house.svg` / `.png` (house, courtyard and the Haeseong site sketch).
- **Where.** An old single-storey house on the hill north of the harbour road, up the stepped lane (ch008).
- **Layout (key, ch008).** The main room 5 m east–west by 6 m north–south, dark timber beams, a warm cone pendant over the low table. South: glazed wooden sliding doors onto a 3 m concrete courtyard (three pots along the east wall, a narrow wooden bench on the west, a plain grey metal double gate centred in the south wall); shoes on the stone step; a peg for jackets and Grandpa's cap. North wall: the worn kitchenette (sink at the west end, two-burner hob in the centre, a small cream fridge at the north-east, cutting board, cleaver, wall cabinets). ch7's kitchen corner is its east end by the east window, with the fishing float on a hook. West wall: the small dark TV on its low cabinet with a plant, Haru's dinosaur books and a small framed photo (the ch1/ch6 picture). North-west: the bedding alcove. East wall: one two-pane window with cream curtains. The courtyard wall hides the sea: the gate is NOT visible from inside the house.
- **The table.** The low wooden table with five floor cushions, five rice bowls, chopsticks, an oval fish platter, two side-dish plates, a metal teapot (ch8 lunch).
- **Seating lock (ch8 P20–P41).** Grandma at the WEST end (back to the TV cabinet, nearest the sink); Grandpa at the EAST end (back to the east window, facing the TV and the photo); Haru (by Grandma) and Taeo (by Grandpa) on the SOUTH side, backs to the sliding doors; Nib alone on the NORTH side, back to the kitchenette, facing the way in, kneeling upright (ch008).
- **Chapters.** 7 (the kitchen corner only), 8 (Sunday lunch), 21 (video image), 30 (video call: the purple arm), 43 (flashback: the broadcast on the old TV, Taeo's tears on Haru's head), 62, 96.
- **Colour script.** Warm amber key #D3AB73, walls #D2BE9B, timber #9A7750, brown shadow #7F674D, steam #E9E4D4, curtains #C5BB9F (key; ART_BIBLE A4 grandparents' kitchen).

### haeseong_school · Haru's school

- **Where.** Haeseong's school, a few minutes from the harbour road **(decided here)**. No key.
- **Chapters.** 59 (a video call from the school corridor: "YOU SAID YOU'D COME."), 96 (the re-run of the dinosaur presentation: velociraptors, feathers, the T. rex arms).
- **Look (decided here).** A small rural school: a long corridor with a polished floor, children's drawings on the walls (blank shapes), a classroom with a low stage and a projector screen.

## 6. Out of town

### chungju_river_gate · the Chungju underground river (+ chungju_gate_site, chungju_gate_staging)

- **Where.** Chungju, North Chungcheong Province: a fictional fenced service cutting by the river (ch063; ch071 calls the staging ground "riverside"). An A-grade gate. Dong Seoul to Chungju is about 1 h 33 by intercity bus (bus timetable, asamaru).
- **Staging (`chungju_gate_site`, `chungju_gate_staging`).** A fenced service cutting; a short concrete access tunnel ends at a steel scaffold frame round a door-height violet-black slit. Outside it, left looking in: the white consortium canopy and map table; right: Sejin's medical canopy; van parking in the open cutting behind; Haein's grey base station beside the frame (ch063). The gravel floor of the cutting is the staging ground: a scaffold rim brace, a folding radio table under a white canopy, ambulance access behind it; the Ryu cable enters at the brace's foot (ch071). Ordinary daylight reaches the tunnel mouth; work lamps light the final approach.
- **Inside (ch063, ch071).** NO SKY: an unbroken low stone ceiling over a broad underground river. From the entry landing the river flows from the distant upper right toward the lower left (downstream); a walkable near-bank survey shelf follows it upstream, so walking upstream the water is on your LEFT and the wall on your RIGHT (ruling C24). Recessed stone signal posts stand above old flood lines, with scored channels and paired sockets, unlit at first ("the same hand", ch66). A carved settlement sign lies on the first shelf, away from the water. Marker 9 is farther upstream, unseen in ch63. Channel B is a recessed run on the shelf's water side under a low rock lip; a higher dry alcove connects back to the shelf (ch071). Portable white survey lamps key the slate stone; reflected violet gate light; ink-dark water, muted teal, wet violet shadows. Ryu cable with grey relays every 50 m. See the inset on `otherside_map.png`.
- **Chapters.** 62 (the hook: Chae's call), 63 (the consortium; river stone), 64 (echo coral from a quick consortium job), 66–74, 77–79 (the loop; the shot; Ilan's cylinder in the debris).
- **Locks.** Never draw stars, a horizon or a sky. The predator never knocks (P17).

### sera_hospital · where Sera is treated

- **Where.** A general hospital in Chungju city, within the hour Sejin gives her (ch71 hook) **(decided here)**. No key.
- **Chapters.** 72 (the corridor: "YOU TRUSTED A WINDOW OVER MY EYES."), 75 (the apology).
- **Look (decided here).** A plain ward corridor, pale green walls, a window at the end; her room with one bed, the arm in a brace.

### yeoju_anchor_field · the Yeoju anchor field (+ yeoju_demo_ring, the depot)

- **Where.** On the Namhangang floodplain east of Yeoju town, Gyeonggi Province **(decided here)**. Seoul Express Bus Terminal to Yeoju is about 1 h 56 by bus (bus timetable, asamaru; rome2rio).
- **The field (ch093).** Five independent door-height gates, A to E, in scaffold safety frames, west to east along a gravel apron; A is first and westmost. The supply depot is north; the operator canopy south-west, outside every gate; the medical shelter south. The A/B relay pair shares the exterior apron: it is not a walkable tunnel between pockets. The outer frames carry bolt-on steel knock plates; frame tags are blank until lettered. Pocket skies: not given in any script yet.
- **Demo ring (`yeoju_demo_ring`, ch093).** A public gravel training ring outside the depot, padded boundary on its east side, spectators on the west. Iron Vow's displacement demo (ch92 hook). Not inside a gate.
- **Chapters.** 83 (described), 84 (the pre-contract survey: field ore), 92 (the demo), 93 (dawn: Taeo knocks twice on the first frame; three knocks answer), 94 (the depot's Venn anchor fault; the displacement at threshold B), 95, 97 (the final territory, gate E **(decided here)**), 98 (the board: WINNER). 96: Nib meets Taeo off the bus at night.
- **Locks.** Taeo stays outside at the operator canopy and manages two thresholds. Knocks: two outside = come back, three inside = coming.

### provincial_clinic · the dialysis clinic

- **Where.** A small-town clinic in Yeoju-si, near the field's supply route **(decided here)**: its dialysis machines run on processed anchor fragments supplied by Venn Logistics (ch87), the same supplier whose anchor fails at the Yeoju depot (ch94).
- **Chapters.** 87; the ch100 hook call (two patients in danger).
- **Look (decided here).** A low two-storey clinic, a bright ward of reclining dialysis chairs, steel canisters with a blank supplier logo (the letterer adds VENN LOGISTICS only where the script names it).

### Unlocated jobs

- The echo-coral job (ch64), the unrelated site where a modified anchor fails (ch88) and the two stone-survey jobs (ch23) have no site in any script. Do not pin them; give them a site only when a script needs one, and add it here.

## 7. The other side

Drawn on `world/otherside_map.png` (top band). The other side is reached only through contact windows (invitations, STORY_BIBLE §4); nobody from Seoul walks there in Part One. Region positions are **decided here** so Part One reads consistently; Part Two (THE OTHER BANK) may redraw the edges.

| Region | Who | What we know | Source |
|---|---|---|---|
| **The watch country** | Nib | Slopes and walls where goblin scouts keep watch posts along **the old line** of posts and relay stones | STORY_BIBLE.md:37; beats 165, 814 ("THE OLD LINE") |
| `nib_post` · Nib's post | Nib | A wall of rough fitted stones on a slope, chest-high on Nib, one crooked tree behind it, the lower path winding below, a pale white outcrop far off (ch021 flashback, desaturated, soft-edged) | beats 91 (ch4: "WALL HERE. TREE BEHIND IT. YOU COULD SEE THE LOWER PATH. AND THE WHITE BIT."); ch021 |
| Kett's post | Kett, Nib's relief | The next post up the line; "someone was coming to take over" | beats 165; Kett's mark, the three-line fork |
| **The white bit** | — | A forked pale outcrop on the lower path below Nib's post. The tunnel gallery's white stone is "the same kind" (ch11 P07); Sera's map shows the same landmark: "HE LEFT FROM HERE" (ch46) | STORY_BIBLE P07; beats 192, 502 |
| **Sera's river settlement** | Sera, Ilan | A river settlement with a carved settlement sign (ch46 map; the Chungju stills, ch62). Ilan left from the white bit "for responsibilities"; his refuge lies beyond, unmapped (ch80) | STORY_BIBLE.md:236–240 |
| **The shared region** | Part Two | Where the watch country, the white bit and the river meet | STORY_BIBLE P07 |
| **The moss-sky uplands** | Orrin | "A huge, slow shape stirring under a sky full of moss" (ch23 window); he carried for an army that never said thank you (ch24) | beats 316, 324 |
| **The far cliffs** | — | Window 2's winged silhouette, far away: DECLINED (ch22) | beats 306 |
| **The signal halls** | Kesh | Signal stones by an underground river **(decided here)**; the lost communication craft Kesh wants to rebuild. The Chungju relay stones are "the same hand" (ch66, a style clue, not proof) | STORY_BIBLE.md:242–246; beats 619 |
| **The field country** | Dara | Field surgeons **(decided here)**; Tal (Part Two) | STORY_BIBLE.md:248–251 |

**Seams.** A summon seam opens in Seoul where Taeo issues the invitation (cyan curves on the map):
- window 1, Nib: `taeo_flat` (ch1);
- window 2, declined: `ryu_yard_roof` (ch22);
- window 3, Orrin: `taeo_flat` (ch23 window, ch24 arrival);
- window 4, Sera: the Ryu container home at `ryu_practice_yard` (ch45 rules and invitation, ch46 arrival);
- window 5, Kesh: `mapo_tyre_base` (ch65) **(decided here)**;
- window 6, Dara: `mapo_tyre_base` (ch85) **(decided here)**.

## 8. Borderland pockets and the route-alignment windows

**Pocket skies** (the sky inside a gate is always the wrong colour). A sky no script gives stays open; the first script that enters sets it, and this table records it.

| Pocket (id) | Grade | Sky | Fragment kind | Chapters | Source |
|---|---|---|---|---|---|
| `gate_stone_gallery` (metro tunnel) | E | lavender noon, small hard white sun | stone (the white stone) | 10–11 | ch011 |
| `ryu_training_gate_inside` | training | green dusk, no sun | — (the snail; never cleared) | 12 | ch012 |
| `guro_gate_inside` | C | green dusk (teal-green to pale acid green) | — (Kett's mark at stake 14) | 13–17 | ch013, ch017 |
| `salt_iron_cave` | D | acid lime-yellow noon, small hard white sun | salt-iron | 22 | ch022 |
| `stone_survey_inside` ×2 | — | job 1 lavender noon; job 2 rose-purple cloud | stone again (+0%) | 23 | ch023 |
| `terrace_gate_outer` / `terrace_gate_east` | C+ | green dusk | terrace clay (ch23); bridge-boss horn (ch32) | 23, 31–32 | ch023, ch031 |
| `sewer_gate_inside` | — | wrong-colour lavender through broken vaults | copper moss | 23 | ch023 |
| Sinjeong arcade pockets ×7 | — | wrong lavender (Gate 3, food court) | arcade glass | 34–38 (45) | ch035 |
| `exchange_gate_inside` | supervised | lavender noon | exchange-gate sample | 41 | ch041 |
| `chungju_river_gate` | A | NO SKY: an unbroken stone ceiling | river stone (ch63); echo coral (ch64, a separate quick job); flowstone (ch64, decided here) | 63–79 | ch063, ch071 |
| Yeoju gates A–E | — | not given yet | field ore (ch84 survey); levee silt and reed glass (decided here) | 84, 93–98 | ch093 |
| Hanbit Mart gate (G2) | E | never entered | — | 1 | ch001 |
| Film-crew gate (G11) | D | not given | — | 47 | beats |
| Haeseong sea gate | — | never entered | — | 8 | STORY_BIBLE.md:183 |

**Route-alignment windows** (STORY_BIBLE.md:146–156). New kinds raise [ROUTE ALIGNMENT]; at 100% one contact window opens and the meter resets. Two new kinds (+50% each) for windows 2–3; three (+34/33/33%) from window 4. A repeat kind adds 0% (F05); a refusal or a timeout uses up the window (F04).

| Window | Kinds | Where they came from | Answered by | Seam |
|---|---|---|---|---|
| 1 | free emergency first summon | — | Nib (watch country) | ch1, taeo_flat |
| 2 | stone (ch19) + salt-iron (ch22) | tunnel gallery; salt-iron cave | DECLINED (winged, the far cliffs) | ch22, ryu_yard_roof |
| 3 | terrace clay + copper moss (ch23) | Terrace Gate outer edge; the sewer gate | Orrin (moss-sky uplands) | ch24, taeo_flat |
| 4 | bridge-boss horn (ch32) + exchange-gate sample (ch41) + arcade glass (ch45) | Terrace east; Seoryun's depot; Sinjeong | Sera (river settlement) | ch45–46, the Ryu container |
| 5 | river stone (ch63) + echo coral (ch64) + **flowstone** (ch64, decided here) | Chungju river gate; a quick consortium job | Kesh (signal halls) | ch65, mapo_tyre_base |
| 6 | field ore + **levee silt** + **reed glass** (ch84, decided here) | the Yeoju field survey | Dara (field country) | ch85, mapo_tyre_base |

The third kind of window 5 and the two Yeoju kinds of window 6 are named here because the beats name only one or two (ruling C20). Writers may rename them in the scripts, but each window must still integrate three new kinds before it opens.

## 9. Travel table

Walking pace about 75 m a minute on real street lengths with a 25% detour; Line 6 and Line 2 at about 2 minutes a stop. Times are door to door.

| From | To | Time | How |
|---|---|---|---|
| taeo_flat | Mangwon station | 7 min | walk north up the bus street (ch003) |
| taeo_flat | camping_store | 3 min | walk north (ch019) |
| taeo_flat | moon_laundromat | 7 min | walk: the alley, then lanes south-east |
| taeo_flat | hanbit_mart | 20 min | walk via the laundromat and the Hapjeong-dong lanes; or the green bus (10 min) plus a short walk |
| taeo_flat | ryu_practice_yard | 12 min | walk west (ch010) |
| taeo_flat | mangwon_riverside | about 12 min | walk south-west |
| taeo_flat | aao_office | 20 min | walk (ch003); or Line 6 Mangwon to Mapo-gu Office plus 5 min |
| moon_laundromat | hanbit_mart | 13 min | walk (ch005) |
| hanbit_mart | Hapjeong station | 6 min | walk |
| hanbit_mart | pyo_cafe | about 8 min | walk east |
| hanbit_mart | eunchae_gosiwon | 8 min | walk (ch022); the gosiwon is 5 min from Hapjeong station |
| hanbit_mart | mapo_tyre_base | about 6 min | walk south-west |
| hanbit_mart | go_first | 2–3 min | "two streets" (ch99) |
| hanbit_mart | aao_office | about 15 min | Line 6 from Hapjeong, two stops to Mapo-gu Office, plus 5 min |
| ryu_practice_yard | porters_lodging | about 8 min | walk |
| ryu_practice_yard | mangwon_riverside | about 8 min | walk south |
| ryu_practice_yard | mapo_tyre_base | about 15 min | walk; about 5 min by van |
| Mapo (home turf) | guro_pit | about 35–40 min (estimate) | Line 2 Hapjeong to Sindorim (four stops), then south to the site; or the Ryu van |
| Guro | Hapjeong | 4 stops by Line 2 from Sindorim | over the Dangsan Railway Bridge (ch018) |
| Mapo | sinjeong_arcade | about 25 min by van at night (estimate) | south-west across the river |
| Mapo | terrace_gate_rim | about 20 min by van; Line 2 to Mullae plus a walk | across the river (decided here) |
| Mapo | exhibition_arena | about 10 min | Line 6 to World Cup Stadium |
| Mapo | awakened_cram_academy | about 30–35 min | Line 2 to Dangsan then Line 9, or Line 2 to Sindorim then Line 1, to Noryangjin |
| Seoul | Haeseong | about 3 h | coach from Dong Seoul Bus Terminal (Line 2, Gangbyeon) (STORY_BIBLE.md:183) |
| Seoul | Chungju | about 1 h 33 | intercity bus from Dong Seoul (bus timetable) |
| Seoul | Yeoju | about 1 h 56 | bus from the Seoul Express Bus Terminal (bus timetable) |

## 10. Gate incident sites (the violet diamonds on the city map)

| Map | id | Site | Grade | Chapters |
|---|---|---|---|---|
| G1 | `seogyo_gate` | the Seogyo-dong corner seen from the bus (World Cup-ro) | — | 1 |
| G2 | `hanbit_mart` | aisle 2 of Hanbit Mart | E | 1 |
| G3 | `metro_maintenance_tunnel` | the Line 6 maintenance spur | E | 10–11 |
| G4 | `ryu_training_gate` | the cage at the Ryu compound | training | 12 |
| G5 | `guro_pit` | the Guro foundation pit | C | 13–17 |
| G6 | `seongsan_redevelopment` | the salt-iron cave under an emptied villa | D | 22 |
| G7 | `terrace_gate_rim` | Terrace Gate, Mullae-dong freight hardstanding | C+ | 23–32 |
| G8 | `sewer_gate_rim` | the Mapo maintenance chamber | — | 23 |
| G9 | `sinjeong_arcade` | the arcade surge, seven gates | — | 33–40 |
| G10 | `seoryun_base` | the exchange training gate | supervised | 41 |
| G11 | `film_crew_gate` | the DMC backlot | D | 47 |
| G12 | `seogang_camp` | the Seogang camp gate (nine years ago) | — | 40, 43 |
| not pinned | `stone_survey_rim` ×2, echo-coral job, faulty-anchor site | sites unstated | — | 23, 64, 88 |
| off map | Chungju river gate, Yeoju gates A–E, Haeseong sea gate | see sections 5–6 | A, —, — | 63–79, 84–98, 8 |

## 11. Contradictions and rulings

Each line: the clash (file:line), then the ruling. "Locked" means ch001–ch013, whose text is protected.

- **C01 · Taeo's building.** keys/mangwon_street/notes.md:5 calls it "Taeo's three-storey red-brick villa" with the door on the alley. scripts/ch002.yaml:3 and :67 (lettered "U-UNIT 402", locked), ch003.yaml:23 (open-air 4F corridor, ground-floor piloti, locked), ch021.yaml:30, ch022.yaml:24 (twelve studios, three a floor on 2F–5F) and ch029.yaml:27 ("the key's obsolete villa") need a block with a fourth floor. **Ruling:** five storeys, unit 402 on 4F, corridors facing the bus street, stairs north, glass street door in the piloti on the bus street. The key's villa stays in the street as a neighbour on the alley's south side; its brick, meters, wires and lamp are the street's look. (An earlier draft of this file's plan moved Taeo to "302" in the villa; that draft is withdrawn.)
- **C02 · The flat's furniture.** scripts/ch021.yaml:29 ("kitchen strip LEFT, bathroom then desk RIGHT, bed far right by the window") and the first floor plan (6.00 × 3.00 m, desk on the bed side) against keys/taeo_flat/notes.md:5–11 (desk toward the window at the far left, bed along the right wall) and ch023.yaml:28 ("Drawn taeo_flat keys win"). **Ruling:** the key. The plan was redrawn to it.
- **C03 · Curtain or blind.** scripts/ch010.yaml:38 (locked), ch018.yaml:34, ch020.yaml:18, :34, :73, :105 say "curtain"; ch006.yaml:17 and :28 (locked) say "blind"; the key shows no curtain, only a blind box above the window. **Ruling:** a grey-blue blackout roller blind; "curtain" in any script means this blind.
- **C04 · Bus direction at the corner.** scripts/ch003.yaml:24 (locked) says the green branch bus "runs south past the door to the corner stop 30 m away". The key's stop (keys/mangwon_street/notes.md:5) is on the bus street's east kerb at the alley mouth, which serves northbound buses in right-hand traffic, and ch003's bus passes close to the building's kerb. **Ruling:** buses at the corner stop run NORTH past the door toward Mangwon station; ch1's ride to work boards here.
- **C05 · "In the next room" (ch6 hook).** PART_ONE_BEATS.md:122 puts the hook "in the next room"; the first LOCATIONS.md ruled it the flat's bathroom wall; scripts/ch006.yaml:3, :16 and P51–P55 stage it at Hanbit Mart: Taeo in the stockroom corridor, Nib in the break room, the shared wall between them (ledger/CONTINUITY_TODO.md:13). **Ruling:** Hanbit Mart, as ch006. The bathroom ruling is withdrawn.
- **C06 · One notice or two.** PART_ONE_BEATS.md:299 (ch21, vacate in 30 days) and :340 (ch26, "must vacate in 30 days"). **Ruling:** one notice, taped in ch21; ch26 counts the days left on it (ch026 `when:` "the original ch 21 thirty-day housing notice is still running"); the move is ch28.
- **C07 · Where the walk home is.** scripts/ch001.yaml files P42–P46 under `hapjeong_alley` ("A Hapjeong-dong residential alley"); PART_ONE_BEATS.md:107 walks him home "through Mangwon". **Ruling:** the walk starts in the Hapjeong-dong lanes and ends in Mangwon-dong at the corner stop; `hapjeong_alley` is an alias of `mangwon_street`.
- **C08 · The mart's door.** scripts/ch009.yaml:32 (locked) "the door lined up with aisle 2" and the first floor plan (door in the south front) against keys/hanbit_mart/notes.md:5 (glass entrance in the west return near the south-west corner; counter across the north-west rear). **Ruling:** the key.
- **C09 · The kiosk.** scripts/ch018.yaml:32 "on the front strip just west of the door" against ch018.yaml:763 and the continuity report ("the clear strip east of the west-return entrance"). **Ruling:** on the front strip just east of the door; west of a west-wall door would be outside.
- **C10 · The break room.** scripts/ch005.yaml:28 and ch009.yaml:31 (locked: three lockers with Taeo's in the middle, fridge rear left, a sink rear right, the stool against the middle locker) against keys/hanbit_breakroom/notes.md:5 (two lockers on the west wall, fridge north-east, table and stool on the east wall under the whiteboard, no sink). **Ruling:** the key (ch018 already follows it).
- **C11 · The Ryu yard's furniture.** scripts/ch010.yaml:21 and ch012.yaml:24 (locked: a WHITE office with a metal wheelchair ramp, three vans along the far fence with the middle one stickered, a sliding gate in the far fence, a cage in the back right corner) and STORY_BIBLE.md:179 ("three-van survey guild") against keys/ryu_practice_yard/notes.md:5 (grey office, south double gate, one van south-east). **Ruling:** the key for the keyed yard. The far-fence vans and the sliding gate are the north service bay and its back-lane gate, outside the key; the cage is in the compound's back-right corner beyond the yard's north fence; the pedestrian gate is a wicket in the double gate. Three vans until the ch12 tow stays a story fact.
- **C12 · The office window.** scripts/ch010.yaml:22 (locked) "one window just north of" the door; both yard keys show it just south of the door. **Ruling:** the key.
- **C13 · The ramp.** scripts/ch010.yaml:21 and ch012.yaml:24 (locked) "a short metal wheelchair ramp"; ch026.yaml:16 block "a portable timber ramp beside the office's original step". **Ruling:** one removable METAL ramp beside the keyed step (locked text wins).
- **C14 · Which roof.** scripts/ch023.yaml:20 "Opening roof is the established office roof reached by exterior stairs" against ch020.yaml:19–20, ch021.yaml:32, ch022.yaml:31–32 (the workshop roof beyond the north-west boundary, reached by its west stair; "The office container is not the party roof"). **Ruling:** the workshop roof.
- **C15 · Vans after ch29.** scripts/ch030.yaml:22 ("No vans remain after ch 29") and ch031.yaml:19 against ch034.yaml:23 ("Established white Ryu work van") and ch041.yaml:20, ch048.yaml:20, ch052.yaml:18, ch093.yaml:22 (one white van south-east). **Ruling (decided here):** Ryu redeems the last van after ch33's central deposit pays down the Bluebird debt; it is back on the south-east stand from ch34, without a sticker. ch33 should show it.
- **C16 · Kett's mark at the laundromat.** PART_ONE_BEATS.md:363 "on her counter" and the first laundromat plan (the folding counter) against scripts/ch029.yaml:28 (the projecting wooden lip of the NORTH service counter; the older mark only in ch76). **Ruling:** ch029.
- **C17 · The hearing room.** scripts/ch009.yaml:35 (locked: about 12 × 9 m, one door in the back wall, a 40 cm dais) against keys/gma_hearing_room/notes.md:5–9 (8 × 11 m, one-step dais, public double door south-west and staff door north-west, screen on the east wall, high west windows). **Ruling:** the key.
- **C18 · Chae's desk.** scripts/ch021.yaml:33 and :492 ("the hand plate and analogue gauge on a stand, a monitor, two stools, a printer") against keys/aao_office/notes.md:5 and ch003.yaml:28 (two monitors, the flat hand plate, a fob tray, two visitor chairs). **Ruling:** the key; no gauge, no stools.
- **C19 · The café's materials.** scripts/ch006.yaml:176 (locked: pale oak floor, grey stone tabletops, cream walls) against keys/pyo_cafe/notes.md:5 (pale stone tile, a walnut table, a taupe banquette). **Ruling:** the key.
- **C20 · Windows 5 and 6.** STORY_BIBLE.md:149 (three kinds from window 4) and :155–156 (a third river kind; "field ore and two Yeoju kinds") against PART_ONE_BEATS.md:610–611 (only echo coral named before 100%) and :722 (only field ore). **Ruling (decided here):** window 5's third kind is flowstone, collected in ch64; window 6's two Yeoju kinds are levee silt and reed glass, from the ch84 survey.
- **C21 · Mangwon Hangang Park.** scripts/ch019.yaml:25 says the park runs from Seongsan Bridge to Yanghwa Bridge; the official Hangang Park site gives 7.4 km of north bank from the north end of Wonhyo Bridge to the Hongjecheon Bridge in Sangam-dong. **Ruling:** the scenes sit on the Seongsan–Yanghwa stretch; nothing in the art changes.
- **C22 · What the Terrace Gate lot was.** scripts/ch023.yaml:24 "former clay-storage yard"; ch030.yaml:23 "fenced disused freight hardstanding with low warehouses". **Ruling:** the same lot: a former clay-storage yard later used as freight hardstanding.
- **C23 · Where Taeo lives after ch33.** PART_ONE_BEATS.md:398 ("an old tyre-shop compound ... with separate rooms") and the first tyre-base plan (rooms for Taeo and Nib, the rules on its container) against CODEX_SCRIPT_BRIEF.md:44, PART_ONE_BEATS.md:477, :488, :511 (the container door, the rules on the container wall, the propped-open door) and scripts/ch041.yaml:20, ch048.yaml:20, ch052.yaml:18, ch063.yaml:20. **Ruling:** Taeo and Nib stay in the Ryu container home until ch99; the tyre base's rooms are for Sera, Kesh and Dara; Orrin sleeps under its shed roof.
- **C24 · Which bank in Chungju.** scripts/ch063.yaml:22 (from the landing the river flows from upper right to lower left; the near-bank shelf follows it upstream) against ch071.yaml:23 ("Looking downstream from the entrance landing, the dry survey shelf follows the right bank"; Channel B on its waterward left). Looking downstream, the near bank is on the LEFT. **Ruling:** ch063; ch071 means looking UPSTREAM (shelf on the right, water on the left).
- **C25 · The family photo's shelf.** scripts/ch006.yaml:54 (locked: "On the shelf above the bed") against keys/taeo_flat (the shelf above the desk); ledger/CONTINUITY_TODO.md:46. **Ruling:** the key; check ch006 P01's finished art.
- **C26 · The grandparents' TV.** keys/grandparents_house shows a small flat-screen TV; PART_ONE_BEATS.md:474 calls it "the old TV" in the ch43 flashback; ledger/CONTINUITY_TODO.md:57. **Ruling:** nine years ago an old box TV stood on the same cabinet; today's set is the key's flat screen.
- **C27 · The Sinjeong landing.** scripts/ch034.yaml:26 (the door "opens into a 3 m square underground landing") and ch037.yaml:28–29 (a 3 m stair-side apron north of the door AND a 3 m landing south of it). **Ruling:** both: apron, door, landing, then F (plan).
- **C28 · The Chungju staging.** scripts/ch063.yaml:21 (a fenced service cutting with a short concrete access tunnel) and ch071.yaml (a riverside staging ground of gravel). **Ruling:** the cutting runs down to the riverside; its gravel floor at the tunnel mouth is the staging ground.
- **C29 · The Guro pit.** ch017's first pit description against locked ch013. **Resolved** by the continuity pass (ch017 `_status`: reconciled to ch13).

## 12. Decisions writers must follow

1. **Taeo's building:** five storeys, unit 402 on 4F, 401 south and 403 north toward the stairs; open-air corridors on the west face; glass street door in the piloti on the bus street; the corner stop 30 m south at the alley mouth, with the GMA zone sign from ch22; buses there run north.
2. **Taeo's flat:** draw it from the key. Real compass: the window wall is east, the kitchenette north, the bed south, the door west. The roller blind is the "curtain". THE CUP is a white mug with one thin green band. "1. ASK FIRST." hangs on the wet room's outside wall facing the bed. The photo is on the shelf above the desk.
3. **Hanbit Mart:** door in the west return near the south-west corner; counter across the north-west rear facing south; two aisles, the gate in aisle 2; the kiosk on the front strip just east of the door from ch18; unstaffed 22:00–06:00 from the ch18 Friday; a 24-hour chain.
4. **The ch6 hook** is at Hanbit Mart: the stockroom corridor and the break room share the wall.
5. **The laundromat:** Kett's mark on the north service counter's wooden lip (ch29); the older faded mark only from ch76; Granny Moon lives behind the north-east staff door.
6. **The Ryu compound:** the keyed yard plus the plan's west strip (container home, Orrin's awning), the north-west workshop with its roof, the north service bay and the cage in the back-right corner. Office grey; maze fixed; ramp metal; window south of the door.
7. **Vans:** three to ch12, two to ch23, one to ch29, none ch29–33, one again from ch34 (redeemed). The crew's own van from ch62 lives at the tyre base.
8. **The workshop roof** is the party roof: ch20, ch22, ch23's opening and ch82's "yard roof".
9. **Homes from ch28:** Taeo and Nib in the Ryu container until ch99. From ch33 the crew works from `mapo_tyre_base`, where Sera, Kesh and Dara have rooms and Orrin sleeps in bay 3. "The yard" in the beats means the Ryu compound.
10. **Seams:** window 4 (Sera) opens at the Ryu container; windows 5 and 6 (Kesh, Dara) at the tyre base.
11. **Fragment kinds:** window 5's third kind is flowstone (ch64); window 6's are field ore, levee silt and reed glass (ch84).
12. **Sinjeong:** follow the plan: F stair on the north pavement, 14 steps south, apron, east-hinged door, landing, 20 m of corridor to the T, pharmacy west, food court east, the wall across F's north arm, the stockroom bypass. No station exit numbers.
13. **Terrace Gate:** Mullae-dong freight hardstanding; two separate connections on one apron; on the east terrace the cliff is on the RIGHT and the void on the LEFT when advancing.
14. **The exhibition:** Seoul World Cup Stadium; grey padded course; operator boxes at the near barrier, runners going away from them; VIP enclosure high on the opposite side; the draw stage has a broad ramp for Orrin.
15. **Chungju:** no sky; the survey shelf is the near bank; walking upstream the water is on your left.
16. **Yeoju:** gates A–E west to east, A first; depot north, operator canopy south-west, medical shelter south; gate E is the final territory.
17. **GO FIRST:** a former print works two streets (2–3 minutes) from the mart; the external goods hoist; the ch100 party on the roof garden.
18. **Other places decided here:** the porters' lodging in Mangwon 1-dong; the AAO exam hall and practical hall in the AAO building; the cram academy in Noryangjin; Seoryun's depot on the Tojeong-dong riverside; the Long Night memorial in Seonyudo Park; the Seogang camp on the Seogang riverside; the Yoon flat in Sangsu-dong; the film-crew gate at a DMC backlot; Meridian Tower in Yeouido; Sera's hospital in Chungju; the provincial clinic in Yeoju; Haru's school in Haeseong; Nib's boots from the camping store (ch43).
19. **The gate zone** is everything within 1 km of G1 or G2.
20. **"The old Hanbit Mart"** (ch99) means Taeo's old workplace; the store is still open.
21. **Skies** not set by a script stay open; the first script that enters sets the sky and this file records it.

## 13. Script and bible lines to correct

None of these is mine to edit (they are outside `world/`). Locked chapters keep their words; the art follows the rulings above.

| File:line | Now | Should read |
|---|---|---|
| scripts/ch003.yaml:24 (locked) | "runs south past the door to the corner stop 30 m away" | buses at the corner stop run north past the door (C04) |
| scripts/ch021.yaml:29 | "kitchen strip LEFT, bathroom then desk RIGHT, bed far right by the window" | "kitchenette LEFT, desk LEFT by the window, bed RIGHT" (C02) |
| scripts/ch018.yaml:32 | kiosk "just west of the door" | "on the front strip just east of the west-return door" (C09) |
| scripts/ch023.yaml:20 | "the established office roof" | "the workshop roof, reached by its west stair" (C14) |
| scripts/ch026.yaml:16 block | "A portable timber ramp" | "A portable metal ramp" (C13) |
| scripts/ch021.yaml:33, :492 | "analogue gauge on a stand ... two stools" | the key's desk: two monitors, the flat hand plate, a fob tray, two visitor chairs (C18) |
| scripts/ch071.yaml:23 | "Looking downstream from the entrance landing" | "Looking upstream from the entrance landing" (C24) |
| scripts/ch010.yaml:38, ch018.yaml:34, ch020.yaml:18, :34, :73, :105 | "curtain" | "blind" (optional; C03 already rules) |
| scripts/ch019.yaml:25 | the park "runs ... from Seongsan Bridge ... to Yanghwa Bridge" | "this stretch of the park lies between Seongsan and Yanghwa bridges" (optional; C21) |
| ch033 (not yet written) | — | show Ryu redeeming the last van (C15) |
| PART_ONE_BEATS.md:398 | "with separate rooms" | add: the rooms are for the companions; Taeo and Nib keep the Ryu container (C23) |
| PART_ONE_BEATS.md:122 | "In the next room" | "In the break room, on the other side of the stockroom wall" (C05) |
| PART_ONE_BEATS.md:610–611, :722; STORY_BIBLE.md:155–156 | one or two kinds named | name flowstone; levee silt and reed glass (C20) |
| scripts/ch005.yaml:28, ch009.yaml:31–32, ch009.yaml:35, ch010.yaml:21–22, ch012.yaml:24, ch006.yaml:54, :176 (all locked) | see C08, C10–C12, C17, C19, C25 | no text change; check the finished art against the keys |

## 14. Sources (real geography)

Fetched or searched during this pass; each confirms the fact named.

- Hapjeong station: Lines 2 and 6, on Yanghwa-ro, Hapjeong-dong (https://en.wikipedia.org/wiki/Hapjeong_station).
- Line 6 station order Digital Media City, World Cup Stadium, Mapo-gu Office, Mangwon, Hapjeong, Sangsu, Gwangheungchang, Daeheung, Gongdeok (https://en.wikipedia.org/wiki/Seoul_Subway_Line_6); station positions (https://en.wikipedia.org/wiki/Mangwon_station, https://en.wikipedia.org/wiki/Mapo-gu_Office_station, https://en.wikipedia.org/wiki/World_Cup_Stadium_station_(Seoul)).
- Hapjeong-dong and Mangwon-dong, their neighbours, and Mangwon-dong's flooding history (https://en.wikipedia.org/wiki/Hapjeong-dong, https://en.wikipedia.org/wiki/Mangwon-dong).
- World Cup-ro and the other city roads (https://en.wikipedia.org/wiki/Special_Metropolitan_City_roads_of_Seoul); road names in Hapjeong-dong and Mangwon 1-dong, including Poeun-ro (dorojuso.kr address listings).
- Bridges, west to east: Gayang, World Cup, Seongsan, Yanghwa, Seogang, Mapo, Wonhyo; the Dangsan Railway Bridge carries Line 2 (https://en.wikipedia.org/wiki/Yanghwa_Bridge, https://en.wikipedia.org/wiki/Seongsan_Bridge, https://en.wikipedia.org/wiki/Seogang_Bridge, https://en.wikipedia.org/wiki/World_Cup_Bridge, https://en.wikipedia.org/wiki/Dangsan_Railway_Bridge, https://www.koreajoongangdaily.com/korea/100-years-of-history-in-han-river-spans/10589730).
- Mangwon Hangang Park: between Wonhyo and Seongsan bridges on the north bank, 7.4 km, 422,347 m² (https://hangang.seoul.go.kr/www/contents/666.do?mid=468; also https://www.koreabybike.com/routes/hangang-bicycle-path/seoul-north-side/mangwon-hangang-park/).
- Seonyudo, the island park at Yanghwa Bridge (https://en.wikipedia.org/wiki/Seonyudo,_Seoul).
- Seoul World Cup Stadium in Seongsan-dong and World Cup Park on the former Nanji landfill (https://en.wikipedia.org/wiki/Seoul_World_Cup_Stadium, https://en.wikipedia.org/wiki/World_Cup_Park); Nanji Hangang Park's position, used to keep Terrace Gate off the park (https://aroundus.com/p/8345017-nanji-hangang-park).
- Sinjeong station: Line 5, Sinjeong-dong, Yangcheon-gu (https://en.wikipedia.org/wiki/Sinjeong_station).
- Seoul bus colours: green buses are local branch routes (https://en.wikipedia.org/wiki/Buses_in_Seoul).
- Noryangjin as Seoul's cram-school district (https://www.koreajoongangdaily.com/business/noryangjin-kids-last-chance-for-their-dreams/10365774).
- Mullae-dong's quasi-industrial steel and machine-shop blocks (https://stg-m.koreaherald.com/series/333; https://view.asiae.co.kr/en/article/2026032708411868546).
- Intercity bus times: Dong Seoul to Chungju about 1 h 33; Yeoju from the Seoul Express Bus Terminal about 1 h 56 (https://transportation.asamaru.net timetables; https://www.rome2rio.com/s/Seoul/Yeoju-Bus-Terminal).
- District boundaries for every pin: KOSTAT 2013 and JUSO 2015 boundary files (github.com/southkorea/seoul-maps).

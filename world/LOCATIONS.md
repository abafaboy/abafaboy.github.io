# My Summons Go First: location bible (Part One, chapters 1–100)

This file fixes every place the story goes in Part One, so scripts and art stay consistent for 100 chapters. Canon order: `STORY_BIBLE.md` decides what happens, `ART_BIBLE.md` how it looks, this file **where** it happens and what the place looks like.

**How to use it**
- **Script writers:** use the `id` as the location key in `locations:` (SCRIPT_FORMAT.md). Use the travel times when you write `when:` lines and time tags. Respect the continuity locks.
- **Artists (Codex):** attach the floor plan from `world/floorplans/` and the location key image (`locations/<id>.png`, once drawn) for every establishing shot. Furniture never moves unless a panel moves it (ART_BIBLE A10).
- **Signs carry no readable text in the art** (ART_BIBLE A6, A9). Every sign below is described by shape and colour only; the letterer adds words only where a script names them.
- **"(decided here)"** marks a decision this file makes because the bible files are silent. Writers must follow it like canon. **Contradictions** between bible files are listed inside the entry they affect and collected in the last section, each with file, line and the ruling.
- **Real geography.** The city is the real Seoul with fictional businesses. Real neighbourhoods, roads, stations and bridges named here were checked on the web (sources listed at the end). Fictional premises are placed on real streets or street *types* only; no real address is given for any private person or fictional business.
- **Travel times** use walking at about 75 m a minute, Seoul Metro Line 6 station spacing (Hapjeong–Mangwon 0.8 km, Mangwon–Mapo-gu Office 1.0 km, Mapo-gu Office–World Cup Stadium 0.8 km) and about 2 minutes per stop on the subway.
- **Season.** Chapter 1 is a Tuesday in early spring; Part One covers about 14 months (PART_ONE_BEATS.md line 12). Light and weather notes below follow that calendar.

<!-- INDEX -->

---

## A. Home turf: Hapjeong-dong and Mangwon-dong, Mapo-gu

### taeo_flat · Taeo's studio flat, unit 402

- **Keys.** `taeo_flat` (scripts/ch001.yaml). Sub-keys (decided here): `taeo_building` for the stairs, the open-air corridor and the ground-floor piloti; `taeo_street` for the bus street and the corner bus stop outside.
- **Floor plan.** `world/floorplans/taeo_flat.svg` (+ `.png`): plan, site sketch and section.
- **Where.** Mangwon-dong (the Mangwon 2-dong administrative area), Mapo-gu. A fictional five-storey studio block on a two-lane bus street that runs south from Mangwon station toward the river; no real address. **(decided here)**
  - Mangwon station (Line 6, under World Cup-ro) is 7 minutes' walk north.
  - Mangwon Market, a 215 m covered arcade between World Cup-ro 13-gil and Mangwon-ro, is 4 minutes north.
  - The riverside (Mangwon Hangang Park) is about 12 minutes south-west.
  - Why here: Mangwon-dong flooded regularly until the early 1990s, so its housing is older and cheaper than Hapjeong-dong's. That is how Taeo affords ₩450,000 a month (ch5) on a ₩5,000,000 deposit (ch15).
- **Street level** (`taeo_street`, `taeo_building`).
  - A red-brick facade. The ground floor is an open piloti car park holding the glass street door, the mailboxes and the bottom of the stair. Above it are four floors of studios (2F–5F).
  - Each floor has an open-air access corridor on the street (west) side, under a roof, with a waist-high metal rail. From it you look down on the bus street. That is where Nib sees "a scooter below, too many lights" (ch2).
  - The back (east) faces a narrow rear lane and the back of the next block.
  - A bus stop with a lit advertising screen stands at the south corner, 30 m from the street door. This is ch1 P45's "corner before his building" and ch3's "bus roars past" at the street door.
  - Street furniture: gas meters, tangled overhead wires, a cat on a wall, a convenience-store sign far off (ch1 P42 vocabulary).
- **Chapters.**
  - **1:** the draw; Nib arrives.
  - **2:** the whole chapter (standoff, cup, 3 a.m., the registration text).
  - **3:** the morning call; the street door and the bus.
  - **5:** hook, the knife on the table.
  - **6:** the sleepless night with the photo and the patch; hook, Nib in "the next room".
  - **18:** hook, Chae's call and the shard that glows. This takes place here on the morning after his last weeknight. **(decided here)**
  - **19:** the interface opens; integration at night.
  - **21:** Nib's rage; the open door; "1. ASK FIRST."; Grandma's call; Nib's return; the notice on the door.
  - **23:** hook, the moss window. The copper moss is integrated at home that night, so the window opens here and ch24 follows straight on. **(decided here)**
  - **24:** Orrin's summoning; the corridor; the ladder truck.
  - **28:** packing; the empty room.
  - Mentioned, not shown: 6 (Pyo: "an 18-square-metre flat"), 15 and 17 (the deposit), 22 (rezoning, the landlord selling), 26 (the deadline).
- **Exterior.**
  - The door: a flat slate-grey steel slab with a lever handle. Its number plate is a small blank brass rectangle, never lettered in the art.
  - The block: a five-storey red-brick studio block with a dark grey parapet on the roof.
  - At night the corridor is lit by cold white tube lights, and sodium-orange street glow comes up from below.
- **Interior** (looking IN from the door, which faces east):
  - **Entry:** a short tiled shoe area, one step down. A grey shoe cabinet stands in the NW corner. The navy jacket hangs on a hook on the bathroom wall beside the door.
  - **Left (north) wall:** the kitchenette strip, 2.40 m long. West to east: under-counter washer, sink, two-ring induction hob, under-counter fridge, with wall cabinets above. Past it stands the chrome clothes rack, hung with black hoodies; the olive backpack (patch out) lives on the rack's end hook.
  - **Right (south) side:** the bathroom door first. The bathroom is a wet room with shower, toilet and basin, and no window. Then the desk (1.00 m) with a stool. On the wall shelf above the desk stand **the framed photo** (parents, Taeo at 14, baby Haru) and a small box for the patch. The **desk lamp** sits on the desk's bed end.
  - **Far right:** the bed, a 1.10 × 2.00 m super-single on storage drawers, with a grey duvet and one pillow. Its head is against the window wall.
  - **Middle:** a low folding table in pale wood (floor-sitting height), where Taeo's mug lives.
  - **Far (east) wall:** the ONE window, a 1.60 m two-panel aluminium sliding door onto the balcony, with a grey-blue blackout curtain (he sleeps by day after nights). A wall AC unit is mounted high on the north wall.
  - **Balcony** (0.90 m deep): the AC outdoor unit, a folding drying rack, a 1.0 m metal rail. View: the back of the opposite block (a few lit windows at night) and the rear lane below.
- **Key props (decided here).**
  - THE CUP (ch2, packed in ch28): a plain white ceramic mug with one thin green band.
  - From ch21, a sheet of printer paper reading "1. ASK FIRST." is taped at eye height on the bathroom wall facing the bed.
- **Time-of-day looks.**
  - Night: lamp only, warm on the south (desk) side and blue-grey on the north side. The phone screen gives the cyan-white accent.
  - Morning: grey-blue daylight, and a yellow band through the curtain gap when it is open.
  - Daytime with the curtain closed: dim blue-grey with one yellow line at the curtain edge.
  - Summon: cyan #3FE3F2 takes over the whole room (ch1 P52–P54, ch24).
- **Colour script.**

  | Look | Key | Shadows | Accent |
  |---|---|---|---|
  | Night | warm lamp orange on one side | deep blue-grey | phone-screen cyan-white |
  | Morning | cool grey-blue daylight | soft blue | yellow from the window |
  | Summon (proposed) | interface cyan on everything | navy #0B1530 | the summoned person's own colour (Nib's amber eyes, Orrin's slate-green) |
  | Corridor, night (proposed) | cold white tube light | blue-grey | sodium orange from the street |

  The first two rows are ART_BIBLE A4.
- **Travel.**
  - Hanbit Mart: 20 minutes' walk, east along Poeun-ro and through the Hapjeong-dong villa lanes, passing Granny Moon's laundromat. Or the green branch bus from the corner stop, north to Mangwon station and east along World Cup-ro, getting off one stop before Hapjeong station: about 6 minutes on the bus plus 4 minutes on foot.
  - Granny Moon's laundromat: 7 minutes' walk.
  - Ryu Survey yard: 12 minutes' walk (see `ryu_yard`).
  - Ability Assessment Office: 20 minutes' walk north-west, or Line 6 one stop from Mangwon to Mapo-gu Office plus 5 minutes.
  - Haeseong: Line 6 and Line 2 to the express bus terminal, then the 3-hour bus (see `haeseong_bus`).
- **Continuity locks.**
  - 18.0 m² interior, 6.00 × 3.00 m, ceiling 2.30 m.
  - Fourth floor (4F) of five, unit 402, no lift; the stairs are at the corridor's north end.
  - The door opens OUT into the corridor. Seen from inside, the handle is on the viewer's LEFT and the hinges on the RIGHT. This is the published edition's hardware lock, kept.
  - Screen geography: looking in from the door, the kitchen strip is LEFT and the bed RIGHT by the window. Never mirror the room.
  - Only one window, facing east, with morning sun. The door wall faces west onto the corridor and the street.
  - The only other room is the bathroom. "In the next room" (PART_ONE_BEATS.md line 122, ch6 hook) therefore means **the bathroom**: Nib presses his palm to the bathroom side of the wall shared with the room.
  - The summon circle is 1.4 m across, centred 1.6 m from the bed's head end on the floor between the bed and the folding table. Taeo sits against the bed's drawers when it opens (ch1 P48–P54).
  - Orrin (ch24) pins the bed and cracks the glass door. To get him out, the glazier lifts both sliding panels out of the frame. The ladder truck docks at the balcony from the rear lane at night, and Orrin bends the rail climbing onto its platform. The rail stays bent and the glass stays taped until the move (ch28).
  - The building is inside the Hapjeong gate advisory zone declared in ch21 (see `hapjeong_gate_zone`).
- **Contradictions.**
  - PART_ONE_BEATS.md line 122 says "in the next room" in an 18 m² studio (lines 43, 115). Ruling: the next room is the bathroom.
  - PART_ONE_BEATS.md line 299 (ch21: "vacate in 30 days") and line 340 (ch26: "Taeo must vacate in 30 days") describe one notice. Ruling: ch26 shows the days *left* on the ch21 notice (about 10), not a new 30-day notice, and the move is ch28.
  - scripts/ch001.yaml files the walk home and "the corner before his building" (P42–P45) under `hapjeong_alley`, while PART_ONE_BEATS.md line 107 has him walk home "through Mangwon". Ruling: the walk starts in the Hapjeong-dong lanes and ends in Mangwon-dong. P45's corner is the corner of `taeo_street`, so draw it to match.

### hanbit_mart · Hanbit Mart, Hapjeong store

- **Keys.** `hanbit_mart` (shop floor, counter, aisles), `hanbit_mart_breakroom` and `mart_street`, all from scripts/ch001.yaml. Sub-key (decided here): `hanbit_mart_stockroom`, for the stockroom and back store (ch5 "stockroom maths"); scripts may also just use `hanbit_mart`.
- **Floor plan.** `world/floorplans/hanbit_mart.svg` (+ `.png`), with an enlarged break-room inset.
- **Where.** Western Hapjeong-dong, Mapo-gu (STORY_BIBLE.md line 182; ch001 P06 tag). A fictional chain grocery on the ground floor of a three-storey red-brick building with two floors of villas above. It stands on the corner of a two-lane residential street (south) and a 3 m lane (east), in the villa blocks south of World Cup-ro between Hapjeong station and Mangwon-dong. No real address. **(decided here)**
  - Hapjeong station (Lines 2 and 6, on Yanghwa-ro) is 6 minutes' walk east.
  - Mangwon station is 12 minutes' walk west.
  - Real texture: the residential lanes of Hapjeong-dong are lined with low villas, many built on the sites of 1930s railway housing, and have few convenience stores. A neighbourhood mart fills that gap.
- **Chapters.**
  - **1:** the shift, the courier, the break room, the gate, the street outside.
  - **5:** the construct stocker arrives; Eunchae meets Nib; stockroom maths.
  - **9:** montage. Eunchae teaches Nib Hangul with flashcards at the break-room table **(decided here)**, and the stocker works nights.
  - **18:** Dokgo's awkward apology at the counter; Eunchae moved to mornings; Taeo's last weeknight.
  - **99** (mentioned): the guild building is "two streets from the old Hanbit Mart". "Old" means his old workplace. The store is still open in Part One. **(decided here)**
- **Opening hours (decided here).** Open 24 hours; it is a chain, which is why head office can put a construct on nights. Taeo's night shift starts at 20:00 (ch1). From ch5 the construct stocker does nights and Taeo works weekend days. Eunchae moves to mornings in ch18.
- **Exterior** (`mart_street`).
  - A glass storefront facing south, with aluminium frames. The glass wraps the south-east corner for one metre.
  - A single glass door, lined up with aisle 2, opening inward, with a small bell on the frame above it (the JINGLE).
  - Signs: a long green fascia panel with one white circle logo and no letters, plus a small green projecting box sign on the corner.
  - On the pavement (2.5 m): a delivery-scooter spot east of the door, a potted plant beside the door, a stack of blue plastic crates by the west window, a utility pole at the kerb with a streetlight, tangled overhead wires, and a bicycle chained to the pole. Low red-brick villas opposite.
  - The back door opens onto the east lane, beside the recycling bins.
  - ch1 night: police tape across the door from the plant to the crates; officers and customers on the pavement; violet gate glow showing through the glass in aisle 2.
- **Interior: shop floor** (`hanbit_mart`). Interior 8.00 m wide; shop floor 8.60 m deep; ceiling 2.8 m.
  - **Two aisles**, each 1.30 m wide. Aisle 1 is the west aisle and aisle 2 the east.
    - Between them stands the double-sided **noodle gondola**: cup noodles on its aisle-1 face (Eunchae stocks them, ch1 P17), packet noodles on its aisle-2 face, and cup-noodle multipacks along the top (so cups can tumble in aisle 2, P31).
    - Aisle 2's other side is a one-sided **snack shelf** (crisps, biscuits, the spicy seaweed snacks Haru likes).
    - The west wall carries rice, oil, sauces and tissue.
    - The aisles end at the north wall: three glass-door **drinks fridges** at the end of aisle 2, a bread rack, and the break-room door at the end of aisle 1.
  - **Front strip:** an ice-cream chest freezer under the west window, a basket stack beside the door, and a low drinks display.
  - **Promo end cap:** the gondola's south end, facing the door. It carries the red "two-for-one" sale tag, the only saturated note (P07–P08).
  - **Counter:** just east of the door, running north–south, 2.80 × 0.60 m, with a return toward the glass. The till sits at its south end facing the door, with the card reader and Taeo's coffee cup. Customers stand on its west side.
  - **Behind the cashier** (east wall): the cigarette shelves. Above their north end, on a bracket 2.0 m up, a small TV angled at the counter (screen: green).
  - **Stockroom door:** at the counter's north end, "beside the counter" (P10). Nib listens behind it in ch5.
- **Interior: stockroom and back store** (`hanbit_mart_stockroom`). An L-shaped room behind the counter and along the back.
  - Racks; the manager's small desk with a CCTV monitor; cartons on the floor.
  - A staff WC.
  - The steel back door to the east lane.
  - From ch5, a taped rectangle by the back door where the construct stocker stands between tasks. **(decided here)**
- **Interior: break room** (`hanbit_mart_breakroom`). 2.60 × 3.00 m, no window.
  - The door opens inward and is hinged on its west jamb.
  - Seen from the door (P18): three grey **lockers** on the LEFT wall, with Taeo's in the middle (decided here). A small fridge with the **microwave on top** at the rear left. Storage boxes and green crates on the back wall. A utility sink with a mirror and coat hooks at the rear right. The **rota whiteboard** on the RIGHT wall, 1.2–1.8 m up.
  - A pale **folding table** with one **black plastic stool** stands against the lockers. Taeo sits with his back to his own locker, facing the whiteboard: the phone propped on a cup in P22, his head back against the locker in P26.
  - One fluorescent tube runs over the table (the "hard white bar", P26).
- **Time-of-day looks.**
  - Night (ch1, ch5): fluorescent green-white throughout, and the glass front is a black mirror.
  - Day (ch18 mornings, ch9 montage): sun through the south glass makes warm patches on the front strip, with the aisles still fluorescent.
  - The break room is always the same warmer fluorescent.
  - Outside at night: sodium-orange streetlight and the shop's green-white spill on the pavement; the gate's violet in ch1.
- **Colour script.**

  | Look | Key | Shadows | Accent |
  |---|---|---|---|
  | Shop floor, night | pale fluorescent green-white | grey-green | muted shelf colours; the red sale tag is the only saturated note |
  | Break room (proposed) | warmer fluorescent cream | grey-brown | the whiteboard's blue marker, the phone screen |
  | Street, night (proposed) | sodium orange | deep navy | the store's green-white glow; violet gate light in ch1 |
  | Shop floor, day (proposed) | daylight cream at the front, fluorescent behind | grey-green | the red sale tag |

  The first row is ART_BIBLE A4; the break room and street rows follow the scripts/ch001.yaml palette notes.
- **Travel.**
  - Taeo's flat: 20 minutes' walk west via the Hapjeong-dong lanes and Poeun-ro, passing Granny Moon's laundromat at about 13 minutes.
  - Hapjeong station: 6 minutes' walk.
  - Ability Assessment Office: Line 6 from Hapjeong, two stops to Mapo-gu Office, then 5 minutes' walk: about 15 minutes door to door.
  - Bae's QuickHaul round covers Mapo by scooter and golem on foot. The golem walks, which is why Bae is always late.
- **Continuity locks.**
  - TWO aisles. The door lines up with aisle 2. Looking north down aisle 2, the noodles are on the LEFT and the snacks on the RIGHT (P28).
  - **The gate (ch1)** opens in the middle of aisle 2, 4.6 m from the glass. It starts as a chest-height hairline crack, then becomes a door-height slit across the aisle, facing the door. From the doorway it is "far down the aisle" (P34), with the fridges glowing behind it.
  - The counter is east of the door, and the cashier's back is to the cigarettes and the TV.
  - Break room: lockers LEFT and whiteboard RIGHT as seen from its door; the stool is always against the middle locker.
  - The rota whiteboard is a grid of days with names as squiggles. Only "TAEO" in the SUNDAY column may be legible in ch1 (ch001 P18), and it is erased and rewritten as the rota changes (ch5 "SUNDAY OFF" in the published edition; nights go to the unit from ch5).
- **Reconciled, not contradictory.** scripts/ch001.yaml has noodle cups in aisle 1 (P17) and instant noodles on the left of aisle 2 (P28). Both are true: they are the two faces of the same noodle gondola.

<!-- END OF ENTRIES -->

# Codex task: character model sheets, scale chart, location keys and a style test

You are the lead character designer for the remake of the webtoon *My Summons Go First*. Use your image generation tool (imagegen).

Read `bible/ART_BIBLE.md` first. Part A is the drawing style, and Part C is the checklist every image must pass.

These sheets become the reference attached to every panel of 100 chapters. They must be:
- clean;
- consistent;
- unmistakably drawn in a modern Korean webtoon style: flat cel colour, hard-edged shadows, line-weight variation, no painterly gloss.

The old series art had problems: designs drifted, faces were neutral, rendering was uniform. Fix all of that here.

## Deliverables (put everything under `characters/`, `locations/` and `style_test/`)

For each character in the cast list below, make a folder `characters/<id>/`.

| File | What it shows |
|---|---|
| `turnaround.png` | Full body, plain light-grey background. Front, 3/4, side, back. Same pose height, standing relaxed, feet visible. No text except a small name label at the bottom. |
| `expressions.png` | 8 head-and-shoulders expressions: neutral, small smile, laughing, angry, shocked, crying or holding back tears, embarrassed, and a COMEDY face (simplified chibi version). |
| `details.png` | Close-ups of locked props and details: hands, shoes, anything listed under "locked". |
| `card.json` | Hex colours for skin, hair, eyes and each garment; height in cm; locked details as a list; outfit list. Fill the hex values by sampling your final images with Python. |

**Process.** Generate the turnaround first. Then attach it as the reference image when you generate the expressions and details, so all three match.

If a result drifts (a different hairstyle, a wrong colour, missing props), regenerate. Do not keep a drifted sheet.

### Also make
- `characters/scale_chart.png`. Everyone in the cast standing in a line on a height grid in cm, in the same style. Nib's head must reach Taeo's belt.
- **Location keys** in `locations/`. Each is one establishing view plus a small top-down floor plan drawn beside it, so furniture positions are locked.
  - `hanbit_mart.png`: a small neighbourhood grocery at night. Two aisles, a counter by the glass door, a break room door at the back, the rota whiteboard in the break room. Fluorescent pale green-white light.
  - `taeo_flat.png`: an 18 m² studio. Door, short entry with shoe area, tiny kitchen strip on the left, a bed with grey duvet on storage drawers by the window, a folding table, a clothes rack. A framed photo of four people (two parents, a boy, a baby) on the shelf. One window with a view of other buildings.
  - `assessment_office.png`: a government lobby with numbered-ticket chairs and a TV on the wall. One assessment room with a desk, a hand plate and an analogue gauge on a stand, a monitor, two stools.
  - `survey_yard.png`: a fenced outdoor practice yard with movable plywood screens forming a maze, orange safety fencing, a site office container, radios on a table.
- **Style test** in `style_test/`. Four finished panels from the new Chapter 1, in final quality, with NO text, bubbles or SFX drawn in. Use the model sheets and location keys as references.
  1. `p1_store_establishing.png` (wide). Night street, the lit Hanbit Mart on a corner, Taeo visible through the glass door at the counter. A delivery scooter parked outside.
  2. `p2_crack.png` (tall). Inside the aisle. A hairline black crack in the air between two shelves, faint violet light leaking from it. Taeo in the foreground, from a low angle, his hand out to stop a customer, face alarmed.
  3. `p3_nib_reveal.png` (tall, full width). Taeo's dark flat. A circle of cyan light on the floor and a tall thin seam of light standing in it. Nib stepping out of the seam toward the camera: crouched, hand on his knife, amber eyes catching the light, ear notch visible. Low camera. This is the series' most important image so far, so make it unforgettable without painterly gloss.
  4. `p4_comedy.png` (square). A comedy beat in simplified chibi style: Nib deadpan, holding a mug of water at arm's length, staring at Taeo, who is sweating, on a flat screentone background.

## Cast list (first story arc)

Names are fixed: Taeo and Nib come from the published chapters; the other names are the series' new canon.

1. **`taeo`: Yoon Taeo, 23, 181 cm.** Grocery clerk, newly awakened Summoner.
   - **Body:** lean, slightly round-shouldered from tiredness, normal proportions (no stretched model legs).
   - **Face and hair:** messy near-black hair falling over his brow; brown eyes with tired lower lids; a small mole under his right eye.
   - **Outfits:**
     - (a) black hoodie, black cargo trousers, black low sneakers with one white stripe;
     - (b) work: the same plus a grey-green Hanbit Mart vest with a white name tag "TAEO";
     - (c) outdoors: a navy zip jacket over the hoodie.
   - **Locked:**
     - an old canvas backpack (olive) carrying a faded orange embroidered **team patch**: a shield with an open door in its centre;
     - his phone: dark grey, a hairline crack in the top-left corner, a clear case with a small green dinosaur sticker.
   - **Expression notes:** a polite, worried default; his rare real smile is lopsided.
2. **`nib`: Nib, goblin scout, adult, 105 cm.**
   - **Build:** wiry, long-limbed, a soldier's posture (balanced, weight forward, always one hand near his knife).
   - **Skin and face:** olive-green skin (#7A8B4A, shadow #5F6E38); amber eyes (#F2A93B); a long pointed nose; one small lower fang on the left; faint pale scars on both forearms.
   - **Hair and ears:** spiky black hair; long pointed ears with a clear **V-notch in the top edge of the LEFT ear**.
   - **Clothes:** a torn pinkish-tan sleeveless wrap top, torn charcoal knee shorts, a BROWN rope belt, barefoot.
   - **On the belt:** a leather drawstring pouch on his right hip; a knife in a BROWN WOODEN sheath on his left hip.
   - **Locked:** ear notch, belt colour, sheath, pouch side, fang side.
   - **NEVER cute.** He is a weathered adult: lines under the eyes, a narrow face, a sharp jaw. His comedy face is a flat deadpan stare, not a chibi pout.
3. **`grandma`: Grandma, Kim Okja, 71, 152 cm.**
   - **Look:** short permed grey hair; reading glasses on a beaded cord; sharp, lively eyes; sturdy and small. Strong work-worn hands (she sold fish at a market for 40 years).
   - **Clothes:** a red-and-navy plaid shirt, a quilted beige vest, loose dark trousers, house slippers.
   - **Expression notes:** she scolds with love; her laugh is huge.
4. **`grandpa`: Grandpa, Yoon Gilsu, 74, 166 cm.**
   - **Look:** thin, slightly stooped, short white hair, a weathered tan. A faded blue work cap and a grey work jacket with many pockets.
   - **Locked:** a hand cart he pulls when collecting cardboard and recycling.
   - **Expression notes:** a gentle, quiet smile, his eyes crinkling. He says "it's fine" too often.
5. **`haru`: Yoon Haru, Taeo's little brother, 10, 138 cm.**
   - **Look:** messy black hair with a cowlick; a missing front tooth; a yellow T-shirt with a small dinosaur print, blue shorts, sneakers with velcro.
   - **Locked:** loves dinosaurs and spicy seaweed snacks.
   - **Expression notes:** loud, cheeky, very expressive.
6. **`eunchae`: Shin Eunchae, 25, 163 cm.** Taeo's coworker.
   - **Look:** long brown hair in a high ponytail, brown eyes.
   - **Clothes:** a cream shirt with rolled sleeves, the grey-green Hanbit Mart vest with name tag "EUNCHAE", black trousers, black-and-white canvas sneakers.
   - **Locked:** a dog-eared food-hygiene exam workbook with sticky tabs, often under her arm.
   - **Expression notes:** brisk, sharp-tongued, kind.
7. **`chae`: Chae Yuri, 34, 165 cm.** Assessor at the Ability Assessment Office.
   - **Look:** a chin-length brown bob.
   - **Clothes:** a navy cardigan over a white collared shirt, black trousers, low heels.
   - **Locked:** an ID card on a lanyard; a work tablet in a blue cover.
   - **Expression notes:** calm, precise, a tiny smile when something interests her.
8. **`minho`: Ryu Minho, 26, 178 cm.** Survey-crew lead of his family's small guild, Ryu Survey.
   - **Look:** short black hair with a premature grey streak at the left temple; strong eyebrows; tired eyes.
   - **Clothes:** a brown work jacket, a grey T-shirt, olive cargo trousers with black knee pads, brown work boots, a wristwatch.
   - **Locked:** a radio clipped to his chest.
   - **Expression notes:** terse and fair. Rare laughter catches him off guard.
9. **`seoryun`: Han Seoryun, S-rank hunter, "The Returning Captain", 38, 172 cm.**
   - **Look:** long dark hair in a loose low ponytail; a thin scar through her left eyebrow; broad shoulders; a steady gaze.
   - **Clothes:** an olive field jacket over a black T-shirt, dark tactical trousers, boots.
   - **Locked:** her team emblem (a shield with an open door) on the shoulder; a large hexagonal barrier shield with the same emblem, shown on the details sheet.
   - **Expression notes:** tired kindness. On TV she looks smaller than in person.
10. **`courier`: Bae Jungho, 41, 170 cm**, and his summon **`golem`**.
    - **Courier look:** stubble. A navy cap and navy QuickHaul work jacket with a reflective stripe; a phone mounted on his wrist.
    - **Golem:** 190 cm. A grey boulder body, dot eyes, a slit mouth, a canvas apron, a rope harness carrying crates. Its movements are slow and literal.
11. **`manager`: Store manager, Oh Daesik, 50, 168 cm.** Short black hair, a black polo shirt, a clipboard, a permanently harried look.

## Report
Write `characters/REPORT.md` covering:
- what you made;
- any design decision you took that is not in this brief;
- anything that failed.

Keep rejects in `characters/_rejects/`.

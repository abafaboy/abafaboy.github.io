# My Summons Go First: art and lettering bible (remake edition)

> **Partly superseded on 25 October 2026 (the rebuild).**
> - **Replaced:** A1 (the look), A3 (colour), A4 (locations) and A11 (characters), by `codex/MANHWA_STYLE_GUIDE.md` and `codex/CHARACTER_DESIGNS_v2.md`.
> - **Refined:** A2, A5 and A8 are refined there; where they differ, the style guide wins.
> - **Still in force as rules, ignoring the old examples:**
>   - A5b (chibi): new chibi sheets go in `characters_v2/`.
>   - A6.
>   - A7 (camera): panel counts are now 60–75, see `codex/MANHWA_ART_DIRECTION.md`.
>   - A9 (no text in art): its two exceptions, drawn-in screens and named signs, are withdrawn. The letterer adds all text; the only drawn glyph is the T on Jaeha's vest.
>   - A10 (continuity): sheets now come from `characters_v2/`, locks from `CHARACTER_DESIGNS_v2.md`.
> - **Part B** (lettering and UI) is the letterer's. Its examples and window colours belong to the old story and will be revised; amber now belongs to Nib.
> - **Part C** (the anti-AI checklist) applies, except that its old Nib locks (belt, pouch, sheath) are replaced by `CHARACTER_DESIGNS_v2.md`.
> - Taeo, Hanbit Mart and the rest of the old cast below are retired.

This bible is built from a direct survey of episode 1 of 103 Korean webtoons. Every image slice was viewed, and the UI and lettering were checked at full size. The survey log is in `research/VISUAL_SURVEY.md`.

It replaces every earlier style instruction for this series. The story bible decides what happens; this file decides how it looks.

Part A is for whoever draws panels (Codex image generation). Part B is for lettering and UI (system windows, phones, bubbles, SFX). Part C is the anti-AI checklist that every panel must pass.

---

## Part A: drawing

### A1. The look in one sentence
A modern Korean webtoon look in the family of *Questism*, *The Constellations Are My Disciples*, *Eleceed* and *True Beauty*:
- clean, confident line art with thicker outer contours;
- flat cel colour with one or two hard-edged shadow tones and small crisp highlights;
- drawn (never photographic) backgrounds, simplified behind dialogue;
- one dominant hue per scene, plus one saturated accent.

It must read as drawn by a person, not rendered.

### A2. Line art
- **Colour and weight.** Lines are warm near-black (#2B2523), never pure #000 grey-black.
  - Outer silhouette: about 3 px at 1080 px panel width.
  - Inner detail (folds, features): 1.5 px.
  - Hair strands: tapered.
- **Weight variation.** Thicker lines on the shadow side and where forms overlap, thinner on the lit side. One uniform line weight everywhere is an AI tell.
- **Close-ups.** Eyes and faces in close-up may use coloured lines, a darker shade of the local colour, for a softer read.
- **Skip.** No sketchy construction lines and no hatching on skin. Hatching is allowed only for comedy backgrounds and shock effects.

### A3. Colour and shading
- **Base.** Flat local colour, plus ONE hard-edged shadow tone, cooler and about 15–25% darker. Add a second, deeper shadow only for night scenes or a strong key light.
- **Highlights.** Small, crisp and shaped: on hair (one band), eyes (one or two catchlights), lips, metal and wet surfaces. NO airbrushed skin gradients, glossy plastic skin, or full-face rim lights.
- **Gradients are allowed only for:** sky; gate glow; summon and interface light; page-background transitions; mood washes behind a reaction shot.
- **Palette.** One dominant hue per scene, and one saturated accent at most. Daily life is muted. The supernatural brings the saturated colour.
- **Fixed signature colours** (never reuse them for anything else):
  - **Operator interface** (Taeo's system windows and summon-circle light): cyan **#3FE3F2** on deep navy **#0B1530**.
  - **Nib's link colour:** amber **#F2A93B**, the same as his eyes. Used only when Taeo feels Nib through the link: a thin amber pulse in Taeo's palm, an amber thread in a symbolic panel.
  - **Gates:** a violet-black core **#1A1026** with a cold white-cyan rim. Inside a gate, the sky is the WRONG colour (lavender noon, green dusk).
  - **Grit accent:** red, used sparingly for real danger, blood, warnings and the emergency-alert banner. Use it like *Bloodhounds* or *The Boxer*: one red thing in an otherwise muted panel.

### A4. Location colour scripts
| Location | Key | Shadows | Accent |
|---|---|---|---|
| Hanbit Mart (grocery, night shift) | Pale fluorescent green-white | Grey-green | Shelf colours muted; the red sale tag is the only saturated note |
| Taeo's studio flat (night) | Warm lamp orange on one side | Deep blue-grey | Phone screen cyan-white |
| Taeo's studio flat (morning) | Cool grey-blue daylight | Soft blue | Yellow from the window |
| Ability Assessment Office | Clean blue-white institutional | Light slate | Navy cardigans, green exit signs |
| Survey yard (plywood maze) | Dusty ochre | Warm brown | Sky blue, orange safety vests |
| Noodle shop / grandparents' kitchen | Warm amber | Brown | Steam white |
| Inside gates | Wrong-colour sky, saturated | Violet | The danger red appears only with a threat |
| Flashbacks and memories | Desaturated, cooler, soft-edged | — | One warm colour for the remembered person |

### A5. Proportions, faces and acting
- **Proportions.** Realistic adult proportions, about 7.5 heads. NO fashion-model leg stretching; Taeo is tall but normal. Kids are about 5–6 heads.
- **Faces.** Korean webtoon features: medium eyes with defined lids and one or two catchlights; simple nose (line plus shadow); mouth shapes that ACT.
- **Range.** Every chapter needs at least:
  - one big reaction (shock, laughter, tears);
  - one comedic face;
  - one extreme close-up (eyes or hands).
- **Comedy beats** switch to simplified faces: dot eyes, line mouths, big sweat drops, chibi bodies. Put them on flat colour, screentone or gag-pattern backgrounds. Use this for Nib's deadpan, Grandma's scolding and Taeo's panic.
- **Hands act.** Paying, holding the radio, pressing a palm, gripping a phone. Hands always have five fingers in plausible poses.
- **Silent acting.** At least three panels per chapter carry an emotion with no text at all.

### A5b. Chibi (owner request)
- **Proportions.** 2.5 heads tall, with a round head and a stubby body. The colours, hair, outfit and locked props are identical to the full model (Nib's ear notch, belt, pouch and sheath; Taeo's patch).
- **Faces:** dot or line eyes, big expressive mouths, and gag marks: sweat drops, steam, waterfall tears, sparkles, a snot bubble, turning to stone.
- **Backgrounds:** flat colour, screentone, speed lines, or a gag pattern. Never a full detailed scene.
- **Use.** Chibi is for comedy beats only: 1–3 chibi panels or insets per chapter, and a small chibi gag on every end card. The script marks a panel with `style: chibi`.
- **Never** during grief, danger or a serious confession. The cut back to normal style is part of the joke and the rhythm (the *Mount Hua* lesson).
- **Model sheets:** `characters/<id>/chibi.png`, 8 gag poses each.

### A6. Backgrounds
- **Establishing shots** (first panel of a new location) are detailed and drawn: a Seoul street, the Hanbit Mart aisle, the Assessment Office lobby, the survey yard, the grandparents' coastal town.
- **Dialogue and reaction panels** drop to one of these backgrounds:
  - simplified shapes;
  - flat colour;
  - a soft gradient;
  - focus or speed lines;
  - screentone;
  - white;
  - black.
- Never paint the same photographic density into every panel.
- **Real-life clutter carries the story** (prices, notices, the rota whiteboard), but keep it to the few items the scene needs.
- **Drawn text:** signs and labels stay simplified (blocks or squiggles) unless the script names the text. All readable text is added in lettering.

### A7. Camera and panel rhythm (vertical scroll)
- **Panel count.** 45–65 panels per chapter. A chapter is a 4–7 minute read.
- **Panel shapes** (use at least four in every chapter):
  - full-width establishing (wide, about 16:9);
  - full-width tall (falls, reveals, height);
  - wide strip (about 3:1, eyes and hands);
  - inset left or right (about 55% width, reactions);
  - narrow tall inset (about 35% width, a figure or a phone);
  - borderless vignette fading into white or black;
  - bleed panel that breaks its border (big moments only).
- **Camera.** Change angle every two or three panels:
  - low angle for power;
  - high angle for vulnerability;
  - over the shoulder for conversation;
  - Dutch tilt for unease;
  - extreme close-up for emotion;
  - silhouette for drama.
- **Avoid repeats.** Never more than two consecutive panels from the same camera position.
- **Spacing.** White space between panels is part of the rhythm:
  - short gaps (60–120 px) within a beat;
  - long gaps (300–800 px) for time passing or a held breath;
  - black page stretches for dread or grief.
- **Endings.** Every chapter ends on a hook panel: a tall or full-width image, a reveal, a line, a face. Never a quiet mug refill without a turn.

### A8. Effects
- **Speed lines and impact frames** in action. Focus lines for shock. Screentone dots for comedy and some backgrounds.
- **Particles** only at an impact, a summon, or a gate opening/closing. Never as decoration.
- **Banned as decoration:** bloom, haze, glowing dust motes, god rays, lens flares and depth-of-field blur. Use them only when the script calls for them, for example the summon flash.
- **The summon**, every time, looks the same:
  - a circle of cyan light on the floor;
  - a thin vertical seam of light;
  - the person stepping through it, never materialising from sparkles.
- **Gates open the same way every time:** a hairline crack, a hum, the crack widening, then a door-height black-violet slit with a cold rim and wrong-coloured light inside. Never a flat curtain.

### A9. Text in the art
- **NO lettering in generated art:** no speech bubbles, captions, SFX, system windows or readable UI.
- **Phone screens.** Draw them as a flat pure green (#00FF00) area with crisp edges, so the letterer can composite the app UI in perspective. The exception is when a brief explicitly asks for a drawn-in screen.
- **Signs.** If the brief names the sign text, draw it simply and legibly in English. Otherwise use blocks.

### A10. Continuity locks (apply to every panel)
- Always attach the current character model sheets (`characters/<name>/sheet.png`) and, for a location, the location key (`locations/<name>.png`) when generating.
- **Scale.** Nib is 105 cm tall. Standing beside Taeo, the top of his head reaches Taeo's belt. Taeo is 181 cm. Use the scale chart in `characters/scale_chart.png`.
- **Wardrobe** changes only when the script says so. Model sheets list each outfit and the chapters it applies to.
- **Props** are locked (knife sheath, belt colour, phone case, the team patch). Model sheets show them. A prop never changes colour or shape between panels.
- **Sets.** Taeo's flat, the store and the Assessment Office have floor-plan keys. Furniture never moves between panels unless someone moves it.

### A11. Character essentials (full designs on the model sheets)
- **Taeo (Yoon Taeo), 23.**
  - Messy near-black hair that falls over his brow, brown eyes with tired lower lids, a lean build.
  - Wardrobe: black hoodie, black cargo trousers, black low sneakers with one white stripe.
  - At work, a grey-green Hanbit Mart vest with the white name tag "TAEO".
  - Outdoors, a navy zip jacket.
  - His old canvas backpack carries a faded orange embroidered **team patch**: a shield with an open door, the emblem of Han Seoryun's rescue team.
  - His phone has a hairline crack in the top-left corner and a clear case with a small green dinosaur sticker (his brother's).
- **Nib, goblin scout, adult.**
  - Body: 105 cm, wiry and long-limbed, olive-green skin (#7A8B4A base, #5F6E38 shadow).
  - Head: spiky black hair; long pointed ears with a **V-notch in the top of the left ear**; a long pointed nose; amber eyes (#F2A93B); one small lower fang on the left; faint pale scars on both forearms.
  - Clothes: a torn pinkish-tan sleeveless wrap top, torn charcoal knee shorts, a BROWN rope belt.
  - On the belt: a leather drawstring pouch on his right hip and a knife in a BROWN WOODEN sheath on his left hip.
  - Barefoot until he chooses otherwise (the story bible decides when).
  - **Tone.** He is an adult and must never be drawn cute, round or babyish. Read him as a weathered, wiry adult with a soldier's posture.
- The remaining cast (Grandma, Grandpa, Haru, Eunchae, Chae, Minho, Han Seoryun, the courier and his golem) is defined on their sheets, generated from the story bible.

---

## Part B: lettering and UI (letterer and UI kit)

These rules are what every surveyed series does. The UI kit (system, phone, bubbles, captions, logo) is designed by Codex image generation in several formats. The letterer fills in text in code.

### B1. Dialogue font and size
- **Font.** All-caps condensed comic lettering (Anime Ace / Wild Words family; open-licence stand-ins are acceptable).
- **Size.** 30–34 px at 1080 width for normal speech; 40–60 px for shouts; 24 px for whispers and asides.
- **Emphasis.** Bold italic for key words, never colour. Lines are centred with a balanced rag.

### B2. Speech bubbles
- **Default.** A white, slightly flattened oval with a THIN even outline (2–2.5 px at 1080 width).
- **Tail.** A short or medium curved wedge pointing at the speaker's mouth.
- **Placement.** The bubble sits in the white gutter beside the panel it belongs to, or overlaps the panel edge. It never covers a face, a hand doing something, or the action.
- **Chains.** Consecutive bubbles from one speaker are linked by a short bar, or overlap slightly. Only the first carries a tail.
- **Order.** Reading order is top to bottom, alternating left and right as the speakers stand.

### B3. Bubble and caption types (each is in the UI kit)
| Type | Look | Used for |
|---|---|---|
| Speech | White oval, thin outline, curved wedge tail | Normal talk |
| Shout | White jagged burst, sharp spikes, large text | Yelling, alarm |
| Intense ring | White bubble with a thick fuzzy, radially hatched black outline | An inner vow, panic, exasperation, shock (the most common special bubble in the survey) |
| Thought (quiet) | White oval plus 2–3 shrinking circles toward the head | Private thoughts in scene |
| Thought (floating) | No bubble: small caps text floating in white space beside the thinker | Interior monologue (Taeo's voice) |
| Nervous | Wobbly, scalloped outline | Stammering, embarrassment |
| Whisper | Dashed outline, smaller text | Whispers, asides |
| Menace / non-human | Black bubble, white text; for a gate creature, black with red text and a red outline | Threats, monsters, the cold voice |
| Phone / speaker voice | Angular light-blue polygon with a zig-zag tail, toward the device | Anyone heard through a phone, radio, TV or speaker |
| Announcement | Hexagon | Counting, public address, a streamer's greeting |
| Narration | White rectangle, thin black border, centred caps | Time, place, the narrator |
| Narration (dark) | Black rectangle, white text; or white text straight on a black page, one key word in red | Prologues, flashbacks, dread |
| Place/time tag | Small rounded tag: "MAPO-GU, SEOUL · 11:40 PM" | Scene openers |
| Footnote | Small text under a box: "*ABOUT US$18" | Prices in won |

### B4. System windows (Taeo's operator interface)
- **Brackets and text.** Window text sits in [square brackets], at most 3–4 lines, with a centred headline.
- **In the scene.** The window floats in the scene in perspective, angled toward Taeo. Seen from behind or from another character's side, its text is MIRRORED.
- **Sound.** Every pop-in gets a hand-lettered "DING" in cyan, or "DU-DUN" for big ones.
- **Stacking.** Successive notices cascade down the scroll. Older ones fade to about 40% opacity.
- **Window types in the kit:**
  - one-line notice;
  - standard window with buttons;
  - summon card with a portrait slot;
  - warning (amber);
  - log/list window;
  - glitched/damaged window;
  - small achievement toasts.
- **Lore note for the designers.** The interface is an OLD EMERGENCY PROTOCOL from somewhere else, and it is slightly damaged. It should feel like emergency equipment, not a video game. It is functional, a little worn, and has an occasional glitch. The glitch matters to the plot later.
- **Public systems use ordinary phone apps, not floating windows:** the gate emergency alert, Gate Safety Korea status, Assessment Office booking. Only Taeo (and later other operators) sees floating windows.

### B5. Phones and screens
Two formats, chosen per panel by the script:
1. **Phone in hand.** A drawn phone in a drawn hand inside its own framed panel. The screen arrives as flat green and the letterer composites the app UI in perspective. Hand-lettered SFX go next to it (BZZT, DING, TAP).
2. **The panel becomes the app.** A full-width flat recreation of the app with its chrome:
   - status bar;
   - header with back arrow and title;
   - avatars and name labels;
   - message bubbles;
   - timestamps and read counts;
   - date dividers;
   - keyboard strip.
   
   Reactions are lettered ON TOP of the UI in the series' bubble styles.

**Invented apps.** No real brands; distinctive, believable palettes.
| App | Purpose | Notes |
|---|---|---|
| **TTOK** (똑똑, "knock knock") | Messenger | Door-knock icon. Its palette must not copy KakaoTalk (yellow/brown) or LINE/WhatsApp (green). |
| **Saebom Bank** | Banking | Transfer and balance screens (₩24,800). |
| **Gate Safety Korea** | Government | Gate status (OPEN / CLOSED / "Recording retained"), cordon maps. |
| **Emergency Alert** | Korean-style disaster text | Red header banner: "[Emergency Alert] Gate advisory — Mapo-gu …" |
| **Ability Assessment Office** | Booking | Appointment card, assessment result sheet. |
| **QuickHaul** | Courier gig app | Countdown timers, star ratings, "late" penalties. |
| **HunterLink** | Hunter rankings and fan app | Rank charts, fan votes, sponsor banners. |
| **LIVE** | Streaming | Viewer count, chat rows (round avatar plus rounded chip, casual sentence-case text), donation "Stars". |
| **KNN 24** | TV news | Channel bug, lower third ("HAN SEORYUN • S-RANK HUNTER"), red ticker. |

### B6. SFX
- **Always hand-lettered and drawn into the picture:** outlined, scaled to the sound, angled with the motion, coloured to the scene palette. NEVER a typed word with a full stop.
- **Long sounds** stack vertically down the scroll (THUMP… THUMP…, VMMMMM).
- **Small life sounds** are lettered too: DING, TAP, BZZT, JINGLE (shop door), SLURP, POKE.
- **Gate hum** is always VMMMM in the gate's violet with a cyan outline.
- **Summon** is a thin, tall "SHIIING" in cyan.

### B7. Title, end and intro cards
- **Series logo** (from the kit) appears after the cold open of every chapter, with "CHAPTER N · TITLE" under it.
- **End card.** The last image, then "TO BE CONTINUED" small, then a next-chapter teaser line.
- **Character intro cards** for important first appearances (survey: *Juvenile Detention Center*, *Killer Peter*): a portrait crop plus a white plate reading "HAN SEORYUN · S-RANK · THE RETURNING CAPTAIN".

---

## Part C: anti-AI checklist (every panel, before it is accepted)

1. Hands have five fingers, joints bend correctly, and held objects are actually gripped.
2. Wardrobe, props and colours match the model sheet: Nib's notch, belt, pouch and sheath; Taeo's patch and phone crack.
3. Scale matches the chart. Nib's head is at Taeo's belt.
4. No melted or merged objects, no impossible furniture, no random glyph text, no extra limbs or teeth.
5. Lighting comes from a stated source, with the shadow side consistent with it.
6. Rendering is flat cel with hard shadows: no airbrushed skin, plastic gloss, bloom haze or uniform hyper-detail.
7. The camera differs from the previous two panels.
8. The face is ACTING the emotion in the script, not a neutral pose.
9. There is room for lettering where the script needs it (a calm zone or a gutter side), and nothing important sits in it.
10. If two candidates exist, keep the one a human artist would have drawn: the clearer silhouette and the stronger gesture.

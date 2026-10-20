# Codex task: design the My Summons Go First UI kit (system windows, phones, bubbles, captions, logo)

You are the UI designer for the remake of the webtoon *My Summons Go First*. Use your image generation tool (imagegen) to design every element below.

Read these first, in this folder:
- `bible/ART_BIBLE.md`: Part B is the spec for everything here.
- `bible/VISUAL_SURVEY.md`: what 103 real Korean webtoons do.

Do not copy any existing webtoon's artwork, logo or app design. Real brands are not allowed; the apps here are invented.

## Why this kit exists
Panels are drawn without any text. A letterer program adds the bubbles, system windows and phone screens afterwards, so it needs:
- your **designs**, for the owner to judge;
- **text-free templates** it can fill with each chapter's words.

So every element is delivered in two forms:
1. **Design sheet** `<name>_sheet.png`. All variants of the element on one image, filled with the sample text given below, so a person can judge the look.
2. **Blank templates** `<name>_<variant>_blank.png`. The same artwork with ALL text removed.
   - Background: transparent if your tool supports it. Otherwise pure flat #FF00FF magenta, with nothing (no glow, no shadow) touching the magenta. Keep glows inside the shape's own boundary.
   - One template per file, centred, with at least 24 px of empty margin.
   - Generate at the largest size your tool allows. Never upscale a smaller image.

For every blank template, also write `<name>_<variant>.json`:
```json
{"file": "system_notice_blank.png", "size": [w, h],
 "text_boxes": [{"id": "headline", "rect": [x, y, w, h], "align": "center", "max_lines": 1, "color": "#E8FBFF", "suggested_font": "condensed bold sans"}],
 "tail_anchor": null, "screen_quad": null, "notes": "..."}
```
- `text_boxes`: the rectangles where text goes, in pixels of the template image. Measure them with Python on the actual file; do not guess.
- `tail_anchor`: for bubbles, the point where a tail would attach.
- `screen_quad`: for phones-in-hand, the four corners of the green screen in order TL, TR, BR, BL, found by detecting the #00FF00 pixels.

Put everything under `kit/`, in the subfolders below. Finish by writing `kit/INDEX.md`: a table of every file with a one-line description and its JSON.

---

## 1. System windows: `kit/system/`

**Lore.** Taeo's system is an OLD EMERGENCY PROTOCOL from somewhere else, slightly damaged. It should feel like emergency rescue equipment that happens to float in the air, not like a video-game menu.

**Design direction A (build every variant in this).**
- Deep navy translucent glass (#0B1530 at about 85% opacity).
- A thin cyan double frame (#3FE3F2) with chamfered (cut) corners.
- Small amber chevron ticks (#F2A93B) at two corners, like hazard markings.
- A tiny letter-spaced header strip at the top reading "OPERATOR INTERFACE". Treat this as a label, part of the design.
- A faint scanline texture inside, and a soft cyan outer glow kept tight to the frame.
- Text: white-cyan, condensed bold sans, in [square brackets].
- It must look worn: one corner tick slightly chipped, a faint scratch across the glass.

**Direction B.** One alternative sheet only (`system_altB_sheet.png`), in a direction you think could be better. Briefly explain the choice in INDEX.md.

**Variants** (sheet + blank + json each):
| Variant | Shape | Sample text for the sheet |
|---|---|---|
| `notice` | Wide one-line bar, about 5:1 | [AWAKENING COMPLETE] |
| `notice_small` | Small toast, about 4:1, for cascades | [CONDITION MET] |
| `window` | Standard window, about 4:3: header, 2–3 body lines, one or two buttons | Header: [FIRST SUMMON AVAILABLE] · body: [AVAILABLE DRAWS: 1] · button: [DRAW] |
| `summon_card` | Portrait card, about 3:4: square portrait slot (leave the slot as a flat dark area), name plate under it | [NIB — GOBLIN SCOUT] |
| `warning` | Same family, amber frame and amber header, hazard stripes | [LINK UNSTABLE] |
| `log` | Tall list window, about 3:5, 6–8 monospace-like lines | [INTERFACE LOG] · 00:41:07 ARRIVAL · ROUTE: EMERGENCY · CATEGORY 7 · CONSENT: — · STATUS: STABLE |
| `glitch` | The `window` variant, damaged: RGB-split edges, a torn scanline band, a few dead-pixel squares. Text partly corrupted on the sheet | [FIRST SUMMON AVA██ABLE] |
| `button` | A single pressable button, on its own | [DRAW] |

Also produce one **in-scene example** (`system_inscene_example.png`): an empty studio flat at night, drawn in the series style from ART_BIBLE Part A, with the `window` floating at an angle in perspective in front of the camera. Text may appear here because it is an example only. This shows how windows sit in a scene. Make a second version seen from behind, with mirrored text.

---

## 2. Phones and apps: `kit/phone/`

### 2a. Phones in hands (drawn in the series art style, ART_BIBLE Part A)
Each is a drawing of a hand holding a phone. The screen is flat pure #00FF00 green with crisp edges, so app UI can be composited in perspective.
- **Taeo's phone:** a dark grey modern phone, a hairline crack in the top-left corner of the glass, a clear case with a small green dinosaur sticker on the back.
- **Variants:**
  - `taeo_right_front`: right hand, screen facing the reader, straight on;
  - `taeo_left_tilt`: left hand, tilted 3/4;
  - `taeo_thumb_tap`: close-up with the thumb pressing the screen;
  - `taeo_pov_ots`: over-the-shoulder view, phone in the foreground with a simplified flat behind;
  - `grandma_phone`: an elderly woman's hand, an older budget phone with a big-font case;
  - `chae_tablet`: a woman's hands holding a work tablet in a blue cover;
  - `phone_on_table`: phone face-up on a wooden table, buzzing, with motion ticks (the ticks are drawn lines, not letters).
- In each `.json`, fill `screen_quad` from the green pixels.

### 2b. Flat app screens ("the panel becomes the app")
These are full-width flat UI layouts at a 1080-wide-friendly aspect. Make each as a **design sheet with sample content** AND as a **blank chrome template**: header, status bar, empty message area and keyboard, with the text areas empty. Invent each app's look; it must not resemble any real app's brand.

| App | Screens |
|---|---|
| **TTOK** messenger (똑똑 "knock knock"; door-knock icon; NOT KakaoTalk yellow/brown, NOT LINE/WhatsApp green) | `ttok_chat`: chat with header "Grandma", received white bubbles left with a round avatar, sent bubbles right, timestamps, unread "1", a date divider · `ttok_notification`: lock-screen banner · `ttok_call`: incoming voice call (big avatar, accept/decline) · `ttok_video_call`: the caller's video fills the screen, own video in a corner |
| **Saebom Bank** | `bank_transfer`: "Transfer sent · To: Grandma · ₩150,000 · Available balance ₩24,800" |
| **Emergency Alert** (Korean-style disaster text) | `emergency_alert`: a red-header banner over the lock screen: "[Emergency Alert] Gate advisory: Hapjeong-dong, Mapo-gu. Avoid the area and follow responders." |
| **Gate Safety Korea** (government) | `gate_status`: a gate record card "GATE STATUS: CLOSED · Recording retained" with a small map thumbnail |
| **Ability Assessment Office** | `aao_booking`: an appointment card · `aao_result`: a result sheet "Output: LOW · Response: intermittent sensory" |
| **QuickHaul** courier app | `quickhaul_order`: a delivery timer counting down, star rating, red "LATE −₩500" penalty |
| **HunterLink** rankings/fan app | `hunterlink_rank`: a ranking chart with portrait thumbnails, ranks, fan votes, a sponsor banner |
| **LIVE** streaming | `live_stream`: a video area, viewer count, chat rows (round avatar + rounded chip, casual sentence-case text), a donation "Stars" pop-up |
| **KNN 24** TV news | `tv_lowerthird`: a broadcast frame overlay: channel bug top-right, lower-third name strap "HAN SEORYUN • S-RANK HUNTER", red ticker. Deliver the strap and the bug as separate blank templates too |

For flat apps, the letterer may rebuild the chrome in code. Your design sheets fix the look: colours, radii, icon style and layout. Write the exact colours (hex), corner radii and spacing into each `.json` `notes`.

---

## 3. Bubbles and captions: `kit/bubbles/`

Hand-drawn feel, consistent line weight. Thin outlines: about 2.5 px when the bubble is 600 px wide.

| Variant | Look (ART_BIBLE B3) | Shapes to deliver as separate blank templates |
|---|---|---|
| `speech` | White, slightly flattened oval, thin even outline, NO tail on the template | Aspect ratios 1:1, 1.3:1, 1.7:1, 2.2:1, 3:1, and one tall 1:1.3 |
| `tail` | Separate tail pieces: short curved wedge, medium curved wedge, long curved wedge, each pointing down-left (the letterer rotates and flips them) | 3 |
| `shout` | White jagged burst, sharp irregular spikes | Small, medium and wide |
| `intense` | White bubble with a THICK fuzzy, radially hatched black ring | 1:1, 1.6:1, 2.4:1 |
| `thought` | White oval plus a trail of 3 shrinking circles (deliver the circles as a separate piece) | 1.3:1, 2:1, plus the circles |
| `nervous` | Wobbly scalloped outline | 1.4:1, 2.2:1 |
| `whisper` | Dashed outline | 1.4:1, 2.2:1 |
| `menace` | Black fill; and a monster variant, black fill with a red outline | 1.4:1, 2.2:1 for each |
| `phone_voice` | Angular light-blue polygon, plus a separate zig-zag tail | 1.4:1, 2.2:1, plus the tail |
| `announce` | Hexagon | 1.3:1, 2:1 |
| `narration` | White rectangle with thin black border · black rectangle · white rectangle with a grey offset drop shadow | 3 |
| `tag` | Small rounded place/time tag | 1 |

On the design sheet, put sample text in each:
- WHERE AM I? (speech)
- DON'T TOUCH THAT! (shout)
- I'M NOT GOING INTO A DUNGEON. I JUST WANT TO SEE. (intense)
- …HE TALKS. (thought)
- I-I DIDN'T KNOW IT WOULD BE SOMEONE. (nervous)
- KEEP YOUR VOICE DOWN. (whisper)
- YOU SMELL LIKE A DOOR. (menace)
- TAEO? ARE YOU EATING? (phone voice)
- THREE! (announce)
- THAT NIGHT, THE STORE ON HAPJEONG-RO CLOSED EARLY. (narration)
- MAPO-GU, SEOUL · 11:40 PM (tag)

---

## 4. Logo and cards: `kit/logo/`
- `logo`: the series logo "MY SUMMONS GO FIRST".
  - It hints at the premise: someone stepping through first, a doorway, a thin seam of light.
  - Make it bold, legible at small sizes, and with a strong silhouette.
  - Deliver it on transparent, and also on black and on white.
  - Make 3 logo explorations on one sheet first, then the final.
- `title_card`: the chapter title card layout. The logo plus "CHAPTER 1 · ONE MORE SHIFT" under it. Also a blank version without the chapter line.
- `end_card`: "TO BE CONTINUED" small and elegant, with space for one teaser line.
- `intro_card`: character introduction plate: a portrait crop area plus a white name plate reading "HAN SEORYUN · S-RANK · THE RETURNING CAPTAIN".

---

## Working rules
- **Order:** system → bubbles → phone → logo. Write `INDEX.md` as you go, so partial results are usable.
- Generate a few candidates per variant and keep the best. Put rejects in `kit/_rejects/`, not in the delivery folders.
- **Check every blank template with Python:**
  - it has no text pixels;
  - its background is actually transparent or #FF00FF;
  - the measured `text_boxes` are inside the shape.
- **Do not:**
  - draw characters other than the phone-holding hands and the in-scene example;
  - add text to blank templates;
  - use any real brand name or logo.
- When finished, write a short `kit/REPORT.md` covering:
  - what you made;
  - what you would improve;
  - anything your image tool could not do (for example, transparency).

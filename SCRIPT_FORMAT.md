# Chapter script format (one YAML file per chapter: `scripts/chNNN.yaml`)

One file drives everything:
- **Codex** reads `art` / `camera` / `shape` to draw each panel.
- **The letterer** (`autostrip`) reads `lines` / `sfx` / `ui` / `gap` / `bg` to build the strip.
- **The narrator** (Kokoro) reads `lines` in order, with each speaker's voice.

Write it so all three can work without asking a question.

```yaml
chapter: 1
title: One More Shift
when: "Tuesday, early spring. 9:40 PM to 11:55 PM."
story_beats: PART_ONE_BEATS.md#1          # the beats this chapter must deliver
cast:                                      # model-sheet ids + outfit for this chapter
  taeo: work      # outfit key from the model sheet: default | work | outdoor
  nib: default
  eunchae: work
locations: [night_bus, hanbit_mart, taeo_flat]
panels:
  - id: P01                 # P01, P02 … in reading order; never renumber after art exists (use P12a for inserts)
    shape: wide             # see shapes below
    gap: none               # space BEFORE this panel: none | short | long | black | fade-black | fade-white
    bg: white               # page background around this panel: white | black | navy | <hex> | gradient:<from>-><to>
    camera: "inside a night bus, eye level, looking down the aisle"
    art: >
      Everything Codex must draw, as a short paragraph:
      - who (model-sheet id), outfit, pose, ACTING (the emotion on the face);
      - where (location key), time and light source;
      - palette (from ART_BIBLE A4);
      - props;
      - what must NOT appear.
      Say "screen: green" for any phone or TV screen that the letterer fills.
      Never ask for text, bubbles or SFX in the art.
    calm: top-right         # where lettering may overlap the art: top | bottom | top-left | … | none
    lines:                  # in reading order; the letterer places them, the narrator reads them
      - {who: taeo, type: float, text: "NOBODY LOOKS UP ANYMORE."}
      - {who: nib, type: speech, text: "WHERE AM I?", side: r}
    sfx:
      - {text: "BEEEP", style: alert, at: [0.72, 0.30], size: L, rot: -8}
    ui:
      - {kind: phone.emergency_alert, on: screen, text: "[Emergency Alert] Gate advisory: Seogyo-dong, Mapo-gu. Avoid the area and follow responders."}
    silent: false           # true = no lines and no sfx at all (a held beat)
    style: normal           # normal | chibi (comedy beats only, ART_BIBLE A5b)
    notes: "continuity notes for whoever picks this up"
```

## Shapes
Panels are lettered at 1080 px wide. Codex generates at the size given; the letterer crops or scales.

| shape | Final size on the strip | Generate at | Use |
|---|---|---|---|
| `full` | 1080 × 720–1080 | 1536×1024 | establishing shots, two-shots |
| `wide` | 1080 × 720 | 1536×1024 | standard action and conversation |
| `strip` | 1080 × 360 | 1536×1024, with the subject kept in the middle third | eyes, hands, reaction lines |
| `tall` | 1080 × 1620 | 1024×1536 | falls, reveals, height, hooks |
| `inset-l` / `inset-r` | 600 × 600, sitting left or right | 1024×1024 | reactions; bubbles go in the white beside it |
| `narrow-l` / `narrow-r` | 380 × 760 | 1024×1536 | a single figure, a phone, a door |
| `vignette` | 1080 × 720, no border, edges fade into the page | 1536×1024 | memories, quiet beats |
| `bleed` | 1080 × 1620, breaking the frame | 1024×1536 | the big moments only (at most 2 per chapter) |

## Line types (ART_BIBLE B3)
- `speech` · `shout` · `intense` · `thought` · `float` (Taeo's narration in white space) · `nervous` · `whisper` · `menace` · `monster`
- `phone` (any voice through a phone, radio, TV or speaker)
- `announce` · `narr` · `narr_dark` · `tag` (place/time) · `footnote`
- `system` (a system window: put its text in `ui` instead; the narrator reads it in the interface voice)

Rules:
- `side: l | c | r` says which side of the panel the speaker stands on. The tail points there. When the panel review located the speaker's head, the tail aims at the mouth and stops just outside the head, never on the face.
- `who` is a cast id, or `offpanel:<id>`, or `crowd`.

## SFX styles
- `impact` (big outlined), `quiet` (small hand-lettered), `alert` (red), `gate` (violet with cyan outline), `summon` (thin tall cyan), `phone` (small, with motion ticks), `comic` (rounded and bouncy).
- `at: [x, y]` is the position as a fraction of the panel. `size`: S | M | L | XL. `rot` is in degrees.

## UI kinds (from the Codex UI kit, `kit/INDEX.md`)
- **System:** `system.notice` · `system.notice_small` · `system.window` (fields: headline, body, button) · `system.summon_card` (name) · `system.warning` · `system.log` (lines[]) · `system.glitch`
- **Phone:** `phone.ttok_chat` (messages[]: {from, text, time}) · `phone.ttok_notification` · `phone.ttok_call` · `phone.ttok_video_call` · `phone.bank_transfer` · `phone.emergency_alert` · `phone.gate_status` · `phone.aao_booking` · `phone.aao_result` · `phone.quickhaul_order` · `phone.hunterlink_rank` · `phone.live_stream` (on a screen it can show what the drone filmed: `source: P43` and an optional `subject` box crop that panel's art into the video area) · `phone.sumex_ad` · `phone.info_card` · `phone.camera` (a phone filming: the viewfinder shows `subject: [x0, y0, x1, y1]`, a box of the same panel's art in fractions, with REC and `timer`; `on: screen` only)
- **Desktop:** `pc.video_editor` (a video editor: a 16:9 preview of another panel's art, `source: P21` with an optional `subject` box, transport, `timecode`, a timeline with a `playhead`) · `pc.channel_stats` (a channel dashboard: `title`, `count`, `change`, a rising graph)
- **TV:** `tv.lowerthird`
- **Placement:** `on:` is `screen` (composited into the green screen of the art), `float` (the window floats over the art in perspective), or `panel` (the whole panel becomes the app; leave `art` empty except for a note).
- **Floating windows:** `at: [x, y]` puts the window's top centre there. The letterer keeps every window wholly inside its panel (a window placed so low that the bottom edge would cut it moves up), never lets two windows in a panel overlap, and moves a window that covers a drawn face (smaller, or to another place along the top). Give `wf` (the window's width as a fraction of the panel) only to override the kind's default. Window text is kept readable on a phone: a short body grows to fill the box drawn for it, and a window whose smallest words would still be under about 2.4% of the panel's width grows (up to 94% of the panel) before the face pass runs, so keep window bodies short (about 60 characters) where a face leaves little room.
- **Lit screens:** `screens_lit: alert` (or a `"#RRGGBB"` glow) on a panel lights every green screen no `ui` fills, small background phones included: `alert` is a white screen with a red top band (ch010 P60, every phone in the street shrieking at once). Without it, an unfilled screen is filled dark.
- **Screen spill:** around every green screen the letterer turns the screen's green glow (on a desk, a hand, hair) into the screen's own light, or removes it for a dark screen. Teal greens and a screen in a green surround are left alone. Set `despill: false` on a panel to keep a real green object near a screen (ch005 P17's pot plant).

## Chapter rules (checked before art)
1. 45–65 panels.
2. A cold open, then the title card (`kind: title` panel), then the story; the last panel is the hook.
3. At least 3 `silent: true` panels, one big reaction, one comedy face, one extreme close-up, and 1–3 `style: chibi` panels on comedy beats. The end card always carries a small chibi gag.
4. Never more than two panels in a row from the same camera position.
5. Every beat in `story_beats` is delivered. Every plant used is logged in `notes` as `PLANT P07`.
6. Each speech bubble holds at most 18 words. Split longer lines into two bubbles, chained.
7. Prices, times and counts are exact and consistent with earlier chapters.

## Letterer features (autostrip2)
- `focus: [x, y]` on a panel: the point (0–1 fractions of the art) the letterer keeps when it crops the art to the panel shape. Default centre.
- **Kit phone hands.** For a phone close-up, a panel may use one of the UI kit's drawn phone hands instead of new art. Set `art: "KIT HAND"` and put `hand: <id>` in the phone's `ui` entry (`on: screen`). Ids: `taeo_right_front`, `taeo_left_tilt`, `taeo_thumb_tap`, `taeo_pov_ots`, `grandma_phone`, `chae_tablet`, `phone_on_table`. Use them on narrow, inset or tall panels. This saves an image generation, so prefer it for plain "Taeo reads his phone" beats.
- **System windows** (`on: float`) accept `at: [x, y]` (the window's top centre as fractions of the panel), `tilt` (degrees of perspective turn, default ±8) and `mirror: true` (seen from behind, so the text reads reversed).
- **Screens.** Write "screen: green" in `art` only when the same panel has a `ui` entry with `on: screen` that fills it. A green screen with no `ui` is blacked out by the letterer and flagged.
- **Placement.** Lines are lettered in the white space around a panel, straddling its edge, in reading order: the first half above, the rest below (all below when `calm` is a bottom zone). Two lines from speakers on opposite sides (`side: l` and `side: r`) are set as a staggered pair. On `inset-*` and `narrow-*` panels the lines sit in a column beside the panel; keep those at most 12 words, and put shouts on wide, full, tall or bleed panels. Keep at most 3 lines per panel.
- **Name captions.** On a character's first appearance, `intro: "SEO JIWON · S-RANK · SUNLINE"` on the panel adds a nameplate (name, then role) at its lower left. Use it once per major character.
- **YAML note.** `on:` is read correctly by the letterer even though YAML 1.1 treats a bare `on` key as a boolean; write it as in ch001.

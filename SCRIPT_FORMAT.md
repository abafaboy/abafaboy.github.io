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
- `side: l | c | r` says which side of the panel the speaker stands on. The tail points there.
- `who` is a cast id, or `offpanel:<id>`, or `crowd`.

## SFX styles
- `impact` (big outlined), `quiet` (small hand-lettered), `alert` (red), `gate` (violet with cyan outline), `summon` (thin tall cyan), `phone` (small, with motion ticks), `comic` (rounded and bouncy).
- `at: [x, y]` is the position as a fraction of the panel. `size`: S | M | L | XL. `rot` is in degrees.

## UI kinds (from the Codex UI kit, `kit/INDEX.md`)
- **System:** `system.notice` · `system.notice_small` · `system.window` (fields: headline, body, button) · `system.summon_card` (name) · `system.warning` · `system.log` (lines[]) · `system.glitch`
- **Phone:** `phone.ttok_chat` (messages[]: {from, text, time}) · `phone.ttok_notification` · `phone.ttok_call` · `phone.ttok_video_call` · `phone.bank_transfer` · `phone.emergency_alert` · `phone.gate_status` · `phone.aao_booking` · `phone.aao_result` · `phone.quickhaul_order` · `phone.hunterlink_rank` · `phone.live_stream` · `phone.sumex_ad` · `phone.info_card`
- **TV:** `tv.lowerthird`
- **Placement:** `on:` is `screen` (composited into the green screen of the art), `float` (the window floats over the art in perspective), or `panel` (the whole panel becomes the app; leave `art` empty except for a note).

## Chapter rules (checked before art)
1. 45–65 panels.
2. A cold open, then the title card (`kind: title` panel), then the story; the last panel is the hook.
3. At least 3 `silent: true` panels, one big reaction, one comedy face, one extreme close-up, and 1–3 `style: chibi` panels on comedy beats. The end card always carries a small chibi gag.
4. Never more than two panels in a row from the same camera position.
5. Every beat in `story_beats` is delivered. Every plant used is logged in `notes` as `PLANT P07`.
6. Each speech bubble holds at most 18 words. Split longer lines into two bubbles, chained.
7. Prices, times and counts are exact and consistent with earlier chapters.

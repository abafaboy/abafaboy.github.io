# The Lord Who Measured Zero: production pipeline (for helper agents)

`S = /tmp/claude-0/-home-claude/74687d11-0cc0-5bfd-9d7d-ad4189ed4d7b/scratchpad`
`U = /mnt/user-data/uploads/Videos/LordWhoMeasuredZero` holds art staged from the user's PC.
The PC folder is `~/Videos/LordWhoMeasuredZero` (Windows path `C:\Users\abafa\Videos\LordWhoMeasuredZero`).

Each chapter N lives in `S/epN/`:

| File | Who writes it | What it is |
| --- | --- | --- |
| `script.json` | writer | Voiced lines, one per panel beat |
| `brief.txt` | writer | Codex brief that describes every panel to draw |
| `sound_chN.py` | writer | Music cues and sound effects keyed to line indices |
| `art/` | layout agent | Symlinks to the staged PNGs, plus `end.png` |
| `layout_chN.py` | layout agent | HTML layout of the vertical strip, with face boxes |
| `READY` | layout agent | Touch it once the layout passes. Background runners then voice, mix and render |
| `voice.wav`, `timeline.json` | runner (`runner_tts.py`) | Automatic |
| `full/...mp4`, `BUILT` | runner (`runner_build.py`) | Automatic |

Canon and plan sources:
- `S/plan/series_plan.md`: the 222-chapter plan, the rules and the side-quest ledger.
- `S/bible.txt`: canon, power system and characters. Its old Storyline section is superseded.
- The finished scripts `S/ep15..ep28/script.json`.

Read the previous 2–3 chapters' scripts before writing or laying out a chapter, so names, tone and facts stay consistent.

## 1. script.json

```json
{"title": "The Lord Who Measured Zero", "chapter": "Chapter 29: The Invitation",
 "voices": {"LUCAN": "am_fenrir", "BRAM": "bm_lewis"},
 "lines": [
  {"panel": "p01", "who": "LUCAN", "text": "Narration in first person past tense."},
  {"panel": "p02", "who": "BRAM", "text": "Spoken line."},
  {"panel": "p03", "who": "LUCAN", "say": true, "text": "Lucan speaking aloud, not narrating.", "pause_after": 0.6},
  {"panel": "end", "who": "LUCAN", "text": "The Lord Who Measured Zero. Chapter thirty, coming soon.", "pause_after": 1.5}
 ]}
```

- **Narration.** Lucan narrates everything in first person past tense, including scenes he didn't witness ("Wren told me later..."). Lines Lucan speaks aloud get `"say": true`.
- **Length.** 16–30 lines per chapter, about 100–160 seconds of audio. The second-to-last line gets `"pause_after": 2.0`. The last line is always the end-card line, with panel `"end"`.
- **Line style.** Lines are short, as spoken dialogue should be. Every chapter has at least one light or comic beat. Every chapter ends on a hook. No modern slang. Spell numbers out in words (the TTS reads text literally). Use plain ASCII apostrophes and quotes.
- **Panels.** Panel ids are `p01`, `p02`, and so on, in reading order. Several lines can share a panel. Every panel id must appear in the brief.
- **Canonical voices.** Kokoro voice names. Never change a recurring character's voice.

| Character | Voice | Character | Voice |
| --- | --- | --- | --- |
| LUCAN | am_fenrir | BRAM | bm_lewis |
| ILSE | bf_isabella | WREN | af_kore |
| TOBIN | am_michael | OSWIN | bm_george |
| HASK | bm_fable | TAMSIN | bf_alice |
| DUNN | am_liam | KELL | am_echo |
| VANCE | bm_daniel | SABINE | bf_emma |
| PELL | am_puck | FATHER (Lord Varr) | am_onyx |
| MARIC | am_adam | YRSA | af_river |
| GARROW | am_onyx (never in a scene with FATHER) | HALVARD | am_santa |
| YSOLDE | bf_lily | PENHALLOW | am_eric |
| MIRELLE | af_heart | ELINOR | af_aoede |
| NELL, CHILD | af_sky | BOY | af_nova |
| MOTHER, GRANNY, villager woman | af_sarah | HERALD, guard, generic man | am_liam, or am_puck if Dunn or Pell is in the scene |

  For a minor character, pick an unused voice from af_alloy, af_bella, af_jessica or af_nicole for women; for men, reuse a male voice that nobody else in that chapter uses. Never put two characters in one chapter on the same voice.

## 2. brief.txt (the Codex panel brief)

The layout is: line 1 `BRIEF: "The Lord Who Measured Zero", Chapter N panel illustrations`, a blank line, the contents of `S/plan/brief_head.txt`, then:

```
- Save every file to: C:\Users\abafa\Videos\LordWhoMeasuredZero\chN\ (create the folder).

FILES (name = filename, size, description):
p01.png 1536x1024: <description>
...
Work through all of them without stopping to ask me anything. When finished, list the saved file paths.
```

- **Sizes.** Use only 1536x1024 (wide), 1024x1536 (tall) or 1024x1024 (square). Mix them: wides for establishing shots and action, talls and squares for faces and dialogue.
- **Descriptions.** One sentence of setting, then who is in the panel (names as on the sheets) and what they are doing, then expression and lighting. Ask for empty space wherever a bubble will go.
- **No text.** Never ask for readable text, letters or signs. Books and maps show "illegible squiggles".
- **Mood and arc notes.** Optional lines before FILES, e.g. "This chapter is a NIGHT BATTLE".
- **Character sheets.** These are listed in `brief_head.txt` (A, B, C, D, E). A new recurring character needs a sheet before any panel draws them. Write a separate `S/plan/sheet_X_brief.txt` modelled on step 1 of `S/ep16/brief.txt`, save path `...\sheets\sheet_X.png`, and add the new sheet line to the header of every brief that uses it. The coordinator dispatches sheet briefs first.
- **Hard rules.** Bram has ONE arm, with the LEFT arm missing. Ash is horse-sized, glossy black, amber eyes, torn ear. Measurers wear navy robes with silver trim and a silver lens. The setting is a medieval northern fantasy.
- **Staging.** After writing, copy the brief to `/mnt/user-data/outputs/briefs/chN_brief.txt`.

## 3. sound_chN.py

```python
"""Chapter N sound."""
def T0(i, pad=0.3): return at(i) - pad
M("tender", 0, T0(5), fade_in=0.8)                      # music cue from t0 to t1
S("candle_fire", 0, 0.1, length=T0(5), fade_out=1.0)    # sound effect at time t
M("dread", T0(5), T0(9), nothing_at=at(7) - T0(5))      # dread hits its stinger at nothing_at (relative)
M("reveal", T0(9), T0(12), hit_at=at(10) - T0(9) + 0.3) # reveal hits at hit_at (relative)
M("outro", T0(LASTIDX), END, fade_in=0.8, fade_out=2.0)
```

- **Timing helpers.**
  - `at(i)` is the start of line i, with i the 0-based index into `lines`.
  - `at(i, f)` is a fraction f through line i.
  - `END` is the end of the audio.
- **Cue rules.** Cues must tile the timeline with no gaps: each `M` starts where the previous one ends. The final cue is always `outro`, starting at the end-card line.
- **Music cues.**
  - realm, triumph, dawn: grand or hopeful
  - tender, sorrow: emotional
  - wry, mockery: comedy and teasing
  - mystery, cold, frost: tension, night, cold
  - dread (needs `nothing_at`), reveal (needs `hit_at`)
  - labour: work and building
  - battle: action
  - outro
- **Sound effects** (in `U/sfx`): candle_fire, coins, crowd_cheer_1, crowd_cheer_2, crowd_gasp, crowd_murmur_1, crowd_murmur_2, dog_growl, dog_whimper, footsteps_stone, heartbeat, magic_shimmer, man_chuckle, paper_rustle_1, stone_crack, sword_draw, wind_winter, wolf_howl_1, wolf_howl_2, woman_laugh_1, woman_laugh_2, wood_creak.
- **Gain.** Ambience 0.08–0.15, effects 0.25–0.45.

## 4. layout_chN.py (vertical strip, 1080 px wide)

Copy the structure of `S/ep17/layout_ch17.py` (day), `S/ep15/layout_ch15.py` (night) or `S/ep18/layout_ch18.py` (mixed). The helpers are injected:

- `img(name, cls='', style='')` places the panel `art/<name>.png`. Placements:
  - wide: `img('p01','full')`, which renders at 1080x720
  - tall: `img('p02','', 'width:720px;height:1080px')` inside a div with `style="margin-left:0"` or `margin-left:330px`
  - square: `img('p03','', 'width:660px;height:660px')` inside a div with `margin-left` 0, 210 or 300
- `bub(text, 'L7', tail, style)` is a speech bubble anchored to line 7. `tail` is `'left'`, `'right'` (tail on the bottom pointing down-left or down-right) or `'up'` (tail on top). Position it absolutely inside the panel's `<div class="rel">`. Put it in the free side space next to a tall or square panel (e.g. `left:-300px;top:400px;width:400px` when the panel sits at margin-left 330), or above or below a wide panel (`bottom:-200px`, `top:-250px`).
- `narr(text, 'L3', style)` is a narration oval. Use it standalone with `margin:0 120px` in the flow, or absolutely inside a panel div, with the anchor left empty (`''`) and `data-a="L3"` on the panel div.
- `sfx(text, style, cls)` is sound-effect lettering over art: `cls` `''` is loud, or `'quiet'`. Use at most 1–3 per chapter, and never over a face.
- `gap(h, bg)` is vertical space. Use `bg` for gradient transitions such as `'linear-gradient(#fff,#0b0d16)'`.
- **Sections.**
  - `<div class="sec white">` holds the chapter header: `<div class="chap"><div class="c0">THE LORD WHO MEASURED ZERO</div><div class="c1">CHAPTER N</div><div class="c2">Title</div></div>`. It is dark text, so it only goes in white.
  - `<div class="sec night">` for night.
  - `<div class="sec black">` for the end card.
- **End card.** Always exactly this, with the last line's index as the anchor:
  ```
  <div class="sec black"><div class="rel" data-a="L<last>" style="margin-left:120px">{img('end','', 'width:840px;height:1260px')}
  <div class="title"><div class="t1">THE LORD<br>WHO MEASURED</div><div class="t2">ZERO</div><div class="t3">CHAPTER <N+1> · COMING SOON</div></div></div>{gap(360)}</div>
  ```
- **Anchors.** Every line index 0..last needs exactly one element with anchor `L<i>`. Optionally add `L<i>b` on a following element to scroll during a long line. Bubbles go in reading order, top to bottom, and left before right.
- **Gaps.** Leave enough gap under a panel for the bubbles that hang below it: usually bubble height plus 100. A bubble's height is roughly 120 + 42 × (number of text lines).
- **Face boxes.** `FACES = {"p01": [(x0, y0, x1, y1), ...]}` in the ORIGINAL PNG's pixel coordinates (1536x1024, 1024x1536 or 1024x1024). Box every visible face, padded by about 25 px. For crowds, box the whole crowd band.
  - To read the coordinates, run `python3 S/ep1/gridsheet.py S/chk/gN.png S/epN/art/p0*.png` and Read the PNG. Each thumbnail has a grid every 128 source px, labelled 256, 512 and so on, and the panel name at the bottom left. Map positions to source pixels with the grid.
- **Build check.** From `S/ep1`, run `python3 strip.py S/epN/art S/fonts S/epN/full S/epN/layout_chN.py`. It must print `OVERLAPS: none`. A FACE overlap means move the bubble. A TEXT OVERLAP means add gap or move one of the pair.
- **Visual check.** Make a preview and Read it to confirm the strip reads well, with no giant empty gaps and no bubble cut off at the page edge:
  ```
  python3 -c "from PIL import Image; im=Image.open('S/epN/full/strip.png'); W,H=im.size; n=4; h=H//n; o=Image.new('RGB',(n*270,h//4),'white'); [o.paste(im.crop((0,k*h,W,(k+1)*h)).resize((270,h//4)),(k*270,0)) for k in range(n)]; o.save('S/chk/sN.jpg',quality=70)"
  ```

## 5. Layout agent workflow for chapter N

1. **Check the art.** List `~/Videos/LordWhoMeasuredZero/chN` with `mcp__remote-devices__device_list_dir`. Every panel named in `S/epN/brief.txt` must be present. If any are missing, wait and retry later, or report back.
2. **Stage the art.** Use `mcp__remote-devices__device_stage_files` with paths like `~/Videos/LordWhoMeasuredZero/chN/p01.png` (at most 50 per call). Files land in `U/chN/` within a few seconds.
3. **Link the art.** `mkdir -p S/epN/art S/epN/full; for f in U/chN/*.png; do ln -sf $f S/epN/art/; done; ln -sf U/ch1_v2/c33.png S/epN/art/end.png`
4. **Check sizes** against the brief.
5. **Review the art.** Flag any panel with visible text or letters, Bram drawn with two arms, a wrong character design, or a broken anatomy or composition. Note the filename for a redraw, but still lay out the chapter with what exists.
6. **Lay out.** Annotate faces, write `layout_chN.py`, iterate until `OVERLAPS: none`, then do the visual check.
7. **Hand off.** `touch S/epN/READY`. The build runner renders and exports automatically. Do NOT start mix or scroll yourself, because the machine has only 2 CPU cores.
8. **Report.** Chapter done, strip height, and any panels needing a redraw, with the reason.

Never touch other chapters' folders, the runners, or the GitHub repo.

## 6. Lessons from Chapters 15–28 (read these)

- **Speaker vs drawing.** If a line is spoken by a minor or generic character, the brief must describe that person so they cannot be mistaken for a named one. For example: "a young bald Measurer with a round face, NOT Hask and NOT Tamsin". Codex otherwise draws the nearest named character, and the viewer then hears the wrong voice from a known face.
- **Spell out numbers** in script text, end cards included: "Chapter thirty-one, coming soon", not "Chapter 31".
- **Length.** Aim for 20–28 lines, about 110–160 s. Chapters under 90 s feel thin.
- **Staging.** Stage at most 15 files per device_stage_files call; bigger calls time out on the last files.
- **Waiting for art (layout agents).** Before staging a chapter, list its PC folder. If panels are still missing, Codex is still drawing: run `sleep 240` in Bash and check again, for up to about 75 minutes. Report the chapter as not ready only after that.
- **Bubble tails** are now placed at 30% of the bubble's width, so wide bubbles are fine.
- **New sheets.** Each new recurring character needs a sheet brief, and the coordinator dispatches sheet briefs before chapter briefs. Existing sheets:
  - A: Lucan, Bram, Ash
  - B: Maric, Father, Sabine, Ilse
  - C: Wren, Tobin, Oswin, Pell
  - D: Vance, King Edric, Mirelle
  - E: Hask, Tamsin, Dunn, Kell
  - F: Yrsa, Garrow, Freydis, the white she-wolf, the frost-wyrm
  - G: Halvard, Ysolde, Penhallow, Agna (the Saltmouth elder), and the pups Rook, Birk and Tarn
- **Voices added by the Season 1 writers.**
  - FREYDIS af_alloy, RUNE af_nova, AGNA af_bella, RESSA af_alloy
  - MAGISTRATE af_jessica, FACTOR and HOLT bm_fable, ALDO am_echo, RIDER am_puck
  - Corvin returns in Season 2: CORVIN am_santa. He is never in a scene with HALVARD; if he is, CORVIN uses am_puck.
- **Season 2+ voices.** Never cast two of these in the same chapter on the same voice.

| Character | Voice |
| --- | --- |
| KING EDRIC | am_echo (Kell is in the north) |
| CADDOC | am_liam (Dunn is dead) |
| AURELIO | am_eric (never with Penhallow) |
| STANE | am_puck (never with Pell) |
| CORVIN | am_santa (never with Halvard) |
| generic capital man | am_michael (never with Tobin) |
| MIRELLE | af_heart |
| ELINOR | af_aoede |
| NELL | af_sky |
| Lowmarket woman | af_nicole |
| Ashby elder | af_jessica |

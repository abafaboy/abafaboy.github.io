# The Lord Who Measured Zero: handoff to Abafadot / Codex

From now on you run production of this manhwa series end to end. Claude built the pipeline and the plan. Abafa wants the remaining work done on this PC, by you and by Codex sessions you start.

This branch (`manhwa-pipeline` of github.com/abafaboy/abafaboy.github.io) contains everything:

| Path | Contents |
| --- | --- |
| `plan/series_plan.md` | The 222-chapter plan: arcs, rules, secrets, side-quest ledger |
| `plan/story_bible_canon.txt` | Canon, power system, characters |
| `plan/PIPELINE.md` | All conventions: script, brief, sound, layout formats; canonical voice table; lessons. Read it fully. Its paths are from Claude's Linux box; use the Windows equivalents below. |
| `plan/brief_head.txt`, `plan/sheet_*_brief.txt` | Codex brief header and character-sheet briefs |
| `chapters/chNNN/` | One folder per chapter: `script.json`, `brief.txt`, `sound.py`, and `layout.py` once laid out. `STATUS_BUILT` means the video is finished. |
| `tools/` | strip.py (layout to strip + face/overlap check), tts.py (Kokoro voices), mix.py + music.py + cues.py (score and SFX), scroll.py (1080x1920 video), build_chapter.py (all of it in one command), site_export.py (website), gridsheet.py |
| `assets/fonts`, `sf/` | Lettering fonts and the music instrument samples |

## Folders on this PC

- `C:\Users\abafa\Videos\LordWhoMeasuredZero\` (VID) holds the art folders `chN\`, `sheets\`, `style_refs\`, `sfx\`, `final\` (finished vertical videos), `volumes\` and `briefs\`.
- Clone this branch to `VID\pipeline` (the repo root; `config.json` is there).
- Clone `main` of the same repo to `VID\site`. That is the GitHub Pages site, and the reader lives in `site\manhwa\` (https://abafaboy.github.io/manhwa/).

## One-time setup

```
cd C:\Users\abafa\Videos\LordWhoMeasuredZero
git clone -b manhwa-pipeline https://github.com/abafaboy/abafaboy.github.io pipeline
git clone https://github.com/abafaboy/abafaboy.github.io site
cd pipeline
py -m pip install -r requirements.txt
py -m playwright install chromium
mkdir dl
curl -L -o dl\kokoro-v1.0.int8.onnx https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.int8.onnx
curl -L -o dl\voices.bin https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin
```

- ffmpeg is already installed (winget Gyan.FFmpeg).
- Check that `git push` works from `site`. If it isn't authenticated, run `gh auth login` once (Abafa may need to click through it).

## Per-chapter loop

1. **Art.**
   - If `VID\chN\` lacks panels, start a Codex session with: "Read `VID\pipeline\chapters\chNNN\brief.txt` and follow it exactly…" The briefs are also copied in `VID\briefs\chN_brief.txt`.
   - Generate character-sheet briefs first when a brief lists a sheet that doesn't exist yet in `VID\sheets\`:
     - `sheet_G` (Halvard, Ysolde, Penhallow, Agna, the pups) is needed from Ch 43. Check it exists.
     - `sheet_H` (Caddoc, Corvin, Aurelio, Stane, the Hounds) is needed from Ch 61.
     - `sheet_I` (Elinor, Nell, the Lowmarket foreman, Edda) is needed from Ch 83.
   - **Save PNGs as plain files, never hardlinks.**
2. **Layout.** Write `chapters\chNNN\layout.py`, following PIPELINE.md section 4 and the existing finished layouts. Good models are ch017, ch022, ch025, ch028 and ch031.
   - **Face boxes.** In `FACES`, give the box of every visible face, in the panel PNG's own pixel coordinates. You drew the panels, so look at each one.
   - **Bubbles and narration.** Speech bubbles and narration ovals must never cover a face.
   - **Check.** Run `py tools\build_chapter.py N --strip-only` until it prints `OVERLAPS: none`, then open `chapters\chNNN\full\preview.jpg` and look at it.
   - **Drafts.** ch029, ch030 and ch033 already have draft layouts with most face boxes. Add boxes for the panels marked missing (p14–p18 in ch29; p04, p05, p07 and p10–p17 in ch30; p01–p02 in ch33), and re-check the bubble positions near them.
3. **Build.** Run `py tools\build_chapter.py N`. It voices the chapter (Kokoro, voices from script.json), mixes music and SFX, renders the 1080x1920 video into `VID\final\`, records the end-card cut in `VID\briefs\volume_cuts.json`, and exports the chapter to `site\manhwa\`.
4. **Publish.** In `VID\site`, run `git add manhwa && git commit -m "Add chapter N" && git push`. Also commit any changed `chapters\chNNN\layout.py` to the pipeline branch.
5. **Volumes.** Every 30 or so chapters, aligned to arcs, run `py VID\make_volume.py FIRST LAST VOL`. It cuts the "coming soon" end cards except on the last chapter.
   - Volume 1 is Ch 1–28.
   - Volume 2 is Ch 29–60, the Season 1 finale.
   - Volume 3 is Ch 61–94.
   - Volume 4 is Ch 95–120.
   - Volume 5 is Ch 121–158.
   - Volume 6 is Ch 159–196.
   - Volume 7 is Ch 197–222.

## Status at handoff (17 Oct 2026, 02:30)

- **Finished videos, in `final\`:** Ch 1–28, 31, 32 and 46. Chapters 15–28, 31, 32 and 46 are also exported to the website; Ch 1–28 are pushed live.
- **Art finished, layout needed:** Ch 29, 30 and 33 (drafts exist), and probably 34–35 (check the folders).
- **Written, needing art:** Ch 36–60 (Season 1 rest), 61–108 (Season 2) and 109–134 (Season 2 finale + Season 3 opener).
- **Still to write:** Ch 135–222. Follow `plan/series_plan.md` and PIPELINE.md sections 1–3 (formats, voices, lessons). Chapters run 20–28 lines, about 110–160 s, Lucan narrating in first person past tense, with a hook at the end of every chapter. Keep every plan beat, plant and payoff. Read the previous 2–3 chapters first for continuity.

## Quality rules (Abafa's)

- **Bubbles.** Never put a bubble or narration over a face. Bubbles are oval, manhwa style.
- **Voices.**
  - Kokoro at natural speed with no pitch change.
  - Lucan is am_fenrir.
  - Never change a recurring character's voice. See the voice table in PIPELINE.md.
- **Music and sound.** Medieval music that changes with the mood, plus sound effects.
- **Character consistency.**
  - Characters stay consistent with the sheets unless they grow or get more muscular.
  - Bram has ONE arm; the LEFT one is missing.
  - Ash is horse-sized, black, with amber eyes and a torn ear.
- **Style references.** Use them for style only. Never copy their characters.
- **No text in art.** No text in generated art. Books show squiggles.
- **Speaker identity.** A speaking minor character must not be drawn to look like a named character.

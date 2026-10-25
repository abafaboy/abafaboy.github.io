# Publishing plan: YouTube

## Current instruction (Abafa, 25 October 2026, 18:12 Dubai time, after watching chapter 1)
> "holy this is great. i approve. as soon as you make around 30 chapters, upload it as a longform youtube video for public view. i trust you now"

- **What:** the first ~30 chapters as ONE long-form narrated 16:9 video, published **Public** on the channel Abafaboy (@AbafaboyGames, UCFgwXHmeW-ntGBdrior1YqA). This replaces the earlier "all 100 chapters in one video" plan for the first release; chapters 1–100 can still follow as a later compilation.
- **Where it ends (decision):** chapter 33, the Arc 4 finale ("Your head is S-rank. Your body is garbage."), the arc ending nearest 30 (`ARC3_4_BEATS.md`).
- **Approval:** he pre-approved publishing this video publicly ("upload it ... for public view. i trust you now"). That replaces the old "show him the title, thumbnail and visibility and wait for his OK" step for this video. Still send him the link the moment it is live.
- **Before upload:**
  - re-check the Blambot font licence for a public video (see below); the channel has 14 subscribers and is not monetised, which the free terms cover more clearly than a monetised one, but check the current terms;
  - chapter 1's P09, P21 and P22 redrawn for scale and perspective (`codex/CH001_FIXES.md`), then chapter 1 re-lettered and re-rendered;
  - run the format checks: no chapter cards between chapters, one narrator, title in the recap style with the manhwa's name, the Lyra thumbnail.
- **Per-chapter previews:** each finished chapter also goes up as an **Unlisted** video so he can read along (chapter 1: https://youtu.be/HLKuVxv0gIA, uploaded 25 October 2026).
- **Upload route** (learned on chapter 1): Studio's file picker is a native dialog the browser tools can't drive, so the file goes in through the page itself in 10 MB pieces from the container (`file_upload` into a hidden input, reassembled in the page). For a multi-hour compilation, encode at a size that keeps this practical (visually lossless for YouTube's re-encode, checked by PSNR against the master), and never hash the whole file inside the page (that froze the renderer at 588 MB).

## Season one: how it ships (written 25 October 2026, while the laptop is off)

**Font licence (checked 25 Oct 2026, blambot.com/pages/licenses).** Blambot's free "Non-profit/Indie Comics Use" fonts, Anime Ace among them, may be used by independent comic creators "in print, flattened into web graphics, on merchandise directly supporting your indie comic" and in videos "directly promoting your indie comic", "even if you are making money with your project". Our lettering is flattened into the comic's own pages and the video presents that comic, so it is covered. To keep the question off the thumbnail, its words use Anton (SIL Open Font License, free for any use). If the channel ever becomes a business, Blambot's paid Basic Desktop licence settles it for good.

**AI disclosure.** YouTube asks for the "altered or synthetic content" label only for realistic content (a real person saying something they didn't, a real place or event changed, a realistic scene that never happened). It says creators "don't need to disclose non-realistic content that's made with AI", such as a fully animated video (support.google.com/youtube/answer/14328491, checked 25 Oct 2026). An illustrated manhwa with a narrator is non-realistic, so the answer is No.

**Encode settings (measured 25 Oct 2026).** `tools/recap_video.py` renders 2560x1440 at 30 fps, x264 CRF 16, tune animation, a keyframe every 10 s (`--gop 300`), BT.709. On a 30-second stretch of chapter 1 (holds and pans) against its CRF 12 master:

| Keyframes | CRF 14 | CRF 16 | CRF 18 |
|---|---|---|---|
| every 10 s | 6.8 Mbps, 52.9 dB | **5.0 Mbps, 51.4 dB** | 3.7 Mbps, 49.6 dB |
| every 2 s | 8.5 Mbps, 53.4 dB | 6.4 Mbps, 51.8 dB | |
| every 0.5 s (YouTube's suggestion) | | about 11 Mbps (60 s test: 11.2 Mbps, 50.6 dB) | |

Above 50 dB the difference from the master can't be seen, and YouTube re-encodes everything anyway. Ten-second keyframes cost nothing visible because the art holds still most of the time. A season of about 165 minutes comes to about 6 GB, which the page-upload route can carry. The container's disk is tight: before the season join, free about 13 GB by deleting the old story's renders (`/home/claude/flight`, `/home/claude/flightrepo`, the scratchpad's `ep1`, `flight*` and test folders).

**Steps, per chapter (as each chapter's art is reviewed and approved):**
1. Letter: `tools/autostrip2.py scripts_v2/chNNN.yaml ART OUT --dpr 2`.
2. Render: `tools/recap_video.py OUT recaps_v2/chNNN.json --chapter N` (the settings above are its defaults).
3. Upload `recap.mp4` to YouTube as **Unlisted**, titled `My Summons Go First · Chapter N: <title>`, and add the link to the table at the end of this file.

**Steps, at chapter 33:**
1. Chapter 1 redrawn (P09, P21, P22), re-lettered and re-rendered with the season settings.
2. `tools/longform_build.py --chapters 1-33 --name MSGF_S1` joins the chapters without re-encoding (they share settings), rebuilds the narration track in sync, adds MP4 chapter markers and writes the YouTube timestamps.
3. Thumbnail: Codex draws the key art (`codex/THUMBNAIL_BRIEF.md`, chat T1); `tools/thumbnail_text.py` crops it to 16:9 and adds the words (for example OPERATOR, with an arrow to Jaeha, and a "1-33" tag). Lyra's face, smile and bow are the focal point, never her body (YouTube's thumbnail rule above).
4. Upload as **Public** through YouTube Studio in Abafa's Chrome. Settings: not made for kids; altered content No; category Film & Animation; language English; the timestamps in the description (they become YouTube chapters); the thumbnail. Send Abafa the link the moment it is live.

**Title** (recap style, with the manhwa's name; under 100 characters). First choice:
> [1-33] The F-Rank BAIT Every Guild Sent In First Became an OPERATOR | My Summons Go First

Alternatives: "[1-33] Hunters Used Him as Bait... Now His Summons Walk In First | My Summons Go First"; "[1-33] Guilds Sent the F-Rank BAIT In First... Until His Summons Did | My Summons Go First".

**Description** (the timestamps come from `MSGF_S1_description.txt`):
> Kang Jaeha is an F-rank trap-tester: the man hunter guilds send into a gate first, so the traps hit him instead of them. Then a raid leader locks him in with a boss to die, and he wakes up as something the system calls an Operator. His summons go first now. A goblin scout who never got to come home, a mossy giant who holds doors, a river archer who loves applause. And his one rule: everyone comes back.
>
> My Summons Go First, season one: chapters 1-33, narrated. An original manhwa by Abafaboy.
>
> 0:00 Chapter 1: Bait
> ...
>
> #manhwa #manhwarecap #webtoon #summoner #system

## Earlier plan (21 October 2026, kept for reference)

When all 100 chapters are done, upload them to YouTube through YouTube Studio in Abafa's own browser (Claude in Chrome). Use the channel **abafaboy games**, and put the manhwa's name in the title.

## Style he pointed to (YouTube search for "manhwa", screenshot sent 21 Oct 2026)
- **Titles.** A hook sentence about the hero's power, cut off with "...". Some carry a chapter-range or completeness tag. Examples:
  - "[FULL] He Unlocked the Survival System..."
  - "[1-102] He Only Tames the WEAKEST..."
  - "He Became a Bacteria Necromancer, and N..."
  - "A Medical Student Unlocked an SSS Sy..."
- **Thumbnails.** 16:9 and very saturated. The hero in the foreground, often with a before/after split or a power effect. Big outlined yellow or white words: FULL, SSS, BEFORE / AFTER, CH.1-102, #1-250, DAY 01 / DAY 365.
- **Format.** Long narrated compilations (about 1 to 19 hours) covering many chapters.

## Thumbnails: an attractive woman (Abafa, 25 October 2026)
- **His finding:** "the youtube thumbnails with an attractive woman do well". He sent two examples:
  - "#1 NECROMANCER Reincarnates As POWERLESS But Can STEAL ANY..." (Frieren Manhwa, 174K views in 22 hours, 3:43:50). The hero leans over a white-haired woman pinned to a wall; big yellow labels with arrows: ANGEL and SS-RANK HUNTER.
  - The recap he pointed to for the acting study ("He Activated a System That Summons Monsters...", Tyler's Manhwa, 3:46:32). A panicking hoodie hero labelled SUMMONER stands beside his summons: a horned winged demon woman, a green hooded goblin with a giant sword, and a white-haired woman knight, all on glowing summoning circles in his bedroom.
- **The formula:** custom key art, not a panel from the chapter. One big label word with an arrow; the hero reacting; an attractive adult woman as large as the hero.
- **For us:** an attractive adult woman goes into the MSGF thumbnail.
  - **Abafa chose Lyra,** the river archer summon (25 October).
  - He wants her "similar on the attractiveness to the thumbnail i sent u since it obviously works". Her design is in `codex/CHARACTER_DESIGNS_v2.md` 2.10, and her sheet is drawn early (S14).
  - He was told about the age-restriction risk below and chose this level.
- **YouTube's limit** (Thumbnails policy, support.google.com/youtube/answer/9229980, checked 25 Oct 2026):
  - Thumbnails can't show nudity or sexually gratifying imagery.
  - Where breasts, buttocks or genitals are the focal point, or the pose or clothing is meant to arouse, YouTube may age-restrict the video or remove the thumbnail.
  - An age restriction on a 12-hour compilation would cut its reach, so the focal point stays on faces, the pose and the conflict.
- **Never** Kang Seoa, who is 15.

## Format (confirmed by Abafa, 21 October 2026)
- Chapters 1–100 together in one large video.
- It is a long narrated 16:9 compilation, titled "[1-100] ..." with the name My Summons Go First, with a thumbnail in the style above.

## Channel (checked in YouTube Studio through Claude in Chrome, 21 Oct 2026)
- Abafa's Chrome is signed in to YouTube Studio on the channel "Abafaboy", handle @AbafaboyGames (channel id UCFgwXHmeW-ntGBdrior1YqA).
- Feature eligibility: standard and intermediate features are enabled and the phone number is verified, so uploads longer than 15 minutes are allowed. Advanced features show "can be enabled".

## YouTube limits (YouTube Help, answer 71673, checked 21 Oct 2026)
- The maximum upload is 256 GB or 12 hours, whichever is smaller.
- Uploads are limited to 15 minutes until the Google account is phone-verified.
- If the narrated 1–100 cut runs over 12 hours, tell Abafa before cutting anything. The options are tightening the pacing, or splitting it into Part 1 and Part 2.

## Before publishing
- Publishing is public: show Abafa the title, the thumbnail and the visibility settings, and wait for his OK before clicking Publish.
- Font licence: Blambot's free terms cover indie comics flattened into images, and promotional videos for them. A monetised full-chapter video is not clearly covered. Check this, or get Blambot's commercial licence, before upload.
- Never upload the font files anywhere.

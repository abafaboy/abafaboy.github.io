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

# Narrator recaps for the rebuilt story (v2)

One file per chapter: a JSON list of `{"panel": "<id>", "text": "<narration>"}` in reading order, read by `tools/recap_video.py` (voice am_michael, speed 1.2, gap 0.08, 2560x1440 at 30 fps).

- One narrator, recap-channel pace: about 800–900 words for a 60-panel chapter.
- Every panel id must have art. Never use caption or title panels (P08, P25 and P59 in chapter 1).
- The order never goes backwards: the camera only scrolls down.
- The old story's recaps stay in `recaps/` and are not used for the rebuild.

## Rendering and delivery
- Render: `tools/recap_video.py OUT_DIR recaps_v2/chNNN.json --chapter N` (2560x1440, 30 fps, x264 CRF 16, a keyframe every 10 s, preset medium). The camera frames each panel with its bubbles, holds while the entry is read, pans slowly through tall panels and moves only between entries.
- Names are respelled for the narrator's ear by `tools/pron.py` (Jaeha is said "Jay-ha", Seoa "Suh-ah", Baek "Beck", and so on, following `NAME_SHEET.md`). The recap files keep the real spellings.
- `tools/precache_tts.py recaps_v2/ch*.json` voices every entry ahead of time into the cache the renderer reads.
- Season settings (25 October 2026): CRF 16 with 10-second keyframes came to 5.0 Mbps at 51.4 dB PSNR against chapter 1's CRF 12 master, where YouTube's half-second keyframes need about 11 Mbps for the same CRF. Chapter 1's first render (CRF 12, half-second keyframes) was 561 MiB for 4 min 36 s; at the season settings a chapter is about 170-200 MB.
- The season video is joined from the chapter files without re-encoding by `tools/longform_build.py`.

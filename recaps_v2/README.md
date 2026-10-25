# Narrator recaps for the rebuilt story (v2)

One file per chapter: a JSON list of `{"panel": "<id>", "text": "<narration>"}` in reading order, read by `tools/recap_video.py` (voice am_michael, speed 1.2, gap 0.08, 2560x1440 at 30 fps).

- One narrator, recap-channel pace: about 800–900 words for a 60-panel chapter.
- Every panel id must have art. Never use caption or title panels (P08, P25 and P59 in chapter 1).
- The order never goes backwards: the camera only scrolls down.
- The old story's recaps stay in `recaps/` and are not used for the rebuild.

## Rendering and delivery
- Render: `tools/recap_video.py OUT_DIR recaps_v2/chNNN.json --chapter N` (2560x1440, 30 fps, x264 CRF 12, preset medium). The camera frames each panel with its bubbles, holds while the entry is read, pans slowly through tall panels and moves only between entries.
- Chapter 1 came to 561 MiB for 4 min 36 s (about 17 Mbps). The chat upload limit is 500 MiB, so a chapter over it is split losslessly (`ffmpeg -c copy`) at a keyframe on a narration boundary near the middle. Keyframes come every 0.5 s (GOP 15), so the cut lands within a frame of the pause. The parts are never re-encoded.

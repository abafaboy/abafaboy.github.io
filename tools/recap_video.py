#!/usr/bin/env python3
"""recap_video: one-narrator recap video of a lettered chapter, horizontal 16:9 like manhwa recap channels.

The lettered strip scrolls in the middle of the frame; the sides show a blurred, dimmed copy of the same view.
While an entry is read the view holds on its panel framed with its lettering (bubbles, inner voice, notes), or pans
slowly down through it when panel and lettering are taller than the view; between entries it eases down the strip. No chapter
announcements and no title or end cards, so chapters join into one continuous video.

Image quality (owner, 25 October: "make sure no images look compressed ever in the manhwa"):
- 2560x1440 at 30 fps by default, H.264 High profile, 2 consecutive B-frames, closed GOP, 4:2:0, AAC-LC at 48 kHz
  (YouTube's recommended SDR upload settings, support.google.com/youtube/answer/1722171), except the keyframe interval.
- The strip comes from autostrip2 at 2x (layout.json "scale"), so the frame is always a DOWNSCALE of the strip
  (area filter); an upscale, if ever needed, uses Lanczos. Lossless inputs only: strip.png or the lossless
  NNN.webp segments; a JPEG strip is refused.
- x264 CRF 16 with -tune animation and a keyframe every 10 s (season settings, 25 October 2026). Measured on chapter 1
  against its CRF 12 master: 5.0 Mbps at 51.4 dB PSNR, where CRF 16 with YouTube's half-second GOP needs about 11 Mbps
  (the art holds still most of the time, so keyframes were most of the bits). That keeps a 33-chapter season near 6 GB,
  small enough to upload through the browser. BT.709 matrix and tags, and a fixed +-1 level dither on the blurred side
  panels so their smooth dark gradients do not band after YouTube's re-encode.

Inputs: OUT_DIR from autostrip2 (strip.png or segments + layout.json), recap/chNNN.json ([{"panel", "text"}]), Kokoro.
Output: OUT_DIR/recap.mp4

usage: recap_video.py OUT_DIR RECAP.json --chapter N [--voice am_michael] [--speed 1.2]
"""
import argparse
import hashlib
import json
import subprocess
from pathlib import Path

import cv2
import numpy as np
import soundfile as sf

SR = 24000


def load_strip(OUT, lay):
    """The lossless strip: strip.png, or the lossless WebP segments stacked in order. Never a JPEG."""
    sp = OUT / "strip.png"
    if sp.exists():
        img = cv2.imread(str(sp), cv2.IMREAD_COLOR)
        if img is not None:
            return img
    segs = lay.get("segments") or []
    if segs and all((OUT / s[0]).exists() for s in segs):
        parts = [cv2.imread(str(OUT / s[0]), cv2.IMREAD_COLOR) for s in segs]
        if all(p is not None for p in parts):
            return np.vstack(parts)
    if (OUT / "strip.jpg").exists():
        raise SystemExit("only a JPEG strip (lossy) is here: re-letter the chapter so strip.png or the lossless segments exist")
    raise SystemExit("strip.png missing")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("recap")
    ap.add_argument("--chapter", type=int, required=True)
    ap.add_argument("--models", default="/tmp/claude-0/-home-claude/74687d11-0cc0-5bfd-9d7d-ad4189ed4d7b/scratchpad/dl")
    ap.add_argument("--voice", default="am_michael")
    ap.add_argument("--speed", type=float, default=1.2)
    ap.add_argument("--gap", type=float, default=0.08, help="silence between entries (s)")
    ap.add_argument("--w", type=int, default=2560)
    ap.add_argument("--h", type=int, default=1440)
    ap.add_argument("--view", type=float, default=880, help="layout px of strip shown top to bottom")
    ap.add_argument("--fps", type=int, default=30)
    ap.add_argument("--crf", type=float, default=16)
    ap.add_argument("--gop", type=int, default=300, help="keyframe interval in frames (0 = half the frame rate)")
    ap.add_argument("--preset", default="medium")
    ap.add_argument("--max-seconds", type=float, default=0, help="render only the first N seconds (tests)")
    A = ap.parse_args()
    OUT = Path(A.out)
    lay = json.loads((OUT / "layout.json").read_text(encoding="utf-8"))
    rec = json.loads(Path(A.recap).read_text(encoding="utf-8"))
    pan = {p["id"]: p for p in lay["panels"]}
    k_ = float(lay.get("scale", 1))  # strip pixels per layout pixel
    strip = load_strip(OUT, lay)
    wl = int(round(float(lay.get("width", strip.shape[1] / k_)) * k_))
    if strip.shape[1] > wl:
        strip = strip[:, :wl]  # drop any white padding right of the lettered strip
    H = strip.shape[0]
    W0 = strip.shape[1]
    vh = int(round(A.view * k_))  # strip pixels shown top to bottom
    sc = A.h / vh
    cw = int(round(W0 * sc)) // 2 * 2  # centre column width on screen
    x0 = (A.w - cw) // 2
    interp = cv2.INTER_AREA if sc <= 1 else cv2.INTER_LANCZOS4

    from kokoro_onnx import Kokoro
    k = Kokoro(str(Path(A.models) / "kokoro-v1.0.int8.onnx"), str(Path(A.models) / "voices.bin"))
    import os
    cache = Path(os.environ.get("TTS_CACHE", "/home/claude/flight/tts_cache"))
    cache.mkdir(parents=True, exist_ok=True)
    lang = "en-gb" if A.voice.startswith("b") else "en-us"

    from pron import respell  # names spelled for the narrator's ear (pron.py); the recap text itself is unchanged

    def say(text):
        text = respell(text)
        h = cache / (hashlib.sha1(f"{A.voice}|{A.speed}|{text}".encode()).hexdigest() + ".npy")
        if h.exists():
            return np.load(h)
        s, sr = k.create(text, voice=A.voice, speed=A.speed, lang=lang)
        assert sr == SR
        a = np.asarray(s, dtype=np.float32)
        np.save(h, a)
        return a

    # every voiced line (bubble, inner voice, note) belongs to a panel: the camera frames the panel with its lettering
    ext = {}
    for ln in lay.get("lines") or []:
        a0, b0 = ext.get(ln.get("panel_id"), (1e12, -1e12))
        ext[ln.get("panel_id")] = (min(a0, ln["y_top"]), max(b0, ln["y_bottom"]))
    clamp = lambda y: float(min(max(y, 0), max(H - vh, 0)))
    margin = 24 * k_

    def span_for(pid):
        """(top at the start of the entry, top at its end), in strip px. The panel and its lettering fit: one held
        framing, centred. Taller than the view: start with the top (the first bubble) and pan slowly down to the bottom."""
        p = pan.get(pid)
        if not p:
            return None
        a0, b0 = ext.get(pid, (p["y_top"], p["y_bottom"]))
        u0, u1 = min(p["y_top"], a0) * k_, max(p["y_bottom"], b0) * k_
        if u1 - u0 + 2 * margin <= vh:
            y = clamp((u0 + u1) / 2 - vh / 2)
            return y, y
        return clamp(u0 - margin), clamp(u1 + margin - vh)

    audio, keys, t, missing = [], [], 0.0, 0
    for e in rec:
        sp = span_for(str(e.get("panel", "")))
        if sp is None:
            missing += 1
            if not keys:
                continue
            sp = (keys[-1][1], keys[-1][1])
        a = say(str(e["text"]).strip())
        dur = len(a) / SR + A.gap
        y0, y1 = sp
        t0 = t + 0.45 if keys else 0.0  # arrive early in the entry (the move starts as the last entry ends)
        if keys:
            y0 = max(y0, keys[-1][1])  # never scroll back up
        y1 = max(y1, y0)
        keys.append((t0, y0))
        t1 = t + dur - 0.35
        if t1 > t0 + 0.15:  # hold the framing (or pan slowly through a tall panel) while the entry is read
            keys.append((t1, y1))
        audio += [a, np.zeros(int(SR * A.gap), np.float32)]
        t += dur
    if not keys:
        raise SystemExit("no recap entry matches a panel")
    total = t + 0.3
    if A.max_seconds:
        total = min(total, A.max_seconds)
    sf.write(str(OUT / "recap.wav"), np.concatenate(audio + [np.zeros(int(SR * 0.3), np.float32)]), SR)

    kt = np.array([q[0] for q in keys])
    ky = np.array([q[1] for q in keys])

    def view_at(tt):
        i = np.searchsorted(kt, tt) - 1
        if i < 0:
            return ky[0]
        if i >= len(kt) - 1:
            return ky[-1]
        a, b = kt[i], kt[i + 1]
        u = 0.0 if b <= a else (tt - a) / (b - a)
        u = u * u * (3 - 2 * u)
        return ky[i] + (ky[i + 1] - ky[i]) * u

    gop = A.gop if A.gop > 0 else max(1, A.fps // 2)
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{A.w}x{A.h}", "-r", str(A.fps), "-i", "-",
           "-i", str(OUT / "recap.wav"),
           "-vf", "scale=out_color_matrix=bt709:out_range=tv:flags=lanczos+accurate_rnd+full_chroma_int,format=yuv420p",
           "-c:v", "libx264", "-preset", A.preset, "-tune", "animation", "-crf", str(A.crf), "-profile:v", "high",
           "-g", str(gop), "-keyint_min", str(min(gop, max(1, A.fps // 2))), "-bf", "2", "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709",
           "-c:a", "aac", "-ar", "48000", "-b:a", "128k", "-shortest", "-movflags", "+faststart", str(OUT / "recap.mp4")]
    ff = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    pad = np.full((vh, W0, 3), 255, np.uint8)
    # side panels: a blurred, dimmed copy of the view, from a 1/16 copy of the strip (cheap), dithered by +-1 level
    q = 16
    thumb = cv2.resize(strip, (max(1, W0 // q), max(1, H // q)), interpolation=cv2.INTER_AREA)
    tpad = np.full((max(1, vh // q), thumb.shape[1], 3), 255, np.uint8)
    dither = np.random.default_rng(7).uniform(-1.0, 1.0, (A.h, A.w, 3)).astype(np.float32)
    frame = np.zeros((A.h, A.w, 3), np.uint8)
    last_y = None
    for f in range(int(total * A.fps)):
        y0 = int(round(view_at(f / A.fps)))
        if y0 != last_y:  # held frames reuse the previous image
            crop = strip[y0:y0 + vh]
            if crop.shape[0] < vh:
                crop = np.vstack([crop, pad[: vh - crop.shape[0]]])
            tc = thumb[y0 // q: y0 // q + max(1, vh // q)]
            if tc.shape[0] < tpad.shape[0]:
                tc = np.vstack([tc, tpad[: tpad.shape[0] - tc.shape[0]]])
            small = cv2.resize(tc, (16, 9), interpolation=cv2.INTER_AREA).astype(np.float32) * 0.45
            bg = cv2.resize(small, (A.w, A.h), interpolation=cv2.INTER_CUBIC)
            cv2.add(bg, dither, dst=bg)
            frame[:] = cv2.convertScaleAbs(bg)  # rounds and saturates to 0-255
            frame[:, x0:x0 + cw] = cv2.resize(crop, (cw, A.h), interpolation=interp)
            last_y = y0
        ff.stdin.write(frame.data)
    ff.stdin.close()
    ff.wait()
    print(f"ch{A.chapter}: {len(rec)} entries, {missing} without a panel, {total / 60:.1f} min, {A.w}x{A.h}@{A.fps} "
          f"(strip x{k_:g}, view {vh}px, frame scale {sc:.3f}) -> {OUT / 'recap.mp4'}")


if __name__ == "__main__":
    main()

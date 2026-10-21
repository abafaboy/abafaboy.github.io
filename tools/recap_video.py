#!/usr/bin/env python3
"""recap_video: one-narrator recap video of a lettered chapter, horizontal 16:9 like manhwa recap channels.

The lettered strip scrolls in the middle of the frame; the sides show a blurred, dimmed copy of the same view.
While an entry is read the view settles on its panel; between entries it eases down the strip. No chapter
announcements and no title or end cards, so chapters join into one continuous video.

Inputs: OUT_DIR from autostrip2 (strip.png + layout.json), recap/chNNN.json ([{"panel", "text"}]), Kokoro models.
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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("recap")
    ap.add_argument("--chapter", type=int, required=True)
    ap.add_argument("--models", default="/tmp/claude-0/-home-claude/74687d11-0cc0-5bfd-9d7d-ad4189ed4d7b/scratchpad/dl")
    ap.add_argument("--voice", default="am_michael")
    ap.add_argument("--speed", type=float, default=1.2)
    ap.add_argument("--gap", type=float, default=0.08, help="silence between entries (s)")
    ap.add_argument("--w", type=int, default=1280)
    ap.add_argument("--h", type=int, default=720)
    ap.add_argument("--view", type=int, default=880, help="strip pixels shown top to bottom")
    ap.add_argument("--fps", type=int, default=24)
    A = ap.parse_args()
    OUT = Path(A.out)
    lay = json.loads((OUT / "layout.json").read_text(encoding="utf-8"))
    rec = json.loads(Path(A.recap).read_text(encoding="utf-8"))
    pan = {p["id"]: p for p in lay["panels"]}
    H = int(lay["height"])
    sp = OUT / "strip.png" if (OUT / "strip.png").exists() else OUT / "strip.jpg"
    strip = cv2.imread(str(sp), cv2.IMREAD_COLOR)
    if strip is None:
        raise SystemExit("strip.png missing")
    if strip.shape[1] > int(lay.get("width", strip.shape[1])):
        strip = strip[:, : int(lay["width"])]  # drop any white padding right of the lettered strip
    W0 = strip.shape[1]
    vh = A.view
    sc = A.h / vh
    cw = int(round(W0 * sc)) // 2 * 2  # centre column width on screen
    x0 = (A.w - cw) // 2

    from kokoro_onnx import Kokoro
    k = Kokoro(str(Path(A.models) / "kokoro-v1.0.int8.onnx"), str(Path(A.models) / "voices.bin"))
    import os
    cache = Path(os.environ.get("TTS_CACHE", "/home/claude/flight/tts_cache"))
    cache.mkdir(parents=True, exist_ok=True)
    lang = "en-gb" if A.voice.startswith("b") else "en-us"

    def say(text):
        h = cache / (hashlib.sha1(f"{A.voice}|{A.speed}|{text}".encode()).hexdigest() + ".npy")
        if h.exists():
            return np.load(h)
        s, sr = k.create(text, voice=A.voice, speed=A.speed, lang=lang)
        assert sr == SR
        a = np.asarray(s, dtype=np.float32)
        np.save(h, a)
        return a

    def top_for(pid):
        p = pan.get(pid)
        if not p:
            return None
        c = (p["y_top"] + p["y_bottom"]) / 2
        return float(min(max(c - vh / 2, 0), max(H - vh, 0)))

    audio, keys, t, missing = [], [], 0.0, 0
    for e in rec:
        y = top_for(str(e.get("panel", "")))
        if y is None:
            missing += 1
            if not keys:
                continue
            y = keys[-1][1]
        if keys:
            y = max(y, keys[-1][1])  # never scroll back up
            keys.append((t + 0.5, y))
        else:
            keys.append((0.0, y))
        a = say(str(e["text"]).strip())
        audio += [a, np.zeros(int(SR * A.gap), np.float32)]
        t += len(a) / SR + A.gap
    if not keys:
        raise SystemExit("no recap entry matches a panel")
    total = t + 0.3
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

    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{A.w}x{A.h}", "-r", str(A.fps), "-i", "-",
           "-i", str(OUT / "recap.wav"), "-c:v", "libx264", "-preset", "veryfast", "-crf", "26", "-pix_fmt", "yuv420p",
           "-c:a", "aac", "-b:a", "128k", "-shortest", "-movflags", "+faststart", str(OUT / "recap.mp4")]
    ff = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    pad = np.full((vh, W0, 3), 255, np.uint8)
    frame = np.zeros((A.h, A.w, 3), np.uint8)
    for f in range(int(total * A.fps)):
        y0 = int(round(view_at(f / A.fps)))
        crop = strip[y0:y0 + vh]
        if crop.shape[0] < vh:
            crop = np.vstack([crop, pad[: vh - crop.shape[0]]])
        small = cv2.resize(crop, (16, 9), interpolation=cv2.INTER_AREA)
        bg = cv2.resize(small, (A.w, A.h), interpolation=cv2.INTER_CUBIC)
        frame[:] = (bg * 0.45).astype(np.uint8)
        frame[:, x0:x0 + cw] = cv2.resize(crop, (cw, A.h), interpolation=cv2.INTER_AREA)
        ff.stdin.write(frame.tobytes())
    ff.stdin.close()
    ff.wait()
    print(f"ch{A.chapter}: {len(rec)} entries, {missing} without a panel, {total / 60:.1f} min -> {OUT / 'recap.mp4'}")


if __name__ == "__main__":
    main()

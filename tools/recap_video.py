#!/usr/bin/env python3
"""recap_video: one-narrator recap video of a lettered chapter (vertical 9:16, for phones).

Inputs:
- OUT_DIR from autostrip2 (strip.png + layout.json with panel y positions);
- recap/chNNN.json from Codex: [{"panel": "P07", "text": "..."}, ...] in reading order;
- the Kokoro models (kokoro-v1.0.int8.onnx, voices.bin) and the narrator voice (VOICES.json "narr").

Output: OUT_DIR/recap.mp4 (720x1280, 24 fps, H.264 + AAC). While an entry is read, the view settles on
its panel; between entries it eases down the strip, so panels without narration scroll past.

usage: recap_video.py OUT_DIR RECAP.json --chapter N [--models DIR] [--voice am_onyx] [--speed 0.96]
"""
import argparse
import json
import subprocess
from pathlib import Path

import cv2
import numpy as np
import soundfile as sf

SR = 24000
VW, VH, FPS = 720, 1280, 24


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("recap")
    ap.add_argument("--chapter", type=int, required=True)
    ap.add_argument("--models", default="/tmp/claude-0/-home-claude/74687d11-0cc0-5bfd-9d7d-ad4189ed4d7b/scratchpad/dl")
    ap.add_argument("--voice", default="am_onyx")
    ap.add_argument("--speed", type=float, default=0.96)
    ap.add_argument("--gap", type=float, default=0.45, help="silence between entries (s)")
    A = ap.parse_args()
    OUT = Path(A.out)
    lay = json.loads((OUT / "layout.json").read_text(encoding="utf-8"))
    rec = json.loads(Path(A.recap).read_text(encoding="utf-8"))
    pan = {p["id"]: p for p in lay["panels"]}
    H = int(lay["height"])
    strip = cv2.imread(str(OUT / "strip.png"), cv2.IMREAD_COLOR)
    if strip is None:
        raise SystemExit("strip.png missing")
    W0 = strip.shape[1]
    view_h = int(round(W0 * VH / VW))  # strip pixels shown on screen

    from kokoro_onnx import Kokoro
    k = Kokoro(str(Path(A.models) / "kokoro-v1.0.int8.onnx"), str(Path(A.models) / "voices.bin"))

    def say(text):
        s, sr = k.create(text, voice=A.voice, speed=A.speed, lang="en-us")
        assert sr == SR
        return np.asarray(s, dtype=np.float32)

    def top_for(pid):
        p = pan.get(pid)
        if not p:
            return None
        c = (p["y_top"] + p["y_bottom"]) / 2
        return float(min(max(c - view_h / 2, 0), max(H - view_h, 0)))

    audio, keys, t = [], [(0.0, 0.0)], 0.0
    intro = say(f"My Summons Go First. Chapter {A.chapter}.")
    audio += [intro, np.zeros(int(SR * 0.6), np.float32)]
    t += len(intro) / SR + 0.6
    keys.append((t - 0.2, 0.0))
    missing = 0
    for e in rec:
        y = top_for(str(e.get("panel", "")))
        if y is None:
            missing += 1
            y = keys[-1][1]
        a = say(str(e["text"]).strip())
        keys.append((t + 0.9, max(y, keys[-1][1])))  # arrive on the panel shortly after the line starts; never scroll back up
        audio += [a, np.zeros(int(SR * A.gap), np.float32)]
        t += len(a) / SR + A.gap
    end_top = float(max(H - view_h, 0))
    keys.append((t + 2.5, end_top))
    audio.append(np.zeros(int(SR * 3.5), np.float32))
    total = t + 3.5
    wav = np.concatenate(audio)
    sf.write(str(OUT / "recap.wav"), wav, SR)

    kt = np.array([k_[0] for k_ in keys])
    ky = np.array([k_[1] for k_ in keys])

    def view_at(tt):
        i = np.searchsorted(kt, tt) - 1
        if i < 0:
            return ky[0]
        if i >= len(kt) - 1:
            return ky[-1]
        a, b = kt[i], kt[i + 1]
        u = 0.0 if b <= a else (tt - a) / (b - a)
        u = u * u * (3 - 2 * u)  # ease in-out
        return ky[i] + (ky[i + 1] - ky[i]) * u

    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{VW}x{VH}", "-r", str(FPS), "-i", "-",
           "-i", str(OUT / "recap.wav"), "-c:v", "libx264", "-preset", "veryfast", "-crf", "27", "-pix_fmt", "yuv420p",
           "-c:a", "aac", "-b:a", "96k", "-shortest", "-movflags", "+faststart", str(OUT / "recap.mp4")]
    ff = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    pad = np.full((view_h, W0, 3), 255, np.uint8)
    nfr = int(total * FPS)
    for f in range(nfr):
        y0 = int(round(view_at(f / FPS)))
        crop = strip[y0:y0 + view_h]
        if crop.shape[0] < view_h:
            crop = np.vstack([crop, pad[: view_h - crop.shape[0]]])
        ff.stdin.write(cv2.resize(crop, (VW, VH), interpolation=cv2.INTER_AREA).tobytes())
    ff.stdin.close()
    ff.wait()
    print(f"ch{A.chapter}: {len(rec)} entries, {missing} without a panel, {total / 60:.1f} min -> {OUT / 'recap.mp4'}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""narrate2: voice a lettered chapter with Kokoro and build the reader's scroll cues.

Inputs:
- the chapter script (chNNN.yaml), for panel order and silent beats;
- OUT_DIR from autostrip2 (layout.json with voiced lines, panels and segments);
- msgf-bible/VOICES.json (who speaks with which Kokoro voice).

Outputs in OUT_DIR:
- audio.mp3 (mono, 24 kHz)
- narration.json: {"file": "audio.mp3", "duration": s, "cues": [{"t", "segment", "y", "panel", "line"}]}
  Cue rules (narration.js): first cue at t=0; t strictly rising; absolute y never falling; y within its segment.
  A cue's y is the strip point the reader scrolls to the bottom of the screen while that line plays.

usage: narrate2.py chNNN.yaml OUT_DIR [--voices VOICES.json] [--models DIR]
"""
import argparse
import json
import re
import subprocess
from pathlib import Path

import numpy as np
import soundfile as sf
import yaml

SR = 24000
HERE = Path(__file__).resolve().parent
ACRONYMS = {"GMA", "AAO", "TV", "OK", "KNN", "CCTV", "TTOK", "ATM", "HQ", "GPS", "VIP", "SNS"}
PROPER = ["Taeo", "Nib", "Haru", "Eunchae", "Chae", "Yuri", "Minho", "Seoryun", "Bae", "Oh", "Pyo", "Jaesung", "Kanghan", "Hanbit",
          "Mapo", "Seogyo", "Hapjeong", "Mangwon", "Seogang", "Seoul", "Korea", "Korean", "QuickHaul", "HunterLink", "Saebom",
          "Haeseong", "Kett", "Orrin", "Sera", "Kesh", "Dara", "Sejin", "Dami", "Mansu", "Dokgo", "Ryu", "Moon", "Granny Moon",
          "Grandma", "Grandpa", "Sunline", "Jiwon", "Doyun", "Haein", "BangBang", "Ilan", "Venn", "Baek", "Meridian", "Bluebird",
          "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Yeoju", "Okja", "Gilsu", "Jungho", "Daesik",
          "Gate Safety Korea", "Iron Vow", "Haneul"]


def speakable(t):
    """Script lettering is in caps; Kokoro reads caps as acronyms. Return natural sentence case."""
    t = str(t).replace("**", "")
    t = re.sub(r"₩\s?([\d,]+)", r"\1 won", t)
    t = re.sub(r"US\$\s?([\d,.]+)", r"\1 US dollars", t)
    t = t.replace("≈", "about").replace("…", "...").replace("—", ", ").replace("·", ",")
    t = re.sub(r"\[|\]", "", t)
    parts = re.split(r"(\s+)", t)
    out = []
    for w in parts:
        core = re.sub(r"[^A-Za-z\-]", "", w)
        out.append(w if core.upper() in ACRONYMS and core.isupper() and len(core) > 1 else w.lower())
    s = "".join(out)
    s = re.sub(r"(^|[.!?]\s+|\.\.\.\s*)([a-z])", lambda m: m.group(1) + m.group(2).upper(), s)
    s = re.sub(r"\bi\b", "I", s)
    s = re.sub(r"\bi'(m|ll|ve|d)\b", lambda m: "I'" + m.group(1), s)
    for name in sorted(PROPER, key=len, reverse=True):
        s = re.sub(r"\b" + re.escape(name) + r"\b", name, s, flags=re.I)
    s = re.sub(r"\b([a-e]|s)-(rank|grade|class)\b", lambda m: m.group(1).upper() + "-" + m.group(2), s, flags=re.I)
    s = re.sub(r"(\d)\s?(am|pm)\b", lambda m: m.group(1) + " " + m.group(2).upper(), s)
    s = re.sub(r"\s+,", ",", s).strip(" ,")
    return s or "..."


def band(x, lo, hi):
    """Brick-wall band-pass in the frequency domain with soft edges (phone/radio voice)."""
    n = len(x)
    X = np.fft.rfft(x)
    f = np.fft.rfftfreq(n, 1 / SR)
    g = np.clip((f - lo * 0.7) / (lo * 0.3), 0, 1) * np.clip((hi * 1.25 - f) / (hi * 0.25), 0, 1)
    return np.fft.irfft(X * g, n).astype(np.float32)


def fx(audio, kind):
    if kind == "phone":
        y = band(audio, 320, 3400)
        return np.tanh(y * 2.2) / 2.2
    if kind == "system":
        y = band(audio, 180, 7000)
        d = int(SR * 0.045)
        echo = np.concatenate([np.zeros(d, np.float32), y[:-d] * 0.28]) if len(y) > d else y
        return y + echo
    return audio


def norm(a, target_rms=0.12, peak=0.9):
    rms = float(np.sqrt(np.mean(a ** 2))) or 1e-6
    g = min(2.0, target_rms / rms, peak / (float(np.max(np.abs(a))) or 1e-6))
    return (a * g).astype(np.float32)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("script")
    ap.add_argument("out")
    ap.add_argument("--voices", default=str(Path.home() / "msgf-bible" / "VOICES.json"))
    ap.add_argument("--models", default="/tmp/claude-0/-home-claude/74687d11-0cc0-5bfd-9d7d-ad4189ed4d7b/scratchpad/dl")
    ap.add_argument("--visible", type=int, default=1150, help="strip px the reader can be assumed to show above a cue")
    A = ap.parse_args()
    from kokoro_onnx import Kokoro
    OUT = Path(A.out)
    L = json.load(open(OUT / "layout.json", encoding="utf-8"))
    S = yaml.safe_load(open(A.script, encoding="utf-8"))
    V = json.load(open(A.voices, encoding="utf-8"))
    k = Kokoro(str(Path(A.models) / "kokoro-v1.0.int8.onnx"), str(Path(A.models) / "voices.bin"))
    silent = {p["id"]: bool(p.get("silent")) for p in S["panels"] if "id" in p}
    shapes = {p["id"]: p.get("shape") for p in S["panels"] if "id" in p}
    seg_tops = L["segment_tops"]
    segs = L["segments"]

    def to_seg(y_abs):
        for (name, h), top in zip(segs, seg_tops):
            if top <= y_abs <= top + h:
                return name, int(round(y_abs - top))
        name, h = segs[-1]
        return name, int(h)

    by_panel = {}
    for ln in L["lines"]:
        by_panel.setdefault(ln["panel_id"], []).append(ln)
    chunks, cues = [np.zeros(int(SR * 0.7), np.float32)], []
    t, last_y = 0.7, -1
    cues.append({"t": 0, "segment": segs[0][0], "y": 0})
    line_no = 0
    for pi, p in enumerate(L["panels"], 1):
        lines = by_panel.get(p["id"], [])
        if not lines:
            hold = 1.9 if silent.get(p["id"]) or shapes.get(p["id"]) in ("tall", "bleed") else 1.2
            y = max(last_y, p["y_bottom"])
            seg, sy = to_seg(y)
            if t > cues[-1]["t"] + 0.01:
                cues.append({"t": round(t, 2), "segment": seg, "y": sy, "panel": pi})
            last_y = y
            chunks.append(np.zeros(int(SR * hold), np.float32))
            t += hold
            continue
        for li_, ln in enumerate(lines):
            line_no += 1
            who = str(ln.get("who", "default")).split(":")[-1]
            typ = ln.get("type", "speech")
            if typ == "system":
                who = "system"
            elif typ in ("narr", "narr_dark"):
                who = "narr"
            v = V.get(who) or V["default"]
            speed = v.get("speed", 1.0) * {"shout": 1.06, "whisper": 0.96, "intense": 0.98}.get(typ, 1.0)
            text = speakable(ln["text"])
            audio, sr = k.create(text, voice=v["voice"], speed=speed, lang="en-gb" if v["voice"].startswith("b") else "en-us")
            audio = np.asarray(audio, np.float32)
            audio = fx(audio, "phone" if typ == "phone" else v.get("fx", ""))
            audio = norm(audio, 0.075 if typ == "whisper" else (0.15 if typ == "shout" else 0.12))
            y = max(last_y, ln["y_bottom"], min(p["y_bottom"], ln["y_top"] + A.visible))
            seg, sy = to_seg(y)
            if t > cues[-1]["t"] + 0.01:
                cues.append({"t": round(t, 2), "segment": seg, "y": sy, "panel": pi, "line": line_no})
            last_y = y
            chunks.append(audio)
            t += len(audio) / SR
            cues.append({"t": round(t, 2), "segment": seg, "y": sy, "panel": pi})  # hold the focus to the line's end
            gap = 0.55 if typ in ("float", "narr", "narr_dark", "system") else 0.4
            if li_ == len(lines) - 1 and p["y_bottom"] > y + 40:  # last line: reveal the rest of the panel in the pause
                yb = p["y_bottom"]
                sb, syb = to_seg(yb)
                cues.append({"t": round(t + min(gap, 0.35), 2), "segment": sb, "y": syb, "panel": pi})
                last_y = yb
            chunks.append(np.zeros(int(SR * gap), np.float32))
            t += gap
            print(f"{line_no:3d} {who:12s} {len(audio) / SR:5.2f}s  {text[:60]}", flush=True)
    chunks.append(np.zeros(int(SR * 1.2), np.float32))
    t += 1.2
    full = np.concatenate(chunks)
    sf.write(OUT / "audio.wav", full, SR)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(OUT / "audio.wav"), "-ac", "1", "-b:a", "96k", str(OUT / "audio.mp3")], check=True)
    (OUT / "audio.wav").unlink()
    dur = round(len(full) / SR, 2)
    json.dump({"file": "audio.mp3", "duration": dur, "cues": cues}, open(OUT / "narration.json", "w"), indent=1)
    print(f"duration {dur}s | cues {len(cues)} | lines {line_no}")


if __name__ == "__main__":
    main()

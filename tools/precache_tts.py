#!/usr/bin/env python3
"""precache_tts: voice every recap entry ahead of rendering, into the cache recap_video.py reads (same hash, same
respelling), so a chapter render only draws frames. Clips are written atomically; re-running skips what exists.

usage: precache_tts.py recaps_v2/ch003.json [recaps_v2/ch004.json ...] [--voice am_michael] [--speed 1.2]
"""
import argparse
import hashlib
import json
import os
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pron import respell  # noqa: E402

M = Path("/tmp/claude-0/-home-claude/74687d11-0cc0-5bfd-9d7d-ad4189ed4d7b/scratchpad/dl")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("recaps", nargs="+")
    ap.add_argument("--voice", default="am_michael")
    ap.add_argument("--speed", type=float, default=1.2)
    A = ap.parse_args()
    from kokoro_onnx import Kokoro
    k = Kokoro(str(M / "kokoro-v1.0.int8.onnx"), str(M / "voices.bin"))
    cache = Path(os.environ.get("TTS_CACHE", "/home/claude/flight/tts_cache"))
    cache.mkdir(parents=True, exist_ok=True)
    lang = "en-gb" if A.voice.startswith("b") else "en-us"
    for f in A.recaps:
        new, secs = 0, 0.0
        for e in json.loads(Path(f).read_text(encoding="utf-8")):
            text = respell(str(e["text"]).strip())
            h = cache / (hashlib.sha1(f"{A.voice}|{A.speed}|{text}".encode()).hexdigest() + ".npy")
            if not h.exists():
                s, sr = k.create(text, voice=A.voice, speed=A.speed, lang=lang)
                tmp = h.with_name(h.stem + f".{os.getpid()}.tmp.npy")
                np.save(tmp, np.asarray(s, dtype=np.float32))
                os.replace(tmp, h)
                new += 1
            secs += len(np.load(h, mmap_mode="r")) / 24000
        print(f"{Path(f).stem}: {new} new clips, narration {secs / 60:.1f} min", flush=True)


if __name__ == "__main__":
    main()

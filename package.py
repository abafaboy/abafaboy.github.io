#!/usr/bin/env python3
"""Add lettered chapters to the flight bundle branch and push: chNNN/NNN.webp (lossless segments), layout.json, recap.json.

No lossy copies (owner, 25 October: no image may ever look compressed): the strip travels as autostrip2's
lossless WebP segments, which recap_video stacks back into the strip. Never strip.jpg."""
import shutil
import subprocess
import sys
from pathlib import Path


R = Path("/home/claude/flightrepo")
F = Path("/home/claude/flight")
added = []
for c in map(int, sys.argv[1:]):
    C = f"ch{c:03d}"
    out = F / C / "out"
    if not (out / "strip.png").exists() or not (out / "layout.json").exists():
        print(C, "not lettered yet")
        continue
    d = R / C
    d.mkdir(exist_ok=True)
    import json
    lay = json.load(open(out / "layout.json", encoding="utf-8"))
    for old in list(d.glob("strip.*")) + list(d.glob("[0-9][0-9][0-9].webp")):
        old.unlink()
    for name, _h in lay["segments"]:
        with open(out / name, "rb") as fh:
            if b"VP8L" not in fh.read(4096):
                raise SystemExit(f"{C}/{name} is lossy WebP: re-letter with the current autostrip2")
        shutil.copy(out / name, d / name)
    shutil.copy(out / "layout.json", d / "layout.json")
    shutil.copy(F / "recap" / f"{C}.json", d / "recap.json")
    added.append(C)
if added:
    subprocess.run(["git", "-C", str(R), "add", *added], check=True)
    subprocess.run(["git", "-C", str(R), "-c", "user.name=Claude", "-c", "user.email=noreply@anthropic.com", "commit", "-q", "-m",
                    f"Add lettered {', '.join(added)}\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>\n"
                    "Claude-Session: https://claude.ai/code/session_01TzZgEEphdKofceaVXPhMY8"], check=True)
    subprocess.run(["git", "-C", str(R), "push", "-q", "origin", "msgf-flight"], check=True)
print("pushed", added)

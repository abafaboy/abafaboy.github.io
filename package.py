#!/usr/bin/env python3
"""Add lettered chapters to the flight bundle branch and push: chNNN/strip.jpg, layout.json, recap.json."""
import shutil
import subprocess
import sys
from pathlib import Path

import cv2

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
    img = cv2.imread(str(out / "strip.png"), cv2.IMREAD_COLOR)
    cv2.imwrite(str(d / "strip.jpg"), img, [cv2.IMWRITE_JPEG_QUALITY, 90])
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

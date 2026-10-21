#!/usr/bin/env python3
"""flight_build: letter + narrate + render chapters into one phone video.

For each chapter: unzip staged art (exports/art_chNNN.zip), letter it with autostrip2 (head boxes from REVIEW*.json,
Anime Ace if present), voice the Codex recap with one narrator (recap_video), then join the chapters.

usage: flight_build.py 1 2 3 ... [--name MSGF_flight]
"""
import argparse
import subprocess
import zipfile
from pathlib import Path

U = Path("/mnt/user-data/uploads/Videos/MySummonsGoFirst")
WORK = Path("/home/claude/flight")
BIBLE = Path("/home/claude/msgf-bible")
TOOLS = Path("/home/claude/msgf-tools")


def run(cmd):
    print("+", " ".join(map(str, cmd))[:200], flush=True)
    return subprocess.run(list(map(str, cmd)), check=False)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("chapters", nargs="+", type=int)
    ap.add_argument("--name", default="MSGF_flight")
    ap.add_argument("--skip-letter", action="store_true")
    A = ap.parse_args()
    done = []
    for c in A.chapters:
        C = f"{c:03d}"
        cw = WORK / f"ch{C}"
        art, out = cw / "art", cw / "out"
        z = U / "exports" / f"art_ch{C}.zip"
        recap = U / "recap" / f"ch{C}.json"
        if not recap.exists():
            print(f"ch{C}: no recap yet, skipped", flush=True)
            continue
        if not A.skip_letter or not (out / "strip.png").exists():
            if z.exists():
                art.mkdir(parents=True, exist_ok=True)
                with zipfile.ZipFile(z) as zf:
                    for m in zf.namelist():
                        n = Path(m).name
                        if n and (n.lower().endswith(".png") or n.startswith("REVIEW")):
                            (art / n).write_bytes(zf.read(m))
            elif not art.exists():
                print(f"ch{C}: no art zip, skipped", flush=True)
                continue
            r = run(["python3", TOOLS / "autostrip2.py", BIBLE / "scripts" / f"ch{C}.yaml", art, out, "--seg-max", "3400", "--placeholders"])
            if r.returncode:
                print(f"ch{C}: lettering failed", flush=True)
                continue
        r = run(["python3", TOOLS / "recap_video.py", out, recap, "--chapter", c])
        if r.returncode == 0 and (out / "recap.mp4").exists():
            done.append(out / "recap.mp4")
    if not done:
        raise SystemExit("nothing built")
    lst = WORK / f"{A.name}.txt"
    lst.write_text("".join(f"file '{p}'\n" for p in done))
    final = WORK / f"{A.name}.mp4"
    run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", "-movflags", "+faststart", final])
    print("FINAL", final, round(final.stat().st_size / 1e6, 1), "MB", flush=True)


if __name__ == "__main__":
    main()

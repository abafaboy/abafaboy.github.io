#!/usr/bin/env python3
"""longform_build: join rendered chapters into one long-form video, with YouTube chapter timestamps.

Each chapter comes from recap_video.py: WORK/chNNN/out/recap.mp4 and recap.wav.

Video. By default the chapters' H.264 streams are joined without re-encoding (concat demuxer, stream copy); that needs
every chapter encoded with the same settings, which recap_video guarantees, and the check below refuses a mismatch.
With --crf the joined video is re-encoded once (x264 High, tune animation, GOP 15, BT.709 tags, like recap_video) to
bring a multi-hour upload down to a practical size; pick the CRF with the PSNR ladder in PUBLISH_PLAN.md.

Audio. Rebuilt from each chapter's recap.wav, padded or trimmed to that chapter's exact video length, then encoded
once (AAC-LC, 48 kHz). Stream-copying 33 AAC tracks end to end would drift the narration by up to a frame per join.

Outputs in --out-dir: NAME.mp4 (with MP4 chapter markers), NAME_description.txt (the YouTube timestamps) and
NAME_chapters.json.

usage: longform_build.py --chapters 1-33 [--work /home/claude/work] [--name MSGF_S1] [--crf 18] [--dry-run]
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

import numpy as np
import soundfile as sf
import yaml

BIBLE = Path("/home/claude/msgf-bible")
SR = 24000


def chapters_from(spec):
    out = []
    for part in spec.split(","):
        part = part.strip()
        if "-" in part:
            a, b = part.split("-")
            out += list(range(int(a), int(b) + 1))
        elif part:
            out.append(int(part))
    return out


def probe(mp4):
    """The video stream's settings and its exact frame count (packets counted, not the container's estimate)."""
    r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-count_packets", "-show_entries",
                        "stream=codec_name,profile,width,height,r_frame_rate,pix_fmt,nb_read_packets,color_space,duration",
                        "-of", "json", str(mp4)], capture_output=True, text=True, check=True)
    s = json.loads(r.stdout)["streams"][0]
    num, den = map(int, s["r_frame_rate"].split("/"))
    return {"codec": s["codec_name"], "profile": s.get("profile"), "size": (s["width"], s["height"]),
            "fps": num / den, "fps_str": s["r_frame_rate"], "pix_fmt": s["pix_fmt"],
            "color": s.get("color_space"), "frames": int(s["nb_read_packets"]),
            # the shown length: the stream duration honours an edit list; recap_video files have none, so it equals frames/fps
            "dur": float(s["duration"]) if s.get("duration") not in (None, "N/A") else int(s["nb_read_packets"]) * den / num}


def stamp(t):
    t = int(t)
    h, m, s = t // 3600, t % 3600 // 60, t % 60
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--chapters", required=True, help="e.g. 1-33 or 1,2,5-7")
    ap.add_argument("--work", default="/home/claude/work")
    ap.add_argument("--out-dir", default=None, help="default: WORK")
    ap.add_argument("--name", default="MSGF_S1")
    ap.add_argument("--crf", type=float, default=None, help="re-encode the joined video at this CRF (default: stream copy)")
    ap.add_argument("--preset", default="slow")
    ap.add_argument("--audio-bitrate", default="192k")
    ap.add_argument("--title", default="My Summons Go First", help="MP4 title tag")
    ap.add_argument("--dry-run", action="store_true", help="check inputs and print the timestamps only")
    A = ap.parse_args()
    WORK = Path(A.work)
    OUT = Path(A.out_dir) if A.out_dir else WORK
    OUT.mkdir(parents=True, exist_ok=True)

    chs = []
    for n in chapters_from(A.chapters):
        d = WORK / f"ch{n:03d}" / "out"
        mp4, wav = d / "recap.mp4", d / "recap.wav"
        if not mp4.exists() or not wav.exists():
            sys.exit(f"ch{n:03d}: {mp4} or {wav} missing")
        title = yaml.safe_load((BIBLE / "scripts_v2" / f"ch{n:03d}.yaml").read_text(encoding="utf-8"))["title"]
        chs.append({"n": n, "mp4": mp4, "wav": wav, "title": title, **probe(mp4)})

    ref = chs[0]
    keys = ("codec", "profile", "size", "fps_str", "pix_fmt", "color")
    bad = [c for c in chs if any(c[k] != ref[k] for k in keys)]
    if bad and A.crf is None:
        for c in bad:
            print(f"ch{c['n']:03d} differs: " + ", ".join(f"{k} {c[k]} vs {ref[k]}" for k in keys if c[k] != ref[k]))
        sys.exit("streams differ: re-render those chapters with recap_video.py, or pass --crf to re-encode")

    t = 0.0
    for c in chs:
        c["start"] = t
        t += c["dur"]
    total = t
    if any(c["dur"] < 10 for c in chs):
        print("warning: a chapter under 10 s breaks YouTube's chapter list")

    desc = [f"{'0:00' if i == 0 else stamp(c['start'])} Chapter {c['n']}: {c['title']}" for i, c in enumerate(chs)]
    (OUT / f"{A.name}_description.txt").write_text("\n".join(desc) + "\n", encoding="utf-8")
    (OUT / f"{A.name}_chapters.json").write_text(json.dumps(
        [{"chapter": c["n"], "title": c["title"], "start": round(c["start"], 3), "end": round(c["start"] + c["dur"], 3)} for c in chs],
        indent=1) + "\n", encoding="utf-8")
    print("\n".join(desc))
    print(f"total {stamp(total)} ({total / 3600:.2f} h), {len(chs)} chapters")
    if total > 12 * 3600:
        print("warning: over YouTube's 12-hour upload limit")
    if A.dry_run:
        return

    # 1. video: one join, stream copy or a single re-encode
    lst = OUT / f"{A.name}_list.txt"
    lst.write_text("".join(f"file '{c['mp4']}'\nduration {c['dur']:.6f}\n" for c in chs))
    vid = OUT / f"{A.name}_video.mp4"
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-stats", "-f", "concat", "-safe", "0", "-i", str(lst), "-map", "0:v:0"]
    if A.crf is None:
        cmd += ["-c", "copy"]
    else:
        gop = max(1, int(round(ref["fps"])) // 2)
        cmd += ["-fps_mode", "passthrough",  # keep the chapters' own timestamps: no duplicated frame at a join
                "-c:v", "libx264", "-preset", A.preset, "-tune", "animation", "-crf", str(A.crf), "-profile:v", "high",
                "-g", str(gop), "-bf", "2", "-pix_fmt", "yuv420p",
                "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709"]
    subprocess.run(cmd + [str(vid)], check=True)

    # 2. audio: each chapter's narration padded or trimmed to its video length, encoded once
    aud = OUT / f"{A.name}_audio.m4a"
    enc = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "s16le", "-ar", str(SR), "-ac", "1", "-i", "pipe:0",
                            "-c:a", "aac", "-ar", "48000", "-b:a", A.audio_bitrate, str(aud)], stdin=subprocess.PIPE)
    done = 0
    for c in chs:
        a, sr = sf.read(str(c["wav"]), dtype="int16")
        if sr != SR:
            sys.exit(f"ch{c['n']:03d}: recap.wav is {sr} Hz, expected {SR}")
        if a.ndim > 1:
            a = a[:, 0]
        end = int(round((c["start"] + c["dur"]) * SR))  # cumulative sample target: no rounding drift across chapters
        need = end - done
        a = a[:need] if len(a) >= need else np.concatenate([a, np.zeros(need - len(a), np.int16)])
        enc.stdin.write(a.tobytes())
        done = end
    enc.stdin.close()
    if enc.wait():
        sys.exit("audio encode failed")

    # 3. mux, with MP4 chapter markers
    meta = OUT / f"{A.name}_meta.txt"
    lines = [";FFMETADATA1", f"title={A.title}"]
    for c in chs:
        lines += ["[CHAPTER]", "TIMEBASE=1/1000", f"START={int(round(c['start'] * 1000))}",
                  f"END={int(round((c['start'] + c['dur']) * 1000))}", f"title=Chapter {c['n']}: {c['title']}"]
    meta.write_text("\n".join(lines) + "\n", encoding="utf-8")
    final = OUT / f"{A.name}.mp4"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(vid), "-i", str(aud), "-i", str(meta),
                    "-map", "0:v:0", "-map", "1:a:0", "-map_metadata", "2", "-map_chapters", "2",
                    "-c", "copy", "-movflags", "+faststart", str(final)], check=True)
    for p in (vid, aud):
        p.unlink()
    v = probe(final)
    drift = v["dur"] - total
    print(f"FINAL {final} {final.stat().st_size / 1e9:.2f} GB, {v['frames']} frames, {stamp(v['dur'])} (video vs plan {drift:+.3f} s)")


if __name__ == "__main__":
    main()

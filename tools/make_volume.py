#!/usr/bin/env python3
"""Build a horizontal volume: py tools/make_volume.py FIRST LAST VOLUME_NUMBER.
Paths use videos_root in pipeline/config.json. Original final/ files are read only.
Non-final chapters use briefs/volume_cuts.json and a 0.6-second audio fade.
"""
from __future__ import annotations
import argparse
import json
import math
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time
import uuid

SCRIPT_DIR = Path(__file__).resolve().parent
CONFIG_PATH = SCRIPT_DIR.parent / "config.json"
ROOT = Path(json.loads(CONFIG_PATH.read_text(encoding="utf-8"))["videos_root"]) if CONFIG_PATH.is_file() else SCRIPT_DIR
FILTER = (
    "[0:v]split=2[a][b];"
    "[a]scale=1920:3414,crop=1920:1080:0:(ih-1080)/2,"
    "gblur=sigma=30,eq=brightness=-0.25:saturation=0.8[bg];"
    "[b]scale=608:1080[fg];"
    "[bg][fg]overlay=(W-w)/2:0,fps=30,format=yuv420p[v]"
)

def find_binary(name: str, sibling: Path | None = None) -> str:
    candidates = []
    if sibling:
        candidates.append(sibling.with_name(name + ".exe"))
    found = shutil.which(name)
    if found:
        candidates.append(Path(found))
    local = os.environ.get("LOCALAPPDATA")
    if local:
        winget = Path(local) / "Microsoft" / "WinGet"
        candidates.append(winget / "Links" / (name + ".exe"))
        for package in sorted((winget / "Packages").glob("Gyan.FFmpeg_*"), reverse=True):
            candidates.extend(package.glob("*/bin/" + name + ".exe"))
    for candidate in candidates:
        if candidate.is_file():
            return str(candidate)
    raise RuntimeError(f"{name} was not found. Install both tools with: winget install Gyan.FFmpeg")

def probe(ffprobe: str, path: Path) -> dict:
    result = subprocess.run(
        [ffprobe, "-v", "error", "-show_format", "-show_streams", "-of", "json", str(path)],
        check=True, capture_output=True, text=True, encoding="utf-8",
    )
    info = json.loads(result.stdout)
    duration = float(info.get("format", {}).get("duration", 0))
    if not math.isfinite(duration) or duration <= 0:
        raise RuntimeError(f"ffprobe found no positive duration: {path}")
    return info

def duration_of(info: dict) -> float:
    return float(info["format"]["duration"])

def check_duration(actual: float, expected: float, label: str) -> None:
    tolerance = max(1.0, expected * 0.005)
    if abs(actual - expected) > tolerance:
        raise RuntimeError(
            f"{label}: duration {actual:.3f}s differs from expected {expected:.3f}s "
            f"by more than {tolerance:.3f}s. Horizontal chapters have been retained."
        )

def check_streams(info: dict, path: Path) -> None:
    video = next((s for s in info["streams"] if s["codec_type"] == "video"), None)
    audio = next((s for s in info["streams"] if s["codec_type"] == "audio"), None)
    if video is None or (
        video.get("width"), video.get("height"), video.get("codec_name"), video.get("pix_fmt")
    ) != (1920, 1080, "h264", "yuv420p"):
        raise RuntimeError(f"Unexpected video format in {path}; horizontal chapters retained.")
    numerator, denominator = video.get("avg_frame_rate", "0/1").split("/")
    if float(denominator) == 0 or abs(float(numerator) / float(denominator) - 30) > 0.01:
        raise RuntimeError(f"Expected 30 fps in {path}; horizontal chapters retained.")
    if audio is None or (
        audio.get("codec_name"), audio.get("sample_rate"), audio.get("channels")
    ) != ("aac", "48000", 2):
        raise RuntimeError(f"Unexpected audio format in {path}; horizontal chapters retained.")

def run_ffmpeg(ffmpeg: str, arguments: list[str], label: str, expected: float) -> None:
    command = [ffmpeg, "-hide_banner", "-nostdin", "-y", "-loglevel", "warning",
               "-nostats", "-progress", "pipe:1", *arguments]
    with tempfile.TemporaryFile(mode="w+b") as diagnostics:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=diagnostics,
                                   text=True, encoding="utf-8", errors="replace")
        last_report = time.monotonic()
        try:
            assert process.stdout is not None
            for line in process.stdout:
                key, _, value = line.strip().partition("=")
                if key == "out_time_us" and time.monotonic() - last_report >= 30:
                    try:
                        seconds = max(0.0, int(value) / 1_000_000)
                    except ValueError:
                        continue
                    print(f"{label}: {seconds:.1f}/{expected:.1f}s "
                          f"({min(100.0, 100 * seconds / expected):.1f}%)", flush=True)
                    last_report = time.monotonic()
            code = process.wait()
        except BaseException:
            process.terminate()
            try:
                process.wait(timeout=10)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait()
            raise
        finally:
            if process.stdout:
                process.stdout.close()
        if code:
            diagnostics.seek(0, os.SEEK_END)
            diagnostics.seek(max(0, diagnostics.tell() - 16000))
            detail = diagnostics.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"{label}: ffmpeg exited with code {code}.\n{detail}")

def positive_integer(value: str) -> int:
    number = int(value)
    if number < 1:
        raise argparse.ArgumentTypeError("chapter numbers must be at least 1")
    return number

def volume_integer(value: str) -> int:
    number = int(value)
    if number < 0:
        raise argparse.ArgumentTypeError("volume number must be at least 0")
    return number

def chapter_settings(number: int, last: int, original: float, cuts: dict) -> tuple[float, list[str], list[str]]:
    if str(number) not in cuts:
        print(f"WARNING: chapter {number} is missing from briefs/volume_cuts.json; keeping it complete.", flush=True)
        return original, [], []
    if number == last:
        return original, [], []
    cut = float(cuts[str(number)])
    if not math.isfinite(cut) or cut <= 0 or cut > original:
        raise ValueError(f"Invalid cut for chapter {number}: {cut}; source is {original:.3f}s.")
    return (cut, ["-t", f"{cut:.6f}"],
            ["-af", f"afade=t=out:st={max(0.0, cut - 0.6):.6f}:d=0.6"])

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("first", metavar="FIRST", type=positive_integer)
    parser.add_argument("last", metavar="LAST", type=positive_integer)
    parser.add_argument("volume_number", metavar="VOLUME_NUMBER", type=volume_integer)
    parser.add_argument("--reuse-verified", action="store_true", help="Decode and reuse existing horizontal chapters; never overwrite them.")
    parser.add_argument("--keep-intermediates", action="store_true", help="Retain all horizontal chapters after the volume passes checks.")
    parser.add_argument("--encode-threads", type=positive_integer, default=4)
    args = parser.parse_args()
    if args.last < args.first:
        parser.error("LAST must be greater than or equal to FIRST")
    chapters = []
    for number in range(args.first, args.last + 1):
        source = ROOT / "final" / f"The_Lord_Who_Measured_Zero_Ch{number}.mp4"
        if source.is_file():
            chapters.append((number, source))
        else:
            print(f"WARNING: missing chapter {number}: {source}; skipping.", flush=True)
    if not chapters:
        raise RuntimeError("No requested chapter files exist; no volume was created.")
    cuts_path = ROOT / "briefs" / "volume_cuts.json"
    cuts = json.loads(cuts_path.read_text(encoding="utf-8-sig"))
    if not isinstance(cuts, dict):
        raise ValueError(f"Expected a chapter-to-seconds mapping in {cuts_path}")
    ffmpeg = find_binary("ffmpeg")
    ffprobe = find_binary("ffprobe", Path(ffmpeg))
    print(f"FFmpeg: {ffmpeg}", flush=True)
    print(f"FFprobe: {ffprobe}", flush=True)
    horizontal_dir = ROOT / "horizontal"
    volumes_dir = ROOT / "volumes"
    volume_path = volumes_dir / (
        f"The_Lord_Who_Measured_Zero_Volume_{args.volume_number}_Ch{args.first}-{args.last}.mp4"
    )
    if volume_path.exists():
        raise FileExistsError(f"Volume already exists; move or remove it before rerunning: {volume_path}")
    horizontal_dir.mkdir(exist_ok=True)
    volumes_dir.mkdir(exist_ok=True)
    source_duration = kept_duration = horizontal_duration = 0.0
    horizontal_paths = []
    for number, source in chapters:
        original = duration_of(probe(ffprobe, source))
        source_duration += original
        expected, input_options, audio_filters = chapter_settings(number, chapters[-1][0], original, cuts)
        kept_duration += expected
        chapter_path = horizontal_dir / f"Ch{number}_h.mp4"
        if chapter_path.exists() and args.reuse_verified:
            chapter_info = probe(ffprobe, chapter_path)
            check_streams(chapter_info, chapter_path)
            if abs(duration_of(chapter_info) - expected) > 0.1:
                raise RuntimeError(f"Existing intermediate has the wrong cut; preserving it: {chapter_path}")
            subprocess.run([ffmpeg, "-hide_banner", "-nostdin", "-v", "error", "-xerror", "-err_detect", "explode",
                            "-i", str(chapter_path), "-f", "null", "-"], check=True,
                           stdout=subprocess.DEVNULL)
            print(f"Reusing decoded and verified chapter {number}: {chapter_path}", flush=True)
        else:
            if chapter_path.exists():
                raise FileExistsError(f"Existing intermediate preserved; use --reuse-verified: {chapter_path}")
            # Let FFmpeg create its own new temporary file on Windows.
            temporary_path = horizontal_dir / f".Ch{number}_h_{uuid.uuid4().hex}.mp4"
            print(f"Converting chapter {number} ({expected:.3f}s)...", flush=True)
            try:
                run_ffmpeg(ffmpeg, [
                    *input_options, "-i", str(source),
                    "-filter_complex_threads", str(args.encode_threads), "-filter_complex", FILTER, "-map", "[v]", "-map", "0:a", *audio_filters,
                    "-threads", str(args.encode_threads), "-c:v", "libx264", "-preset", "medium", "-crf", "21",
                    "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
                    str(temporary_path),
                ], f"Chapter {number}", expected)
                chapter_info = probe(ffprobe, temporary_path)
                check_streams(chapter_info, temporary_path)
                check_duration(duration_of(chapter_info), expected, f"Chapter {number}")
                temporary_path.replace(chapter_path)
            finally:
                temporary_path.unlink(missing_ok=True)
        horizontal_paths.append(chapter_path)
        horizontal_duration += duration_of(chapter_info)
        print(f"Chapter {number} verified: {duration_of(chapter_info):.3f}s", flush=True)
    concat_path = horizontal_dir / f".volume_concat_{uuid.uuid4().hex}.txt"
    partial_path = volumes_dir / f".volume_{uuid.uuid4().hex}.mp4"
    try:
        concat_path.write_text("".join(f"file '{path.name}'\n" for path in horizontal_paths), encoding="ascii")
        print(f"Joining {len(horizontal_paths)} chapter(s) in chapter order...", flush=True)
        run_ffmpeg(ffmpeg, [
            "-f", "concat", "-safe", "1", "-i", str(concat_path),
            "-c", "copy", "-movflags", "+faststart", str(partial_path),
        ], "Volume", horizontal_duration)
        partial_path.rename(volume_path)
        volume_info = probe(ffprobe, volume_path)
        check_streams(volume_info, volume_path)
        actual_duration = duration_of(volume_info)
        check_duration(actual_duration, horizontal_duration, "Volume vs horizontal chapter sum")
        check_duration(actual_duration, kept_duration, "Volume vs kept chapter sum")
        size = volume_path.stat().st_size
        print(f"Verified duration {actual_duration:.3f}s; kept sum {kept_duration:.3f}s; "
              f"original sum {source_duration:.3f}s.", flush=True)
        if not args.keep_intermediates:
            for path in horizontal_paths:
                try:
                    path.unlink()
                except OSError as error:
                    print(f"WARNING: could not remove verified intermediate {path}: {error}", flush=True)
        print(f"Volume: {volume_path}", flush=True)
        print(f"Duration: {actual_duration:.3f} seconds", flush=True)
        print("Resolution: 1920x1080; 30 fps", flush=True)
        print(f"Size: {size} bytes ({size / 1024**2:.2f} MiB)", flush=True)
        print("Per-chapter horizontal files retained." if args.keep_intermediates else "Per-chapter horizontal files cleaned up after verification.", flush=True)
    finally:
        concat_path.unlink(missing_ok=True)
        partial_path.unlink(missing_ok=True)
    return 0

if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        print("\nInterrupted; completed chapter files have been retained.", file=sys.stderr)
        raise SystemExit(130)
    except (OSError, ValueError, RuntimeError, subprocess.CalledProcessError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        raise SystemExit(1)

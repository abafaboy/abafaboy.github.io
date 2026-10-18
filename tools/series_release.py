#!/usr/bin/env python3
"""Validate finished public chapter bundles and stage append-only site releases.

This tool never invokes Git, generates art, or copies unreferenced source files.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path
import re
import shutil
import tempfile

from PIL import Image

SLUG = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
IMAGE = re.compile(r"[a-zA-Z0-9][a-zA-Z0-9_.-]*\.(?:webp|png|jpe?g)\Z", re.I)
AUDIO = re.compile(r"[a-zA-Z0-9][a-zA-Z0-9_.-]*\.(?:mp3|m4a|ogg|wav)\Z", re.I)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def fields(value, allowed, required, label):
    require(isinstance(value, dict), f"{label} must be an object")
    require(not (set(value) - set(allowed)), f"{label} has unsupported fields; keep private production data outside the release")
    require(set(required) <= set(value), f"{label} is missing required fields")


def text(value, label, maximum=300):
    require(isinstance(value, str) and bool(value.strip()) and len(value) <= maximum, f"Invalid {label}")


def integer(value, label, maximum):
    require(type(value) is int and 0 < value <= maximum, f"Invalid {label}")


def filename(value, pattern, label):
    require(isinstance(value, str) and pattern.fullmatch(value) is not None, f"Invalid {label}; use a plain filename")


def asset(root, relative, expected_size=None):
    path = root / relative
    require(path.is_file() and not path.is_symlink() and path.resolve().is_relative_to(root), f"Missing or unsafe asset: {relative}")
    if path.suffix.lower() in {".webp", ".png", ".jpg", ".jpeg"}:
        with Image.open(path) as image:
            if expected_size:
                require(image.size == expected_size, f"Image dimensions do not match manifest: {relative}: {image.size} != {expected_size}")
            image.load()
    require(path.stat().st_size > 0, f"Empty asset: {relative}")
    return {"size_bytes": path.stat().st_size, "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}


def validate_release(manifest_path):
    manifest_path = Path(manifest_path).resolve(strict=True)
    root = manifest_path.parent
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    fields(data, {"schema_version", "slug", "title", "synopsis", "cover", "chapters"}, {"schema_version", "slug", "title", "chapters"}, "series")
    require(type(data["schema_version"]) is int and data["schema_version"] == 1, "Unsupported schema version")
    require(isinstance(data["slug"], str) and len(data["slug"]) <= 80 and SLUG.fullmatch(data["slug"]), "Invalid series slug")
    text(data["title"], "series title")
    if "synopsis" in data:
        text(data["synopsis"], "public synopsis", 2000)
    require(isinstance(data["chapters"], list) and data["chapters"], "A release must contain at least one finished chapter")
    assets = {}
    if "cover" in data:
        filename(data["cover"], IMAGE, "cover")
        assets[data["cover"]] = asset(root, data["cover"])
    previous = 0
    for chapter in data["chapters"]:
        fields(chapter, {"n", "title", "width", "segments", "thumbnail", "audio", "gutters", "pdf", "framing_height"}, {"n", "title", "width", "segments"}, "chapter")
        integer(chapter["n"], "chapter number", 9999)
        require(chapter["n"] > previous, "Chapters must be unique and in increasing order")
        previous = chapter["n"]
        text(chapter["title"], "chapter title")
        integer(chapter["width"], "chapter width", 4096)
        require(isinstance(chapter["segments"], list) and chapter["segments"], "A chapter needs finished, lettered image segments")
        if "framing_height" in chapter:
            integer(chapter["framing_height"], "framing height", 10000)
        base = f"ch/{chapter['n']:03d}"
        seen = set()
        for segment in chapter["segments"]:
            require(isinstance(segment, list) and len(segment) == 2, "Segments must be [filename, pixel_height] pairs")
            name, height = segment
            filename(name, IMAGE, "segment filename")
            integer(height, "segment height", 10000)
            require(name not in seen, "A chapter cannot repeat a segment filename")
            seen.add(name)
            relative = f"{base}/{name}"
            assets[relative] = asset(root, relative, (chapter["width"], height))
        if "gutters" in chapter:
            require(isinstance(chapter["gutters"], dict), "Gutters must map chapter segment filenames to spacing")
            for name, gap in chapter["gutters"].items():
                require(name in seen and type(gap) is int and 0 <= gap <= 1000, "Invalid chapter gutter")
        if "thumbnail" in chapter:
            filename(chapter["thumbnail"], IMAGE, "thumbnail")
            relative = f"{base}/{chapter['thumbnail']}"
            assets[relative] = asset(root, relative)
        if "pdf" in chapter:
            filename(chapter["pdf"], re.compile(r"[a-zA-Z0-9][a-zA-Z0-9_.-]*\.pdf\Z", re.I), "PDF filename")
            relative = f"{base}/{chapter['pdf']}"
            assets[relative] = asset(root, relative)
            require((root / relative).read_bytes().startswith(b"%PDF-"), "Invalid reading PDF")
        if "audio" in chapter:
            fields(chapter["audio"], {"file", "duration", "cues"}, {"file"}, "audio")
            filename(chapter["audio"]["file"], AUDIO, "audio filename")
            if "duration" in chapter["audio"]:
                duration = chapter["audio"]["duration"]
                require(type(duration) in {int, float} and math.isfinite(duration) and duration > 0, "Audio duration must be positive seconds")
            if "cues" in chapter["audio"]:
                cues = chapter["audio"]["cues"]
                require(isinstance(cues, list) and cues, "Narration cues must be nonempty")
                positions = {}
                total = 0
                for name, height in chapter["segments"]:
                    positions[name] = (total, height)
                    total += height
                previous_time, previous_y = -1, -1
                for cue in cues:
                    fields(cue, {"t", "segment", "y", "panel", "line"}, {"t", "segment", "y"}, "narration cue")
                    time, y = cue["t"], cue["y"]
                    require(type(time) in {int, float} and math.isfinite(time) and time >= 0 and time > previous_time, "Cue times must increase from zero")
                    require(isinstance(cue["segment"], str) and cue["segment"] in positions, "Cue must reference a chapter segment")
                    top, height = positions[cue["segment"]]
                    require(type(y) in {int, float} and math.isfinite(y) and 0 <= y <= height and top + y >= previous_y, "Cue coordinates must follow chapter reading order within image bounds")
                    if "duration" in chapter["audio"]:
                        require(time <= chapter["audio"]["duration"], "Cue time exceeds narration duration")
                    for key in ("panel", "line"):
                        if key in cue:
                            integer(cue[key], f"cue {key}", 9999)
                    previous_time, previous_y = time, top + y
                require(cues[0]["t"] == 0, "Narration cues must start at zero")
            relative = f"{base}/{chapter['audio']['file']}"
            assets[relative] = asset(root, relative)
    return data, assets


def prepare_release(manifest_path, output_root):
    manifest_path = Path(manifest_path).resolve(strict=True)
    incoming, assets = validate_release(manifest_path)
    output_root = Path(output_root).resolve()
    output_root.mkdir(parents=True, exist_ok=True)
    target = output_root / incoming["slug"]
    require(not target.is_symlink(), "The destination must not be a symlink")
    current = None
    current_bytes = None
    if target.exists():
        require((target / "series.json").is_file(), "An existing destination must contain a valid series manifest")
        current, _ = validate_release(target / "series.json")
        current_bytes = (target / "series.json").read_bytes()
        require(current["slug"] == incoming["slug"] and current["title"] == incoming["title"], "Existing series identity differs")
        require(incoming["chapters"][0]["n"] > current["chapters"][-1]["n"], "Released chapters cannot be replaced by this tool")
    merged = {**(current or {}), **incoming}
    merged["chapters"] = (current or {}).get("chapters", []) + incoming["chapters"]
    require([c["n"] for c in merged["chapters"]] == list(range(1, len(merged["chapters"]) + 1)), "Release chapters consecutively, starting at one")
    for chapter in incoming["chapters"]:
        require(not (target / f"ch/{chapter['n']:03d}").exists(), "A destination chapter directory already exists")
    for relative, metadata in assets.items():
        destination = target / relative
        if destination.exists():
            require(relative == incoming.get("cover") and not destination.is_symlink() and hashlib.sha256(destination.read_bytes()).hexdigest() == metadata["sha256"], f"Refusing to overwrite an existing asset: {relative}")
    created = []
    with tempfile.TemporaryDirectory(prefix=".series-release-", dir=output_root) as temporary:
        staged = Path(temporary) / "release"
        staged.mkdir()
        for relative, metadata in assets.items():
            path = staged / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(manifest_path.parent / relative, path)
            require(hashlib.sha256(path.read_bytes()).hexdigest() == metadata["sha256"], f"Copied bytes changed: {relative}")
        staged_manifest = staged / "series.json"
        staged_manifest.write_text(json.dumps(merged, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        if not target.exists():
            staged.rename(target)
        else:
            require((target / "series.json").read_bytes() == current_bytes, "Series changed during preparation; rerun against the latest release")
            try:
                for chapter in incoming["chapters"]:
                    destination = target / f"ch/{chapter['n']:03d}"
                    (staged / f"ch/{chapter['n']:03d}").rename(destination)
                    created.append(destination)
                cover = incoming.get("cover")
                if cover and not (target / cover).exists():
                    (staged / cover).rename(target / cover)
                    created.append(target / cover)
                staged_manifest.replace(target / "series.json")
            except Exception:
                for path in reversed(created):
                    if path.is_dir():
                        shutil.rmtree(path)
                    else:
                        path.unlink()
                raise
    return target / "series.json"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["validate", "prepare"])
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--output-root", type=Path, default=Path(__file__).resolve().parents[1] / "manhwa/series")
    args = parser.parse_args()
    try:
        path = prepare_release(args.manifest, args.output_root) if args.action == "prepare" else args.manifest
        data, assets = validate_release(path)
        print(json.dumps({"manifest": str(path.resolve()), "slug": data["slug"], "chapters": [c["n"] for c in data["chapters"]], "assets": assets}, indent=2))
    except (OSError, ValueError, Image.DecompressionBombError) as error:
        parser.exit(1, f"Release rejected: {error}\n")


if __name__ == "__main__":
    main()

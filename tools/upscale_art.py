#!/usr/bin/env python3
"""upscale_art: 2x anime upscale of panel art (Real-ESRGAN realesr-animevideov3-x2 on CPU through ncnn), so panels
are never shown enlarged and soft. Tall panels (1024x1536) fill a 2160 px wide strip; without this they would be
stretched about 2.1x. The output is lossless PNG next to nothing else: OUT_DIR/<same name>.png.

Models: the official Real-ESRGAN ncnn release (github.com/xinntao/Real-ESRGAN, v0.2.5.0), files
realesr-animevideov3-x2.param/.bin. Tiles of 256 px with 16 px of context on each side, so no seams.

usage: upscale_art.py IN_DIR OUT_DIR [--models DIR] [--only P01,P07] [--threads 2]
"""
import argparse
import time
from pathlib import Path

import numpy as np
from PIL import Image

MODELS = "/tmp/claude-0/-home-claude/74687d11-0cc0-5bfd-9d7d-ad4189ed4d7b/scratchpad/upscale/models"


def load_net(models, threads):
    import ncnn
    net = ncnn.Net()
    net.opt.use_vulkan_compute = False
    net.opt.num_threads = threads
    net.load_param(str(Path(models) / "realesr-animevideov3-x2.param"))
    net.load_model(str(Path(models) / "realesr-animevideov3-x2.bin"))
    return net


def run(net, rgb):
    import ncnn
    h, w, _ = rgb.shape
    m = ncnn.Mat.from_pixels(np.ascontiguousarray(rgb), ncnn.Mat.PixelType.PIXEL_RGB, w, h)
    m.substract_mean_normalize([0.0, 0.0, 0.0], [1 / 255.0] * 3)
    ex = net.create_extractor()
    ex.input("data", m)
    _, out = ex.extract("output")
    a = np.array(out).transpose(1, 2, 0)
    return np.clip(a * 255.0 + 0.5, 0, 255).astype(np.uint8)


def upscale(net, img, tile=256, pad=16, s=2):
    rgb = np.asarray(img.convert("RGB"))
    H, W, _ = rgb.shape
    src = np.pad(rgb, ((pad, pad), (pad, pad), (0, 0)), mode="reflect")
    out = np.zeros((H * s, W * s, 3), np.uint8)
    for y in range(0, H, tile):
        for x in range(0, W, tile):
            th, tw = min(tile, H - y), min(tile, W - x)
            t = src[y:y + th + 2 * pad, x:x + tw + 2 * pad]
            r = run(net, t)
            out[y * s:(y + th) * s, x * s:(x + tw) * s] = r[pad * s:(pad + th) * s, pad * s:(pad + tw) * s]
    res = Image.fromarray(out)
    if img.mode == "RGBA":  # keep transparency (alpha enlarged with Lanczos)
        res.putalpha(img.getchannel("A").resize(res.size, Image.LANCZOS))
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("inp")
    ap.add_argument("out")
    ap.add_argument("--models", default=MODELS)
    ap.add_argument("--only", default="")
    ap.add_argument("--threads", type=int, default=2)
    A = ap.parse_args()
    IN, OUT = Path(A.inp), Path(A.out)
    OUT.mkdir(parents=True, exist_ok=True)
    only = {x.strip() for x in A.only.split(",") if x.strip()}
    net = load_net(A.models, A.threads)
    for p in sorted(IN.glob("*.png")):
        if only and p.stem not in only:
            continue
        dst = OUT / p.name
        if dst.exists() and dst.stat().st_mtime >= p.stat().st_mtime:
            continue
        t = time.time()
        im = Image.open(p)
        upscale(net, im).save(dst, compress_level=6)
        print(f"{p.name}: {im.size} -> {(im.size[0] * 2, im.size[1] * 2)} in {time.time() - t:.0f}s", flush=True)


if __name__ == "__main__":
    main()

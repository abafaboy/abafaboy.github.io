"""Thumbnails with a 128px coordinate grid, for annotating face boxes. usage: gridsheet.py OUT.png img1 img2 ..."""
import sys, os
from PIL import Image, ImageDraw
out, paths = sys.argv[1], sys.argv[2:]
T = 440; tiles = []
for pth in paths:
    im = Image.open(pth).convert('RGB'); w, h = im.size; d = ImageDraw.Draw(im)
    for x in range(0, w, 128): d.line([(x, 0), (x, h)], fill=(0, 255, 255), width=2)
    for y in range(0, h, 128): d.line([(0, y), (w, y)], fill=(0, 255, 255), width=2)
    im.thumbnail((T, T)); d = ImageDraw.Draw(im)
    s = im.width / w
    for x in range(0, w, 256): d.text((x * s + 2, 2), str(x), fill=(255, 0, 0))
    for y in range(0, h, 256): d.text((2, y * s + 2), str(y), fill=(255, 0, 0))
    d.rectangle([0, im.height - 14, 60, im.height], fill=(0, 0, 0)); d.text((3, im.height - 13), os.path.basename(pth)[:-4], fill=(255, 255, 0))
    tiles.append(im)
cols = 4; rows = (len(tiles) + cols - 1) // cols
sh = Image.new('RGB', (T * cols, T * rows), 'white')
for i, t in enumerate(tiles): sh.paste(t, ((i % cols) * T, (i // cols) * T))
sh.save(out)

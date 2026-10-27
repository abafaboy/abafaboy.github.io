"""A BEFORE / AFTER thumbnail base from approved art: chapter 1 P31 (Mok shoves Jaeha, the bait, at the boss door),
greyed, against the new bright T1B_closeup_1 (Lyra and Jaeha), split by a jagged diagonal."""
import random
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageOps
W, H = 1280, 720
before = Image.open('/home/claude/msgf-art/chapters_v2/ch001/art/P31.png').convert('RGB').crop((250, 0, 1275, 1024)).resize((720, 720), Image.LANCZOS)
g = ImageOps.grayscale(before)
before = Image.merge('RGB', [g.point(lambda v: int(v * 0.92)), g.point(lambda v: int(v * 0.95)), g.point(lambda v: min(255, int(v * 1.05 + 6)))])
before = ImageEnhance.Contrast(before).enhance(0.9)
after = Image.open('/mnt/user-data/uploads/Videos/MySummonsGoFirst/thumbnails_v2/T1B_closeup_1.png').convert('RGB').crop((470, 0, 1500, 1024))
after = after.resize((round(1030 * H / 1024), H), Image.LANCZOS)
after = ImageEnhance.Color(after).enhance(1.15)
canvas = Image.new('RGB', (W, H))
canvas.paste(after, (W - after.width, 0))
# jagged diagonal from the top (x 0.56 W) to the bottom (x 0.44 W)
rnd = random.Random(7)
pts = []
n = 9
for i in range(n + 1):
    t = i / n
    x = (0.56 - 0.12 * t) * W + (rnd.uniform(-26, 26) if 0 < i < n else 0)
    pts.append((x, t * H))
mask = Image.new('L', (W, H), 0)
ImageDraw.Draw(mask).polygon([(0, 0)] + pts + [(0, H)], fill=255)
bfull = Image.new('RGB', (W, H)); bfull.paste(before, (0, 0))
canvas = Image.composite(bfull, canvas, mask)
d = ImageDraw.Draw(canvas)
d.line(pts, fill=(0, 0, 0), width=22, joint='curve')
d.line(pts, fill=(255, 255, 255), width=10, joint='curve')
canvas.save('/tmp/claude-0/-home-claude/74687d11-0cc0-5bfd-9d7d-ad4189ed4d7b/scratchpad/thumbs/before_after_base.png')
print('ok', canvas.size)

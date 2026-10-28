#!/bin/bash
# usage: hf_apply.sh N P01 P05 ...   (chapter number, then the hand fixes Claude approved)
# Copies the approved fixed panels (staged from the laptop) over the canonical art in msgf-art and the work folder,
# then re-letters the chapter, renders the recap video and builds a judge pack.
set -e
n=$1; shift
c=$(printf "ch%03d" $n)
FIX=/mnt/user-data/uploads/Videos/MySummonsGoFirst/chapters_v2/$c/art/hands_fix/fixed
ART=/home/claude/msgf-art/chapters_v2/$c/art
for p in "$@"; do
  test -f $FIX/$p.png || { echo "missing $FIX/$p.png"; exit 1; }
  python3 - "$ART/$p.png" "$FIX/$p.png" <<'PY'
import sys
from PIL import Image
a, b = Image.open(sys.argv[1]), Image.open(sys.argv[2])
assert a.size == b.size, (sys.argv[2], a.size, b.size)
PY
  cp $FIX/$p.png $ART/$p.png
  echo "applied $c $p"
done
cd /home/claude/msgf-art && git add chapters_v2/$c/art && git commit -q -m "$c: hand fixes from Codex (HF), approved by Claude: $*" && echo committed
python3 /home/claude/work/sync_art.py $ART /home/claude/work/$c/art | tail -1
cd /home/claude/msgf-tools
python3 autostrip2.py /home/claude/msgf-bible/scripts_v2/$c.yaml /home/claude/work/$c/art /home/claude/work/$c/out --dpr 2 > /home/claude/work/$c/letter_hf.log 2>&1
tail -3 /home/claude/work/$c/letter_hf.log
python3 recap_video.py /home/claude/work/$c/out /home/claude/msgf-bible/recaps_v2/$c.json --chapter $n > /home/claude/work/$c/video_hf.log 2>&1
tail -2 /home/claude/work/$c/video_hf.log
rm -rf /home/claude/work/judge/${c}_hf
python3 /home/claude/msgf-bible/tools/judge_pack.py /home/claude/work/$c/out /home/claude/msgf-bible/recaps_v2/$c.json /home/claude/work/judge/${c}_hf --max 1800 | tail -1
rm -rf /home/claude/work/$c/out/_work/up   # regenerable upscale cache; the container disk is small
echo "$c done $(date +%H:%M:%S)"

#!/bin/bash
# warm_caches.sh: after chapter 3's build, letter chapters 7, 8, 9, 10, 4, 5, 6 once each (placeholders allowed) so their
# 2x upscale caches exist; the final builds then only re-upscale the panels that change. strip.png is deleted after each.
until grep -q "ch003 done" /home/claude/work/hf_after_ch003.log 2>/dev/null; do sleep 20; done
for n in 7 8 9 10 4 5 6; do
  c=$(printf "ch%03d" $n)
  free=$(df --output=avail -m / | tail -1)
  if [ "$free" -lt 2500 ]; then echo "$c skipped: only ${free} MB free"; continue; fi
  python3 /home/claude/work/sync_art.py /home/claude/msgf-art/chapters_v2/$c/art /home/claude/work/$c/art | tail -1
  echo "$c warm start $(date +%H:%M:%S)"
  cd /home/claude/msgf-tools && python3 autostrip2.py /home/claude/msgf-bible/scripts_v2/$c.yaml /home/claude/work/$c/art /home/claude/work/$c/out --dpr 2 --placeholders > /home/claude/work/$c/letter_warm.log 2>&1
  tail -1 /home/claude/work/$c/letter_warm.log | cut -c1-600
  rm -f /home/claude/work/$c/out/strip.png
  echo "$c warm done $(date +%H:%M:%S)"; df -h / | tail -1
done

#!/bin/bash
# hf_after.sh N : the steps of hf_apply.sh after the fixes are committed (sync, re-letter, render, judge pack)
set -e
n=$1; c=$(printf "ch%03d" $n)
ART=/home/claude/msgf-art/chapters_v2/$c/art
python3 /home/claude/work/sync_art.py $ART /home/claude/work/$c/art | tail -1
cd /home/claude/msgf-tools
echo "letter start $(date +%H:%M:%S)"
python3 autostrip2.py /home/claude/msgf-bible/scripts_v2/$c.yaml /home/claude/work/$c/art /home/claude/work/$c/out --dpr 2 > /home/claude/work/$c/letter_hf.log 2>&1
tail -3 /home/claude/work/$c/letter_hf.log
echo "video start $(date +%H:%M:%S)"
python3 recap_video.py /home/claude/work/$c/out /home/claude/msgf-bible/recaps_v2/$c.json --chapter $n > /home/claude/work/$c/video_hf.log 2>&1
tail -2 /home/claude/work/$c/video_hf.log
rm -rf /home/claude/work/judge/${c}_hf
python3 /home/claude/msgf-bible/tools/judge_pack.py /home/claude/work/$c/out /home/claude/msgf-bible/recaps_v2/$c.json /home/claude/work/judge/${c}_hf --max 1800 | tail -1
rm -rf /home/claude/work/$c/out/_work/up
echo "$c done $(date +%H:%M:%S)"
df -h / | tail -1

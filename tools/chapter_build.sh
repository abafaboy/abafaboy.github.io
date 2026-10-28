#!/bin/bash
# chapter_build.sh N [--drop-cache] : sync the canonical art, re-letter (keeping the upscale cache unless --drop-cache),
# render the recap video, build the judge pack, then delete strip.png (the renderer and long-form use recap.mp4/wav; the
# lossless segments stay).  Log: /home/claude/work/chNNN/build.log
set -e
n=$1; c=$(printf "ch%03d" $n)
ART=/home/claude/msgf-art/chapters_v2/$c/art
W=/home/claude/work/$c
mkdir -p $W/art
python3 /home/claude/work/sync_art.py $ART $W/art | tail -1
cd /home/claude/msgf-tools
echo "$c letter start $(date +%H:%M:%S)"
python3 autostrip2.py /home/claude/msgf-bible/scripts_v2/$c.yaml $W/art $W/out --dpr 2 > $W/letter_build.log 2>&1
tail -3 $W/letter_build.log | cut -c1-1500
echo "$c video start $(date +%H:%M:%S)"
python3 recap_video.py $W/out /home/claude/msgf-bible/recaps_v2/$c.json --chapter $n > $W/video_build.log 2>&1
tail -2 $W/video_build.log
rm -rf /home/claude/work/judge/${c}_final
python3 /home/claude/msgf-bible/tools/judge_pack.py $W/out /home/claude/msgf-bible/recaps_v2/$c.json /home/claude/work/judge/${c}_final --max 1800 | tail -1
rm -f $W/out/strip.png
[ "$2" = "--drop-cache" ] && rm -rf $W/out/_work/up
echo "$c done $(date +%H:%M:%S)"
df -h / | tail -1

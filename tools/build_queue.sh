#!/bin/bash
# build_queue.sh: builds chapters one after another, in the order their numbers are appended to build_queue.txt
# (one line each: "N" or "N --drop-cache"). Waits for new lines; processed lines are logged in build_queue.done.
Q=/home/claude/work/build_queue.txt; D=/home/claude/work/build_queue.done
touch $Q $D
while true; do
  done_n=$(wc -l < $D)
  line=$(sed -n "$((done_n + 1))p" $Q)
  if [ -z "$line" ]; then sleep 20; continue; fi
  # hold while another letterer or renderer is still running (e.g. a build started by hand)
  while pgrep -f "msgf-tools/autostrip2.py|autostrip2.py /home|recap_video.py /home" > /dev/null; do sleep 20; done
  echo "=== build $line start $(date +%H:%M:%S)"
  /home/claude/work/chapter_build.sh $line || echo "=== build $line FAILED"
  echo "$line" >> $D
done

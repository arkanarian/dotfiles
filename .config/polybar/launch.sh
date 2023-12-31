#!/usr/bin/env bash

# Terminate already running bar instances
# If all your bars have ipc enabled, you can use 
polybar-msg cmd quit
# Otherwise you can use the nuclear option:
# killall -q polybar

# Launch bar1 and bar2
echo "---" | tee -a /tmp/lapbar.log /tmp/4kbar.log
polybar lapbar 2>&1 | tee -a /tmp/lapbar.log & disown
#polybar lapbar_big 2>&1 | tee -a /tmp/lapbar.log & disown
polybar 4kbar 2>&1 | tee -a /tmp/4kbar.log & disown

echo "Bars launched..."

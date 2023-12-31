#!/bin/sh
./polybar_lapbar.sh
xrandr --output eDP --primary --mode 1920x1080 --pos 960x2160 --rotate normal \
  --output HDMI-A-0 --off

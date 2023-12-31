#!/bin/sh
./polybar_lapbar_big.sh
xrandr --output eDP --scale 1.6x1.6 --primary --mode 1920x1080 --pos 960x2160 --rotate normal \
  --output HDMI-A-0 --off

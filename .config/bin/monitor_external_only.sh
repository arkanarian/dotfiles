#!/bin/sh
xrandr --dpi 130 \
  --output eDP --off \
  --output HDMI-A-0 --primary --mode 3840x2160 --pos 0x0 #--same-as eDP

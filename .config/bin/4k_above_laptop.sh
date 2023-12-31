#!/bin/sh
./polybar_lapbar_big.sh
# 0.9999x0.9999 for mouse not flikering
xrandr --output eDP --scale 1.6x1.6 --primary --mode 1920x1080 --pos 960x2160 --rotate normal\
  --output HDMI-A-0 --scale 0.9999x0.9999 --mode 3840x2160 --pos 0x0 --rotate normal
# xrandr --output eDP --primary --mode 1920x1080 --pos 960x2160 --rotate normal\
#   --output HDMI-A-0 --mode 3840x2160 --pos 0x0 --rotate normal

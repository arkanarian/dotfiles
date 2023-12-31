#!/bin/sh
if [ $(cat "/sys/class/drm/card0-HDMI-A-1/status") = "connected" ]; then
  ~/.config/bin/4k_above_laptop.sh
  i3 restart
else
  file="/home/imaksus/.Xresources"
  if [[ $(sed -n "1p" "$file") =~ ^[[:space:]]*! ]]; then
    # dpi from laptop
    ~/.config/bin/laptop_only.sh
    i3 restart
  else
    # dpi from 4k
    ~/.config/bin/laptop_only_sacale.sh
    i3 restart
  fi
fi
i3 restart

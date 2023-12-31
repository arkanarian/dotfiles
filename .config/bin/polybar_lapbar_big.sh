#!/bin/sh
file="/home/imaksus/.config/polybar/launch.sh"
llapbar=11
llapbar_big=12
line_lapbar=$(sed -n "${llapbar}p" "$file")
line_lapbar_big=$(sed -n "${llapbar_big}p" "$file")

if [[ ! $line_lapbar =~ ^[[:space:]]*# ]]; then
  # comment lapbar"
  sed -i "${llapbar}s/^\(.*\)/#\1/" "$file"
fi
if [[ $line_lapbar_big =~ ^[[:space:]]*# ]]; then
  # unmcomment lapbar big"
  sed -i "${llapbar_big}s/^#//" "$file"
fi

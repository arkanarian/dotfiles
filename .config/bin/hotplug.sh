#!/bin/sh
output="HDMI-A-1"
echo $output >> /home/imaksus/.config/bin/hotplug.log
cat /sys/class/drm/card0-$output/status >> /home/imaksus/.config/bin/hotplug.log
date +%T >> /home/imaksus/.config/bin/hotplug.log



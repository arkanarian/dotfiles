#!/usr/bin/env python3
import pyudev


def udev_event_received(device):
    from datetime import datetime
    current_time = datetime.now().strftime("%H:%M:%S")
    import time
    time.sleep(0.3)  # для правильного определения статуса
    with open("/sys/class/drm/card0-HDMI-A-1/status", "r") as f:
        status = f.read()
    print(f"{current_time} {status}")
    import subprocess
    if status.strip() == "disconnected":
        # means disconnected, only laptop
        subprocess.run(["/home/imaksus/.config/bin/laptop_only.sh"])
        time.sleep(1)
        subprocess.run(["i3", "restart"])
    else:
        # means connected, both monitors
        subprocess.run(["/home/imaksus/.config/bin/4k_above_laptop.sh"])
        time.sleep(1)
        subprocess.run(["i3", "restart"])

context = pyudev.Context()
monitor_drm = pyudev.Monitor.from_netlink(context)
monitor_drm.filter_by(subsystem='drm')
observer_drm = pyudev.MonitorObserver(monitor_drm, callback=udev_event_received, daemon=False)

observer_drm.start()

# This will prevent the program from finishing:
observer_drm.join()

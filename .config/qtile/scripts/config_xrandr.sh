#!/bin/bash

# properly set my dual monitors with their rate and position

xrandr --output HDMI-A-0 --left-of DisplayPort-1
xrandr --output DisplayPort-1 --mode 1920x1080 --rate 143.85
xrandr --output HDMI-A-0 --mode 1920x1080 --rate 143.98

# TODO: add these lines to /etc/X11/Xsession.d/45custom_xrandr-settings

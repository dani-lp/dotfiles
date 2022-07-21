#!/bin/bash

# properly set my dual monitors with their rate and position

xrandr --output HDMI-1 --left-of DP-2
xrandr --output DP-2 --mode 1920x1080 --rate 143.85
xrandr --output HDMI-1 --mode 1920x1080 --rate 143.98

# TODO: add these lines to /etc/X11/Xsession.d/45custom_xrandr-settings

#!/bin/bash

export PATH="/home/dani/.local/bin:$PATH"

picom -b &
eww daemon &
volctl &
nm-applet &
blueman-applet &
mkfifo /tmp/vol-icon && ~/.config/qtile/scripts/vol_icon.sh &

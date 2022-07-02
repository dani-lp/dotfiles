#!/bin/bash

export PATH="/home/dani/.local/bin:$PATH"

picom -b &
eww daemon &
mkfifo /tmp/vol-icon && ~/.config/qtile/scripts/vol_icon.sh &

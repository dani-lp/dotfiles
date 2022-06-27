#!/usr/bin/env bash

picom -b &
eww daemon &
mkfifo /tmp/vol-icon && ~/.config/qtile/scripts/vol_icon.sh &

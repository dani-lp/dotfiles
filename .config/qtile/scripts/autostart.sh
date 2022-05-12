#!/usr/bin/env bash

~/.config/qtile/scripts/config_xrandr.sh &
picom -b &
mkfifo /tmp/vol-icon && ~/.config/qtile/scripts/vol_icon.sh &

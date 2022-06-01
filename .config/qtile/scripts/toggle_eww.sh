#!/usr/bin/env bash
set -euo pipefail

export PATH="/home/dani/dev/repos/eww/target/release:$PATH"

state=$(eww windows | grep main_bottom)

if [ "$state" == "*main_bottom" ]; then
    eww close main_bottom
else
    eww open main_bottom
fi

#!/usr/bin/env bash
set -euo pipefail

export PATH="/home/dani/Desktop/repos/eww/target/release:$PATH"

state=$(eww windows | grep dashboard)

if [ "$state" == "*dashboard" ]; then
    eww close dashboard
else
    eww open dashboard
fi

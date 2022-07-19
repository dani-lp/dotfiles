fg="#D9E0EE"
unlocker="#00000000"
ring="#1E1E2E"
wrong="#F28FAD"
highlight="#B5E8E0"
date="#DDB6F2"
verify="#DDB6F2"
ring_out="#ABE9B3"

i3lock \
    -n \
    --force-clock \
    -i ~/.config/qtile/wallpapers/cosmos-1080.jpg \
    -e \
    --indicator \
    --radius=40 \
    --ring-width=8 \
    --inside-color=$unlocker \
    --ring-color=$fg \
    --insidever-color=$verify \
    --ringver-color=$verify \
    --insidewrong-color=$wrong \
    --ringwrong-color=$wrong \
    --line-uses-inside \
    --keyhl-color=$ring \
    --separator-color=$verify \
    --bshl-color=$ring \
    --time-str="%H:%M" \
    --time-size=140 \
    --date-str="%a, %d %b" \
    --date-size=45 \
    --verif-text="Verifying Password..." \
    --wrong-text="Wrong Password!" \
    --noinput-text="" \
    --greeter-text="Type the password to unlock" \
    --time-font="JetBrainsMono Nerd Font" \
    --date-font="JetBrainsMono Nerd Font" \
    --verif-font="JetBrainsMono Nerd Font" \
    --greeter-font="JetBrainsMono Nerd Font" \
    --wrong-font="JetBrainsMono Nerd Font" \
    --verif-size=23 \
    --greeter-size=23 \
    --wrong-size=23 \
    --time-pos="300:560" \
    --date-pos="300:630" \
    --ind-pos="1620:520" \
    --greeter-pos="1620:630" \
    --wrong-pos="1620:670" \
    --verif-pos="1620:670" \
    --date-color=$date \
    --time-color=$date \
    --greeter-color=$fg \
    --wrong-color=$wrong \
    --verif-color=$verify \
    --pointer=default \
    --refresh-rate=0 \
    --pass-media-keys \
    --pass-volume-keys
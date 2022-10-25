from libqtile import hook
import subprocess
import os

from core import (
    groups,
    keys,
    mod,
    shift,
    layouts,
    floating_layout,
    screens,
    main_screen_bar,
    widget_defaults,
)

auto_fullscreen = True
auto_minimize = False
bring_front_click = False
cursor_warp = False
dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
focus_on_window_activation = 'smart'
# reconfigure_screens = True
wmname = "qtile"

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/scripts/autostart.sh"])

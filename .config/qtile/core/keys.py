from libqtile.config import Key, KeyChord
from libqtile.lazy import lazy

import os

mod = "mod4"
control = "control"
shift = "shift"
alt = "mod1"
terminal = "kitty"
home = os.path.expanduser('~')

# resize functions
def resize(qtile, direction):
    layout = qtile.current_layout
    child = layout.current
    parent = child.parent

    while parent:
        if child in parent.children:
            layout_all = False

            if (direction == "left" and parent.split_horizontal) or (
                direction == "up" and not parent.split_horizontal
            ):
                parent.split_ratio = max(5, parent.split_ratio - layout.grow_amount)
                layout_all = True
            elif (direction == "right" and parent.split_horizontal) or (
                direction == "down" and not parent.split_horizontal
            ):
                parent.split_ratio = min(95, parent.split_ratio + layout.grow_amount)
                layout_all = True

            if layout_all:
                layout.group.layout_all()
                break

        child = parent
        parent = child.parent


@lazy.function
def resize_left(qtile):
    current = qtile.current_layout.name
    layout = qtile.current_layout
    if current == "bsp":
        resize(qtile, "left")
    elif current == "columns":
        layout.cmd_grow_left()


@lazy.function
def resize_right(qtile):
    current = qtile.current_layout.name
    layout = qtile.current_layout
    if current == "bsp":
        resize(qtile, "right")
    elif current == "columns":
        layout.cmd_grow_right()


@lazy.function
def resize_up(qtile):
    current = qtile.current_layout.name
    layout = qtile.current_layout
    if current == "bsp":
        resize(qtile, "up")
    elif current == "columns":
        layout.cmd_grow_up()


@lazy.function
def resize_down(qtile):
    current = qtile.current_layout.name
    layout = qtile.current_layout
    if current == "bsp":
        resize(qtile, "down")
    elif current == "columns":
        layout.cmd_grow_down()


keys = [
    # essentials
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "q", lazy.window.kill(), desc="Kill active window"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle forward layout"),
    Key([mod, shift], "Tab", lazy.prev_layout(), desc="Toggle last layout"),
    # qtile
    Key([mod, shift], "r", lazy.restart(), desc="Restart Qtile"),
    # menus
    Key([mod], "e", lazy.spawn("rofi -show drun -theme ~/.config/rofi/launcher.rasi"), desc="Launch Rofi (drun)"),
    Key([mod], "r", lazy.spawn("rofi -show run -theme ~/.config/rofi/launcher.rasi"), desc="Launch Rofi (run)"),
    Key([mod, shift], "e", lazy.spawn("" + home + "/.local/bin/power"), desc="Power Menu"),
    Key([mod, shift], "n", lazy.spawn("" + home + "/.local/bin/nmgui"), desc="Network Menu"),
    # focus, move windows and screens
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down in current stack pane"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up in current stack pane"),
    Key([mod], "Left", lazy.layout.left(), desc="Move focus left in current stack pane"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus right in current stack pane",),
    Key([mod, shift], "Down", lazy.layout.shuffle_down(), lazy.layout.move_down(), desc="Move windows down in current stack",),
    Key([mod, shift], "Up", lazy.layout.shuffle_up(), lazy.layout.move_up(), desc="Move windows up in current stack",),
    Key([mod, shift], "Left", lazy.layout.shuffle_left(), lazy.layout.move_left(), desc="Move windows left in current stack",),
    Key([mod, shift], "Right", lazy.layout.shuffle_right(), lazy.layout.move_right(), desc="Move windows right in the current stack",),
    Key([mod], "x", lazy.next_screen(), desc="Move focus to next monitor",),    # TODO find a better hotkey
    Key([mod, control], "Down", lazy.layout.flip_down(), desc="Flip layout down"),
    Key([mod, control], "Up", lazy.layout.flip_up(), desc="Flip layout up"),
    Key([mod, control], "Left", lazy.layout.flip_left(), lazy.layout.swap_column_left(), desc="Flip layout left"),
    Key([mod, control], "Right", lazy.layout.flip_right(), lazy.layout.swap_column_left(), desc="Flip layout right"),
    # window resizing
    Key([mod, alt], "Left", resize_left, desc="Resize window left"),
    Key([mod, alt], "Right", resize_right, desc="Resize window Right"),
    Key([mod, alt], "Up", resize_up, desc="Resize windows upward"),
    Key([mod, alt], "Down", resize_down, desc="Resize windows downward"),
    Key([mod, alt], "n", lazy.layout.normalize(), desc="Normalize window size ratios"),
    # window states
    Key([mod], "m", lazy.window.toggle_maximize(), desc="Toggle window between minimum and maximum sizes",),
    Key([mod, shift], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
    Key([mod], "i", lazy.window.toggle_floating(), desc="Toggle floating mode for a window"),
    # floating mode
    # Key([mod] , "i", lazy.layout.grow(), desc="Increase window size"),
    # Key([mod, shift] , "i", lazy.layout.shrink(), desc="Decrease window size"),
    # program launches
    Key([mod], "f", lazy.spawn("firefox"), desc="Launch Firefox"),
    Key([mod], "p", lazy.spawn("nautilus"), desc="Launch Nautilus"),
    Key([mod], "c", lazy.spawn("code"), desc="Launch VSCode"),
    Key([mod], "n", lazy.spawn("notion-app-enhanced"), desc="Launch Notion"),
    Key([mod], "s", lazy.spawn("spotify"), desc="Launch Spotify"),
    Key([mod], "t", lazy.group["scratchpad"].dropdown_toggle("term")),
    Key([mod, shift], "t", lazy.group["scratchpad"].dropdown_toggle("btop-term")),
    # screenshots
    Key([], "Print", lazy.spawn("" + home + "/.local/bin/prtscreen"), desc="Print Screen"),
    Key([mod], "Print", lazy.spawn("" + home + "/.local/bin/prtscreenregion"), desc="Print region of screen"),
    Key([mod, shift], "s", lazy.spawn("" + home + "/.local/bin/prtscreenregion"), desc="Print region of screen"),
    # audio stuff
    Key([], "XF86AudioRaiseVolume", lazy.spawn("./.config/qtile/scripts/temp_vol.sh up"), desc="Increase volume",),
    Key([], "XF86AudioLowerVolume", lazy.spawn("./.config/qtile/scripts/temp_vol.sh down"), desc="Decrease volume",),
    Key([], "XF86AudioMute", lazy.spawn("./.config/qtile/scripts/temp_vol.sh mute"), desc="Toggle volume mute",),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc="Play last audio",),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="Play next audio"),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc="Toggle play/pause audio"),
    # Key([mod], "F8", lazy.spawn("playerctl stop"), desc="Stop audio"),
    # eww
    Key([mod], "d", lazy.spawn("" + home + "/.local/bin/toggle_eww"), desc="Toggle eww dashboard",),
    # brightness
    Key([], 'XF86MonBrightnessUp', lazy.spawn('brightnessctl set +5%'), desc='Increase brightness'), 
    Key([], 'XF86MonBrightnessDown', lazy.spawn('brightnessctl set 5%-'), desc='Decrease brightness'),
    # misc
    Key([mod], "w", lazy.spawn("" + home + "/.local/bin/wmname"), desc='Get wmname of a window',),
    # keychords
    KeyChord([mod], "l", [
        Key([], "a", lazy.spawn("aseprite"), desc="Launch Aseprite"),
        Key([], "d", lazy.spawn("discord"), desc="Launch Discord"),
        Key([], "m", lazy.spawn("gnome-mahjongg"), desc="Launch Gnome Mahjongg"),
        Key([], "t", lazy.spawn("cat /home/dani/.token | xclip -selection clipboard"), desc="Copy GitHub token into the clipboard"),
        Key([], "e", lazy.spawn("/bin/bash /home/dani/dev/jku/system_software/SSW_Editor/editor_dev.sh file.txt"), desc="Copy GitHub token into the clipboard"),
    ], name="Launcher", ),
]

def show_keys():
    key_help = ""
    for i in range(0, len(keys)):
        k = keys[i]
        if not isinstance(k, Key):
            continue
        mods = ""

        for m in k.modifiers:
            if m == "mod4":
                mods += "Super + "
            else:
                mods += m.capitalize() + " + "

        if len(k.key) > 1:
            mods += k.key.capitalize()
        else:
            mods += k.key

        key_help += "{:<25} {}".format(mods, k.desc + ("\n" if i != len(keys) - 1 else ""))

    return key_help

keys.extend(
    [
        Key(
            [mod],
            "a",
            lazy.spawn(
                "sh -c 'echo \""
                + show_keys()
                + '" | rofi -dmenu -theme ~/.config/rofi/hotkeys.rasi -i -p ""\''
            ),
            desc="Print keyboard bindings",
        ),
    ]
)

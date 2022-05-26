from libqtile import bar, hook, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile import qtile
import subprocess
import os

# from libqtile.utils import guess_terminal
from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration

mod = "mod4"
# terminal = guess_terminal()
terminal = "kitty"

# TODO
# - dropdown terminal
# - custom icons for layouts
# - customize special rofi menus
# - screenshots
# - bar functions
# - qtile hooks
# 
# Take a look at:
# - Countdown, Memory widget

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
    Key([mod, "shift"], "Tab", lazy.prev_layout(), desc="Toggle last layout"),
    # qtile
    Key([mod, "shift"], "r", lazy.restart(), desc="Restart Qtile"),
    # menus
    Key([mod], "e", lazy.spawn("rofi -show drun"), desc="Launch Rofi"),
    # Key([mod, "shift"], "e", lazy.spawn("power"), desc="Power Menu"),
    # focus, move windows
    Key(
        [mod], "Down", lazy.layout.down(), desc="Move focus down in current stack pane"
    ),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up in current stack pane"),
    Key(
        [mod], "Left", lazy.layout.left(), desc="Move focus left in current stack pane"
    ),
    Key(
        [mod],
        "Right",
        lazy.layout.right(),
        desc="Move focus right in current stack pane",
    ),
    Key(
        [mod, "shift"],
        "Down",
        lazy.layout.shuffle_down(),
        lazy.layout.move_down(),
        desc="Move windows down in current stack",
    ),
    Key(
        [mod, "shift"],
        "Up",
        lazy.layout.shuffle_up(),
        lazy.layout.move_up(),
        desc="Move windows up in current stack",
    ),
    Key(
        [mod, "shift"],
        "Left",
        lazy.layout.shuffle_left(),
        lazy.layout.move_left(),
        desc="Move windows left in current stack",
    ),
    Key(
        [mod, "shift"],
        "Right",
        lazy.layout.shuffle_right(),
        lazy.layout.move_right(),
        desc="Move windows right in the current stack",
    ),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle forward layout"),
    Key([mod, "shift"], "Tab", lazy.prev_layout(), desc="Toggle last layout"),
    # TODO revise layout flipping + swapping
    # window resizing
    Key([mod, "mod1"], "Left", resize_left, desc="Resize window left"),
    Key([mod, "mod1"], "Right", resize_right, desc="Resize window Right"),
    Key([mod, "mod1"], "Up", resize_up, desc="Resize windows upward"),
    Key([mod, "mod1"], "Down", resize_down, desc="Resize windows downward"),
    Key([mod, "mod1"], "n", lazy.layout.normalize(), desc="Normalize window size ratios"),
    # window states
    Key(
        [mod],
        "m",
        lazy.window.toggle_maximize(),
        desc="Toggle window between minimum and maximum sizes",
    ),
    Key([mod, "shift"], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
    # program launches
    Key([mod], "f", lazy.spawn("firefox"), desc="Launch Firefox"),
    Key([mod], "p", lazy.spawn("nautilus"), desc="Launch Nautilus"),
    Key([mod], "c", lazy.spawn("code"), desc="Launch VSCode"),
    Key([mod], "n", lazy.spawn("notion-app"), desc="Launch Notion"),
    # TODO rofi variants
    # system shortcuts
    # Key([], "Print", lazy.spawn("prtscr"), desc="Print Screen"),  # TODO enable
    # Key([mod], "Print", lazy.spawn("prtregion -d"), desc="Print region of screen"),   # TODO enable
    # Key([mod, "shift"], "Print", lazy.spawn("prtregion -c"), desc="Print region of screen to clipboard"), # TODO enable
    # audio stuff
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("./.config/qtile/scripts/temp_vol.sh up"),
        desc="Increase volume",
    ),
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("./.config/qtile/scripts/temp_vol.sh down"),
        desc="Decrease volume",
    ),
    Key(
        [mod],
        "F5",
        lazy.spawn("playerctl previous"),
        desc="Play last audio",
    ),
    Key([mod], "F6", lazy.spawn("playerctl next"), desc="Play next audio"),
    Key(
        [mod], "F7", lazy.spawn("playerctl play-pause"), desc="Toggle play/pause audio"
    ),
    Key([mod], "F8", lazy.spawn("playerctl stop"), desc="Stop audio"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
]

# workspace_names = [
#     " WEB",
#     " DEV",
#     " SYS",
#     " DISC",
#     " MUS",
#     " DIR",
#     " NOT",
# ]

workspace_names = [
    "",
    "",
    "",
    "",
    "",
    "",
    "",
]

# TODO revise "lay", wm_classes
workspaces = [
    {"name": workspace_names[0], "key": "1", "matches": [Match(wm_class="firefox")], "lay": "bsp"},
    {"name": workspace_names[1], "key": "2", "matches": [Match(wm_class="code")], "lay": "bsp"},
    {"name": workspace_names[2], "key": "3", "matches": [], "lay": "bsp"},
    {
        "name": workspace_names[3],
        "key": "4",
        "matches": [Match(wm_class="discord")],
        "lay": "bsp",
    },
    {"name": workspace_names[4], "key": "5", "matches": [Match(wm_class="spotify")], "lay": "bsp"},
    {
        "name": workspace_names[5],
        "key": "6",
        "matches": [Match(wm_class="org.gnome.Nautilus")],
        "lay": "bsp",
    },
    {
        "name": workspace_names[6],
        "key": "7",
        "matches": [Match(wm_class="notion-app")],
        "lay": "bsp",
    },
]

groups = [Group(i) for i in "123456789"]

for workspace in workspaces:
    matches = workspace["matches"] if "matches" in workspace else None
    groups.append(Group(workspace["name"], matches=matches, layout=workspace["lay"]))
    keys.append(
        Key(
            [mod],
            workspace["key"],
            lazy.group[workspace["name"]].toscreen(toggle=True),
            desc="Focus this desktop",
        )
    )
    keys.append(
        Key(
            [mod, "shift"],
            workspace["key"],
            lazy.window.togroup(workspace["name"]),
            desc="Move focused window to another group",
        )
    )

# for i in groups:
#     keys.extend(
#         [
#             # mod1 + letter of group = switch to group
#             Key(
#                 [mod],
#                 i.name,
#                 lazy.group[i.name].toscreen(),
#                 desc="Switch to group {}".format(i.name),
#             ),
#             # mod1 + shift + letter of group = switch to & move focused window to group
#             Key(
#                 [mod, "shift"],
#                 i.name,
#                 lazy.window.togroup(i.name, switch_group=True),
#                 desc="Switch to & move focused window to group {}".format(i.name),
#             ),
#             # Or, use below if you prefer not to switch to that group.
#             # # mod1 + shift + letter of group = move focused window to group
#             # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
#             #     desc="move focused window to group {}".format(i.name)),
#         ]
#     )

# Catppuccin colors

colors = [
    ["#DDB6F2", "#DDB6F2"],  #  0 mauve
    ["#F5C2E7", "#F5C2E7"],  #  1 pink
    ["#E8A2AF", "#E8A2AF"],  #  2 maroon
    ["#F28FAD", "#F28FAD"],  #  3 red
    ["#F8BD96", "#F8BD96"],  #  4 peach
    ["#FAE3B0", "#FAE3B0"],  #  5 yellow
    ["#ABE9B3", "#ABE9B3"],  #  6 green
    ["#B5E8E0", "#B5E8E0"],  #  7 teal
    ["#96CDFB", "#96CDFB"],  #  8 blue
    ["#89DCEB", "#89DCEB"],  #  9 sky
    ["#161320", "#161320"],  # 10 black 0
    ["#1A1826", "#1A1826"],  # 11 black 1
    ["#1E1E2E", "#1E1E2E"],  # 12 black 2
    ["#302D41", "#302D41"],  # 13 black 3
    ["#575268", "#575268"],  # 14 black 4
    ["#6E6C7E", "#6E6C7E"],  # 15 gray 0
    ["#988BA2", "#988BA2"],  # 16 gray 1
    ["#C3BAC6", "#C3BAC6"],  # 17 gray 2
    ["#D9E0EE", "#D9E0EE"],  # 18 white
    ["#C9CBFF", "#C9CBFF"],  # 19 lavender
    ["#F5E0DC", "#F5E0DC"],  # 20 rosewater
]

layout_theme = {
    "border_width": 2,
    "margin": 2,
    "border_focus": colors[2][1:],  # REVIEW might have to add second coordinates
    "border_normal": colors[12][1:],
    # "font": "JetBrains Mono",
    "font": "FiraCode Nerd Font",
    "grow_amount": 2,  # TODO tf is this
}

# TODO revise every option
layouts = [
    layout.Bsp(**layout_theme, fair=False, border_on_single=True),
    layout.MonadTall(**layout_theme, ratio=0.6),
]

widget_defaults = dict(
    font="FiraCode Nerd Font",
    fontsize=14,
    padding=2,
    background=colors[13],
    decorations=[
        BorderDecoration(
            colour=colors[8],
            border_width=[0, 0, 0, 0],
        )
    ],
)
extension_defaults = widget_defaults.copy()

group_box_settings = {
    "active": colors[2],  # or [1]
    "background": colors[12],  # background is [10-12]
    "block_highlight_text_color": colors[2],
    "borderwidth": 2,
    "disable_drag": True,
    "fontsize": 14,
    "foreground": colors[18],  # might need a lighter color
    "highlight_color": colors[13],  # TODO revise
    "highlight_method": "line",
    "inactive": colors[14],
    "other_current_screen_border": colors[12],
    "other_screen_border": colors[12],
    "padding_x": 10,
    "padding_y": 16,
    "rounded": False,
    "this_current_screen_border": colors[2],
    "this_screen_border": colors[2],  # or [1], [2]
    "urgent_border": colors[3],
}

# Define functions for bar
# TODO

# Mouse_callback functions
def open_launcher():
    qtile.cmd_spawn("rofi -show drun")

def open_powermenu():
    qtile.cmd_spawn("power")


def create_bar():
    """Create top bar, defined as function to allow duplication in other monitors"""
    def _separator():
        return widget.Sep(
            foreground=colors[18],
            padding=10,
            linewidth=2,
            size_percent=55,
            background=colors[12],
        )
    
    return bar.Bar(
        [
            widget.TextBox(
                # text=" ",
                text=" ",
                font="FiraCode Nerd Font",
                fontsize=20,
                foreground=colors[2],
                background=colors[10],
                padding=16,
                mouse_callbacks={"Button1": open_launcher},
            ),
            # Workspaces
            widget.GroupBox(  # WEB
                font="Font Awesome 6 Brands",
                visible_groups=[workspace_names[0]],
                **group_box_settings,
            ),
            widget.GroupBox(  # DEV, SYS
                font="Font Awesome 6 Free Solid",
                visible_groups=[workspace_names[1], workspace_names[2]],
                **group_box_settings,
            ),
            widget.GroupBox(  # DISC, MUS
                font="Font Awesome 6 Brands",
                visible_groups=[workspace_names[3], workspace_names[4]],
                **group_box_settings,
            ),
            widget.GroupBox(  # FILE, NOT
                font="Font Awesome 6 Free Solid",
                visible_groups=[workspace_names[5], workspace_names[6]],
                **group_box_settings,
            ),
            widget.CurrentLayoutIcon(
                custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
                foreground=colors[2],
                background=colors[10],
                padding=10,
                scale=0.5,
            ),
            # Middle spacer
            widget.Clipboard(),
            widget.Spacer(),
            # Sound
            widget.TextBox(
                text="",
                foreground=colors[6],
                background=colors[12],
                font="Font Awesome 6 Free Solid",
                # fontsize=38,
                padding=8,
            ),
            widget.PulseVolume(
                foreground=colors[6],
                background=colors[12],
                limit_max_volume="True",
                # mouse_callbacks={"Button3": open_pavu},
                padding=8,
            ),
            _separator(),
            # Date
            widget.TextBox(
                text="",
                font="Font Awesome 6 Free Solid",
                foreground=colors[7],  # teal
                # fontsize=38
                background=colors[12],
                padding=8,
            ),
            widget.Clock(
                format="%a, %b %d",
                foreground=colors[7],
                background=colors[12],
                padding=8,
            ),
            _separator(),
            # Clock
            widget.TextBox(
                text="",
                font="Font Awesome 6 Free Solid",
                foreground=colors[8],  # blue
                # fontsize=38
                background=colors[12],
                padding=8,
            ),
            widget.Clock(
                format="%I:%M %p",
                foreground=colors[8],
                background=colors[12],
                padding=8,
            ),
            # Power button
            widget.TextBox(
                text="⏻",
                background=colors[10],
                foreground=colors[2],
                font="Font Awesome 6 Free Solid",
                fontsize=16,
                padding=20,
                mouse_callbacks={"Button1": open_powermenu},
            ),
        ],
        32,
        margin=[6, 6, 6, 6],
        opacity=1,
    )

main_screen_bar = create_bar()
secondary_screen_bar = create_bar()

screens = [
    Screen(
        wallpaper="~/.config/qtile/wallpapers/evening-sky.png",
        wallpaper_mode="fill",
        top=main_screen_bar,
        bottom=bar.Gap(4),
        left=bar.Gap(4),
        right=bar.Gap(4),
    ),
    Screen(
        wallpaper="~/.config/qtile/wallpapers/evening-sky-flipped.png",
        wallpaper_mode="fill",
        top=secondary_screen_bar,
        bottom=bar.Gap(4),
        left=bar.Gap(4),
        right=bar.Gap(4),
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
# bring_front_click = "floating_only"
cursor_warp = False
floating_layout = layout.Floating(
    **layout_theme,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        # TODO add matches
    ],
)
auto_fullscreen = True
focus_on_window_activation = "smart"  # TODO check using "focus" instead of "smart"
# reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = False

# When using the Wayland backend, this can be used to configure input devices.
# wl_input_rules = None

# TODO take a look at hooks
@hook.subscribe.startup
def start():
    main_screen_bar.window.window.set_property("QTILE_BAR", 1)

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/scripts/autostart.sh"])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

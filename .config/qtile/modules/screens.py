import os

from libqtile import bar, qtile, widget
from libqtile.config import Screen

from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration

from utils.settings import colors, two_monitors, wallpaper_main, wallpaper_sec, workspace_names


widget_defaults = dict(
    font="FiraCode Nerd Font",
    fontsize=14,
    padding=2,
    background=colors[12],
    # background='#00000000',
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
    qtile.cmd_spawn("rofi -show drun -theme ~/.config/rofi/launcher.rasi")

def open_powermenu():
    qtile.cmd_spawn("power")

def parse_window_name(text):
    """Simplifies the names of a few windows, to be displayed in the bar"""
    target_names = [
        'Mozilla Firefox',
        'Visual Studio Code',
        'Discord',
    ]
    return next(filter(lambda name: name in text, target_names), text)


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
                text="",
                font="FiraCode Nerd Font",
                fontsize=34,
                foreground='#ffffff',
                # foreground=colors[2],
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
            # Middle spacer
            widget.Spacer(),
            # Window name TODO
            widget.TextBox(
                text=" ",
                foreground='#ffffff',
                # background='#00000000',
                # fontsize=38,
                font="Font Awesome 6 Free Solid",
            ),
            widget.WindowName(
                # background='#00000000',
                foreground='#ffffff',
                width=bar.CALCULATED,
                empty_group_string="Desktop",
                max_chars=40,
                parse_text=parse_window_name,
                # mouse_callbacks={"Button2": function_to_define},
            ),
            widget.Spacer(),
            # WM layout indicator
            widget.CurrentLayoutIcon(
                custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
                foreground=colors[2],
                background=colors[12],
                padding=10,
                scale=0.5,
            ),
            _separator(),
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
                format="%b %d, %H:%M",
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
        30,
        margin=[4, 6, 2, 6],
        opacity=1,
        background='#00000000'
    )

main_screen_bar = create_bar()
secondary_screen_bar = create_bar()

screens = [
    Screen(
        wallpaper=wallpaper_main,
        wallpaper_mode="fill",
        top=main_screen_bar,
        bottom=bar.Gap(2),
        left=bar.Gap(2),
        right=bar.Gap(2),
    ),
]

if two_monitors:
    screens.append(
        Screen(
            wallpaper=wallpaper_sec,
            wallpaper_mode="fill",
            top=secondary_screen_bar,
            bottom=bar.Gap(2),
            left=bar.Gap(2),
            right=bar.Gap(2),
        ),
    )
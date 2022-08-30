from libqtile import bar, qtile, lazy

from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration

from utils.settings import colors, with_battery, with_wlan, workspace_names

import os

home = os.path.expanduser("~")

group_box_settings = {
    "active": colors[0],
    "block_highlight_text_color": colors[0],
    "this_current_screen_border": colors[0],
    "this_screen_border": colors[0],
    "urgent_border": colors[3],
    "background": colors[12],  # background is [10-12]
    "other_current_screen_border": colors[12],
    "other_screen_border": colors[12],
    "highlight_color": colors[13],
    "inactive": colors[14],
    "foreground": colors[18],
    "borderwidth": 2,
    "disable_drag": True,
    "fontsize": 14,
    "highlight_method": "line",
    "padding_x": 10,
    "padding_y": 16,
    "rounded": False,
}

# functions for callbacks
def open_launcher():
    qtile.cmd_spawn("rofi -show drun -theme ~/.config/rofi/launcher.rasi")


def open_powermenu():
    qtile.cmd_spawn("" + home + "/.local/bin/power")


def open_calendar():
    qtile.cmd_spawn("" + home + "/.local/bin/toggle_cal")


# TODO fix
def toggle_maximize():
    lazy.window.toggle_maximize()


def parse_window_name(text):
    """Simplifies the names of a few windows, to be displayed in the bar"""
    target_names = [
        "Mozilla Firefox",
        "Visual Studio Code",
        "Discord",
    ]
    return next(filter(lambda name: name in text, target_names), text)


# separator
def separator():
    return widget.Sep(
        # foreground=colors[18],
        foreground=colors[12],
        padding=4,
        linewidth=3,
    )


def separator_sm():
    return widget.Sep(
        # foreground=colors[18],
        foreground=colors[12],
        padding=1,
        linewidth=1,
        size_percent=55,
    )


# widget decorations
base_decor = {
    "colour": colors[13],
    "filled": True,
    "padding_y": 4,
    "line_width": 0,
}


def _full_decor(color):
    return [
        RectDecoration(
            colour=color,
            radius=4,
            filled=True,
            padding_y=4,
        )
    ]


# def _left_decor(color):
#     return [
#         RectDecoration(
#             colour=color,
#             radius=[4, 0, 0, 4],
#             filled=True,
#             padding_y=4,
#         )
#     ]


# def _right_decor(color):
#     return [
#         RectDecoration(
#             colour=colors[10],
#             radius=0,
#             filled=True,
#             padding_y=5,
#             padding_x=0,
#         ),
#         RectDecoration(
#             colour=color,
#             radius=[0, 4, 4, 0],
#             filled=False,
#             line_width=2,
#             padding_y=5,
#             padding_x=0,
#         ),
#     ]


def _left_decor(color, padding_x=None, padding_y=4):
    return [
        RectDecoration(
            colour=color,
            radius=4,
            filled=True,
            padding_x=padding_x,
            padding_y=padding_y,
        )
    ]


def _right_decor(color):
    return [
        RectDecoration(
            colour=colors[13],
            radius=4,
            filled=True,
            padding_y=4,
            padding_x=0,
        )
    ]


# hollow knight icon
w_hk = widget.Image(
    background=colors[0],
    margin_x=14,
    margin_y=3,
    mouse_callbacks={"Button1": open_launcher},
    filename="~/.config/qtile/icons/hkskull.png",
)

# left icon
w_sys_icon = widget.TextBox(
    # text=" ",
    # text="",
    # text="ﮊ",
    # text="",
    # text="",
    text="",
    font="Font Awesome 6 Free Solid",
    fontsize=22,
    foreground="#000000",
    # foreground=colors[2],
    background=colors[0],
    padding=16,
    mouse_callbacks={"Button1": open_launcher},
)

# workspace groups
w_groupbox_1 = widget.GroupBox(  # WEB
    font="Font Awesome 6 Brands",
    visible_groups=[workspace_names[0]],
    **group_box_settings,
)

w_groupbox_2 = widget.GroupBox(  # DEV, SYS
    font="Font Awesome 6 Free Solid",
    visible_groups=[workspace_names[1], workspace_names[2]],
    **group_box_settings,
)

w_groupbox_3 = widget.GroupBox(  # DISC, MUS
    font="Font Awesome 6 Brands",
    visible_groups=[workspace_names[3], workspace_names[4]],
    **group_box_settings,
)

w_groupbox_4 = widget.GroupBox(  # FILE, NOT
    font="Font Awesome 6 Free Solid",
    visible_groups=[workspace_names[5], workspace_names[6]],
    **group_box_settings,
)


def gen_groupbox():
    return (
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
    )


# spacers
def gen_spacer():
    return widget.Spacer()


# window name
w_window_name_icon = widget.TextBox(
    text=" ",
    foreground="#ffffff",
    font="Font Awesome 6 Free Solid",
)

w_window_name = widget.WindowName(
    foreground="#ffffff",
    width=bar.CALCULATED,
    empty_group_string="Desktop",
    max_chars=40,
    parse_text=parse_window_name,
    mouse_callbacks={"Button1": toggle_maximize},
)

# systray
w_systray = widget.Systray(
    padding=5,
)

# current layout
def gen_current_layout():
    color = colors[5]

    return (
        widget.CurrentLayoutIcon(
            custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
            padding=3,
            scale=0.65,
            use_mask=True,
            foreground=colors[12],
            decorations=_left_decor(color),
        ),
        separator_sm(),
        widget.CurrentLayout(
            foreground=color,
            padding=8,
            decorations=_right_decor(color),
        ),
        separator(),
    )


# battery
w_battery = (
    (
        widget.Battery(
            format="{char}",
            charge_char="",
            discharge_char="",
            full_char="",
            unknown_char="",
            empty_char="",
            show_short_text=False,
            foreground=colors[10],
            fontsize=18,
            padding=8,
            decorations=_left_decor(colors[1]),
        ),
        separator_sm(),
        widget.Battery(
            format="{percent:2.0%}",
            show_short_text=False,
            foreground=colors[1],
            padding=8,
            decorations=_right_decor(colors[5]),
        ),
        separator(),
    )
    if with_battery
    else ()
)

# volume
w_volume_icon = widget.TextBox(
    text="墳",
    foreground=colors[10],
    font="JetBrainsMono Nerd Font",
    fontsize=20,
    padding=8,
    decorations=_left_decor(colors[6]),
)

w_volume = widget.PulseVolume(
    foreground=colors[6],
    limit_max_volume="True",
    # mouse_callbacks={"Button3": open_pavu},
    padding=8,
    decorations=_right_decor(colors[6]),
)

# internet
w_wlan = (
    (
        widget.Wlan(
            format="󰖩",
            foreground=colors[10],
            disconnected_message="󰖪",
            fontsize=16,
            interface="wlo1",
            update_interval=5,
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn("" + home + "/.local/bin/nmgui"),
                # "Button3": lambda: qtile.cmd_spawn(myTerm + " -e nmtui"),
            },
            padding=4,
            decorations=_left_decor(colors[2]),
        ),
        separator_sm(),
        widget.Wlan(
            format="{percent:2.0%}",
            disconnected_message=" ",
            interface="wlo1",
            update_interval=5,
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn("" + home + "/.local/bin/nmgui"),
                # "Button3": lambda: qtile.cmd_spawn(myTerm + " -e nmtui"),
            },
            padding=8,
            decorations=_right_decor(colors[2]),
        ),
        separator(),
    )
    if with_wlan
    else ()
)

# time, calendar
def gen_clock():
    color = colors[8]

    return (
        widget.TextBox(
            text="",
            font="JetBrainsMono Nerd Font",
            fontsize=16,
            foreground=colors[10],  # blue
            padding=8,
            decorations=_left_decor(color),
            mouse_callbacks={"Button1": open_calendar},
        ),
        separator_sm(),
        widget.Clock(
            format="%b %d, %H:%M",
            foreground=color,
            padding=8,
            decorations=_right_decor(color),
            mouse_callbacks={"Button1": open_calendar},
        ),
        separator(),
    )


# power menu
w_power = widget.TextBox(
    text="⏻",
    background=colors[0],
    foreground="#000000",
    font="Font Awesome 6 Free Solid",
    fontsize=18,
    padding=16,
    mouse_callbacks={"Button1": open_powermenu},
)

w_test = widget.WidgetBox(
    close_button_location="right",
    fontsize=24,
    font="JetBrainsMono Nerd Font",
    text_open=" ",
    text_closed=" ",
    widgets=[w_systray],
    decorations=_left_decor(colors[2]),
)

# widget box
w_box = widget.WidgetBox(
    close_button_location='right',
    fontsize=24,
    text_closed='',
    text_open='',
    widgets=[
        widget.CPU(
        
        ),
        widget.DF(
        
        ),    # free disk space
        widget.Memory(
        
        ),
        # widget.Net(
        
        # ),
        # TODO uptime, CPU, temp, diskfree, memory
    ],
)

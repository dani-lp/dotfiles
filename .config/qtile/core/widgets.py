from libqtile import bar, qtile, lazy

from qtile_extras import widget
from qtile_extras.widget import decorations
from qtile_extras.widget.decorations import RectDecoration


from utils.settings import workspace_names
from utils import color, config

import os

home = os.path.expanduser('~')

group_box_settings = {
    'active': color['fg'],
    'block_highlight_text_color': color['fg'],
    'this_current_screen_border': color['fg'],
    'this_screen_border': color['fg'],
    'urgent_border': color['red'],
    'background': color['bg'],  # background is [10-12]
    'other_current_screen_border': color['bg'],
    'other_screen_border': color['bg'],
    'highlight_color': color['darkgray'],
    'inactive': color['gray'],
    'foreground': color['white'],
    'borderwidth': 2,  # change to 2 to add bottom border to active group
    'disable_drag': True,
    'fontsize': 20,
    'highlight_method': 'line',
    'padding_x': 10,
    'padding_y': 16,
    'rounded': False,
}

# functions for callbacks


def open_launcher():
    qtile.cmd_spawn('rofi -show drun -theme ~/.config/rofi/launcher.rasi')


def open_powermenu():
    qtile.cmd_spawn('' + home + '/.local/bin/power')


def open_calendar():
    qtile.cmd_spawn('' + home + '/.local/bin/toggle_cal')


def parse_window_name(text):
    '''Simplifies the names of a few windows, to be displayed in the bar'''
    target_names = [
        'Mozilla Firefox',
        'Visual Studio Code',
        'Discord',
    ]
    try:
        return next(filter(lambda name: name in text, target_names), text)
    except TypeError:
        return text


# separator
def separator():
    return widget.Sep(
        # foreground=color['white'],
        foreground=color['bg'],
        padding=4,
        linewidth=3,
    )


def separator_sm():
    return widget.Sep(
        # foreground=color['white'],
        foreground=color['bg'],
        padding=1,
        linewidth=1,
        size_percent=55,
    )


# widget decorations
base_decor = {
    'colour': color['black'],
    'filled': True,
    'padding_y': 4,
    'line_width': 0,
}


def _left_decor(color: str, padding_x=None, padding_y=4, round=False):
    radius = 4 if round else [4, 0, 0, 4]
    return [
        RectDecoration(
            colour=color,
            radius=radius,
            filled=True,
            padding_x=padding_x,
            padding_y=padding_y,
        )
    ]


def _right_decor(round=False):
    radius = 4 if round else [0, 4, 4, 0]
    return [
        RectDecoration(
            colour=color['darkgray'],
            radius=radius,
            filled=True,
            padding_y=4,
            padding_x=0,
        )
    ]


# hollow knight icon
w_hk = widget.Image(
    background=color['fg'],
    margin_x=14,
    margin_y=3,
    mouse_callbacks={'Button1': open_launcher},
    filename='~/.config/qtile/icons/hkskull.png',
)

# left icon
w_sys_icon = widget.TextBox(
    # text=' ',
    # text='',
    # text='ﮊ',
    # text='',
    # text='',
    # text='',
    text='',
    # text='',
    # text='',
    font='Font Awesome 6 Free Solid',
    fontsize=22,
    foreground='#000000',
    # foreground=color['maroon'],
    background=color['fg'],
    padding=16,
    mouse_callbacks={'Button1': open_launcher},
)


# workspace groups
def gen_groupbox():
    return (
        widget.GroupBox(
            # font='Font Awesome 6 Free Solid',
            font='Xiaolai SC',
            visible_groups=workspace_names,
            ** group_box_settings,
        ),
    )


def chord():
    return (
        widget.Chord(
            # name_transform=lambda name: f'"{name}"',
            foreground=color['bg'],
            decorations=_left_decor(color=color['fg'], round=True),
        )
    )


# spacers
def gen_spacer():
    return widget.Spacer()


# window name
def window_name():
    return (
        widget.TextBox(
            text=' ',
            foreground='#ffffff',
            font='Font Awesome 6 Free Solid',
        ),
        widget.WindowName(
            foreground='#ffffff',
            width=bar.CALCULATED,
            empty_group_string='Desktop',
            max_chars=40,
            parse_text=parse_window_name,
        )
    )


w_window_name_icon = widget.TextBox(
    text=' ',
    foreground='#ffffff',
    font='Font Awesome 6 Free Solid',
)

w_window_name = widget.WindowName(
    foreground='#ffffff',
    width=bar.CALCULATED,
    empty_group_string='Desktop',
    max_chars=40,
    parse_text=parse_window_name,
)

# systray
w_systray = widget.Systray(
    padding=5,
    icon_size=20,
)

# current layout


def gen_current_layout():
    w_color = color['pink']

    return (
        widget.CurrentLayoutIcon(
            custom_icon_paths=[os.path.expanduser('~/.config/qtile/icons')],
            scale=0.65,
            use_mask=True,
            foreground=color['bg'],
            decorations=_left_decor(w_color),
        ),
        separator_sm(),
        widget.CurrentLayout(
            foreground=w_color,
            padding=8,
            decorations=_right_decor(),
        ),
        separator(),
    )


# battery
w_battery = (
    (
        widget.Battery(
            format='{char}',
            charge_char='',
            discharge_char='',
            full_char='',
            unknown_char='',
            empty_char='',
            show_short_text=False,
            foreground=color['dark'],
            fontsize=18,
            padding=8,
            decorations=_left_decor(color['yellow']),
        ),
        separator_sm(),
        widget.Battery(
            format='{percent:2.0%}',
            show_short_text=False,
            foreground=color['yellow'],
            padding=8,
            decorations=_right_decor(),
        ),
        separator(),
    )
    if config['with_battery']
    else ()
)

# volume
w_volume_icon = widget.TextBox(
    text='墳',
    foreground=color['dark'],
    font='JetBrainsMono Nerd Font',
    fontsize=20,
    padding=8,
    decorations=_left_decor(color['green']),
)

w_volume = widget.PulseVolume(
    foreground=color['green'],
    limit_max_volume='True',
    # mouse_callbacks={'Button3': open_pavu},
    padding=8,
    decorations=_right_decor(),
)

# internet
w_wlan = (
    (
        widget.Wlan(
            format='󰖩',
            foreground=color['dark'],
            disconnected_message='󰖪',
            fontsize=16,
            interface='wlo1',
            update_interval=5,
            mouse_callbacks={
                'Button1': lambda: qtile.cmd_spawn('' + home + '/.local/bin/nmgui'),
                # 'Button3': lambda: qtile.cmd_spawn(myTerm + ' -e nmtui'),
            },
            padding=4,
            decorations=_left_decor(color['maroon']),
        ),
        separator_sm(),
        widget.Wlan(
            format='{percent:2.0%}',
            disconnected_message=' ',
            interface='wlo1',
            update_interval=5,
            mouse_callbacks={
                'Button1': lambda: qtile.cmd_spawn('' + home + '/.local/bin/nmgui'),
                # 'Button3': lambda: qtile.cmd_spawn(myTerm + ' -e nmtui'),
            },
            padding=8,
            decorations=_right_decor(),
        ),
        separator(),
    )
    if config['with_wlan']
    else ()
)

# time, calendar


def gen_clock():
    w_color = color['blue']

    return (
        widget.TextBox(
            text='',
            font='JetBrainsMono Nerd Font',
            fontsize=16,
            foreground=color['dark'],  # blue
            padding=8,
            decorations=_left_decor(w_color),
            mouse_callbacks={'Button1': open_calendar},
        ),
        separator_sm(),
        widget.Clock(
            format='%b %d, %H:%M',
            foreground=w_color,
            padding=8,
            decorations=_right_decor(),
            mouse_callbacks={'Button1': open_calendar},
        ),
        separator(),
    )


# power menu
w_power = widget.TextBox(
    text='⏻',
    background=color['fg'],
    foreground='#000000',
    font='Font Awesome 6 Free Solid',
    fontsize=18,
    padding=16,
    mouse_callbacks={'Button1': open_powermenu},
)

w_test = widget.WidgetBox(
    close_button_location='right',
    fontsize=24,
    font='JetBrainsMono Nerd Font',
    text_open=' ',
    text_closed=' ',
    widgets=[w_systray],
    decorations=_left_decor(color['maroon']),
)


def w_updates():
    w_color = color['red']

    return (
        widget.CheckUpdates(
            display_format='󰊠',
            distro='Arch',
            initial_text='󰊠',
            no_update_string='󰧵',
            font='Material Design Icons',
            fontsize=18,
            foreground=color['dark'],  # blue
            colour_have_updates=color['dark'],  # blue
            colour_no_updates=color['dark'],  # blue
            padding=4,
            decorations=_left_decor(w_color),
        ),
        separator_sm(),
        widget.CheckUpdates(
            display_format='{updates}',
            distro='Arch',
            initial_text='󰮯',
            no_update_string="0",
            foreground=w_color,
            padding=8,
            decorations=_right_decor(),
        ),
        separator(),
    )


# widget box
# w_box = widget.WidgetBox(
#     close_button_location='right',
#     fontsize=24,
#     text_closed='',
#     text_open='',
#     widgets=[
#         widget.CPU(
#
#         ),
#         widget.DF(
#
#         ),    # free disk space
#         widget.Memory(
#
#         ),
#         # widget.Net(
#
#         # ),
#         # TODO uptime, CPU, temp, diskfree, memory
#     ],
# )

from libqtile import bar
from libqtile.config import Screen

from qtile_extras import widget

from modules.widgets import *
from utils.settings import colors, two_monitors, wallpaper_main, wallpaper_sec


widget_defaults = dict(
    font="JetBrainsMono Nerd Font",
    fontsize=15,
    padding=2,
    background=colors[12],
)
extension_defaults = widget_defaults.copy()


def create_bar():
    """Create top bar, defined as function to allow duplication in other monitors"""
    return bar.Bar(
        [
            w_sys_icon,
            # Workspaces
            w_groupbox_1,
            w_groupbox_2,
            w_groupbox_3,
            w_groupbox_4,

            # Left spacer
            w_spacer_1,

            # Window name
            w_window_name_icon,
            w_window_name,
            
            # Right spacer
            w_spacer_2,

            # WM layout indicator
            w_current_layout_icon,
            w_systray,
            separator(),
            # Battery
            *w_battery,
            # Sound
            w_volume_icon,
            separator_sm(),
            w_volume,
            separator(),
            # Wlan
            w_wlan_1,
            separator_sm(),
            w_wlan_2,
            separator(),
            # Clock
            w_clock_icon,
            separator_sm(),
            w_clock,
            separator(),
            # w_wifi,
            # widget.WidgetBox(
            #     close_button_location="right",
            #     fontsize=24,
            #     text_open=" ",
            #     text_closed=" ",
            #     widgets=[
            #         *w_battery,
            #         # Sound
            #         w_volume_icon,
            #         w_volume,
            #         separator(),
            #         # Clock
            #         w_clock_icon,
            #         w_clock,
            #         separator(),
            #     ],
            # ),
            # Power button
            w_power,
        ],
        30,
        margin=[4, 6, 2, 6],
    )


main_screen_bar = create_bar()
if two_monitors:
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

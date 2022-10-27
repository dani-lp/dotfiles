from libqtile import bar
from libqtile.config import Screen

from utils import config
from core.bar import main_screen_bar, secondary_screen_bar


screens = [
    Screen(
        wallpaper=config['wallpaper_main'],
        wallpaper_mode="fill",
        top=main_screen_bar,
        bottom=bar.Gap(2),
        left=bar.Gap(2),
        right=bar.Gap(2),
    ),
]

if config['two_monitors']:
    screens.append(
        Screen(
            wallpaper=config['wallpaper_sec'],
            wallpaper_mode="fill",
            top=secondary_screen_bar,
            bottom=bar.Gap(2),
            left=bar.Gap(2),
            right=bar.Gap(2),
        ),
    )

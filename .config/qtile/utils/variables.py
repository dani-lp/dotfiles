import json
from utils import dir

directory = f'{dir.get()}/settings.json'

default_settings = [
    {
        "general": {
            "mod": "mod1",
            "network": "ens33",
            "two_monitors": True,
            "with_battery": False,
            "with_wlan": False,
        },
        "applications": {
            "terminal": "kitty",
            "editor": "vscodium",
            "browser": "librewolf",
            "app_launcher": "rofi -show drun",
            "mail_client": "thunderbird",
            "note_app": "obsidian",
            "screenshot_app": "flameshot gui",
        },
        "theme": {
            "bar": "decorated",
            "colorscheme": "catppuccin.json",
            "wallpapers": {
                "wallpaper_main": "~/pictures/wallpapers/floating_astronaut.png",
                "wallpaper_sec": "~/pictures/wallpapers/floating_astronaut.png",
            },
            "workspace_names": {
                "workspace_0": "\ue007",
                "workspace_1": "\uf121",
                "workspace_2": "\uf120",
                "workspace_3": "\uf70e",
                "workspace_4": "\uf0e0",
                "workspace_5": "\uf167",
                "workspace_6": "\uf1bc",
                "workspace_7": "\uf412",
                "workspace_8": "\uf4f9",
            },
        },
    }
]


def load_settings(cls):
    def wrap():
        instance = cls()
        instance.settings = read_settings_file()
        return instance

    def read_settings_file():
        try:
            with open(directory) as f:
                return dict(json.load(f)[0])
        except (json.JSONDecodeError, FileNotFoundError):
            return default_settings[0]

    return wrap


@load_settings
class Variables:
    def __init__(self):
        pass

    def __getattr__(self, name):
        value = self.settings.get(name)
        if isinstance(value, dict):
            sub_instance = Variables()
            sub_instance.settings = value
            return sub_instance

    def __getitem__(self, name):
        return self.settings[name]
    
    def get(self, key, default=None):
        return self.settings.get(key, default)


var = Variables()

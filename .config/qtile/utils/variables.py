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
            "colors": {
                "color_1": "#DDB6F2",
                "color_2": "#F5C2E7",
                "color_3": "#E8A2AF",
                "color_4": "#F28FAD",
                "color_5": "#F8BD96",
                "color_6": "#FAE3B0",
                "color_7": "#ABE9B3",
                "color_8": "#B5E8E0",
                "color_9": "#96CDFB",
                "color_10": "#89DCEB",
                "color_11": "#161320",
                "color_12": "#1A1826",
                "color_13": "#1E1E2E",
                "color_14": "#302D41",
                "color_15": "#575268",
                "color_16": "#6E6C7E",
                "color_17": "#988BA2",
                "color_18": "#C3BAC6",
                "color_19": "#D9E0EE",
                "color_20": "#C9CBFF",
                "color_21": "#F5E0DC",
            },
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

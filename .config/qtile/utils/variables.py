import json
from utils import dir

directory = f'{dir.get()}/config.json'
variables = {
    'bar': 'decorated',
    'colorscheme': 'catppuccin',
    'terminal': 'kitty',
    'wallpaper': '~/.config/qtile/wallpapers/mini_black_hole.png',
}

try:
    with open(directory, 'r') as file:
        config = json.load(file)
        file.close()
except FileNotFoundError:
    with open(directory, 'w') as file:
        file.write(json.dumps(variables, indent = 2))
        config = variables.copy()
        file.close()

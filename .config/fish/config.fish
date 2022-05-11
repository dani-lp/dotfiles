set -g -x fish_greeting ''

source ~/.config/fish/.shells/alias
source ~/.config/fish/.shells/functions
source ~/.config/fish/.shells/exports

# init starship prompt
starship init fish | source

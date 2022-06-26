set -g -x fish_greeting ''

source ~/.config/fish/alias

# exports
set PATH $PATH $HOME/.local/Aseprite $HOME/.cargo/bin

# init starship prompt
starship init fish | source

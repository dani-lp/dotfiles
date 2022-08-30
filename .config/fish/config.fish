set -g -x fish_greeting ''

source ~/.config/fish/alias

# exports
set PATH $PATH $HOME/.local/Aseprite $HOME/.cargo/bin $HOME/.local/bin

# init nvm
bass source /usr/share/nvm/init-nvm.sh

# init starship prompt
starship init fish | source

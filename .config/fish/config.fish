set -g -x fish_greeting ''

source ~/.config/fish/alias

# exports
set PATH $PATH $HOME/.local/Aseprite $HOME/.cargo/bin $HOME/.local/bin $HOME/Desktop/Programs/idea-IU-222.4167.29/bin

# init nvm
bass source /usr/share/nvm/init-nvm.sh

# init starship prompt
starship init fish | source

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
eval /home/dani/Desktop/Programs/miniconda3/bin/conda "shell.fish" "hook" $argv | source
# <<< conda initialize <<<
fish_add_path /home/dani/.spicetify

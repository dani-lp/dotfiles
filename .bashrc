# If not running interactively, don't do anything
[ -z "$PS1" ] && return

# User info
export USERNAME="Dani"
export NICKNAME="danilp"

# Divide bashrc into smaller and specific files
source ~/.shells/alias
source ~/.shells/defaults
source ~/.shells/functions

# starship
eval "$(starship init bash)"

[ -f ~/.fzf.bash ] && source ~/.fzf.bash

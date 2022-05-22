set -g -x fish_greeting ''

source ~/.config/fish/.shells/alias
source ~/.config/fish/.shells/functions
source ~/.config/fish/.shells/exports

# functions TODO move to external files
function reload_dots
  echo "Reloading dots"

  echo "Copying bat config..."
  /bin/cp -rf ~/.config/bat/ ~/dev/dotfiles/.config/

  echo "Copying fish config..."
  /bin/cp -rf ~/.config/fish/ ~/dev/dotfiles/.config/

  echo "Copying kitty config..."
  /bin/cp -rf ~/.config/kitty/ ~/dev/dotfiles/.config/

  echo "Copying neofetch config..."
  /bin/cp -rf ~/.config/neofetch/ ~/dev/dotfiles/.config/

  echo "Copying neovim config..."
  /bin/cp -rf ~/.config/nvim/ ~/dev/dotfiles/.config/

  echo "Copying qtile config..."
  /bin/cp -rf ~/.config/qtile/ ~/dev/dotfiles/.config/

  echo "Copying rofi config..."
  /bin/cp -rf ~/.config/rofi/ ~/dev/dotfiles/.config/

  echo "Copying starship config..."
  /bin/cp -rf ~/.config/starship.toml ~/dev/dotfiles/.config/
end

# exports
set PATH "$HOME/.local/Aseprite:$PATH"

# init starship prompt
starship init fish | source

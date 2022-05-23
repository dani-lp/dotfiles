set -g -x fish_greeting ''

source ~/.config/fish/.shells/alias
# source ~/.config/fish/.shells/functions
# source ~/.config/fish/.shells/exports

# functions TODO move to external files
function save_dots
  echo "Saving dots to repo"

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

function load_dots
  echo "Loading dots into system"

  echo "Loading bat config..."
  /bin/cp -rf ~/dev/dotfiles/.config/bat/ ~/.config/

  echo "Loading fish config..."
  /bin/cp -rf ~/dev/dotfiles/.config/fish/ ~/.config/

  echo "Loading kitty config..."
  /bin/cp -rf ~/dev/dotfiles/.config/kitty/ ~/.config/

  echo "Loading neofetch config..."
  /bin/cp -rf ~/dev/dotfiles/.config/neofetch/ ~/.config/

  echo "Loading neovim config..."
  /bin/cp -rf ~/dev/dotfiles/.config/nvim/ ~/.config/

  echo "Loading qtile config..."
  /bin/cp -rf ~/dev/dotfiles/.config/qtile/ ~/.config/

  echo "Loading rofi config..."
  /bin/cp -rf ~/dev/dotfiles/.config/rofi/ ~/.config/

  echo "Loading starship config..."
  /bin/cp -rf ~/dev/dotfiles/.config/starship.toml ~/.config/
end

# exports
set PATH "$HOME/.local/Aseprite:$PATH"

# init starship prompt
starship init fish | source

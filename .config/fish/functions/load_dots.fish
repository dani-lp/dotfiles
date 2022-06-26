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

  echo "Loading picom config..."
  /bin/cp -rf ~/dev/dotfiles/.config/picom ~/.config/
end
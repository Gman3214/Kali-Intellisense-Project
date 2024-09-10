#!/bin/bash

# Clone zsh-autocomplete repository
git clone --depth 1 https://github.com/marlonrichert/zsh-autocomplete.git ~/.zsh-autocomplete

# Clone Kali Intellisense Project repository
git clone https://github.com/Gman3214/Kali-Intellisense-Project ~/.kip

# Edit the .zshrc file
sed -i '/# see \/usr\/share\/doc\/zsh\/examples\/zshrc for examples/a\
source ~/.zsh-autocomplete/zsh-autocomplete.plugin.zsh\nsource ~/.kip/kip.zsh' ~/.zshrc

# Open a new terminal and close this one
x-terminal-emulator & disown
exit

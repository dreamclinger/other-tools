#!/usr/bin/env bash

ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install python
sudo easy_install pip
pip install python-docx
pip install PIL
pip install lxml
pip install python-dateutil

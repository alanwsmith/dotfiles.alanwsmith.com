#!/usr/bin/env python3

import json
import subprocess
import sys
import time
from app_mover import AppMover

# you can see window names with:
# yabai -m query --windows | jq '.[] | { app: .app, title: .title }'

# This is the setup for working from the house with

if __name__ == "__main__":
    am = AppMover()

    am.stage_apps()

    # Screen 1 - Desktops 1-8

    am.move_app_to_space('iTerm2', 1)
    am.insert_from_anchor('iTerm2', 'west', 'Google Chrome')
    am.insert_from_anchor('Google Chrome', 'south', 'nvALT')
    am.expand_left('iTerm2', 180)

    am.move_app_to_space('Fork', 2)

    am.move_app_to_space('Code', 3)

    am.move_app_to_space('CodeRunner', 4)
    am.insert_from_anchor('CodeRunner', 'north', 'Sublime Text')

    am.move_app_to_space('Adobe Photoshop 2022', 5)

    am.move_app_to_space('Soulver 3', 6)
    # am.move_app_to_space('Lightroom Classic', 7)

    # Screen 2 - Desktops 9-16
    am.move_app_to_space('Safari', 9)
    am.move_app_to_space('1Password 7', 10)
    am.insert_from_anchor('1Password 7', 'south', 'Keychain Access')
    am.move_app_to_space('Discord', 11)


    am.focus_app('Safari')
    am.focus_app('iTerm2')


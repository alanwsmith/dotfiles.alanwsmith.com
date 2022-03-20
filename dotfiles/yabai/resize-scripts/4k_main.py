#!/usr/bin/env python3

import json
import subprocess
import sys
import time

from app_mover import AppMover

# you can see window names with:
# yabai -m query --windows | jq '.[] | { app: .app, title: .title }'

if __name__ == "__main__":

    am = AppMover()
    am.stage_apps()


    # Screen 2 - Desktops 9-16

    am.move_app_to_space('Discord', 10)
    am.move_app_to_space('1Password 7', 11)
    am.insert_from_anchor('1Password 7', 'west', 'Keychain Access')


    # Screen 1 - Desktops 2-8

    am.move_app_to_space('Adobe Photoshop 2022', 2)
    am.move_app_to_space('Adobe Bridge 2022', 2)


    # Screen 1 - Desktops 1

    am.move_app_to_space('iTerm2', 1)
    am.insert_from_anchor('iTerm2', 'west', 'Google Chrome')
    am.expand_left('iTerm2', 660)

    am.insert_from_anchor('iTerm2', 'south', 'CodeRunner')
    am.expand_bottom('iTerm2', 480)

    am.insert_from_anchor('iTerm2', 'east', 'Code')
    am.expand_right('iTerm2', 150)

    am.insert_from_anchor('Code', 'north', 'Sublime Text')
    am.expand_bottom('Sublime Text', 350)

    am.insert_from_anchor('Sublime Text', 'north', 'Safari')
    am.expand_bottom('Safari', 300)

    am.insert_from_anchor('iTerm2', 'north', 'Fork')
    am.expand_top('iTerm2', 200)

    am.insert_from_anchor('Google Chrome', 'south', 'nvALT')
    am.expand_bottom('Google Chrome', 270)

    am.insert_from_anchor('Google Chrome', 'north', 'Soulver 3')
    am.expand_top('Google Chrome', 350)




    # Final Focus 

    am.focus_app('1Password 7')
    am.focus_app('iTerm2')


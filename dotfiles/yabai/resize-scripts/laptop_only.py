#!/usr/bin/env python3

import json
import subprocess
import sys
import time
from app_mover import AppMover

if __name__ == "__main__":
    am = AppMover()

#    yabai -m config window_gap 6
#    yabai -m config top_padding 6
#    yabai -m config bottom_padding 6
#    yabai -m config left_padding 6
#    yabai -m config right_padding 6

    am.stage_apps()

    am.move_app_to_space('Google Chrome', 1)
    am.insert_from_anchor('Google Chrome', 'south', 'iTerm2')
    am.insert_from_anchor('iTerm2', 'west', 'nvALT')
    am.move_app_to_space('Code', 2)
    am.move_app_to_space('CodeRunner', 3)
    am.insert_from_anchor('CodeRunner', 'east', 'Sublime Text')
    am.move_app_to_space('Adobe Photoshop 2022', 4)
    am.move_app_to_space('Safari', 5)
    am.move_app_to_space('1Password 7', 6)
    am.insert_from_anchor('1Password 7', 'south', 'Keychain Access')

    am.move_app_to_space('Discord', 7)

    am.focus_app('iTerm2')


#!/usr/bin/env python3

import json
import subprocess
import sys
import time
from app_mover import AppMover

if __name__ == "__main__":
    am = AppMover()

    am.stage_apps()

    # Screen 1 - Desktops 1-8
    am.move_app_to_space('iTerm2', 9)
    am.insert_from_anchor('iTerm2', 'west', 'Google Chrome')
    am.insert_from_anchor('Google Chrome', 'south', 'nvALT')
    am.move_app_to_space('GitHub Desktop', 10)
    am.move_app_to_space('Code', 11)
    am.move_app_to_space('CodeRunner', 12)
    am.insert_from_anchor('CodeRunner', 'east', 'Sublime Text')
    am.move_app_to_space('Adobe Photoshop 2022', 13)

    # Screen 2 - Desktops 9-16
    am.move_app_to_space('Safari', 1)
    am.move_app_to_space('1Password 7', 2)
    am.insert_from_anchor('1Password 7', 'south', 'Keychain Access')

    am.move_app_to_space('Discord', 3)

    am.focus_app('Safari')
    am.focus_app('iTerm2')


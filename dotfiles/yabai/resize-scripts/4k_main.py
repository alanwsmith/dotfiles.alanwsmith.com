#!/usr/bin/env python3

import json
import subprocess
import sys
import time

from app_mover import AppMover

if __name__ == "__main__":

    am = AppMover()
    am.stage_apps()

    am.move_app_to_space('Adobe Photoshop 2022', 2)
    am.move_app_to_space('Code', 3)
    am.move_app_to_space('Safari', 6)
    am.move_app_to_space('Music', 7)
    am.move_app_to_space('Discord', 8)
    am.move_app_to_space('1Password 7', 9)
    am.insert_from_anchor('1Password 7', 'south', 'Keychain Access')
    am.move_app_to_space('iTerm2', 1)
    am.insert_from_anchor('iTerm2', 'west', 'Google Chrome')
    am.expand_left('iTerm2', 660)
    am.insert_from_anchor('iTerm2', 'north', 'GitHub Desktop')
    am.expand_top('iTerm2', 390)
    am.insert_from_anchor('iTerm2', 'south', 'CodeRunner')
    am.expand_bottom('iTerm2', 130)
    am.insert_from_anchor('CodeRunner', 'east', 'DBeaver Community')
    am.insert_from_anchor('Google Chrome', 'south', 'nvALT')
    am.insert_from_anchor('iTerm2', 'east', 'Code')
    am.expand_right('iTerm2', 300)
    am.insert_from_anchor('GitHub Desktop', 'east', 'Soulver 3')
    am.insert_from_anchor('Soulver 3', 'south', 'Sublime Text')
    am.expand_right('GitHub Desktop', 140)
    am.focus_app('Google Chrome')
    am.focus_app('Safari')
    am.focus_app('iTerm2')


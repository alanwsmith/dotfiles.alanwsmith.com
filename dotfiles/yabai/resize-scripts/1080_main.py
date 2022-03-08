#!/usr/bin/env python3

import json
import subprocess
import sys
import time

if __name__ == "__main__":
    am = AppMover()

    am.stage_apps()
    am.move_app_to_space('GitHub Desktop', 2)
    am.move_app_to_space('Adobe Photoshop 2022', 3)
    am.move_app_to_space('DB Browser for SQLite', 4)
    am.move_app_to_space('Code', 5)
    am.move_app_to_space('Discord', 6)
    am.move_app_to_space('Music', 7)
    am.move_app_to_space('1Password 7', 8)
    # am.move_app_to_space('Keychain Access', 9)

    am.move_app_to_space('iTerm2', 1)
    am.insert_from_anchor('iTerm2', 'west', 'Google Chrome')
    # am.expand_left('iTerm2', 280)
    am.insert_from_anchor('Google Chrome', 'south', 'nvALT')

    # am.insert_from_anchor('iTerm2', 'north', 'GitHub Desktop')
    # am.expand_top('iTerm2', 390)
    # am.insert_from_anchor('iTerm2', 'south', 'CodeRunner')
    # am.expand_bottom('iTerm2', 130)
    # am.insert_from_anchor('CodeRunner', 'east', 'Sublime Text')
    # am.insert_from_anchor('iTerm2', 'east', 'Terminal')
    # am.expand_right('iTerm2', 300)
    # am.insert_from_anchor('GitHub Desktop', 'east', 'Safari')
    # am.expand_right('GitHub Desktop', 140)

    # am.focus_app('Music')
    am.focus_app('iTerm2')


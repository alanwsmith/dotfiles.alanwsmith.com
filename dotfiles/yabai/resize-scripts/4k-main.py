#!/usr/bin/env python3

import json
import subprocess
import time

# This doesn't currently deal with two windows for the same app

# Theres a bunch of sleep lines in that prevent race conditions. 
# It slows things down, but it works. I've got an idea about how 
# to bounch of the window and space status queries to make it 
# faster. That's for a future iteration. 

# Note that app window names don't always match what's shown in 
# the menu bar. e.g. 'Photoshop' is really something like 
# 'Adobe Photoshop 2022'. You can check them with:
# 
# yabai -m query --windows



class WindowMover():
    def __init__(self):
        self.windows = self.get_window_status()
        self.spaces = self.get_spaces_status()
        self.apps = {}
        self.map_app_names()

    def add_app_after_direction(self, initial_app, direction, new_app):
        print(f"Adding app {new_app} to the {direction} of {initial_app}")
        for window in self.windows:
            if (window['app'] == initial_app):
                target_space = window['space']
                time.sleep(1)
                subprocess.run(f"/opt/homebrew/bin/yabai -m window --focus {self.apps[initial_app]['id']}".split(' '), check=True)
                time.sleep(0.5)
                subprocess.run(f"/opt/homebrew/bin/yabai -m window --insert {direction}".split(' '), check=True)
                time.sleep(1)
                subprocess.run(f"/opt/homebrew/bin/yabai -m window --focus {self.apps[new_app]['id']}".split(' '), check=True)
                time.sleep(0.5)
                subprocess.run(f"/opt/homebrew/bin/yabai -m window --space {target_space}".split(' '), check=True)
                time.sleep(0.5)

    def get_spaces_status(self):
        results = subprocess.run(['/opt/homebrew/bin/yabai', '-m', 'query', '--spaces'], capture_output=True, check=True)
        return json.loads(results.stdout.decode('utf-8'))

    def get_window_status(self):
        results = subprocess.run(['/opt/homebrew/bin/yabai', '-m', 'query', '--windows'], capture_output=True, check=True)
        return json.loads(results.stdout.decode('utf-8'))

    def map_app_names(self):
        for window in self.windows:
            self.apps[window['app']] = { 'id': window['id']}

    def stage_apps(self):
        for window in self.windows:
            print(f"Staging app: {window['app']} in window {window['id']}")
            subprocess.run(f"/opt/homebrew/bin/yabai -m window --focus {window['id']}".split(' '), check=True)
            subprocess.run(f"/opt/homebrew/bin/yabai -m window --space {len(self.spaces)}".split(' '), check=True)
            time.sleep(0.5)

    def move_app_to_space(self, app, space):
        print(f"Moving app {app} to space {space}")
        # TODO: Figure out which of these delays is necessary 
        # and see if it has to do with space moves and see if
        # there's a way to optimize it.
        time.sleep(0.8)
        subprocess.run(f"/opt/homebrew/bin/yabai -m window --focus {self.apps[app]['id']}".split(' '), check=True)
        time.sleep(0.8)
        subprocess.run(f"/opt/homebrew/bin/yabai -m window --space {space}".split(' '), check=True)
        time.sleep(0.8)
        subprocess.run(f"/opt/homebrew/bin/yabai -m window --focus {self.apps[app]['id']}".split(' '), check=True)
        time.sleep(0.8)

    def reset_bsp(self):
        # Just move the current window across all spaces and reset them to bsp
        # Not totally sure this works
        for space in self.spaces:
            print(f"Resetting space {space['index']} to bsp")
            subprocess.run(f"/opt/homebrew/bin/yabai -m window --focus {self.windows[0]['id']}".split(' '), check=True)
            time.sleep(1)
            subprocess.run(f"/opt/homebrew/bin/yabai -m window --space {space['index']}".split(' '), check=True)
            time.sleep(1)
            subprocess.run(f"/opt/homebrew/bin/yabai -m window --focus {self.windows[0]['id']}".split(' '), check=True)
            time.sleep(1)
            subprocess.run(f"/opt/homebrew/bin/yabai -m space --layout bsp".split(' '))
            time.sleep(0.3)

    def resize_app(self, app, details):
        print(f"Resizing app: {app} - {details}")
        time.sleep(0.5)
        subprocess.run(f"/opt/homebrew/bin/yabai -m window --focus {self.apps[app]['id']}".split(' '), check=True)
        time.sleep(0.5)
        subprocess.run(f"/opt/homebrew/bin/yabai -m window --resize {details}".split(' '), check=True)
        time.sleep(0.5)

    def select_app(self, app):
        print(f"Selecting app: {app}")
        subprocess.run(f"/opt/homebrew/bin/yabai -m window --focus {self.apps[app]['id']}".split(' '), check=True)
        time.sleep(0.5)

    def stack_apps(self, top_app, bottom_app):
        print(f"Stacking apps: {top_app} - {bottom_app}")
        for window in self.windows:
            if (window['app'] == top_app):
                target_space = window['space']
                time.sleep(0.7)
                subprocess.run(f"/opt/homebrew/bin/yabai -m window --focus {self.apps[top_app]['id']}".split(' '), check=True)
                time.sleep(0.7)
                subprocess.run(f"/opt/homebrew/bin/yabai -m window --insert stack".split(' '), check=True)
                time.sleep(0.7)
                subprocess.run(f"/opt/homebrew/bin/yabai -m window --focus {self.apps[bottom_app]['id']}".split(' '), check=True)
                time.sleep(0.7)
                subprocess.run(f"/opt/homebrew/bin/yabai -m window --space {target_space}".split(' '), check=True)
                time.sleep(0.7)
                subprocess.run(f"/opt/homebrew/bin/yabai -m window --focus {self.apps[top_app]['id']}".split(' '), check=True)
                time.sleep(0.7)



if __name__ == '__main__':
    wm = WindowMover()

    # wm.reset_bsp() # shouldn't need to do this unless you change things to float manually
    wm.stage_apps()
    wm.move_app_to_space('iTerm2', 1)
    wm.move_app_to_space('nvALT', 1)
    wm.move_app_to_space('Google Chrome', 1)
    wm.move_app_to_space('Adobe Photoshop 2022', 3)
    wm.move_app_to_space('Discord', 5)
    wm.move_app_to_space('Music', 6)
    wm.move_app_to_space('Safari', 7)
    wm.resize_app('iTerm2', 'left:-420:0')

    wm.stack_apps('iTerm2', 'Code')
    wm.stack_apps('Google Chrome', 'Terminal')
    wm.stack_apps('nvALT', 'GitHub Desktop')

    wm.add_app_after_direction('iTerm2', 'south', 'CodeRunner')
    wm.add_app_after_direction('CodeRunner', 'east', 'Sublime Text')

    #wm.resize_app('iTerm2', 'top:0:-360')
    wm.resize_app('iTerm2', 'bottom:0:120')
    wm.resize_app('CodeRunner', 'right:120:0')

    wm.select_app('iTerm2')

    print("Resizing complete")


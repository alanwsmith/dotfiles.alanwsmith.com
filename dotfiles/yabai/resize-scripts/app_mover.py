#!/usr/bin/env python3

import json
import subprocess
import sys
import time

############################################################
#
# NOTE: you can see window names with:
# yabai -m query --windows
#
############################################################
#
# TODO:
#
# - Setup so the script can work off a config
# 
# - Make optimizations to remove unnecessary moves
#   and see if you can avoid staging all apps and
#   only stage the ones that need it. 
#
# - Figure out how to set this up so that
#   it opens the app which is named differently.
#   One example is Code/Visual Studio Code.
#
# - Setup to split any apps that aren't explitly
#   defined across any spaces that haven't been used. 
#
# - Deal with apps where more than one window 
#   is opened. 
#
# - Create a map of app names that show up in the 
#   windows vs the ones that are launched so the app 
#   can open them as needed. 
#
# - Figure out how to deal with multiple windows
#   Probably pick one and use it's ID for the movement
#   and then just stack the other ones behind it?
#
# - Send a notification when done, or when there's 
#   trouble with the process.
# 
# - Pass in the time and yabai path?
#
# - Use screen numbers with space offset for.
#   positioining. For exmple, Instead of Space 10, 
#   use Screen 2 - Space 2. That way if you add
#   more spaces to the first screen it won't 
#   effect the spaces of the spaces of the
#   second one
#
############################################################

class AppMover():
    def __init__(self):
        print("Initialzing AppMover")
        self.time_padding = 0.2
        self.yabai_path = '/opt/homebrew/bin/yabai'

    def app_space_id(self, app):
        for window in self.windows():
            if window['app'] == app:
                return window['space']

    def contract_bottom(self, app, amount):
        print(f"Contracting left: {app} - {amount}")
        self.focus_app(app)
        subprocess.run(f"{self.yabai_path} -m window --resize bottom:0:-{amount}".split(' '), check=True)

    def contract_left(self, app, amount):
        print(f"Contracting left: {app} - {amount}")
        self.focus_app(app)
        subprocess.run(f"{self.yabai_path} -m window --resize left:{amount}:0".split(' '), check=True)

    def contract_right(self, app, amount):
        print(f"Contracting left: {app} - {amount}")
        self.focus_app(app)
        subprocess.run(f"{self.yabai_path} -m window --resize right:-{amount}:0".split(' '), check=True)

    def contract_top(self, app, amount):
        print(f"Contracting left: {app} - {amount}")
        self.focus_app(app)
        subprocess.run(f"{self.yabai_path} -m window --resize top:0:{amount}".split(' '), check=True)

    def ensure_app_is_open(self, app):
        print(f"Ensuring {app} is open")
        if self.window_id_for_app(app) == None:
            print(f"Opening {app}")
            subprocess.run(['open', '-a', app])
            for i in range(1,50):
                time.sleep(self.time_padding)
                print('.', end='')
                if self.window_id_for_app(app) != None:
                    print(f"Opened {app}")
                    return True
            print(f"Could not open {app} in a reasonalbe time")
            print("Process halted.")
            sys.exit()

    def expand_bottom(self, app, amount):
        print(f"Resizing left: {app} - {amount}")
        self.focus_app(app)
        subprocess.run(f"{self.yabai_path} -m window --resize bottom:0:{amount}".split(' '), check=True)

    def expand_left(self, app, amount):
        print(f"Resizing left: {app} - {amount}")
        self.focus_app(app)
        subprocess.run(f"{self.yabai_path} -m window --resize left:-{amount}:0".split(' '), check=True)

    def expand_right(self, app, amount):
        print(f"Resizing left: {app} - {amount}")
        self.focus_app(app)
        subprocess.run(f"{self.yabai_path} -m window --resize right:{amount}:0".split(' '), check=True)

    def expand_top(self, app, amount):
        print(f"Resizing left: {app} - {amount}")
        self.focus_app(app)
        subprocess.run(f"{self.yabai_path} -m window --resize top:0:-{amount}".split(' '), check=True)

    def focus_app(self, app):
        print(f"Switching focus to {app}")
        # See if it's already in focus
        for window in self.windows():
            if window['app'] == app and window['has-focus']:
                print(f"{app} already has focus")
                return True
        # otherwise make sure it's open and switch focus to it
        self.ensure_app_is_open(app)
        print(f"Focusing: {app}")
        for window in self.windows():
            if window['app'] == app:
                subprocess.run(f"{self.yabai_path} -m window --focus {window['id']}".split(' '), check=True)
                for i in range(1,14):
                    print(f"Checking focus on: {app}")
                    for check_window in self.windows():
                        if check_window['has-focus'] == True and check_window['app'] == app:
                            print(f"Confirmed {app} is in focus")
                            # need this padding to let the system catch up
                            time.sleep(self.time_padding)
                            return True
                    time.sleep(self.time_padding)
        print(f"Could not focus on {app}")
        print("Process halted")
        sys.exit()

    def insert_from_anchor(self, anchor_app, direction, new_app):
        print(f"Insert from anchor: {anchor_app} - {direction} - {new_app}")
        self.focus_app(anchor_app)
        subprocess.run(f"{self.yabai_path} -m window --insert {direction}".split(' '), check=True)
        self.move_app_to_space(new_app, self.app_space_id(anchor_app))

    def move_app_to_space(self, app, space):
        print(f"Moving: {app} to: {space}")
        if self.app_space_id(app) == space:
            print(f"No need to move. {app} is already on space {space}")
        else:
            # TODO: Make this a recursive function instead of copy paste    
            self.focus_app(app)
            subprocess.run(f"{self.yabai_path} -m window --space {space}".split(' '), check=True)
            print(f"Confirming {app} moved to space {space}")
            for i in range(1, 20):
                if self.app_space_id(app) == space:
                    print(f"- Moved: {app} to: {space}")
                    time.sleep(self.time_padding)
                    return True
                time.sleep(self.time_padding)
                print('.', end='')

            print("- Move didn't work. Trying again")
            self.focus_app(app)
            subprocess.run(f"{self.yabai_path} -m window --space {space}".split(' '), check=True)
            for i in range(1, 30):
                if self.app_space_id(app) == space:
                    print(f"- Moved: {app} to: {space}")
                    time.sleep(self.time_padding)
                    return True
                time.sleep(self.time_padding)
                print('.', end='')

            print("- Move didn't work. Trying again")
            self.focus_app(app)
            subprocess.run(f"{self.yabai_path} -m window --space {space}".split(' '), check=True)
            for i in range(1, 30):
                if self.app_space_id(app) == space:
                    print(f"- Moved: {app} to: {space}")
                    time.sleep(self.time_padding)
                    return True
                time.sleep(self.time_padding)
                print('.', end='')

            print()
            print(f"Failed to move {app} to space {space}")
            print(f"Process halted")
            sys.exit()

    def place_app_under_app(self, lower_app, upper_app):
        print(f"Placing {lower_app} under {upper_app}")
        if self.app_space_id(lower_app) == self.app_space_id(upper_app):
            print(f"Skipping: {lower_app} is already in space {self.app_space_id(lower_app)} with {upper_app}")
            return False
        else:
            self.focus_app(upper_app)
            subprocess.run(f"{self.yabai_path} -m window --insert stack".split(' '), check=True)
            self.focus_app(lower_app)
            self.move_app_to_space(lower_app, self.app_space_id(upper_app))
            print(f"Placed: {lower_app} under {upper_app}")

    def window_id_for_app(self, app):
        for window in self.windows():
            if window['app'] == app:
                print(f"App {app} has ID: {window['id']}")
                return window['id']
        return None

    def spaces(self):
        results = subprocess.run([self.yabai_path, '-m', 'query', '--spaces'], capture_output=True, check=True)
        return json.loads(results.stdout.decode('utf-8'))

    def stage_apps(self):
        staging_space = len(self.spaces())
        for window in self.windows():
            if window['is-floating'] == False:
                self.move_app_to_space(window['app'], staging_space)

    def windows(self):
        results = subprocess.run(f'{self.yabai_path} -m query --windows'.split(' '), capture_output=True)
        return json.loads(results.stdout.decode('utf-8'))


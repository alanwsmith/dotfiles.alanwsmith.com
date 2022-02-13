#!/usr/bin/env python3

import json
import subprocess
import sys
import time

class AppMover():
    def app_space_id(self, app):
        for window in self.windows():
            if window['app'] == app:
                return window['space']

    def contract_bottom(self, app, amount):
        print(f"Contracting left: {app} - {amount}")
        self.focus_app(app)
        subprocess.run(f"/opt/homebrew/bin/yabai -m window --resize bottom:0:-{amount}".split(' '), check=True)

    def contract_left(self, app, amount):
        print(f"Contracting left: {app} - {amount}")
        self.focus_app(app)
        subprocess.run(f"/opt/homebrew/bin/yabai -m window --resize left:{amount}:0".split(' '), check=True)

    def contract_right(self, app, amount):
        print(f"Contracting left: {app} - {amount}")
        self.focus_app(app)
        subprocess.run(f"/opt/homebrew/bin/yabai -m window --resize right:-{amount}:0".split(' '), check=True)

    def contract_top(self, app, amount):
        print(f"Contracting left: {app} - {amount}")
        self.focus_app(app)
        subprocess.run(f"/opt/homebrew/bin/yabai -m window --resize top:0:{amount}".split(' '), check=True)

    def ensure_app_is_open(self, app):
        print(f"Ensuring {app} is open")
        if self.window_id_for_app(app) == None:
            print(f"Opening {app}")
            subprocess.run(['open', '-a', app])
            for i in range(1,50):
                time.sleep(.1)
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
        subprocess.run(f"/opt/homebrew/bin/yabai -m window --resize bottom:0:{amount}".split(' '), check=True)

    def expand_left(self, app, amount):
        print(f"Resizing left: {app} - {amount}")
        self.focus_app(app)
        subprocess.run(f"/opt/homebrew/bin/yabai -m window --resize left:-{amount}:0".split(' '), check=True)

    def expand_right(self, app, amount):
        print(f"Resizing left: {app} - {amount}")
        self.focus_app(app)
        subprocess.run(f"/opt/homebrew/bin/yabai -m window --resize right:{amount}:0".split(' '), check=True)

    def expand_top(self, app, amount):
        print(f"Resizing left: {app} - {amount}")
        self.focus_app(app)
        subprocess.run(f"/opt/homebrew/bin/yabai -m window --resize top:0:-{amount}".split(' '), check=True)

    def focus_app(self, app):
        self.ensure_app_is_open(app)
        print(f"Focusing: {app}")
        for window in self.windows():
            if window['app'] == app:
                subprocess.run(f"/opt/homebrew/bin/yabai -m window --focus {window['id']}".split(' '), check=True)
                for i in range(1,20):
                    print(f"Checking focus on: {app}")
                    for check_window in self.windows():
                        if check_window['has-focus'] == True and check_window['app'] == app:
                            print(f"Confirmed {app} is in focus")
                            return True
                    time.sleep(0.1)
        print(f"Could not focus on {app}") 
        print("Process halted")
        sys.exit()

    def insert_from_anchor(self, anchor_app, direction, new_app):
        print(f"Insert from anchor: {anchor_app} - {direction} - {new_app}")
        self.focus_app(anchor_app)
        #time.sleep(0.3)
        subprocess.run(f"/opt/homebrew/bin/yabai -m window --insert {direction}".split(' '), check=True)
        # Not sure of a good way to check that this is set, so just adding some time
        #time.sleep(0.3)
        self.move_app_to_space(new_app, self.app_space_id(anchor_app))


    def move_app_to_space(self, app, space):
        # TODO: Check if the app is already on the space and don't mess with it if it is
        print(f"Moving: {app} to: {space}")
        if self.app_space_id(app) == space:
            print(f"No need to move. {app} is already on space {space}")
        else:
            self.focus_app(app)
            subprocess.run(f"/opt/homebrew/bin/yabai -m window --space {space}".split(' '), check=True)
            print(f"Confirming move.")
            for i in range(1, 35):
                if self.app_space_id(app) == space:
                    print(f"Moved: {app} to: {space}")
                    return True
                time.sleep(0.1)
                print('.', end='')
            print("Move didn't work. Trying again")
            self.focus_app(app)
            subprocess.run(f"/opt/homebrew/bin/yabai -m window --space {space}".split(' '), check=True)
            print(f"Confirming move.")
            for i in range(1, 40):
                if self.app_space_id(app) == space:
                    print(f"Moved: {app} to: {space}")
                    return True
                time.sleep(0.1)
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
            subprocess.run(f"/opt/homebrew/bin/yabai -m window --insert stack".split(' '), check=True)
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
        results = subprocess.run(['/opt/homebrew/bin/yabai', '-m', 'query', '--spaces'], capture_output=True, check=True)
        return json.loads(results.stdout.decode('utf-8'))

    def stage_apps(self):
        staging_space = len(self.spaces())
        for window in self.windows():
            self.move_app_to_space(window['app'], staging_space)

    def windows(self):
        results = subprocess.run('/opt/homebrew/bin/yabai -m query --windows'.split(' '), capture_output=True)
        return json.loads(results.stdout.decode('utf-8'))


if __name__ == "__main__":
    am = AppMover()
    am.stage_apps()

    am.move_app_to_space('Adobe Photoshop 2022', 2)
    am.move_app_to_space('Safari', 5)
    am.move_app_to_space('Discord', 6)
    am.move_app_to_space('Music', 7)

    am.move_app_to_space('iTerm2', 1)
    am.insert_from_anchor('iTerm2', 'west', 'Google Chrome')
    am.expand_left('iTerm2', 500)
    am.insert_from_anchor('iTerm2', 'north', 'GitHub Desktop')
    am.expand_top('iTerm2', 400)
    am.insert_from_anchor('iTerm2', 'south', 'CodeRunner')
    am.expand_bottom('iTerm2', 130)
    am.insert_from_anchor('CodeRunner', 'east', 'Sublime Text')
    am.insert_from_anchor('Google Chrome', 'south', 'nvALT')
    am.insert_from_anchor('iTerm2', 'east', 'Terminal')
    am.expand_right('iTerm2', 300)

    am.focus_app('iTerm2')


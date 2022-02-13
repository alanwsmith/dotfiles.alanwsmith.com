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

    def windows(self):
        results = subprocess.run('/opt/homebrew/bin/yabai -m query --windows'.split(' '), capture_output=True)
        return json.loads(results.stdout.decode('utf-8'))

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
        # TODO: Check if the app is already on the space
        print(f"Moving: {app} to: {space}")
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


    # def place_app_under_app(self, lower_app, upper_app):
    #     self.focus_app(upper_app)
    #     # # # # # # # # subprocess.run(f"/opt/homebrew/bin/yabai -m window --insert stack".split(' '), check=True)
    #     time.sleep(0.1)
    #     self.focus_app(lower_app)

    def window_id_for_app(self, app):
        for window in self.windows():
            if window['app'] == app:
                print(f"App {app} has ID: {window['id']}")
                return window['id']
        return None

    def expand_left(self, app, amount):
        print(f"Resizing left: {app} - {amount}")
        self.focus_app(app)
        subprocess.run(f"/opt/homebrew/bin/yabai -m window --resize left:-{amount}:0".split(' '), check=True)

    def spaces(self):
        results = subprocess.run(['/opt/homebrew/bin/yabai', '-m', 'query', '--spaces'], capture_output=True, check=True)
        return json.loads(results.stdout.decode('utf-8'))

    def stage_apps(self):
        staging_space = len(self.spaces())
        for window in self.windows():
            self.move_app_to_space(window['app'], staging_space)



if __name__ == "__main__":
    am = AppMover()

    # am.stage_apps()

    # am.move_app_to_space('Adobe Photoshop 2022', 3)
    # am.move_app_to_space('GitHub Desktop', 2)

    # am.move_app_to_space('iTerm2', 1)
    # am.insert_from_anchor('iTerm2', 'west', 'Google Chrome')
    am.expand_left('iTerm2', 300)
    # am.insert_from_anchor('Google Chrome', 'south', 'nvALT')
    # am.insert_from_anchor('iTerm2', 'south', 'CodeRunner')
    # am.insert_from_anchor('CodeRunner', 'east', 'Sublime Text')


    # am.move_app_to_space('Google Chrome', 1)
    # am.move_app_to_space('CodeRunner', 1)
    #am.move_app_to_space('Terminal', 1)

    # am.move_app_to_space('GitHub Desktop', 2)
    # am.move_app_to_space('Code', 2)
    # am.move_app_to_space('Sublime Text', 2)

    # am.insert_from_anchor('CodeRunner', 'east', 'Sublime Text')
    # am.insert_from_anchor('Terminal', 'east', 'Code')

    # am.insert_from_anchor('Terminal', 'east', 'Code')
    # am.insert_from_anchor('CodeRunner', 'east', 'Sublime Text')

    # am.insert_from_anchor('CodeRunner', 'east', 'Sublime Text')
    # am.move_app_to_space('Sublime Text', 1)
    #am.move_app_to_space('Code', 1)
    # am.place_app_under_app('Music', 'Google Chrome')



# close stuff to start with:
#subprocess.run(['osascript', '-e', 'quit app "GitHub Desktop"'])


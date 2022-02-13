#!/usr/bin/env python3

import json
import subprocess
import sys
import time

class AppMover():
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

    def insert_anchor(self, app, direction):
        self.focus_app(app)
        subprocess.run(f"/opt/homebrew/bin/yabai -m window --insert {direction}".split(' '), check=True)
        # Not sure of a good way to check that this is set, so just adding some time
        time.sleep(0.1)


    def move_app_to_space(self, app, space):
        print(f"Moving: {app} to: {space}")
        self.focus_app(app)
        subprocess.run(f"/opt/homebrew/bin/yabai -m window --space {space}".split(' '), check=True)

    def window_id_for_app(self, app):
        for window in self.windows():
            if window['app'] == app:
                print(f"App {app} has ID: {window['id']}")
                return window['id']
        return None



if __name__ == "__main__":
    am = AppMover()
    am.move_app_to_space('GitHub Desktop', 2)
    am.move_app_to_space('Code', 2)
    am.move_app_to_space('Sublime Text', 2)
    am.insert_anchor('Terminal', 'east')
    am.move_app_to_space('Sublime Text', 1)
    am.insert_anchor('CodeRunner', 'east')
    am.move_app_to_space('Code', 1)





# close stuff to start with:
#subprocess.run(['osascript', '-e', 'quit app "GitHub Desktop"'])


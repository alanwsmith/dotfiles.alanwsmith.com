#!/usr/bin/env python3

import json
import subprocess
import sys
import time

class AppMover():
    def windows(self):
        results = subprocess.run('yabai -m query --windows'.split(' '), capture_output=True)
        return json.loads(results.stdout.decode('utf-8'))

    def ensure_app_is_open(self, app):
        print(f"Ensuring {app} is open")
        if self.window_id_for_app(app) == None:
            print(f"Opening {app}")
            for i in range(1,5):
                time.sleep(.1)
                print('.', end='')
                if self.window_id_for_app(app) != None:
                    print(f"Opened {app}")
                    return True
            print(f"Could not open {app} in a reasonalbe time")
            print("Process halted.")
            sys.exit()


    def window_id_for_app(self, app):
        window_id = None
        for window in self.windows():
            if window['app'] == app:
                print(window)


    def move_app_to_space(self, app, space):
        self.ensure_app_is_open(app)
        print(f"Moving: {app} to: {space}")


if __name__ == "__main__":
    am = AppMover()
    am.move_app_to_space('GitHub Desktop', 3)




# close stuff to start with:
#subprocess.run(['osascript', '-e', 'quit app "GitHub Desktop"'])


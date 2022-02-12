#!/usr/bin/env python3

import json
import subprocess
import time

with open('/Users/alan/Desktop/testout.txt', 'w') as _file:
    _file.write("hi. this is from the yabai-scripts basic-setup.py file")

print('here')

def get_window_status():
    results = subprocess.run(['/opt/homebrew/bin/yabai', '-m', 'query', '--windows'], capture_output=True, check=True)
    return json.loads(results.stdout.decode('utf-8'))

def run_command(tokens):
    results = subprocess.run(tokens, capture_output=True, check=True)
    print(results)



windows = get_window_status()
apps = {}
for window in windows:
    print(f"{window['id']} - {window['app']}")
    apps[window['app']] = { 'id': window['id']}
    # Could set this up to only move if the window is in the first 
    # space as a possible optimization
    run_command(f"/opt/homebrew/bin/yabai -m window --focus {window['id']}".split(' '))
    run_command('/opt/homebrew/bin/yabai -m window --space 2'.split(' '))
    #time.sleep(1.0)
    # You have to focus back on the window to properly update the 
    # space layout
    run_command(f"/opt/homebrew/bin/yabai -m window --focus {window['id']}".split(' '))
    run_command('/opt/homebrew/bin/yabai -m space --layout float'.split(' '))

# Assume that the last window is still focused and on the second space at
# set it to float

#time.sleep(1.0)

print(apps)
# # Move the apps back
run_command(f"/opt/homebrew/bin/yabai -m window --focus {apps['iTerm2']['id']}".split(' '))
run_command('/opt/homebrew/bin/yabai -m window --space 1'.split(' '))
# time.sleep(1.5)
# You have to refocus the window to be able to set the space back to 
# bsp (if that becomes necessary)
run_command(f"/opt/homebrew/bin/yabai -m window --focus {apps['iTerm2']['id']}".split(' '))
run_command('/opt/homebrew/bin/yabai -m space --layout bsp'.split(' '))

run_command(f"/opt/homebrew/bin/yabai -m window --focus {apps['nvALT']['id']}".split(' '))
run_command('/opt/homebrew/bin/yabai -m window --space 1'.split(' '))

run_command(f"/opt/homebrew/bin/yabai -m window --focus {apps['Google Chrome']['id']}".split(' '))
run_command('/opt/homebrew/bin/yabai -m window --space 1'.split(' '))

# end up on iTerm2
run_command(f"/opt/homebrew/bin/yabai -m window --focus {apps['iTerm2']['id']}".split(' '))
run_command('/opt/homebrew/bin/yabai -m window --resize left:-190:0'.split(' '))

# Setup for a stack
run_command('/opt/homebrew/bin/yabai -m window --insert stack'.split(' '))

# and move github desktop in
run_command(f"/opt/homebrew/bin/yabai -m window --focus {apps['GitHub Desktop']['id']}".split(' '))
run_command('/opt/homebrew/bin/yabai -m window --space 1'.split(' '))

# Then go back to iTerm2
run_command(f"/opt/homebrew/bin/yabai -m window --focus {apps['iTerm2']['id']}".split(' '))

# print(apps)

print("made it to the end")



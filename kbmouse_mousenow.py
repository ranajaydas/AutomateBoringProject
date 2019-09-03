""" Shows the current position on the screen for the mouse
    Note: This program only works on cmd
"""

import pyautogui

print('Press Ctrl-C to quit.')
try:
    while True:
        # Get and print the mouse coordinates.
        x, y = pyautogui.position()
        position = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(position, end='')

        # Erase the last value
        print('\b' * len(position), end='', flush=True)

except KeyboardInterrupt:
    print('\nDone.')

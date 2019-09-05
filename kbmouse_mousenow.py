"""Shows the current position on the screen for the mouse.
Note: This program only works on cmd.
"""

import pyautogui

print('Press Ctrl-C to quit.')
try:
    while True:
        # Get the mouse position
        x, y = pyautogui.position()

        # Get the RGB value at this position
        pixel_colour = pyautogui.screenshot().getpixel((x, y))

        # Create a string for position and color
        position_and_color = 'X: {:4} Y: {:4} | RGB: {:4},{:4},{:4}'.format(x,
                                                                            y,
                                                                            pixel_colour[0],
                                                                            pixel_colour[1],
                                                                            pixel_colour[2])

        print(position_and_color, end='')
        print('\b'*len(position_and_color), end='', flush=True)             # Erase the last value

except KeyboardInterrupt:
    print('\nDone.')

#! python3
"""Adds a * at the beginning of each line in any text copied from the clipboard."""

import pyperclip

raw_text = pyperclip.paste()                # paste the raw text from the clipboard
lines = raw_text.split('\n')                # split the text into a list called 'lines'

lines = ['* ' + lines[i] for i in range(len(lines))]      # add a '* ' using a fookin' constructor!

new_text = '\n'.join(lines)                 # join the lines back together
pyperclip.copy(new_text)                    # copy the result into the clipboard

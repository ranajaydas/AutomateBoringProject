"""A Simple Program to Open Relevant Programs at the start of the day."""

import os
import subprocess
import webbrowser

pdf_path = '../automate-the-boring-stuff-with-python-2015-.pdf'
music_url = 'https://youtu.be/y9eFk8TuV9k'
start_at_1 = '?t=1'

# Choose between Spotify, Youtube
music_source = 'spotify'


# Open the Automate Boring Stuff pdf
proc1 = subprocess.Popen(['start', pdf_path], shell=True)
print('Opened pdf...')

# Open git
proc2 = subprocess.Popen(r'C:\Program Files\Git\git-bash.exe')
print('Opened git...')


# Open the current working directory
os.startfile(os.getcwd())
print('Opened Current Working Directory...')


# Open music
if music_source is 'youtube':
    if 'youtu' in music_url:
        music_url += start_at_1
    webbrowser.open(music_url, 1)

elif music_source is 'spotify':
    proc3 = subprocess.Popen(r'C:\Users\Ranaj\AppData\Roaming\Spotify\Spotify.exe')

# Open the Web Links
webbrowser.open('https://github.com/ranajaydas/AutomateBoringProject', 2)
print('Opened all urls...')

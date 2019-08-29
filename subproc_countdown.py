#! python3
# subproc_countdown.py - Launches a countdown timer (in seconds)

import subprocess
import time
import sys


if len(sys.argv) > 1:
    timer = int(' '.join(sys.argv[1:]))                             # Get timer value from command line.
else:
    timer = int(input('Enter countdown timer value in seconds:'))   # Get timer value from user

while timer > 0:
    print(timer)
    time.sleep(1)
    timer -= 1

subprocess.Popen(['start', 'subproc_countdown_Alarm.wav'], shell=True)

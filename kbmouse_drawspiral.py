import pyautogui
import subprocess
import time

subprocess.Popen('mspaint.exe', shell=True)
time.sleep(2)
pyautogui.moveTo(500, 500)
pyautogui.click()                                   # click to put drawing program in focus
distance = 1000

while distance > 0:
    pyautogui.dragRel(distance, 0)    # move right
    distance -= 5
    pyautogui.dragRel(0, distance)    # move down
    pyautogui.dragRel(-distance, 0)   # move left
    distance -= 5
    pyautogui.dragRel(0, -distance)   # move up
    distance -= 5                     # Add a lil bit of imperfection ;)

# TODO: Make money as an MSPaint artist!

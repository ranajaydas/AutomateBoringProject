""" Some basic functions using pyautogui """
import pyautogui

# Show the size of the screen
print(pyautogui.size())


# Move the mouse (absolute coordinates)
print('Moving mouse in absolute coordinates...')
for i in range(5):
    pyautogui.moveTo(500, 500)
    pyautogui.moveTo(1000, 500, duration=0.1)
    pyautogui.moveTo(1000, 1000, duration=0.25)
    pyautogui.moveTo(500, 1000, duration=0.5)


# Move the mouse (relative coordinates)
print('Moving mouse in relative coordinates...')
pyautogui.moveRel(500, -500, duration=2)
for i in range(5):
    pyautogui.moveRel(500, 0, duration=0.1)
    pyautogui.moveRel(0, 500, duration=0.25)
    pyautogui.moveRel(-500, 0)
    pyautogui.moveRel(0, -500)

# Get the mouse position
print('The mouse is at', pyautogui.position())

# Clicking the mouse
pyautogui.click()

# Clicking the right mouse button at a specified position
pyautogui.click(100, 100, button='Right')



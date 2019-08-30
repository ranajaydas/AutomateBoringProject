""" Simple Selenium Program to play the game 2048 """

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
weblink = 'https://play2048.co'
time_between_moves = 0.001
counter = 1

# Opening the page #
browser.get(weblink)                                                                # get command opens weblinks


# Send keystrokes to the page #
html_elem = browser.find_element_by_tag_name('html')

while True:
    html_elem.send_keys(Keys.ARROW_UP)
    time.sleep(time_between_moves)
    html_elem.send_keys(Keys.ARROW_RIGHT)
    time.sleep(time_between_moves)
    html_elem.send_keys(Keys.ARROW_DOWN)
    time.sleep(time_between_moves)
    html_elem.send_keys(Keys.ARROW_LEFT)
    time.sleep(time_between_moves)

    try:
        retry = browser.find_element_by_link_text('Try again')
    except:
        continue
    else:
        print('Game played {} times.'.format(counter))
        counter += 1
        retry.click()



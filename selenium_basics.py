"""Some basic Selenium commands.

Requires chromedriver from https://chromedriver.chromium.org/downloads."""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()                                                        # Use Chrome webdriver
weblink = 'https://github.com/ranajaydas?tab=repositories'                          # Weblink to be opened
classname = 'show-on-focus'
link2click = 'AutomateBoringProject'

# Opening a page #
browser.get(weblink)                                                                # get command opens weblinks

# Finding an element on the page #
try:
    elem = browser.find_element_by_class_name(classname)                            # Find the classname
    print('Found {} element with that class name!'.format((elem.tag_name)))
except:
    print('Was not able to find an element with that name.')

# Clicking a link on the page #
link_elem = browser.find_element_by_link_text(link2click)
link_elem.click()


# Send keystrokes to the page #
html_elem = browser.find_element_by_tag_name('html')
html_elem.send_keys(Keys.END)                                                       # Scrolls to bottom
time.sleep(2)
html_elem.send_keys(Keys.HOME)                                                      # Scrolls to top
time.sleep(2)


# Click Browser Buttons #
browser.back()
time.sleep(2)
browser.refresh()
time.sleep(2)
browser.quit()

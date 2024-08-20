import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import  ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


browser = webdriver.Edge()
browser.get("https://www.python.org/")

# instantiate action chains
action = ActionChains(browser)

# instance of WebDriverWait created
wait = WebDriverWait(browser,100)

donate_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME,'donate-button')))



action.click_and_hold(on_element=donate_button)
action.perform()
time.sleep(15)


# move by offset
# move cursor to a particular coordinate in the webpage


# action.move_by_offset(100,100)


#using move to element and move to offset together
btn= browser.find_element_by_link_text('About')
action.move_to_element_with_offset(btn,250,0).click().perform()









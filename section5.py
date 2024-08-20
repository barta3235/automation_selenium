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

# action.move_to_element(donate_button).click().send_keys().perform()
action.move_to_element(donate_button).click().perform()


# another way
# action.click(on_element=donate_button)
# action.perform()

time.sleep(1000)


# browser.close()  // closes the current tab
# browser.quit()    // closes the webDriver instance


# action.click_and_hold(on_element=donate_button) // clicks and holds element
# time.sleep(10)  // holds the button for 10 seconds
# action.release(donate_button)




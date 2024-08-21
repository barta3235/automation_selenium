import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import  ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Edge()
driver.get('https://www.python.org/')

action = ActionChains(driver)

search= driver.find_element(By.ID,'id-search-field')

action.key_down('p',search).key_down('y')  # key down cannot take multiple variable

action.click(search).send_keys('I love Python')



# Special keys

# action.key_down(Keys.SHIFT, search).send_keys('iamnotgood')

# action.key_down(Keys.SHIFT, search).send_keys('iamnotgood').key_up(Keys.SHIFT).send_keys('Mannn')
action.key_down(Keys.SHIFT, search).send_keys('iamnotbad').key_down(Keys.SPACE).send_keys('Mannn')



# reset keys
action.reset_actions()


action.perform()
time.sleep(200)

driver.quit()
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser= webdriver.Edge()
browser.get("https://www.python.org/")

elt=browser.find_elements(By.ID,'mainnav')
#  this will return list of all elements that matches the class name
print(elt)

elts=browser.find_element(By.CLASS_NAME,'donate-button')
print(elts)


# XPATH
elts= browser.find_element(By.XPATH,'//*[@id="touchnav-wrapper"]/header/div/div[1]/a')
# every element has a individual xpath


# By link text
# Link text only works with anchor tags
elts= browser.find_element(By.LINK_TEXT,'Donate')
print(elts)


# By tag name
elts= browser.find_elements(By.TAG_NAME,'div')
# lists all the tags of div



# by name attribute
elts= browser.find_elements(By.NAME,'q')






time.sleep(5000)

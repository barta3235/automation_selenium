import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (NoSuchElementException,TimeoutException,ElementNotInteractableException,StaleElementReferenceException,InvalidSelectorException,NoSuchAttributeException,ElementClickInterceptedException,NoSuchFrameException,WebDriverException,NoSuchWindowException)

# FOR SELECT TAG
from selenium.webdriver.support.ui import Select


try:
    browse = webdriver.Edge()
    browse.get('https://authtest.mynagad.com:10900/authentication-service-provider-1.0/login')


    # loggin into the portal

    wait = WebDriverWait(browse,10)
    user_cred = wait.until(EC.presence_of_element_located((By.ID,'username')))
    user_cred.clear()
    user_cred.send_keys('uatdemo01@gmail.com')

    user_cred = wait.until(EC.presence_of_element_located((By.ID, 'password')))
    user_cred.clear()
    user_cred.send_keys('N@gad1234')

    loginButton_field = wait.until(EC.element_to_be_clickable((By.ID, 'login_button')))
    loginButton_field.click()

    # Getting into merchant registration

    element= wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'navbar-header')))
    element.click()
    element=wait.until(EC.element_to_be_clickable((By.XPATH,"//span[@class='menu-title' and text()='Merchant Management']")))
    element.click()
    element = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='menu-title' and text()='Merchant Registration']")))
    element.click()


    # accessing select tags and printing the text of all option tags
    select = Select(wait.until(EC.presence_of_element_located((By.NAME, 'mno'))))
    options=select.options
    for option in options:
        print(option.text)


    # accessing an option tag from select tag
    select = Select(wait.until(EC.presence_of_element_located((By.NAME, 'mno'))))
    select.select_by_visible_text('Robi')






    time.sleep(5000)

except (NoSuchElementException,TimeoutException,ElementNotInteractableException,StaleElementReferenceException,InvalidSelectorException,NoSuchAttributeException,ElementClickInterceptedException,NoSuchFrameException,WebDriverException,NoSuchWindowException, Exception) as e:
    print(e)


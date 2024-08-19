import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


try:

    browser = webdriver.Edge()
    browser.get("https://authtest.mynagad.com:10900/authentication-service-provider-1.0/login")

    wait = WebDriverWait(browser,100)
    username_field = wait.until(EC.presence_of_element_located((By.ID, 'username')))
    username_field.clear()
    username_field.send_keys('uatdemo01@gmail.com')

    password_field = wait.until(EC.presence_of_element_located((By.ID,'password')))
    password_field.clear()
    password_field.send_keys('N@gad1234')

    loginButton_field = wait.until(EC.element_to_be_clickable((By.ID,'login_button'))).click()

    element_temp = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='navbar-header']")))
    element_temp.click()

    element_temp = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='menu-title' and text()='Distributor Management']")))
    element_temp.click()

    element_temp = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[@class='menu-title' and text()='Add New Distributor']")))
    element_temp.click()

    time.sleep(5000)






except Exception as e:
    print(f'Error:{e}')


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import ElementClickInterceptedException

ACC_NAME='michaelscottdaily'
USERNAME=''
PASSWORD=''

class InstagramBot:
    def __init__(self):
        self.driver = webdriver.Edge()

    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login')
        time.sleep(5)  # 5 seconds to compensate the loading time

        username = self.driver.find_element(By.NAME,'username')
        password = self.driver.find_element(By.NAME, 'password')

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)
        time.sleep(10)
        self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/div/div[1]').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,'/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()


    def find_users(self):
        time.sleep(5)
        self.driver.get(f'https://www.instagram.com/{ACC_NAME}')
        time.sleep(5)

        self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[2]/div/div/div[2]/div/div[1]/button').click()
        time.sleep(2)

        self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[2]/div').click()

    def follow(self,number):
        time.sleep(5)
        follow_buttons=[]

        for i in range(1, number+1):
            btn = self.driver.find_element(By.XPATH,f'/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div[4]/div[{i}]/div/div/div/div/div/div/div[3]/div/button')
            follow_buttons.append(btn)

        for button in follow_buttons:
            try:
                button.click()
                time.sleep(1)
            except Exception as e:
                print(f'Click has been intercepted by a modal {e}')

    def close(self):
        time.sleep(5)
        self.driver.quit()






bot= InstagramBot()
bot.login()
bot.find_users()
bot.follow(10)
time.sleep(10)
bot.close()


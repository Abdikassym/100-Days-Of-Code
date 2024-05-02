import time

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from os import environ


class InstagramFollowBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

        self.EMAIL = environ["EMAIL"]
        self.PASSWORD = environ["PASSWORD"]

    def log_in(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(1.5)
        email_field = self.driver.find_element(By.XPATH, value='''//*[@id="loginForm"]/div/div[1]/div/label/input''')
        email_field.send_keys(self.EMAIL)
        password_field = self.driver.find_element(By.XPATH, value='''//*[@id="loginForm"]/div/div[2]/div/label/input''')
        password_field.send_keys(self.PASSWORD, Keys.ENTER)
        time.sleep(5)

    def find_followers(self):
        self.driver.get("https://www.instagram.com/python.hub")
        time.sleep(3)
        followers = self.driver.find_element(By.XPATH, value='''/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a''')
        followers.click()
        time.sleep(4)

    def follow(self):
        followers_pop_up = self.driver.find_element(By.XPATH,
                                                    value='''/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]''')

        # for i in range(5):
        for i in range(1, 50):
            try:
                follow_buttons = self.driver.find_element(By.XPATH, value=f'/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[{i}]/div/div/div/div[3]/div/button')
                follow_buttons.click()
            except selenium.common.exceptions.ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.CLASS_NAME, value='''_a9_1''')
                cancel_button.click()
            except selenium.common.exceptions.NoSuchElementException:
                self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_pop_up)
            finally:
                time.sleep(1.5)


bot = InstagramFollowBot()
bot.log_in()
bot.find_followers()
bot.follow()

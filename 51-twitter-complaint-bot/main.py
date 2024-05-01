import time

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from os import environ


class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

        self.EMAIL = environ["EMAIL"]
        self.PASSWORD = environ["PASSWORD"]
        self.PROMISED_UP = 10
        self.PROMISED_DOWN = 150
        self.TWITTER_USERNAME = "abdikasymt"

    def get_internet_speed(self):
        self.driver.get(url="https://www.speedtest.net/")
        start_button = self.driver.find_element(By.XPATH, value='''//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]''')
        start_button.click()
        time.sleep(50)

        download_speed = float(self.driver.find_element(By.XPATH, value='''//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span''').text)
        upload_speed = float(self.driver.find_element(By.XPATH, value='''//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span''').text)
        return [download_speed, upload_speed]

    def tweet_a_provider(self, internet_speed):
        self.driver.get(url="https://twitter.com/")
        log_in_button = self.driver.find_element(By.XPATH,
                                                 value='''//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a/div''')
        log_in_button.click()
        time.sleep(2)

        email_field = self.driver.find_element(By.XPATH,
                                               value='''//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input''')
        email_field.send_keys(self.EMAIL, Keys.ENTER)
        time.sleep(2)

        try:
            password_field = self.driver.find_element(By.XPATH,
                                                      value='''//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input''')
            password_field.send_keys(self.PASSWORD, Keys.ENTER)
        except selenium.common.exceptions.NoSuchElementException:
            username_field = self.driver.find_element(By.XPATH,
                                                      value='''//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input''')
            username_field.send_keys(self.TWITTER_USERNAME, Keys.ENTER)
            time.sleep(1)
            password_field = self.driver.find_element(By.XPATH,
                                                      value='''//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input''')
            password_field.send_keys(self.PASSWORD, Keys.ENTER)
        else:
            pass
        finally:
            time.sleep(7)
        tweet_field = self.driver.find_element(By.XPATH, value='''//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div''')
        tweet_field.send_keys(f"Hi! My internet speed is {internet_speed[0]} download and {internet_speed[1]} upload.")
        time.sleep(1)
        try:
            tweet_button = self.driver.find_element(By.XPATH, value='''//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]''')
            tweet_button.click()
        except selenium.common.exceptions.ElementClickInterceptedException:
            pop_up = self.driver.find_element(By.XPATH, value='''//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[1]/div/div/svg''')
            pop_up.click()
        else:
            pass

        print("Tweet has been posted.")


bot = InternetSpeedTwitterBot()
bot.tweet_a_provider(bot.get_internet_speed())

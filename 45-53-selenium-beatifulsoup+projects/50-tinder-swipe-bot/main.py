import time
from os import environ

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://tinder.com/")
driver.maximize_window()
time.sleep(2)

PHONE_NUMBER = environ["PHONE_NUMBER"]
PASSWORD = environ["PASSWORD"]

log_in_button = driver.find_element(By.XPATH, value="""//*[@id="u-684883901"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]/div""")
log_in_button.click()
time.sleep(3)

fb_button = driver.find_element(By.XPATH, value="""//*[@id="u1881702319"]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div/div/div""")
fb_button.click()
time.sleep(3)

# There are 2 windows created, because of FB pop-up. We choose the second window
tinder_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]

# Here we switch our selenium to FB window
driver.switch_to.window(fb_login_window)

email_field = driver.find_element(By.ID, value="email")
email_field.send_keys(PHONE_NUMBER)
pass_field = driver.find_element(By.ID, value="pass")
pass_field.send_keys(PASSWORD, Keys.ENTER)
time.sleep(10)

driver.switch_to.window(tinder_window)
allow_location_button = driver.find_element(By.XPATH, value="""//*[@id="u1881702319"]/div/div[1]/div/div/div[3]/button[1]/div[2]/div[2]""")
allow_location_button.click()
time.sleep(1)
allow_notifications_button = driver.find_element(By.XPATH, value="""//*[@id="u1881702319"]/div/div[1]/div/div/div[3]/button[2]/div[2]/div[2]/div""")
allow_notifications_button.click()
time.sleep(4)

close_button = driver.find_element(By.XPATH, value="""//*[@id="u1881702319"]/div/div[1]/div/div[3]/button[2]/div[2]/div[2]/div""")
close_button.click()
time.sleep(3)

cookies_button = driver.find_element(By.XPATH, value="""//*[@id="u-684883901"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]/div""")
cookies_button.click()


x_button = driver.find_element(By.XPATH, value="""//*[@id="u-684883901"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[2]/button""")


count = 10
while count > 0:
    try:
        x_button.click()
        time.sleep(2)
    except selenium.common.exceptions.ElementClickInterceptedException:
        promotion_pop_up = driver.find_element(By.XPATH,
                                               value="""//*[@id="u1881702319"]/div/div[1]/div[2]/button[2]/div[2]/div[2]/div""")
        promotion_pop_up.click()
    else:
        pass


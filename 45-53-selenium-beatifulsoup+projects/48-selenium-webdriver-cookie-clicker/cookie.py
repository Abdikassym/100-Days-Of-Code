import datetime
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://orteil.dashnet.org/experiments/cookie/")

# Click the cookie
cookie = driver.find_element(By.ID, value="cookie")

# Check the menu
items = driver.find_elements(By.CSS_SELECTOR, value="#store b")
del items[-1]

# Item ids
item_ids = [f"buy{item.text.split(' - ')[0].replace(',', '')}" for item in items][::-1]


def buy_item():
    global items
    items = driver.find_elements(By.CSS_SELECTOR, value="#store b")
    del items[-1]
    item_prices = [int(item.text.split(' - ')[1].replace(",", "")) for item in items][::-1]
    for item_price in item_prices:
        money = int(driver.find_element(By.ID, value="money").text.replace(',', ''))
        if money > item_price:
            item_to_buy_id = item_ids[item_prices.index(item_price)]
            item_to_buy = driver.find_element(By.ID, value=item_to_buy_id)
            item_to_buy.click()
            break


# The whole process
timeout = time.time() + 60 * 5
refresh_time = time.time() + 15
while time.time() < timeout:
    cookie.click()
    if time.time() > refresh_time:
        buy_item()
        refresh_time = time.time() + 15


cps = driver.find_element(By.ID, value="cps").text
print(cps)

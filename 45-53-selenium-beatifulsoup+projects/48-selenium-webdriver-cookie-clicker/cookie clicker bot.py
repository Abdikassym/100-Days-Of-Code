import datetime
import time
import threading

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://orteil.dashnet.org/experiments/cookie/")

# Bot active time
start_time = time.time()

cookie = driver.find_element(By.ID, value="cookie")


def buy_item():
    store = driver.find_elements(By.CSS_SELECTOR, value="#store b")[:-1]
    for item in store[::-1]:
        money = int(driver.find_element(By.ID, value="money").text.replace(",", ""))  # current amount of cookies in int
        price = int(item.text.split(' - ')[1].replace(",", ""))
        if money > price:
            print("I would buy ")


while start_time <= time.time() + 300:
    start_time_minutes = datetime.datetime.now().minute
    cookie.click()
    buy_item()



cps = float(driver.find_element(By.ID, value="cps").text.split(" ")[2])  # cookies per second in float
print(cps)
driver.quit()


















# Store

#
# while start_time != end_time:
#     print("start of a new cycle")
#     time.sleep(5)
#     store = driver.find_elements(By.CSS_SELECTOR, value="#store b")
#
#     for item in store[::-1]:
#         time.sleep(1)
#         print(f"start with {item.text}")
#         try:
#             price = int(item.text.split(" - ")[1].replace(",", ""))
#             print(f"{item.text.split(' - ')[0]} - has a price of {price}. I have {money}")
#             if price <= money:
#                 item.click()
#                 print(f"{item.text.split(' - ')[0]} has been purchased.")
#                 break
#             else:
#                 print(f"{item.text.split(' - ')[0]} is too expensive.")
#         except IndexError:
#             pass
#         time.sleep(1)
#
#
#     start_time = datetime.datetime.now().minute  # working timer


# driver.quit()

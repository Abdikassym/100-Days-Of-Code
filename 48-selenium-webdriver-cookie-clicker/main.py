from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get(url="https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")
driver.get(url="https://www.python.org/")

# captcha = driver.find_element(By.LINK_TEXT, "Try different image")
# captcha.click()

# price_dollars = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"{price_dollars.text}.{price_cents.text}")
#
# search_bar = driver.find_element(By.NAME, value="q")  # find value by NAME
# print(search_bar.tag_name)
# print(search_bar.get_attribute("role"))  # can get any attribute of a html element, either, class, id, role
#
# go_button = driver.find_element(By.ID, value="submit")  # find value by ID
# print(go_button.size)  # can get other css properties
#
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")  # find a element by is sequence
# print(documentation_link.text)
#
# bug_link = driver.find_element(By.XPATH,
#                                value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')  # find element by its path on website, works everytime
# print(bug_link.text, bug_link.get_attribute("href"))

dates = [date.text for date in driver.find_elements(By.CSS_SELECTOR, value=".event-widget ul li time")]
events = [event.text for event in driver.find_elements(By.CSS_SELECTOR, value=".event-widget ul li a")]

result = {i: {"time": dates[i], "name": events[i]} for i in range(len(dates))}
print(result)

# for i in range(len(dates)):  # Made this before dict comprehension above ^
#     result[i] = {
#         "time": dates[i],
#         "name": events[i]
#     }


# driver.close()  # closes current tab
driver.quit()  # closes the whole window




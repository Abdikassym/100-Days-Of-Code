from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("Abdesha")

last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("Tolybaev")

email = driver.find_element(By.NAME, value="email")
email.send_keys("abdikas@gmail.com")

button = driver.find_element(By.CLASS_NAME, value="btn")
button.click()





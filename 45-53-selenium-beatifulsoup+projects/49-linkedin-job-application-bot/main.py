import time
from os import environ
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://www.linkedin.com/jobs/search/?currentJobId=3911843950&distance=25&f_AL=true&geoId=102257491&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R")
driver.maximize_window()
time.sleep(3)


# Log in into LinkedIn
login = environ["EMAIL"]
password = environ["PASSWORD"]

log_in_button = driver.find_element(By.XPATH, value="/html/body/div[1]/header/nav/div/a[2]")
log_in_button.click()
time.sleep(2)

username_field = driver.find_element(By.ID, value="username")
password_field = driver.find_element(By.ID, value="password")
sign_in_button = driver.find_element(By.XPATH, value="""//*[@id="organic-div"]/form/div[3]/button""")

username_field.send_keys(login)
password_field.send_keys(password)
sign_in_button.click()
time.sleep(2)

# Saving job application
list_of_jobs = driver.find_elements(By.CLASS_NAME, value="jobs-search-results__list-item")

jobs_saved = 0
for job in list_of_jobs:
    job.click()
    job.click()
    time.sleep(2)
    job_save_button = driver.find_element(By.CLASS_NAME, value="jobs-save-button")
    job_save_button.click()
    jobs_saved += 1
    print("jobs saved:", jobs_saved)

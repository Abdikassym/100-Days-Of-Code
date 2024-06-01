import time
from bs4 import BeautifulSoup
import requests
import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from os import environ


class DataCollectorBot:

    def __init__(self):
        self.ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"
        zillow_webpage = requests.get(url=self.ZILLOW_URL).text
        self.soup = BeautifulSoup(zillow_webpage, "html.parser")

    def get_all_addresses(self):
        all_addresses = [address.getText().strip() for address in self.soup.select("div div a address")]
        return all_addresses

    def get_all_prices(self):
        all_prices = [price.getText().split("+")[0].split('/')[0] for price in self.soup.select(".PropertyCardWrapper__StyledPriceLine")]
        return all_prices

    def get_all_links(self):
        links = [link.get('href') for link in self.soup.select(".StyledPropertyCardDataArea-anchor")]
        return links

    def sorted_data(self):
        data = []
        for address, price, link in zip(self.get_all_addresses(), self.get_all_prices(), self.get_all_links()):
            data_dict = {
                "address": address,
                "price": price,
                "link": link
            }
            data.append(data_dict)
        return data


class DataEntryBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.FORM_LINK = "https://docs.google.com/forms/d/e/1FAIpQLScV83IaO4uJBSW8dYReulWueAUvMF1Ynm8d4cg7WJ2Mf2_1rQ/viewform?usp=sf_link"

    def fill_form(self, entry_data: list):
        for data in entry_data:
            self.driver.get(url=self.FORM_LINK)
            time.sleep(2)
            address_field = self.driver.find_element(By.XPATH, '''//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input''')
            address_field.send_keys(data['address'])
            price_field = self.driver.find_element(By.XPATH, value='''//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input''')
            price_field.send_keys(data['price'])
            link_field = self.driver.find_element(By.XPATH, value='''//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input''')
            link_field.send_keys(data['link'])
            submit_button = self.driver.find_element(By.XPATH, value='''//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span''')
            submit_button.click()
            time.sleep(2)


data_bot = DataCollectorBot()
entry_bot = DataEntryBot()
entry_bot.fill_form(data_bot.sorted_data())


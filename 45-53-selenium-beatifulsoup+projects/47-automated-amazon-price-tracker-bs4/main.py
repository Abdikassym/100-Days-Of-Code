from bs4 import BeautifulSoup
import smtplib
import requests

URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
my_email = "abdikasymt@gmail.com"
password = "ojdt wgth vtin iatc"

headers = {
    "Accept-Language": "ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

webpage_link = requests.get(url=URL).text
soup = BeautifulSoup(webpage_link, "html.parser")

price = soup.findAll(class_="a-price-whole")[1].getText()
price_fraction = soup.findAll(class_="a-price-fraction")[1].getText()

final_price = float(f"{price}{price_fraction}")

if final_price < 100:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=f"thespasrabota@gmail.com",
                            msg=f"Subject:Low Price!\n\nPrice is lower than 100$ as you wanted! On URL -> {URL}")
        print("message sent")

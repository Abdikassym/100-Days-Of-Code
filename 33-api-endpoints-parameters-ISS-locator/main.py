import time

import requests
from datetime import datetime
import smtplib


MY_LAT = 43.243138
MY_LONG = 76.904552

my_email = "abdikasymt@gmail.com"
password = "ojdt wgth vtin iatc"

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    "tzid": "Asia/Almaty"
}


def is_night():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    if time_now.hour > sunset or time_now.hour < sunrise:
        return True


def iss_overhead():

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT + 5 > iss_latitude > MY_LAT - 5 and MY_LONG + 5 > iss_longitude > MY_LONG - 5:
        return True


while True:
    time.sleep(60)
    if iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=my_email, msg="Subject:Look up!\n\nISS IS ABOVE YOU!")
            print("Message sent!")





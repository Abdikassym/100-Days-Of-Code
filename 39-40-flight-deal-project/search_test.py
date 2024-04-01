from datetime import datetime, timedelta
import requests

KIWI_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
ID = "yR1LeaULXWAE3Hfp3k123AbKjHhRSxy8"

parameters = {
    "fly_from": "LON",
    "fly_to": "PAR",
    "date_from": datetime.today().strftime("%d/%m/%Y"),
    "date_to": (datetime.today() + timedelta(days=5)).strftime("%d/%m/%Y"),
    "limit": 1,
    "price_to": 54
            }

header = {
            "apikey": ID
        }
response = requests.get(url=KIWI_ENDPOINT, headers=header, params=parameters)
response.raise_for_status()
print(response.text)

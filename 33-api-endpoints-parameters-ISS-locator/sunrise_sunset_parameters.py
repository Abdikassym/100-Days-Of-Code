import requests
from datetime import datetime as dt


LATITUDE = 43.243106
LONGITUDE = 76.904421
URL = "https://api.sunrise-sunset.org/json"

parameters = {
    'lat': LATITUDE,
    'lng': LONGITUDE,
    'tzid': 'Asia/Almaty',
    'formatted': 0
}

response = requests.get(url=URL, params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data['results']['sunrise'].split("T")[1].split(":")[0]
sunset = data['results']['sunset'].split("T")[1].split(":")[0]

time_now = dt.now()

print(f'''Sunset: {sunset}\nSunrise: {sunrise}''')

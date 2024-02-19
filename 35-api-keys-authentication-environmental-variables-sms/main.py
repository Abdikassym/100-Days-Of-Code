import requests
from twilio.rest import Client

API_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "7b5bb331fa97f33fad151c456cbdd317"
LAT = 36.543474
LON = 31.987515

ACCOUNT_SID = "ACa33a433d0e9e15d41a5e946e8ffd2676"
ACCOUNT_TOKEN = "0f3382e490dcc08df8ef1108d49073bc"

# LAT = 36.543474 rain place
# LON = 31.987515
# LAT = 43.243122 my house
# LON = 76.904502

parameters = {
    'lat': LAT,
    'lon': LON,
    'appid': API_KEY,
    'cnt': 5
}

response = requests.get(url=API_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()

will_be_rain = False

for list_item in weather_data["list"]:
    weather_id = list_item["weather"][0]["id"]

    if weather_id < 1600:
        will_be_rain = True

if will_be_rain:
    client = Client(ACCOUNT_SID, ACCOUNT_TOKEN)
    message = client.messages \
                    .create(
                         body="Доброе утро, моя дорогая! ️❤️",
                         from_='+14124447572',
                         to='+77024528029',)

    print(message.status)
else:
    print("There is no rain.")

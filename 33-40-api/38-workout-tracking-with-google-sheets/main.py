import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime as dt
import os

APP_KEY = os.environ["APP_KEY"]
APP_ID = os.environ["APP_ID"]

username = os.environ["USERNAME"]
password = os.environ["PASSWORD"]

basic = HTTPBasicAuth(username=username, password=password)

NUTRITIONIX_ENDPOINT = os.environ["NUTRITIONIX_ENDPOINT"]
SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]

header = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

parameters = {
    "query": input("What did you do today? "),
    "weight_kg": 84,
    "height_cm": 172,
    "age": 22
}

# get values from nutritionix
response = requests.post(url=NUTRITIONIX_ENDPOINT, json=parameters, headers=header, auth=basic)
workouts = response.json()

for workout in workouts["exercises"]:

    date_today = dt.today().strftime("%d/%m/%Y")
    time_now = dt.now().strftime("%H:%M:%S")

    content = {
        "workout":
            {
                "date": date_today,
                "time": time_now,
                "exercise": workout["name"],
                "duration": workout["duration_min"],
                "calories": workout["nf_calories"],
            }
    }

    response = requests.post(url=SHEETY_ENDPOINT, json=content)
    print(response.text)

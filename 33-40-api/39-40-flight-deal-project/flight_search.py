import requests
from datetime import datetime, timedelta
from flight_data import FlightData
from data_manager import DataManager


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    KIWI_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
    ID = "yR1LeaULXWAE3Hfp3k123AbKjHhRSxy8"
    USER_ID = "pixuflightsearch"

    header = {
        "apikey": ID
    }

    def search_flight(self, cities_to_flight):

        result_cities = []

        for city in cities_to_flight.items():

            params = {
                "fly_from": "LON",
                "fly_to": city[1]["iataCode"],
                "date_from": (datetime.today() + timedelta(days=30)).strftime("%d/%m/%Y"),
                "date_to": (datetime.today() + timedelta(days=30*3)).strftime("%d/%m/%Y"),
                "price_to": int(city[1]["price"]),
                "limit": 1,
                "nights_in_dst_from": 10,
                "nights_in_dst_to": 14,
            }

            response = requests.get(url=self.KIWI_ENDPOINT, headers=self.header, params=params)
            response.raise_for_status()
            result_cities.append(response.json())

        return result_cities

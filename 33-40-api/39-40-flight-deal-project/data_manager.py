import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    """
    TODO:
    1. Get the name and price of every city from a Google Sheet page
    """

    def __init__(self):
        self.ENDPOINT = "https://api.sheety.co/63627b957e7f2d071eb225065a64ab46/flightDeals/prices"

    def get_response(self):
        response = requests.get(url=self.ENDPOINT)
        return response



class FlightData:
    # This class is responsible for structuring the flight data.

    def organized_flights(self, response):
        cities = response.json()["prices"]

        cities_to_flight = {
            city['city']: {'price': int(city['lowestPrice']), 'iataCode': city['iataCode']} for city in cities
        }  # {'Paris': {'price': 54, 'iataCode': 'PAR'}

        return cities_to_flight

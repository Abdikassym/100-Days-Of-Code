from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.

data = DataManager()
flight_data = FlightData()
flight_search = FlightSearch()
notification_manager = NotificationManager()

cities_to_fly = flight_data.organized_flights(data.get_response())
my_flights = flight_search.search_flight(cities_to_flight=cities_to_fly)
available_flights = []

for flight in my_flights:
    if not flight['data']:
        pass
    else:
        available_flights.append(flight)

message_to_send = notification_manager.list_of_flight_info(available_flights)
notification_manager.send_message(message_to_send)













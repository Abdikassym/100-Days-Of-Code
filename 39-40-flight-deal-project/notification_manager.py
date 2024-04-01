import requests
import smtplib


class NotificationManager:

    SHEETY_ENDPOINT = "https://api.sheety.co/63627b957e7f2d071eb225065a64ab46/flightDeals/users"

    def __init__(self):
        self.my_email = "abdikasymt@gmail.com"
        self.password = "ojdt wgth vtin iatc"
        self.ACCOUNT_SID = "ACa33a433d0e9e15d41a5e946e8ffd2676"
        self.ACCOUNT_TOKEN = "ff0297509aa89394510fe063cf5f5c19"


    def list_of_flight_info(self, list_of_flights):
        flight_text = ""

        for flight in list_of_flights:
            price = flight['data'][0]['price']
            city_to = flight['data'][0]['cityTo']
            date_of_department = flight['data'][0]['local_departure']
            date_of_return = flight['data'][0]['route'][1]['local_departure']
            flight_link = flight['data'][0]['deep_link']

        flight_text += f"Only {price}€ flight from LON to {city_to} on {date_of_department} - {date_of_return}."
        return flight_text

    def send_message(self, text):

        response = requests.get(url=self.SHEETY_ENDPOINT)

        list_of_emails = [user["email"] for user in response.json()['users']]
        print(list_of_emails)

        for email in list_of_emails:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=self.my_email, password=self.password)
                connection.sendmail(from_addr=self.my_email,
                                    to_addrs=f"{email}",
                                    msg=f"Subject:Cheap Flight Available!\n\n{text}".encode('utf-8'))
                print("message sent")


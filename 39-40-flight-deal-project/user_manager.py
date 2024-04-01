import requests


class UserManager:

    SHEETY_ENDPOINT = "https://api.sheety.co/63627b957e7f2d071eb225065a64ab46/flightDeals/users"

    def __init__(self):
        self.name = input("What is your name? ")
        self.last_name = input("What is your last name? ")
        self.email = input("Please enter your email: ")
        self.email_verified = input("Please verify your email: ")

        if self.check_email():
            self.fill_user_data()

    def check_email(self):
        if self.email == self.email_verified:
            print("Email is verified. Account has been created.")
            return True
        else:
            self.email = input("Email is not verified. Enter your email again: ")
            self.email_verified = input("Please verify your email: ")
            if self.check_email():
                self.fill_user_data()

    def fill_user_data(self):

        user_data = {
            "user": {
                "name": self.name,
                "lastName": self.last_name,
                "email": self.email_verified
            }
        }

        response = requests.post(url=self.SHEETY_ENDPOINT, json=user_data)
        if response.status_code == 200:
            print("Data Saved.")
        else:
            print(response.text)


user = UserManager()

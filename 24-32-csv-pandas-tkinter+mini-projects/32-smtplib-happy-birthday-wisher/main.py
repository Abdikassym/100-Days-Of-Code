##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import smtplib

import pandas
import random

my_email = "abdikasymt@gmail.com"
password = "ojdt wgth vtin iatc"

now = dt.datetime.now()


birthdays_data = pandas.read_csv("birthdays.csv")
birthdays_data_dict = birthdays_data.to_dict(orient="records")


def create_letter(person_name):
    random_number = random.randint(1, 3)
    with open(file=f"letter_templates/letter_{random_number}.txt") as letter:
        text = letter.read()
        text = text.replace("[NAME]", person_name)
        return text


for person in birthdays_data_dict:
    if person["month"] == now.month and person["day"] == now.day:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=f"{person['email']}",
                                msg=f"Subject:Happy Birthday!\n\n{create_letter(person_name=person['name'])}")
            print("message sent")


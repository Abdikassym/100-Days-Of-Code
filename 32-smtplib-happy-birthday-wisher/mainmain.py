# This Python file uses the following encoding: utf-8
# import smtplib
#
# my_email = "abdikasymt@gmail.com"
# password = "lpdj esgb xxaz bvqr"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="thespasrabota@gmail.com",
#                         msg="Subject: Title of an e-mail.\n\nAnd Here is the content of an e-mail.", )


import datetime as dt
import random
import smtplib

now = dt.datetime.now()
year = now.year
# print(year)

week_day = now.weekday()
# print(week_day)

date_of_birth = dt.datetime(year=2001, month=12, day=6, hour=10, minute=30, second=13)
# print(date_of_birth)

text = """Дорогой мой человечек, в этих строках хотелось бы рассказать тебе о своих чувствах, о моей любви к тебе — единственному и желанному. Говорят, что счастливые не пишут писем, ведь у них есть жизнь, которой они заняты и которая окружает их вниманием, общением и новыми приключениями. Ах, как же они ошибаются! В реальной жизни я никогда не смогу тебе рассказать о любви, раскрыть свое сердце и, заглядывая в твои глаза, ждать ответа."""

# ------------------ WEEKLY MOTIVATIONAL QUOTE CHALLENGE ------------------------

my_email = "abdikasymt@gmail.com"
password = "ojdt wgth vtin iatc"

if now.weekday() == 1:
    with open(file="quotes.txt") as quotes_file:
        all_quotes = quotes_file.readlines()
        random_quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="hegaii737@gmail.com",
                            msg=f"Subject:Love letter\n\n{text}".encode('utf-8'))


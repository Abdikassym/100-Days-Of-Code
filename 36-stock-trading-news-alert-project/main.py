import requests
from math import fabs
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla"

STOCK_PRICE_API_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_PRICE_API_KEY = "ZVCFI0VEDROJLY4K"

TWILIO_ACC_SID = "ACa33a433d0e9e15d41a5e946e8ffd2676"
TWILIO_AUTH_TOKEN = "f5f9d2d0fbf9a639ac70358d49bd6309"
TWILIO_PHONE_NUMBER = "+14124447572"

#
# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_api_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_PRICE_API_KEY,
}


def get_price_difference():
    response = requests.get(url=STOCK_PRICE_API_ENDPOINT, params=stock_api_parameters)
    response.raise_for_status()
    data = response.json()["Time Series (Daily)"]

    market_days_list = [day for day in data.items()][0:2]
    last_day_close_price = float(market_days_list[0][1]["4. close"])
    previous_day_close_price = float(market_days_list[1][1]["4. close"])

    return 100 - (previous_day_close_price * 100) / last_day_close_price

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 


NEWS_API_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "cdcd0e789cb04c91971761716bad06e8"


news_api_parameters = {
    "q": COMPANY_NAME,
    "from": "2024-02-18",
    "sortBy": "popularity",
    "apiKey": NEWS_API_KEY,
    "language": "en"
}


def get_news(price):
    news_response = requests.get(url=NEWS_API_ENDPOINT, params=news_api_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()
    articles = news_data["articles"][0:3]
    message = ""
    if price < 0:
        for art in articles:
            message += f"""{COMPANY_NAME}: {price}⬇️\nHeadline: {art["title"]}\nBrief: {art['description']}\n\n"""
    else:
        for art in articles:
            message += f"""{COMPANY_NAME}: {price}⬆️\nHeadline: {art["title"]}\nBrief: {art['description']}\n\n"""
    print(message)

# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


if get_price_difference() > 5:
    client = Client(TWILIO_ACC_SID, TWILIO_AUTH_TOKEN)
    message = client.messages \
        .create(
            body=get_news(get_price_difference()),
            from_=TWILIO_PHONE_NUMBER,
            to='+77024528029', )
else:
    client = Client(TWILIO_ACC_SID, TWILIO_AUTH_TOKEN)
    message = client.messages \
        .create(
            # body=f"Stock price difference is lower than 5%, its only {get_price_difference()}%",
            body=f"Ты моя сладкая булочка!",
            from_=TWILIO_PHONE_NUMBER,
            to='+77024528029', )



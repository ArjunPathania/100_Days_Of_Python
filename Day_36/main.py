import requests
import os
import datetime
from twilio.rest import Client

# Constants
STOCK = "TSLA"
ALPHAVANTAGE_API = os.environ.get("ALPHAVANTAGE_API")
COMPANY_NAME = "Tesla Inc"
NEWS_API = os.environ.get("NEWS_API")
ACCOUNT_SID = os.environ.get("ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

# Stock Exchange Params
stock_exchange_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': ALPHAVANTAGE_API
}

# Get today's date and calculate the date 7 days ago
today = datetime.datetime.today()
week_ago = today - datetime.timedelta(days=7)
day = week_ago.day
month = week_ago.month
year = week_ago.year

# Fetch stock data
stock_url = 'https://www.alphavantage.co/query'
stock_exchange_response = requests.get(stock_url, params=stock_exchange_params)

# Print the raw response content for debugging
print("Stock API Response:", stock_exchange_response.json())

if stock_exchange_response.status_code == 200:
    data = stock_exchange_response.json().get("Time Series (Daily)")
    if data:
        # Extract data for the last two days
        dates = list(data.keys())[:2]  # Get the last two dates
        yesterday_close = float(data[dates[0]]["4. close"])
        day_before_yesterday_close = float(data[dates[1]]["4. close"])

        market_down = yesterday_close < day_before_yesterday_close

        # Calculate percentage change
        percentage_change = ((yesterday_close - day_before_yesterday_close) / day_before_yesterday_close) * 100
        print(f"Percentage change: {percentage_change:.2f}%")

        # Fetch news if the percentage change is >= 5%
        if abs(percentage_change) >= 5:
            news_api_params = {
                'q': COMPANY_NAME,
                'from': f'{year}-{month}-{day}',
                'sortBy': 'relevancy',
                'apiKey': NEWS_API
            }

            news_url = 'https://newsapi.org/v2/everything'
            response = requests.get(news_url, params=news_api_params)
            if response.status_code == 200:
                news_data = response.json()
                # Extract the top 3 articles
                articles = [(article["title"], article["description"]) for article in news_data.get("articles", [])[:3]]

                if articles:
                    # Send the message with the appropriate emoji based on market change
                    emoji = "🔻" if market_down else "🔺"
                    for title, description in articles:
                        message_body = f"TSLA: {emoji} {abs(percentage_change):.2f}%\nHeadline: {title}\nBrief: {description}"
                        client = Client(ACCOUNT_SID, AUTH_TOKEN)
                        message = client.messages.create(
                            body=message_body,
                            from_="+13868663347",  # Replace with your Twilio number
                            to="+91 62830 67068"  # Replace with your recipient number
                        )
                        print(message.status)
            else:
                print(f"Failed to fetch news. Status code: {response.status_code}")
        else:
            print("No significant stock change to report.")
    else:
        print("Error: No time series data found.")
else:
    print(f"Failed to fetch stock data. Status code: {stock_exchange_response.status_code}")

# import requests
# from twilio.rest import Client
#
# VIRTUAL_TWILIO_NUMBER = "your virtual twilio number"
# VERIFIED_NUMBER = "your own phone number verified with Twilio"
#
# STOCK_NAME = "TSLA"
# COMPANY_NAME = "Tesla Inc"
#
# STOCK_ENDPOINT = "https://www.alphavantage.co/query"
# NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
#
# STOCK_API_KEY = "YOUR OWN API KEY FROM ALPHAVANTAGE"
# NEWS_API_KEY = "YOUR OWN API KEY FROM NEWSAPI"
# TWILIO_SID = "YOUR TWILIO ACCOUNT SID"
# TWILIO_AUTH_TOKEN = "YOUR TWILIO AUTH TOKEN"
#
# ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# # When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#
# #Get yesterday's closing stock price
# stock_params = {
#     "function": "TIME_SERIES_DAILY",
#     "symbol": STOCK_NAME,
#     "apikey": STOCK_API_KEY,
# }
#
# response = requests.get(STOCK_ENDPOINT, params=stock_params)
# data = response.json()["Time Series (Daily)"]
# data_list = [value for (key, value) in data.items()]
# yesterday_data = data_list[0]
# yesterday_closing_price = yesterday_data["4. close"]
# print(yesterday_closing_price)
#
# #Get the day before yesterday's closing stock price
# day_before_yesterday_data = data_list[1]
# day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
# print(day_before_yesterday_closing_price)
#
# #Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
# difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
# up_down = None
# if difference > 0:
#     up_down = "🔺"
# else:
#     up_down = "🔻"
#
# #Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
# diff_percent = round((difference / float(yesterday_closing_price)) * 100)
# print(diff_percent)
#
#
### STEP 2: Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
# #Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
# #If difference percentage is greater than 5 then print("Get News").
# if abs(diff_percent) > 5:
#     news_params = {
#         "apiKey": NEWS_API_KEY,
#         "qInTitle": COMPANY_NAME,
#     }
#
#     news_response = requests.get(NEWS_ENDPOINT, params=news_params)
#     articles = news_response.json()["articles"]
#
#     #Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
#     three_articles = articles[:3]
#     print(three_articles)
#
#     ## STEP 3: Use Twilio to send a seperate message with each article's title and description to your phone number.
#
#     #Create a new list of the first 3 article's headline and description using list comprehension.
#     formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
#     print(formatted_articles)
#     #Send each article as a separate message via Twilio.
#     client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
#
#     #8. - Send each article as a separate message via Twilio.
#     for article in formatted_articles:
#         message = client.messages.create(
#             body=article,
#             from_=VIRTUAL_TWILIO_NUMBER,
#             to=VERIFIED_NUMBER
#         )
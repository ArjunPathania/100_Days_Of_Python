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

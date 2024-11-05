import smtplib
import json
import datetime as dt
from random import choice

# Read data from JSON File
with open("secrets.json", "r") as json_file:
    data = json.load(json_file)

my_email = data["accounts"][0]["email"]
password = data["accounts"][0]["password"]

recipient_email = data["accounts"][1]["email"]


# read data fromfile
with open("quotes.txt",mode= 'r') as quotes_file:
    quotes = quotes_file.readlines()
quote_list  = [quote for quote in quotes]

tuesday_quote = choice(quote_list)

# Correct SMTP setup for Gmail
now = dt.datetime.now()

if now.weekday() == 1:
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()  # Secure the connection
            connection.login(my_email, password)
            # Now you can send an email
            connection.sendmail(
                from_addr=my_email,
                to_addrs=recipient_email,
                msg=f"Subject:Quote of the day\n\n{tuesday_quote}"
            )
            print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
#

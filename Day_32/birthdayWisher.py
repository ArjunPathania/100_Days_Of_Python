import smtplib
import datetime as dt
import random as rd

import pandas as pd
import json


# Correct SMTP setup for Gmail
now = dt.datetime.now()
month = now.month
day = now.day

with open("secrets.json", "r") as json_file:
    data = json.load(json_file)

my_email = data["accounts"][0]["email"]
password = data["accounts"][0]["password"]

# read data from csv
with open("birthdays.csv",mode ='r') as birthday_csv:
    birthday_data = pd.read_csv(birthday_csv)
    birthday_list = [value for value in birthday_data.values]

today_birthday = [
    [entry[0], entry[1]]
    for entry in birthday_list
    if entry[3] == month and entry[4] == day
]

with open(f"letter_templates/letter_{rd.randint(1,3)}.txt",mode="r") as mail_body:
    letter_body = mail_body.readlines()

letter_content ="".join(letter_body)
letter_content = letter_content.replace("[NAME]",today_birthday[0][0])


for i in range(len(today_birthday)):
    letter_content.replace("[NAME]",today_birthday[i][0])
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()  # Secure the connection
            connection.login(my_email, password)
            # Now you can send an email
            connection.sendmail(
                from_addr=my_email,
                to_addrs=today_birthday[i][1],
                msg=f"Subject:Happy Birthday\n\n{letter_content}"
            )
            print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
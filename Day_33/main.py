import requests
from datetime import datetime
import smtplib
import json

MY_LAT = 32.2050278 # Your latitude
MY_LONG = 75.70711111111112 # Your longitude

def position_check():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    position_data = response.json()

    iss_latitude = float(position_data["iss_position"]["latitude"])
    iss_longitude = float(position_data["iss_position"]["longitude"])
    if (MY_LAT-5<=iss_latitude<MY_LAT+5) and (MY_LONG-5<= iss_longitude<=MY_LONG+5):
        return True

def night_time_check():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    sun_data = response.json()
    sunrise = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    hour = time_now.hour

    if hour >= sunset or hour <=sunrise:
        return True

# Read data from JSON File
with open("../Day_32/secrets.json", "r") as json_file:
    data = json.load(json_file)

my_email = data["accounts"][0]["email"]
password = data["accounts"][0]["password"]


if position_check() and night_time_check():
    try:
        with smtplib.SMTP("smtp.gmail.com",587) as connection:
            connection.starttls()
            connection.login(user=my_email,password=password)
            connection.sendmail(from_addr=my_email,to_addrs=my_email,msg =f"Subject:Look Up\n\nTry to find the ISS in the night sky")
            print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")


# import requests
# import datetime as dt
# # response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # response.raise_for_status()
# #
# # data = response.json()
# # longitude = data["iss_position"]["longitude"]
# # latitude = data["iss_position"]["latitude"]
# # iss_position = (longitude,latitude)
# # print(iss_position)
#
# parameters = {
#     "lat":32.2050278,
#     "lng" :75.70711111111112,
#     "formatted":0
# }
#
#
#
# response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
# response.raise_for_status()
# data = response.json()
# sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
# sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
# print(sunrise,sunset)
#
# now =dt.datetime.now()
# print(now.hour)
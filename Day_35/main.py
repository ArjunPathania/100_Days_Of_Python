import os
import requests
from twilio.rest  import Client
MY_LAT =12.468890 #32.2050278 # Your latitude
MY_LONG = 75.182938 #75.70711111111112 # Your longitude

api_key  = os.environ.get("OWM_API_KEY")
OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
weather_parameters = {
    "lat":MY_LAT,
    "lon":MY_LONG,
    "appid":api_key,
    "cnt":4
}
account_sid = "AC130eccab7266f7ffafbc53812da14959"
auth_token =   os.environ.get("TWILIO_AUTH_TOKEN")

response = requests.get(url =OWM_endpoint, params=weather_parameters)
response.raise_for_status()
data = response.json()
data_list = data["list"]
weather_id = [data_list[i]["weather"][0]["id"] for i in range(0,4)]
will_rain = False
for id_ in weather_id:
    if id_<700:
        will_rain = True

if will_rain:
    client = Client(account_sid,auth_token)
    message = client.messages \
            .create(
        body="It's going to rain today.Remember to bring an ☂️",
        from_="+13868663347",
        to="+91 62830 67068"
    )
    print(message.status)

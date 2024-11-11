import requests
import os
from datetime import datetime

# Get API credentials from environment variables
API_KEY = os.environ.get("API_KEY")
APP_ID = os.environ.get("APP_ID")
SHEETY_URL = os.environ.get("SHEETY_URL")

# Nutritionix API endpoint for exercise
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    'Content-Type': 'application/json',
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

# Get user input for exercise and define user details
exercise_query = input("What exercise did you do today? ")
user_profile = {
    "query": exercise_query,
    "gender": "male",
    "weight_kg": 75,
    "height_cm": 179,
    "age": 23
}

# Send request to Nutritionix API
response = requests.post(url=nutritionix_endpoint, json=user_profile, headers=headers)
response.raise_for_status()
exercise_data = response.json()

# Extract relevant exercise data
exercise_list = exercise_data.get("exercises", [])
workout_data = [
    (exercise["name"], exercise["duration_min"], exercise["nf_calories"])
    for exercise in exercise_list
]

# Print extracted data for debugging
print("Extracted Exercise Data:", workout_data)
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")

# Sheety API endpoint to log workouts
sheety_endpoint = f"https://api.sheety.co/{SHEETY_URL}/myWorkouts/workouts"
today = datetime.now()

# Log each exercise entry to Sheety

headers = {"Authorization": f"Bearer {AUTH_TOKEN}"}

for exercise_name, duration, calories in workout_data:
    workout_entry = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%H:%M:%S"),
            "exercise": exercise_name.title(),
            "duration": duration,
            "calories": calories
        }
    }
    print("Logging Workout Data:", workout_entry)  # For debugging

    # Send POST request to Sheety
    sheety_response = requests.post(url=sheety_endpoint, json=workout_entry,headers=headers)
    print("Sheety Response:", sheety_response.text)

# import requests
# import os
# from datetime import datetime
#
# API_KEY = os.environ.get("API_KEY")
# APP_ID = os.environ.get("APP_ID")
#
# api_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
#
# header = {
#     'Content-Type': 'application/json',
#     'x-app-id': APP_ID,
#     'x-app-key': API_KEY
# }
# #
# request_params = {
#     "query": input("What exercise did you do today? "),
#     "gender": "male",
#     "weight_kg": 75,
#     "height_cm": 179,
#     "age": 23
# }
#
# query = requests.post(url=api_endpoint, json=request_params, headers=header)
# query.raise_for_status()
# exercise_data = query.json()
# exercise_list = exercise_data.get("exercises", [])
# print(exercise_list)
# print(len(exercise_list))
# workout_data = [(exercise_list[_]["name"], exercise_list[_]["duration_min"], exercise_list[_]["nf_calories"]) for _ in
#                 range(len(exercise_list))]
# print(workout_data)
# today = datetime.now()
#
# SHEETY_URL = os.environ.get("SHEETY_URL")
# sheety_endpoint = f"https://api.sheety.co/{SHEETY_URL}/myWorkouts/workouts"
# print("Exercise List:", exercise_list)
# for item in workout_data:
#     print("Duration:", item[1])
# length = len(workout_data)
# print(length)
#
# for i in range(0,length):
#     workout_params = {
#         "workout": {
#             "date": today.strftime("%d/%m/%Y"),
#             "time": today.strftime("%H:%M:%S"),
#             "exercise": workout_data[i][0].title(),
#             "duration": int(workout_data[i][1]),
#             "calories": workout_data[i][2], }
#     }
#     print(workout_params)
#     response = requests.post(url=sheety_endpoint, json=workout_params)
#     print(response.text)

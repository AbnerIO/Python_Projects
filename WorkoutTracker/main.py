import requests
import datetime
import os

date = datetime.datetime.now().strftime("%d/%m/%Y")
time = datetime.datetime.now().strftime("%H:%M:%S")


API_KEY = os.getenv("API_KEY")
API_ID = os.getenv("API_ID")

trackapi_excercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
sheety_headers = {
    "Authorization": F"Bearer {os.getenv('AUTH_KEY')}"
}
headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY
}
query = input("Type the exersice(s) and time: ")
exercise_params = {
  "query": query,
  "gender": "male",
  "weight_kg": 72,
  "height_cm": 175,
  "age": 20
}
response = requests.post(url = trackapi_excercise_endpoint, json=exercise_params, headers=headers)
exercises = response.json()["exercises"]
for exercise in exercises:
    data = {
            "workout": {
                "date": date,
                "time": time,
                "exercise": exercise["name"].title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"]}

    }
    response = requests.post(url=SHEETY_ENDPOINT, json=data, headers = sheety_headers)
    print(response.text)





import requests
from twilio.rest import Client

account_sid = ""
auth_token = ""
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = ""
weather_params = {
    "lat": 25.740660,
    "lon": -100.301550,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

weather_main = weather_data["weather"][0]["main"]
weather_description = weather_data["weather"][0]["description"]

client = Client(account_sid, auth_token)
message = client.messages \
                .create(
                     body=f"Today´s weather says: {weather_main}. {weather_description}!!",
                     from_='+15...', #number
                     to='+52..' #number
                 )

print(message.status)


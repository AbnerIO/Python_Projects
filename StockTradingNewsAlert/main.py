# NOTA: Recomiendo automatizar la ejecucion de este codigo en pythonanywhere, por ejemplo

import os
import requests
from twilio.rest import Client

TWILO_SID = os.environ.get("TWILO_SID")
TWILO_TOKEN = os.environ.get("TWILO_TOKEN")
ALPHAVANTAGE_KEY = os.environ.get("ALPHAVANTAGE_KEY")
NEWS_KEY = os.environ.get("NEWS_KEY")
TWILO_NUMBER = os.environ.get("TWILO_NUMBER")
MY_NUMBER = os.environ.get("MY_NUMBER")

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


# visualizar el cambio (aumento o disminucion) de la accion entre ayer y hoy
response = requests.get(f"{STOCK_ENDPOINT}?function=TIME_SERIES_DAILY_ADJUSTED&symbol={STOCK}&apikey={ALPHAVANTAGE_KEY}")
response.raise_for_status()
stock_values = response.json()["Time Series (Daily)"]
primeros_dos = []
contador = 0

for valor in stock_values.values():
    if contador < 2:
        primeros_dos.append(valor)
        contador += 1
    else:
        break
today_close = float(primeros_dos[0]["4. close"])
yesterday_close = float(primeros_dos[1]["4. close"])
difference = round(today_close - yesterday_close, 3)

if difference > 0:
    difference_string = f"+ {round(difference * 100 / yesterday_close, 4)}"
else:
    difference_string = f"- {round(difference * 100 / yesterday_close, 4)}"

# visualizar las primeras 3 noticias referentes a la compañia
response = requests.get(f"{NEWS_ENDPOINT}?q={COMPANY_NAME}&apiKey={NEWS_KEY}")
response.raise_for_status()
response_json = response.json()
news = {}
for i in range(3):
    title = response_json["articles"][i]["title"]
    description = response_json["articles"][i]["description"]
    news[i] = {
        "title" : title,
        "description" : description
    }


# enviar un mensaje automatizado a nuestro telefono

client = Client(TWILO_SID, TWILO_TOKEN)
for i in range(3):
    message = client.messages \
                    .create(
                         body=f"{f'{difference_string}%' if i == 0 else ''}"
                              f"{news[i]['title']}"
                              f"{news[i]['description']}",
                         from_=f'{TWILO_NUMBER}',
                         to=f'{MY_NUMBER}'
                     )

print(message.status)




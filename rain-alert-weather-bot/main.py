import os
import requests
import smtplib
from dotenv import load_dotenv

load_dotenv()

MY_LAT = float(os.getenv("MY_LAT"))
MY_LNG = float(os.getenv("MY_LNG"))
API_KEY = os.getenv("OPENWEATHER_API_KEY")
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("EMAIL_APP_PASSWORD")

parameters = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": API_KEY,
    "cnt": 4
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()

weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:It'll probably rain\n\nBring an Umbrella \u2602\ufe0f"
        )

import requests
import pandas as pd
from datetime import datetime

API_KEY = "your_api_key_here"
CITY = "London"

def fetch_weather_data(city=CITY):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    parsed = {
        "city": city,
        "timestamp": datetime.now(),
        "temp": data['main']['temp'],
        "humidity": data['main']['humidity'],
        "wind_speed": data['wind']['speed'],
        "weather": data['weather'][0]['main']
    }
    return pd.DataFrame([parsed])
from app import app, db
from app.models import WeatherData
from datetime import datetime
import requests

class WeatherRetriever:
    def __init__(self, api_key, cities, interval):
        self.api_key = api_key
        self.cities = cities
        self.interval = interval
        self.api_url = "https://api.openweathermap.org/data/2.5/weather"
        self.forecast_url = "https://api.openweathermap.org/data/2.5/forecast"

    def get_weather_data(self, city):
        params = {'q': city, 'appid': self.api_key}
        response = requests.get(self.api_url, params=params)
        response.raise_for_status()
        return response.json()

    def get_weather_forecast(self, city):
        params = {'q': city, 'appid': self.api_key, 'units': 'metric'}
        response = requests.get(self.forecast_url, params=params)
        response.raise_for_status()
        return response.json()

    def save_forecast_data(self, data, city):
        with app.app_context():  # Ensure the context is active
            for entry in data.get('list', []):
                forecast = WeatherData(
                    city=city,
                    main=entry['weather'][0]['main'],
                    temp=entry['main']['temp'],
                    feels_like=entry['main']['feels_like'],
                    humidity=entry['main']['humidity'],
                    wind_speed=entry['wind']['speed'],
                    timestamp=datetime.utcfromtimestamp(entry['dt'])
                )
                db.session.add(forecast)
            db.session.commit()

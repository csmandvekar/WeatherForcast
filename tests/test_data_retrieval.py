import unittest
from unittest.mock import patch
from app import app, db
from app.models import WeatherData
from app.data_retrieval import WeatherRetriever
from app.config import Config

class TestWeatherDataRetrieval(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

        # Use a temporary in-memory database for testing
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['TESTING'] = True
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    @patch('app.data_retrieval.WeatherRetriever.get_weather_data')
    @patch('app.data_retrieval.WeatherRetriever.get_weather_forecast')
    def test_get_weather_data(self, mock_get_weather_forecast, mock_get_weather_data):
        # Mock the API responses
        mock_get_weather_data.return_value = {
            'weather': [{'main': 'Clear'}],
            'main': {'temp': 300.15, 'feels_like': 303.15, 'humidity': 50},
            'wind': {'speed': 1.5},
            'dt': 1618329600
        }

        mock_get_weather_forecast.return_value = {
            'list': [
                {
                    'weather': [{'main': 'Clear'}],
                    'main': {'temp': 300.15, 'feels_like': 303.15, 'humidity': 50},
                    'wind': {'speed': 1.5},
                    'dt': 1618329600
                }
            ]
        }

        with app.app_context():
            retriever = WeatherRetriever(
                api_key=Config.OPENWEATHERMAP_API_KEY,
                cities=['Delhi'],
                interval=Config.WEATHER_UPDATE_INTERVAL
            )

            # Simulate retrieving weather data and saving to the database
            data = retriever.get_weather_data('Delhi')
            retriever.save_forecast_data(mock_get_weather_forecast.return_value, 'Delhi')

            # Debugging: Print the saved data to verify
            saved_data = WeatherData.query.all()
            for data in saved_data:
                print(data)

            # Assert that weather data has been saved to the database
            self.assertTrue(WeatherData.query.count() > 0)

if __name__ == '__main__':
    unittest.main()

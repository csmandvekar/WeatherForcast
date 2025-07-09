class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///weather.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    OPENWEATHERMAP_API_KEY = open('apikey.txt', 'r').read().strip()
    WEATHER_UPDATE_INTERVAL = 300  # in seconds (5 minutes)
    ALERT_THRESHOLD_TEMP = 35  # in Celsius
    ALERT_CONSECUTIVE_COUNT = 2


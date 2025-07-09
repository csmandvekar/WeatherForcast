import pandas as pd
from app import db
from app.models import WeatherData

def forecast_summary():
    data = WeatherData.query.all()
    df = pd.DataFrame([(d.city, d.timestamp.date(), d.temp, d.humidity, d.wind_speed) for d in data], columns=['City', 'Date', 'Temperature', 'Humidity', 'Wind Speed'])

    summary = df.groupby(['City', 'Date']).agg(
        Average_Temperature=('Temperature', 'mean'),
        Maximum_Temperature=('Temperature', 'max'),
        Minimum_Temperature=('Temperature', 'min'),
        Average_Humidity=('Humidity', 'mean'),
        Average_Wind_Speed=('Wind Speed', 'mean')
    ).reset_index()

    summary['Dominant_Condition'] = 'Clear'  # Placeholder, update with actual logic

    return summary

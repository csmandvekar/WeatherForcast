import matplotlib.pyplot as plt
from app.data_processing import daily_weather_summary, forecast_summary

def plot_weather_summary():
    summary = daily_weather_summary()
    for city in summary['City'].unique():
        city_data = summary[summary['City'] == city]
        plt.figure(figsize=(12, 8))
        plt.plot(city_data['Date'], city_data['Average_Temperature'], label='Average Temperature')
        plt.plot(city_data['Date'], city_data['Maximum_Temperature'], label='Maximum Temperature')
        plt.plot(city_data['Date'], city_data['Minimum_Temperature'], label='Minimum Temperature')
        plt.plot(city_data['Date'], city_data['Average_Humidity'], label='Average Humidity', linestyle='--')
        plt.plot(city_data['Date'], city_data['Average_Wind_Speed'], label='Average Wind Speed', linestyle='-.')
        plt.title(f'{city} - Daily Weather Summary')
        plt.xlabel('Date')
        plt.ylabel('Metrics')
        plt.legend()
        plt.show()

def plot_forecast_summary():
    summary = forecast_summary()
    for city in summary['City'].unique():
        city_data = summary[summary['City'] == city]
        plt.figure(figsize=(12, 8))
        plt.plot(city_data['Date'], city_data['Average_Temperature'], label='Average Temperature')
        plt.plot(city_data['Date'], city_data['Average_Humidity'], label='Average Humidity', linestyle='--')
        plt.plot(city_data['Date'], city_data['Average_Wind_Speed'], label='Average Wind Speed', linestyle='-.')
        plt.title(f'{city} - Forecast Summary')
        plt.xlabel('Date')
        plt.ylabel('Metrics')
        plt.legend()
        plt.show()

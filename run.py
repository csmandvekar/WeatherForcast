from flask import Flask, render_template, request, jsonify
from app.data_retrieval import WeatherRetriever
from app.config import Config

app = Flask(__name__)

API_KEY = Config.OPENWEATHERMAP_API_KEY

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form.get('city')
    unit = request.form.get('unit')
    if not city or not unit:
        return jsonify({'error': 'City and unit are required'}), 400
    
    try:
        # Fetch current weather
        weather_response = WeatherRetriever(API_KEY, [city], 0).get_weather_data(city)
        forecast_response = WeatherRetriever(API_KEY, [city], 0).get_weather_forecast(city)

        temp = weather_response['main']['temp']
        weather_description = weather_response['weather'][0]['description']
        humidity = weather_response['main']['humidity']
        wind_speed = weather_response['wind']['speed']

        if unit == 'Kelvin':
            temp = temp + 273.15
            unit_symbol = 'K'
        elif unit == 'Fahrenheit':
            temp = (temp) * 9/5 + 32
            unit_symbol = '°F'
        else:
            temp = temp
            unit_symbol = '°C'

        forecast_data = forecast_response['list']
        forecast_summary = []
        for entry in forecast_data[:5]:  # Get forecast for the next 5 intervals (3-hour intervals)
            date = entry['dt_txt']
            temp = entry['main']['temp']
            if unit == 'Kelvin':
                temp = temp + 273.15
            elif unit == 'Fahrenheit':
                temp = (temp) * 9/5 + 32
            else:
                temp = temp
            description = entry['weather'][0]['description']
            forecast_summary.append({
                'date': date,
                'temperature': round(temp, 2),
                'description': description
            })

        return jsonify({
            'city': city,
            'unit': unit_symbol,
            'current': {
                'temperature': round(temp, 2),
                'description': weather_description,
                'humidity': humidity,
                'wind_speed': wind_speed
            },
            'forecast': forecast_summary
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

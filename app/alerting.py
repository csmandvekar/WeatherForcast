from app import app, db
from app.models import WeatherData

def check_alerts():
    threshold = app.config['ALERT_THRESHOLD_TEMP']
    consecutive = app.config['ALERT_CONSECUTIVE_COUNT']

    results = db.session.query(WeatherData.city, WeatherData.temp, WeatherData.timestamp).all()

    city_temp = {}
    for result in results:
        if result.city not in city_temp:
            city_temp[result.city] = []
        city_temp[result.city].append((result.temp, result.timestamp))

    for city, temps in city_temp.items():
        temps.sort(key=lambda x: x[1], reverse=True)
        count = 0
        for temp, _ in temps[:consecutive]:
            if temp > threshold:
                count += 1
            else:
                break
        if count >= consecutive:
            print(f"ALERT: {city} has exceeded {threshold}°C for {consecutive} consecutive updates!")

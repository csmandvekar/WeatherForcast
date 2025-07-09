# Real-Time-Data-Processing-System-for-Weather-Monitoring-with-Rollups-and-Aggregates

This project is a web-based weather application that retrieves and displays current weather data and forecasts for selected cities. The application is built using Flask and integrates with the OpenWeatherMap API to fetch weather data. It includes functionalities such as displaying current weather, forecast data, and alerting based on specific weather conditions.

## Real-Time-Data-Processing-System-for-Weather-Monitoring-with-Rollups-and-Aggregates
```bash
Real-Time-Data-Processing-System-for-Weather-Monitoring-with-Rollups-and-Aggregates
├── app
│   ├── __init__.py
│   ├── alerting.py
│   ├── config.py
│   ├── data_processing.py
│   ├── data_retrieval.py
│   ├── models.py
│   ├── visualizations.py
│   ├── static
│   │   └── styles.css
│   ├── templates
│   │   └── index.html
│   └── tests
│       ├── __init__.py
│       └── test_data_retrieval.py
├── apikey.txt
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── run.py
```
## Getting Started

### Prerequisites

- Python 3.8 or higher
- Docker (optional, for containerized deployment)
- OpenWeatherMap API key (save in `apikey.txt`)

### Installing Dependencies

Install the required Python packages using pip:
```bash
    pip install -r requirements.txt
```
## Configuration

Set the necessary configuration values in app/config.py or using environment variables:

- SQLALCHEMY_DATABASE_URI: Database connection string (default: SQLite)
- OPENWEATHERMAP_API_KEY: API key for OpenWeatherMap (store in apikey.txt)
- WEATHER_UPDATE_INTERVAL: Interval for weather data updates (in seconds)
- ALERT_THRESHOLD_TEMP: Temperature threshold for alerts (in Celsius)
- ALERT_CONSECUTIVE_COUNT: Number of consecutive updates for triggering alerts

## Running the Application

To run the application locally:
```bash
    python run.py
```

The application will be accessible at http://127.0.0.1:5000/.

## Running with Docker

To build and run the application using Docker, use the following commands:
```bash
    docker-compose build
    docker-compose up
```
This will start the application and PostgreSQL database in separate containers. Access the application at http://127.0.0.1:5000/.

## Testing

Unit tests are located in the tests/ directory. To run the tests:
```bash
    python -m unittest discover -s tests
```
## Usage

- Home Page: Enter the city name and select the temperature unit (Celsius, Fahrenheit, Kelvin) to get the current weather and forecast.
- Weather Data: The app fetches and displays current temperature, weather description, humidity, and wind speed.
- Forecast Data: Displays a forecast summary for the next few intervals (e.g., 3-hour intervals).

## Files and Modules
- app/__init__.py: Initializes the Flask app and database.
- app/alerting.py: Contains logic for generating alerts based on weather conditions.
- app/config.py: Configuration settings, including API keys and thresholds.
- app/data_processing.py: Processes and summarizes weather data.
- app/data_retrieval.py: Handles retrieval of weather data from the OpenWeatherMap API.
- app/models.py: Database models for storing weather data.
- app/visualizations.py: (Optional) Module for visualizing weather data.
- static/styles.css: CSS styles for the application.
- templates/index.html: HTML template for the main page.
- tests/test_data_retrieval.py: Unit tests for data retrieval and processing.

## Acknowledgements
- OpenWeatherMap for providing the weather data API.
- Flask, SQLAlchemy, and other open-source projects used in this application.
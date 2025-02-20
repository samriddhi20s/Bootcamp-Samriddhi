#Consume OpenWeatherMap API
#Objective: Fetch weather data for a specified location.
#Task: Create a Python CLI tool that uses the OpenWeatherMap API (https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}) to fetch and display weather information. You'll need to sign up for a free API key.
## Approach: Use argparse to accept a city name from the command line, make a GET request to
# OpenWeatherMap API using the provided API key, and parse the response to display weather details.
import requests
import argparse
def fetch_weather(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()
        weather_data = response.json()
        
        print("Weather Information:")
        print(f"City: {weather_data['name']}")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Weather: {weather_data['weather'][0]['description']}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch weather details for a specified city.")
    parser.add_argument("city", type=str, help="City name")
    parser.add_argument("api_key", type=str, help="OpenWeatherMap API key")
    args = parser.parse_args()
    
    fetch_weather(args.city, args.api_key)

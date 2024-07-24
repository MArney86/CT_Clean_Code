class WeatherDataFetcher:
    def __init__(self):
        self.__weather_data = {"New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}}
        
    def fetch_weather_data(self, city):
        try:
            # Simulated function to fetch weather data for a given city
            print(f"Fetching weather data for {city}...")
            # Simulated data based on city
            return self.__weather_data.get(city, {})
        except KeyError:
            print("That city is not in our data")
        except Exception:
            print(f"There was an error when fetching the weather data for {city}")
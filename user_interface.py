from data_parser import DataParser
from weather_data_fetcher import WeatherDataFetcher


class UserInterface:
    def __init__(self, city):
        self.city = city
        self.weather = WeatherDataFetcher()
        self.parser = DataParser()

    def get_detailed_forecast(self):
        # Function to provide a detailed weather forecast for a city
        data = self.weather.fetch_weather_data(self.city)
        return self.parser.parse_weather_data(data)

    def display_weather(self):
        # Function to display the basic weather forecast for a city
        data = self.weather.fetch_weather_data(self.city)
        if not data:
            print(f"Weather data not available for {self.city}")
        else:
            weather_report = self.parser.parse_weather_data(data)
            print(weather_report)

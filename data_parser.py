
class DataParser:
    def __init__(self):
        pass
    
    def parse_weather_data(self, data):
        # Function to parse weather data
        city = data["city"]
        temperature = data["temperature"]
        condition = data["condition"]
        humidity = data["humidity"]

        if not data:
            return "Weather data not available"
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"
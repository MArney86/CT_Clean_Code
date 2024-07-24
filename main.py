from user_interface import UserInterface

# Weather Forecast Application Script

def main():
    while True:
        city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
        if city.lower() == 'exit':
            break
        interface = UserInterface(city)
        detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
        if detailed == 'yes':
            forecast = interface.get_detailed_forecast()
            print(forecast)
        else:
            forecast = interface.display_weather()

if __name__ == "__main__":
    main()
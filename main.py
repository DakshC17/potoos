from weather_utils import fetch_weather

def main():
    cities = []
    
    print("Enter city names (type 'done' to finish):")
    
    while True:
        city = input("City: ")
        if city.lower() == 'done':
            break
        cities.append(city)
    
    print("\nWeather Report:")
    
    for city in cities:
        weather = fetch_weather(city)
        if weather:
            print(weather)
            print("-" * 118)

if __name__ == "__main__":
    main()

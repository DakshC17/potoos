import requests
import os
from dotenv import load_dotenv
from weather_module import Weather

load_dotenv()

def fetch_weather(city):
    api_key = os.getenv('API_KEY')
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        weather_data = Weather(
            city=data['location']['name'],
            temperature=data['current']['temp_c'],
            condition=data['current']['condition']['text'],
            humidity=data['current']['humidity'],
            wind_speed=data['current']['wind_kph'],
            last_updated=data['current']['last_updated']
        )
        
        return weather_data
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather for {city}: Network error")
        return None
    except KeyError as e:
        print(f"Error fetching weather for {city}: Invalid response format")
        return None
    except Exception as e:
        print(f"Error fetching weather for {city}: {str(e)}")
        return None

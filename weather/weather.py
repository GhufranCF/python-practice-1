from weather.constant import GEOCODING_URL, WEATHER_URL
import requests

        
class NotFoundException(Exception):
    pass

def get_city_coordinates(city_name: str):
    url = GEOCODING_URL + f'name={city_name}'
    response = requests.get(url)
    data = response.json()
    if not data.get('results', None):
        raise NotFoundException
    return data['results'][0]

def get_weather(city_name: str):

    # First we need to get the latitude and longitude of the city
    try:
        coordinates = get_city_coordinates(city_name)
    except NotFoundException:
        return f'City {city_name} not found'
    except:
        return 'Some error occurred. Please try again Later.'

    latitude = coordinates['latitude']
    longitude = coordinates['longitude']

    # Now we can get the weather data using latitude and longitude
    weather_url = WEATHER_URL + f'latitude={latitude}&longitude={longitude}&current=is_day,temperature_2m,rain,relative_humidity_2m'

    try:
        weather_response = requests.get(weather_url)
        weather_data = weather_response.json()
    except:
        return 'Some error occurred. Please try again Later.'


    if 'current' not in weather_data:
        return f"Weather data for '{city_name}' not available."
    
    current_weather = weather_data['current']
    current_units = weather_data['current_units']

    return {
        'city' : city_name,
        'temperature': f"{current_weather['temperature_2m']} {current_units['temperature_2m']}",
        'relative_humidity' : f"{current_weather['relative_humidity_2m']} {current_units['relative_humidity_2m']}",
        'is_day': f"{bool(current_weather['is_day'])}",
        'rain': f"{current_weather['rain']} {current_units['rain']}",

    }
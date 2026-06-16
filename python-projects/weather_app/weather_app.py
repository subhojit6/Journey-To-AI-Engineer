import requests
import json

def get_city():
    return input("Enter the city: ")

def get_coordinates(city):
    try:
        response = requests.get("https://geocoding-api.open-meteo.com/v1/search", params={'name': city, 'count': 1})
        geo_data = response.json()
        if "results" not in geo_data:
            print("City not found.")
            exit()

        latitude = geo_data["results"][0]['latitude']
        longitude = geo_data["results"][0]['longitude']

        return latitude, longitude
    except requests.exceptions.RequestException as e:
        print(f"Please check your internet connection: {e}")
        return None, None
        
def get_weather(latitude, longitude):

        try:
            r = requests.get('https://api.open-meteo.com/v1/forecast', params={'latitude': latitude, 'longitude': longitude, 'current': 'temperature_2m,weather_code,wind_speed_10m'})
            weather_data = r.json()
            current = weather_data["current"]
            return current
        
        except requests.exceptions.RequestException as e:
            print(f"Unable to fetch data: {e}")
            return None

def display_weather(current):

    print(f"Current weather of {city.title()}")
    print(f"Temperature is {current['temperature_2m']}°C")
    print(f"Wind speed is {current['wind_speed_10m']} km/h")
    print(f"Weather code is {current['weather_code']}")

while True:

    city = get_city()
    latitude, longitude = get_coordinates(city)
    if latitude == None or longitude == None:
        print("Failed getting the co-ordinates")
        exit()
    else:
        current = get_weather(latitude, longitude)
        if current == None:
            print("Failed to get weather data")
            exit()
        else:
            display_weather(current)

    repeat = input("Check weather again: ")
    if repeat == "yes":
        continue
    else:
        print("Thank you for using weather app.")
        break
    
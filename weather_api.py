import requests
import os
API_key = os.getenv('ApiWeather')

def print_temp(city):
    site='https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s&mode=json&units=metric&lang=ru' \
         % (city, API_key)
    response = requests.get(site)
    return response.json()['main']['temp']



import requests
from django.conf import settings

def get_weather(city):
    url = f'https://api.weather.yandex.ru/v2/forecast?city={city}'
    headers = {'X-Yandex-API-Key': settings.YANDEX_API_KEY}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        return None
    

def get_weather_data(city):
    url = f"https://api.weather.yandex.ru/v2/forecast?lat={city['latitude']}&lon={city['longitude']}&extra=true"
    headers = {'X-Yandex-API-Key': settings.YANDEX_API_KEY}

    response = requests.get(url, headers=headers)
    data = response.json()
    return data

def get_humidity(city):
    data = get_weather_data(city)
    return data['fact']['humidity']


#    {'name': 'Tashkent', 'lat': '41.3111', 'lon': '69.2401'},
#         {'name': 'Samarkand', 'lat': '39.6270', 'lon': '66.9746'},
#         {'name': 'Bukhara', 'lat': '39.7686', 'lon': '64.4556'},
#         {'name': 'Andijan', 'lat': '40.7829', 'lon': '72.3442'},  
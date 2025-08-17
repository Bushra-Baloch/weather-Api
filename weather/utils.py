import requests, os
from django.core.cache import cache



OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather_data(city):
    cache_key = f"weather_{city.lower()}"
    cached_data = cache.get(cache_key)
    if cached_data:
        return cached_data

    params = {"q": city, "appid": OPENWEATHER_API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    cache.set(cache_key, data, 600)  # cache for 10 mins
    return data

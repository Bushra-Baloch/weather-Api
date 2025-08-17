from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework.views import APIView
from django.core.cache import cache
import requests, os

from .models import FavoriteCity
from .serializers import RegisterSerializer, FavoriteCitySerializer

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"


# ------------------ Weather Utility Functions ------------------ #
def get_weather_data(city):
    cache_key = f"weather_{city.lower()}"
    cached_data = cache.get(cache_key)
    if cached_data:
        return cached_data
    params = {"q": city, "appid": OPENWEATHER_API_KEY, "units": "metric"}
    data = requests.get(BASE_URL, params=params).json()
    cache.set(cache_key, data, 600)
    return data

def get_forecast_data(city):
    params = {"q": city, "appid": OPENWEATHER_API_KEY, "units": "metric"}
    return requests.get(FORECAST_URL, params=params).json()


# ------------------ API Views ------------------ #
class WeatherView(APIView):
    def get(self, request):
        city = request.query_params.get("city")
        if not city:
            return Response({"error": "City is required"}, status=400)
        data = get_weather_data(city)
        return Response(data)


class ForecastView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        city = request.query_params.get("city")
        if not city:
            return Response({"error": "City is required"}, status=400)
        data = get_forecast_data(city)
        return Response(data)


class RegisterView(generics.CreateAPIView):
    queryset = FavoriteCity.objects.all()
    serializer_class = RegisterSerializer


class FavoriteCityListCreateView(generics.ListCreateAPIView):
    serializer_class = FavoriteCitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return FavoriteCity.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FavoriteCityDeleteView(generics.DestroyAPIView):
    serializer_class = FavoriteCitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return FavoriteCity.objects.filter(user=self.request.user)


# ------------------ Function-Based View ------------------ #
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_favorite(request):
    serializer = FavoriteCitySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

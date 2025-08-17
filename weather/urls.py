from django.urls import path
from .views import (
    WeatherView, ForecastView, RegisterView,
    FavoriteCityListCreateView, FavoriteCityDeleteView,
    add_favorite
)

urlpatterns = [
    path('weather/', WeatherView.as_view(), name='weather'),
    path('forecast/', ForecastView.as_view(), name='forecast'),
    path('register/', RegisterView.as_view(), name='register'),
    path('favorites/', FavoriteCityListCreateView.as_view(), name='favorite_list_create'),
    path('favorites/<int:pk>/', FavoriteCityDeleteView.as_view(), name='favorite_delete'),
    path('favorites/add/', add_favorite, name='add_favorite'),
   
]

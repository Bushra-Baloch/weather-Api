from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import FavoriteCity

@admin.register(FavoriteCity)
class FavoriteCityAdmin(admin.ModelAdmin):
    list_display = ('city', 'user')  # Table me kaunse columns show hon
    search_fields = ('city', 'user__username')

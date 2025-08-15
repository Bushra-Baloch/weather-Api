# weather-Api
🌦️ Weather API with Django & DRF
A simple Weather Forecast API built using Django Rest Framework and OpenWeather API.
It allows users to register, login (JWT authentication), fetch current weather, 5-day forecast, and manage favorite cities.

🚀 Features
User Authentication using JWT (access & refresh tokens)
Get current weather by city name
Get 5-day weather forecast (authenticated users only)
Add/Delete favorite cities (authenticated users only)
Caching to reduce API calls
Environment variables for sensitive keys
🛠️ Tech Stack
Python 3
Django 4+
Django Rest Framework
SimpleJWT
OpenWeather API
📂 API Endpoints
Method	Endpoint	Description	Auth Required
POST	/api/token/	Get JWT access & refresh token	❌
POST	/api/token/refresh/	Refresh JWT access token	❌
GET	/api/weather/?city=London	Get current weather for a city	❌
GET	/api/forecast/?city=London	Get 5-day forecast for a city	✅
GET	/api/favorites/	List user's favorite cities	✅
POST	/api/favorites/	Add a city to favorites	✅
DELETE	/api/favorites/<id>/	Remove a city from favorites	✅
⚙️ Setup Instructions
1️⃣ Clone Repository
python -m venv venv
venv\Scripts\activate    # Windows

Install Dependencies
pip install -r requirements.txt

Set Environment Variables
SECRET_KEY=your_django_secret_key
OPENWEATHER_API_KEY=your_openweather_api_key
DEBUG=True

Run Migrations
python manage.py migrate

Create Superuser
python manage.py createsuperuser

Start Development Server
python manage.py runserver


Authentication

This API uses JWT (JSON Web Token) authentication.

Login with POST /api/token/ using:
{
  "username": "bushra",
  "password": "weather"
}
You'll get:

{
  "access": "jwt_access_token",
  "refresh": "jwt_refresh_token"
}

Use the access token in the Authorization header for protected endpoints:

Authorization: Bearer your_access_token


git clone https://github.com/yourusername/weather-api.git
cd weather-api

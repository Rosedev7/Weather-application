from django.shortcuts import render

# Create your views here.
import requests
from django.http import JsonResponse
from django.shortcuts import render

def weather(request):
    city = 'London'  # You can change the city
    api_key = 'your_api_key_here'  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    data = response.json()
    
    if data['cod'] == 200:
        weather_data = {
            'city': city,
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'pressure': data['main']['pressure'],
        }
        return JsonResponse(weather_data)
    else:
        return JsonResponse({'error': 'City not found'})

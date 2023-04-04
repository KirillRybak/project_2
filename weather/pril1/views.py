from django.shortcuts import render
import requests
from .models import City


def index(request):
    return render(request,'pril1/index.html')


def weather(request):
    appid = "ffc9ddf1752ec7778ee7eeb208068b1c"
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'temp_max': res['main']['temp_max'],
            'icon': res ['weather'][0]['icon'],
        }
        all_cities.append(city_info)

    context={
        'info': city_info,
    }
    return render(request,'pril1/weather.html', context)

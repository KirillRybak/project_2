from django.shortcuts import render
import requests

def index(request):


    return render(request,'pril1/index.html')


def weather(request):
    appid = "ffc9ddf1752ec7778ee7eeb208068b1c"
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid

    city = 'Grodno'
    res = requests.get(url.format(city))
    city_info = {
        'city': city,
        'temp': res['main']['temp'],
        'max_temp': res['main']['max_temp'],
        'icon': res['weather'][0]['icon']
    }
    context={
        'info': city_info
    }
    return render(request,'pril1/weather.html', context)

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .apis import pythonweatherapi as pwapi
import asyncio
import logging


logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


class WeatherInfo:
    def __init__(self):
        self.city = None
        self.temperature = None
        self.mintemp = None
        self.maxtemp = None
        self.pressure = None
        self.humidity = None
        self.sunrise = None
        self.sunset = None
        self.country = None
        self.timezone = None
        self.date = None
        self.location = None
        self.skytext = None

# Create your views here.


def home_page(request):

    list_of_cities = ["Chennai", "Delhi", "Mumbai", "Bangalore"]
    # list_of_cities = pwapi.parse_csv()
    tempdetails = dict()
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    for city in list_of_cities:
        try:
            info = loop.run_until_complete(pwapi.getweather(city))
            data = WeatherInfo()
            data.city = city
            data.date = str(info.date)
            data.skytext = info.sky_text
            data.temperature = info.temperature
            tempdetails.update({city: data})
        except Exception as err:
            logging.error(str("Missing City {}".format(city)))

    URL_list = {
        'Google': "https://www.google.com/",
        'Instagram': "https://www.instagram.com/",
        'IEEE': "https://www.ieee.org/",
        'SAE': "https://www.sae.org/"
    }
    Domains = ["Google", "Instagram", "IEEE", "SAE"]

    context = {
        'Domains':  Domains,
        'URL': URL_list,
        'Weather': tempdetails
    }

    template = loader.get_template('../templates/index.html')
    return HttpResponse(template.render(context, request))


def forecast(request, city):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    info = loop.run_until_complete(pwapi.getforecastweather(city))
    context = {
        "forecastinfo": info
    }
    template = loader.get_template('../templates/forecast.html')
    return HttpResponse(template.render(context, request))

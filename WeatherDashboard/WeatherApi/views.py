from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .apis import openweatherapi as openapi
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
    tempdetails = dict()

    for city in list_of_cities:
        try:
            info = openapi.getcurrentdata(city)
            data = WeatherInfo()
            data.city = info.name
            data.temperature = info.main.temperature
            data.mintemp = info.main.temp_min
            data.maxtemp = info.main.temp_max
            data.pressure = info.main.pressure
            data.humidity = info.main.humidity
            data.sunrise = str(info.sys.sunrise)
            data.sunset = str(info.sys.sunset)
            data.country = str(info.sys.country)
            data.timezone = info.timezone
            data.date = str(info.dt)
            data.location = str(info.coord.lat) + ", " + str(info.coord.lon)
            data.skytext = info.sky_text
            tempdetails.update({city: data})
        except Exception as err:
            logging.error(str("Missing City {}".format(city)))

    context = {
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

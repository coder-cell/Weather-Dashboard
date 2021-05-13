import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .apis import openweatherapi as openapi
from .apis import convertsecondstoutc, convert_kelvintocelcius
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
            info = openapi.getweatherdata(city)
            logging.info("Status Code: {}".format(info.cod))
            data = WeatherInfo()
            data.city = info.name
            data.temperature = convert_kelvintocelcius(info.main.temp)
            data.mintemp = convert_kelvintocelcius(info.main.temp_min)
            data.maxtemp = convert_kelvintocelcius(info.main.temp_max)
            data.pressure = info.main.pressure
            data.humidity = info.main.humidity
            data.sunrise = datetime.datetime.utcfromtimestamp(int(info.sys.sunrise)).strftime("%H:%M:%S")
            data.sunset = datetime.datetime.utcfromtimestamp(int(info.sys.sunset)).strftime("%H:%M:%S")
            data.country = str(info.sys.country)
            data.timezone = convertsecondstoutc(info.timezone)
            data.date = datetime.datetime.utcfromtimestamp(int(info.dt)).strftime("%d-%m-%Y")
            data.location = str(info.coord.lat) + ", " + str(info.coord.lon)
            data.skytext = info.weather[0].description
            tempdetails.update({city: data})
        except Exception as err:
            logging.error(str("Missing City {0} with error {1}".format(city, str(err))))

    context = {
        'Weather': tempdetails
    }

    template = loader.get_template('../templates/index.html')
    return HttpResponse(template.render(context, request))


def forecast(request, city):
    # info = loop.run_until_complete(pwapi.getforecastweather(city))
    forcastlist = list()
    jsondatadict = openapi.getweatherdata(city, forecast=True)
    logging.info("Status Code: {}".format(jsondatadict.cod))
    for info in jsondatadict.list:
        data = WeatherInfo()
        data.temperature = convert_kelvintocelcius(info.main.temp)
        data.mintemp = convert_kelvintocelcius(info.main.temp_min)
        data.maxtemp = convert_kelvintocelcius(info.main.temp_max)
        data.pressure = info.main.pressure
        data.humidity = info.main.humidity
        data.date = datetime.datetime.utcfromtimestamp(int(info.dt)).strftime("%d-%m-%Y %H:%M:%S")
        data.skytext = info.weather[0].description
        forcastlist.append(data)

    context = {
        "city": city,
        "location": str(jsondatadict.city.coord.lat) + ", " + str(jsondatadict.city.coord.lon),
        "timezone": convertsecondstoutc(jsondatadict.city.timezone),
        "country": jsondatadict.city.country,
        "forecastinfo": forcastlist
    }
    template = loader.get_template('../templates/forecast.html')
    return HttpResponse(template.render(context, request))

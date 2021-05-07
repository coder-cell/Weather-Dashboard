from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import python_weather
import asyncio
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


class WeatherInfo:
    def __init__(self):
        self.city = None
        self.temperature = None
        self.date = None
        self.skytext = None


async def getweather(city):
    # declare the client. format defaults to metric system (celcius, km/h, etc.)
    client = python_weather.Client(format=python_weather.IMPERIAL)

    # fetch a weather forecast from a city
    weather = await client.find(city)

    # # returns the current city temperature (int)
    # print(weather.current.temperature)
    #
    # # get the weather forecast for a few days
    # for forecast in weather.forecast:
    #     print(str(forecast.date), forecast.sky_text, forecast.temperature)

    # close the wrapper once done
    await client.close()
    return weather.current


def parse_csv():
    import csv
    with open("WeatherDashboard/WeatherApi/artifacts/indian_cities.csv") as csvfile:
        listcities = list()
        csvread = csv.reader(csvfile, delimiter=",")
        linecount = 0
        for row in csvread:
            if linecount > 3:
                listcities.append(row[0])
            linecount += 1
    return listcities


def home_page(request):

    list_of_cities = ["Chennai", "Delhi", "Mumbai", "Bangalore"]
    # list_of_cities = parse_csv()
    tempdetails = dict()
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    for city in list_of_cities:
        try:
            info = loop.run_until_complete(getweather(city))
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


# Create your views here.

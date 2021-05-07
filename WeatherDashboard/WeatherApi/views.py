from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import python_weather
import asyncio


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
    return weather.current.temperature


def home_page(request):

    list_of_cities = ["Chennai", "Delhi", "Mumbai", "Bangalore"]
    tempdetails = dict()
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    for city in list_of_cities:
        temp = loop.run_until_complete(getweather(city))
        tempdetails.update({city: temp})

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

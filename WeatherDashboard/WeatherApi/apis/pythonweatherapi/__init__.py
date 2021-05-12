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
    return weather.current


async def getforecastweather(city):
    # declare the client. format defaults to metric system (celcius, km/h, etc.)
    client = python_weather.Client(format=python_weather.IMPERIAL)

    # fetch a weather forecast from a city
    weather = await client.find(city)

    info = list()
    # get the weather forecast for a few days
    for _forecast in weather.forecast:
        info.append(_forecast)

    # close the wrapper once done
    await client.close()
    return info


def parse_csv():
    import csv
    with open("WeatherDashboard/WeatherApi/artifacts/cities.csv") as csvfile:
        listcities = list()
        csvread = csv.reader(csvfile, delimiter=",")
        linecount = 0
        for row in csvread:
            if linecount > 3:
                listcities.append(row[0])
            linecount += 1
    return listcities

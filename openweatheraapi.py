import requests
import json
from types import SimpleNamespace


API_KEY = "b2759e8099be4432b8f6a37ff9089770"
# BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

BASE_URL = "https://api.openweathermap.org/data/2.5/forecast?"

city_name = "Chennai"

complete_url = BASE_URL + "q=" + city_name + "&appid=" + API_KEY
# complete_url = BASE_URL + "&appid=" + API_KEY

response = requests.get(complete_url)

x = response.json()
strjson = json.dumps(x)
pyobj = json.loads(strjson, object_hook=lambda d: SimpleNamespace(**d))
# print(pyobj.main.temp, pyobj.main.pressure, pyobj.main.humidity, pyobj.weather[0].description)

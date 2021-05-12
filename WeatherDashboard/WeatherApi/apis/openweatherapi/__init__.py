import requests
import json
from types import SimpleNamespace

API_KEY = "b2759e8099be4432b8f6a37ff9089770"


def getcurrentdata(city, forecast=False):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    if forecast:
        base_url = "https://api.openweathermap.org/data/2.5/forecast?"

    complete_url = base_url + "q=" + city + "&appid=" + API_KEY

    response = requests.get(complete_url)

    x = response.json()
    strjson = json.dumps(x)
    return json.loads(strjson, object_hook=lambda d: SimpleNamespace(**d))
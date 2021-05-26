# Weather-Dashboard
Repository that Uses Django and Weather API to display the Weather Details.

**Commands:** <br>
 `django-admin startproject WeatherDashboard` <br>
 `python manage.py runserver` <br>
 `python manage.py startapp WeatherApi` <br>
 `python manage.py migrate` <br>
 `python manage.py makemigrations WeatherApi` <br>
 `python manage.py sqlmigrate WeatherApi 0001` <br>
 `python manage.py migrate` <br>
 `python manage.py createsuperuser` <br>

Till git revision `3f6232b7fdca1de68e27628ad377f905dae906dc`
The application uses [**python_weather**](https://pypi.org/project/python-weather/) python package to retrive the Weather.

After git revision `87cfaf7f334595cd9af972156fa873cac7b242ca`
The application uses [**Open Weather API**](https://openweathermap.org/api)

First Page:
![img.png](img.png)
On Search of City:
![img_2.png](img_2.png)
On clicking the city hyperlink, forecast info will be available:
![img_1.png](img_1.png)
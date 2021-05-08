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

The application uses [**python_weather**](https://pypi.org/project/python-weather/) python package to retrive the 
Weather information for selected cities (Chennai, Mumbai, Delhi, Bangalore).
Note: This package supports only major cities.
![img.png](img.png)
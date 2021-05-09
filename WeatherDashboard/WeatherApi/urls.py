from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='Home-Page'),
    path('forecast', views.forecast, name='Forecast-Page'),
]

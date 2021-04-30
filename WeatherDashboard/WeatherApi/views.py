from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    return HttpResponse('<h>This is My Home Page</h>')


# Create your views here.

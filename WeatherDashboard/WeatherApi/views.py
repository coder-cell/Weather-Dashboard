from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def home_page(request):
    URL_list = [
        "https://www.google.com/",
        "https://www.instagram.com/",
        "https://www.ieee.org/",
        "https://www.sae.org/"
    ]
    Domains = ["Google", "Instagram", "IEEE", "SAE"]

    context = {
        'Domains':  Domains,
        'URL': URL_list,
    }
    return HttpResponse(render(context, request))


# Create your views here.

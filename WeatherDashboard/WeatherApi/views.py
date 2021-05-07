from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def home_page(request):
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
    }

    template = loader.get_template('../templates/index.html')
    return HttpResponse(template.render(context, request))


# Create your views here.

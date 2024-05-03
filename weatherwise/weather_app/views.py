from django.shortcuts import render
import sys, os
sys.path.append(sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'weatherwise', 'api')))
import weatherwise_api
from django.contrib import admin
from django.urls import path, include
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.
def home(request):
    return render(request,'home.html')

def weather(request):
    search_string = request.GET.get('search')
    location = weatherwise_api.get_location_data(search_string)
    if location.coordinates == "N/A,N/A":
        return redirect('../')
    weather = weatherwise_api.get_weather_data(location.coordinates)
    context = {
        'location' : location,
        'weather' : weather
    }
    return render(request,'weather_app/weather.html', context=context)

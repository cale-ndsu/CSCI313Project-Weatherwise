from django.shortcuts import render
from django.contrib import admin
from django.urls import path, include
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def user_settings(request):
    return render(request,'user_settings.html')
from django.shortcuts import render
from django.contrib import admin
from django.urls import path, include
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms

# Create your views here.

def log_out(request):
    return render(request,'logout.html')
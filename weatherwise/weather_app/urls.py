from django.urls import path
from . import views
from django.conf.urls import include
from account_app import views as account_views
app_name = "weather_app"

urlpatterns = [
    path('', views.home, name='home'),
    path('information/', views.weather, name = 'weather'),
    path('about/', views.about, name = 'about'),
]
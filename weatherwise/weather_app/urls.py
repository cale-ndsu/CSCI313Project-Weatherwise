from django.urls import path
from . import views
from django.conf.urls import include
from account_app import views as account_views
app_name = "weather_app"

urlpatterns = [
    path('', views.home, name='home'),
    path('weather/<str:search_string>', views.weather, name = 'weather'),
    path('account/user_settings', account_views.user_settings, name="user_settings")
]
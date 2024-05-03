from django.urls import path
from . import views

app_name = 'account_app'

urlpatterns = [
    #path('user_settings', views.user_settings, name='user_settings'),
    path('logout', views.log_out, name='logout' )
]
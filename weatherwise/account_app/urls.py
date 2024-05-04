from django.urls import path
from . import views

app_name = 'account_app'

urlpatterns = [
    path('logout', views.log_out, name='logout' )
]
from django.urls import path

from .views import *

app_name = 'guest'
urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('message', message, name='message'),
    path('my-booking', my_booking, name='my-booking'),
    path('profile', profile, name='profile'),
]

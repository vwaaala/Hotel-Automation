from django.urls import path

from .views import *

app_name = 'portfolio'
urlpatterns = [
    path('', home, name='home'),
    path('services', service_portfolio, name='services'),
    path('find-us', find_us_portfolio, name='find-us'),
    path('booking', booking_portfolio, name='booking'),
]

from django.urls import path

from .views import *

app_name = 'manager'
urlpatterns = [
    path('', dashboard, name='dashboard'),
]

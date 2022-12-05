from django.urls import path

from .views import *

app_name = 'manager'
urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('guests', guests, name='guests'),
    path('guests-view', guests_view, name='guests-view'),
]

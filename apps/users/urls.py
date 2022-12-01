from django.urls import path

from .views import *

app_name = 'users'
urlpatterns = [
    path('logout', user_logout, name='logout'),
    path('login', user_login, name='login'),
    path('register', guest_create, name='guest-create'),
]

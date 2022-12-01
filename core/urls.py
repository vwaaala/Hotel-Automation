"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.users.urls import user_login, user_logout
urlpatterns = [
    path('', include('apps.portfolio.urls', namespace='portfolio')),
    path("admin/", admin.site.urls),
    path('user/', include('apps.users.urls', namespace='users')),
    path('guest/', include('apps.guest.urls', namespace='guest')),
    path('manager/', include('apps.manager.urls', namespace='manager')),
]

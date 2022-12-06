from django.urls import path
from apps.hrm.views import employee_list
from .views import *

app_name = 'manager'
urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('guests', guests, name='guests'),
    path('guests-view', guests_view, name='guests-view'),
    path('booking', booking, name='booking'),

    path('employee', employee_list, name="employee"),
]

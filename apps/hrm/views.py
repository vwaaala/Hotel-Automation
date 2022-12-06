from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from apps.users.models import Employee


@login_required()
def employee_list(request):
    emoployee = Employee.objects.all()

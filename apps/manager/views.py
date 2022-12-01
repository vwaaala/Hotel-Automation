from django.contrib.auth.decorators import login_required
from django.shortcuts import render

authorized = 'manager'


@login_required()
def dashboard(request):
    role = str(request.user.groups.all()[0])
    path = role + '/'
    if role == authorized:
        return render(request, 'manager/dashboard.html')
    else:
        context = {
            'code': 401,
            'title': "401 | Unauthorized",
            'message': "Whoops! You're not supposed to be here."
        }
        return render(request, 'global/whoops.html', context)

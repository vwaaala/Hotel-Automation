from datetime import datetime, timedelta, date

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count, Q
from django.shortcuts import render

from apps.guest.views import top_guests
from apps.room.models import Booking
from apps.users.models import Guest

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


@login_required()
def guests(request):
    role = str(request.user.groups.all()[0])
    path = role + "/"

    top_guests_limit = 10
    top_guests_list = top_guests(top_guests_limit)

    bookings = Booking.objects.all()
    fd = datetime.combine(date.today() - timedelta(days=30), datetime.min.time())
    ld = datetime.combine(date.today(), datetime.min.time())
    guests = []

    for b in bookings:
        if b.end_date >= fd.date() and b.start_date <= ld.date():
            if b.guest not in guests:
                guests.append(b.guest)

    if request.method == "POST":
        if "filterDate" in request.POST:

            if request.POST.get("f_day") == "" and request.POST.get("l_day") == "":
                guests = Guest.objects.all()

                context = {
                    "role": role,
                    "guests": guests,
                    "fd": "",
                    "ld": ""
                }
                return render(request, path + "guests.html", context)

            if request.POST.get("f_day") == "":
                fd = datetime.strptime("1970-01-01", '%Y-%m-%d')
            else:
                fd = request.POST.get("f_day")
                fd = datetime.strptime(fd, '%Y-%m-%d')

            if request.POST.get("l_day") == "":
                ld = datetime.strptime("2030-01-01", '%Y-%m-%d')
            else:
                ld = request.POST.get("l_day")
                ld = datetime.strptime(ld, '%Y-%m-%d')

            for b in bookings:
                if b.end_date >= fd.date() and b.start_date <= ld.date():
                    if b.guest not in guests:
                        guests.append(b.guest)

        if "filterGuest" in request.POST:
            guests = Guest.objects.all()
            users = User.objects.all()
            if (request.POST.get("id") != ""):
                users = users.filter(
                    id__contains=request.POST.get("id"))
                guests = guests.filter(user__in=users)

            if (request.POST.get("name") != ""):
                users = users.filter(
                    Q(first_name__contains=request.POST.get("name")) | Q(last_name__contains=request.POST.get("name")))
                guests = guests.filter(user__in=users)

            if (request.POST.get("email") != ""):
                users = users.filter(email__contains=request.POST.get("email"))
                guests = guests.filter(user__in=users)

            if (request.POST.get("number") != ""):
                guests = guests.filter(
                    phoneNumber__contains=request.POST.get("number"))

            context = {
                "role": role,
                "guests": guests,
                "id": request.POST.get("id"),
                "name": request.POST.get("name"),
                "email": request.POST.get("email"),
                "number": request.POST.get("number")
            }
            return render(request, path + "guests.html", context)

        if "top" in request.POST:
            top_guests_list = top_guests(request.POST.get('top'))
            context = {
                "role": role,
                "guests": guests,
                "top_guests_list": top_guests_list,
                "top_guests_limit": top_guests_limit,
                "fd": fd,
                "ld": ld
            }
            return render(request, path + "guests.html", context)
    context = {
        "role": role,
        "guests": guests,
        "top_guests_list": top_guests_list,
        "top_guests_limit": top_guests_limit,
        "fd": fd,
        "ld": ld
    }
    return render(request, path + "guests.html", context)

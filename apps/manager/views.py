from datetime import datetime, timedelta, date

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count, Q
from django.shortcuts import render

from apps.guest.views import top_guests, booking_guest_filter_by_date
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

    fd = datetime.combine(date.today() - timedelta(days=30), datetime.min.time())
    ld = datetime.combine(date.today(), datetime.min.time())
    all_guests = booking_guest_filter_by_date(fd, ld)

    if request.method == "POST":
        if "filterDate" in request.POST:
            if request.POST.get("f_day") == "" and request.POST.get("l_day") == "":
                all_guests = Guest.objects.all()
                try:
                    all_guests = Paginator(all_guests, 10)
                except PageNotAnInteger:
                    all_guests = all_guests.page(1)
                except EmptyPage:
                    all_guests = all_guests.page(all_guests.num_pages)
                context = {
                    "role": role,
                    "guests": all_guests,
                    "top_guests_list": top_guests_list,
                    "top_guests_limit": top_guests_limit,
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

            all_guests = booking_guest_filter_by_date(fd, ld)

        if "filterGuest" in request.POST:
            all_guests = Guest.objects.all()
            users = User.objects.all()
            if request.POST.get("id") != "":
                users = users.filter(
                    id__contains=request.POST.get("id"))
                all_guests = all_guests.filter(user__in=users)

            if request.POST.get("name") != "":
                users = users.filter(
                    Q(first_name__contains=request.POST.get("name")) | Q(last_name__contains=request.POST.get("name")))
                all_guests = all_guests.filter(user__in=users)

            if request.POST.get("email") != "":
                users = users.filter(email__contains=request.POST.get("email"))
                all_guests = all_guests.filter(user__in=users)

            if request.POST.get("number") != "":
                all_guests = all_guests.filter(
                    phoneNumber__contains=request.POST.get("number"))
            try:
                all_guests = Paginator(all_guests, 10)
            except PageNotAnInteger:
                all_guests = all_guests.page(1)
            except EmptyPage:
                all_guests = all_guests.page(all_guests.num_pages)
            context = {
                "role": role,
                "guests": all_guests,
                "top_guests_list": top_guests_list,
                "top_guests_limit": top_guests_limit,
                "id": request.POST.get("id"),
                "name": request.POST.get("name"),
                "email": request.POST.get("email"),
                "number": request.POST.get("number")
            }
            return render(request, path + "guests.html", context)

        if "top" in request.POST:
            if request.POST.get('top') == '':
                context = {
                    "role": role,
                    "guests": all_guests,
                    "top_guests_list": top_guests_list,
                    "top_guests_limit": top_guests_limit,
                    "fd": fd,
                    "ld": ld
                }
            else:
                top_guests_list = top_guests(request.POST.get('top'))
                context = {
                    "role": role,
                    "guests": all_guests,
                    "top_guests_list": top_guests_list,
                    "top_guests_limit": top_guests_limit,
                    "fd": fd,
                    "ld": ld
                }
            return render(request, path + "guests.html", context)
    
    try:
        all_guests = Paginator(all_guests, 10)
    except PageNotAnInteger:
        all_guests = all_guests.page(1)
    except EmptyPage:
        all_guests = all_guests.page(all_guests.num_pages)
    context = {
        "role": role,
        "all_guests": all_guests,
        "top_guests_list": top_guests_list,
        "top_guests_limit": top_guests_limit,
        "fd": fd,
        "ld": ld
    }
    return render(request, path + "guests.html", context)


@login_required()
def guests_view(request):
    guest_list = Guest.objects.all()
    context = {
        'guest_list' : guest_list
    }
    return render(request, 'manager/guests_view.html', context)
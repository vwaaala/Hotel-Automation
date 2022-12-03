from django.db.models import Count
from django.shortcuts import render

from apps.room.models import Booking
from apps.users.models import Guest


def dashboard(request):
    return render(request, 'guest/dashboard.html')


def message(request):
    return render(request, 'guest/message.html')


def my_booking(request):
    return render(request, 'guest/my-booking.html')


def profile(request):
    return render(request, 'guest/profile.html')


def top_guests(limit=10):
    guests = Booking.objects.all().values('guest').annotate(total=Count('guest')).order_by('-total')
    top = []
    for t in guests:
        if len(top) > limit:
            # TODO return top list from here
            break
        else:
            top.append(Guest.objects.get(id=t.get('guest')))
    return top


def booking_guest_filter_by_date(from_date, to_date):
    bookings = Booking.objects.all()
    guests = []
    for b in bookings:
        if b.end_date >= from_date.date() and b.start_date <= to_date.date():
            if b.guest not in guests:
                guests.append(b.guest)
    return guests



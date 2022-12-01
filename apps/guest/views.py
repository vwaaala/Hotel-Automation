from django.shortcuts import render


def dashboard(request):
    return render(request, 'guest/dashboard.html')


def message(request):
    return render(request, 'guest/message.html')


def my_booking(request):
    return render(request, 'guest/my-booking.html')


def profile(request):
    return render(request, 'guest/profile.html')

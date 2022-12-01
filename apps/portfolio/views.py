from django.shortcuts import render


def home(request):
    return render(request, 'portfolio/home.html')


def service_portfolio(request):
    return render(request, 'portfolio/service.html')


def find_us_portfolio(request):
    return render(request, 'portfolio/find-us.html')


def booking_portfolio(request):
    return render(request, 'portfolio/booking.html')

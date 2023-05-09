from django.shortcuts import render

from .models import Flights

# Create your views here.

def index(request):
    return render(request, "flights/index.html", {
        "flights": Flights.objects.all()
    })

def flight(request, flight_id):
    flight = Flights.objects.get(pk=flight_id)
    return render(request, "flights/flights.html", {
        "flight": flight,
        "passengers": flight.passengers.all()
    })

from django.shortcuts import render

from .models import Flight


# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all() #"flights" is a variable
    })

def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id) #pk - primary key and is use as an ID
    return render(request, "flights/flight.html", {
        "flight": flight
    })

from django.shortcuts import redirect, render, get_object_or_404
from django.http import Http404

from .models import Flight, Passenger

def index(request):
    return render(request, "flights/index.html",
                  { 'flights': Flight.objects.all()})

def flight(request, flight_id):
    try:
        flight = Flight.objects.get(id=flight_id)
    except Flight.DoesNotExist:
        raise Http404(f'FLight id #{flight_id} does not exist')
    return render(request, "flights/flight.html",
                  { 'flight': flight})


def flight(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    return render(request, "flights/flight.html",
                  { 'flight': flight,
                   'passengers': flight.passengers.all()})

def flight(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    np = Passenger.objects.all()
    print(np)
    return render(request, "flights/flight.html",
                  { 'flight': flight,
                   'passengers': flight.passengers.all(),
                   'non_passengers': Passenger.objects.exclude(flights=flight).all()})

def book(request, flight_id):
    if request.method == "POST":
        p_id = request.POST["passenger"]
        p = Passenger.objects.get(pk=int(p_id))
        flight = get_object_or_404(Flight, id=flight_id)
        p.flights.add(flight)
    return redirect('flights:flight', flight_id=flight_id)

from django.shortcuts import render, redirect
from .models import Car, Customer, WalkIn, Booking, ExchangeVehicle, Payment, Orders
from .forms import CarForm, CustomerForm, WalkInForm, ExchangeVehicleForm, PaymentForm, BookingForm, OrdersForm


# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the seres index.")

def home(request):
    return render(request, 'home.html', {})

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'car_list.html', {'cars':cars})

def add_car(request):
    if request.user.is_authenticated:
        submitted = False
        form = CarForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                car = form.save(commit=False)
                car.user = request.user
                car.save()
                return redirect('car_list')
    else:
        form = CarForm()
        if 'submitted' in request.GET:
            submitted=True
    return render(request, "add_car.html", {'form':form, 'submitted':submitted})
            

def customer_list(request):       
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers':customers})
    
def add_customer(request):
    submitted = 'submitted' in request.GET  # Initialize 'submitted' based on GET parameters
    
    if request.user.is_authenticated:
        form = CustomerForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                car = form.save(commit=False)
                car.user = request.user
                car.save()
                return redirect('customer_list')
    else:
        form = CustomerForm()
    
    return render(request, "add_customer.html", {'form': form, 'submitted': submitted})

def walkin_list(request):       
    walkins = WalkIn.objects.all()
    return render(request, 'walkin_list.html', {'walkins':walkins})
    
def add_walkin(request):
    if request.user.is_authenticated:
        submitted = False
        form = WalkInForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                car = form.save(commit=False)
                car.user = request.user
                car.save()
                return redirect('walkin_list')
    else:
        form = WalkInForm()
        if 'submitted' in request.GET:
            submitted=True
    return render(request, "add_walkin.html", {'form':form, 'submitted':submitted})

def allbookings(request):      
    bookings = Booking.objects.all()
    return render(request, 'allbookings.html', {'bookings':bookings})
    
def add_booking(request):
    if request.user.is_authenticated:
        submitted = False
        form = BookingForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                car = form.save(commit=False)
                car.user = request.user
                car.save()
                return redirect('all-bookings')
    else:
        form = BookingForm()
        if 'submitted' in request.GET:
            submitted=True
    return render(request, "add_booking.html", {'form':form, 'submitted':submitted})


def exchange_vehicle(request):    
    exchange_vehicles = ExchangeVehicle.objects.all()
    return render(request, 'exchange_vehicle.html', {'exchange_vehicles':exchange_vehicles})
    

def add_exchange(request):
    if request.user.is_authenticated:
        submitted = False
        form = ExchangeVehicleForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                car = form.save(commit=False)
                car.user = request.user
                car.save()
                return redirect('exchange-vehicle')
    else:
        form = ExchangeVehicleForm()
        if 'submitted' in request.GET:
            submitted=True
    return render(request, "add_exchange.html", {'form':form, 'submitted':submitted})
    
def all_payments(request):       
    payments = Payment.objects.all()
    return render(request, 'payment.html', {'payments':payments})
    
def add_payments(request):
    if request.user.is_authenticated:
        submitted = False
        form = PaymentForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                car = form.save(commit=False)
                car.user = request.user
                car.save()
                return redirect('all_payments')
    else:
        form = PaymentForm()
        if 'submitted' in request.GET:
            submitted=True
    return render(request, "add_payments.html", {'form':form, 'submitted':submitted})
    
def all_orders(request):   
    orders = Orders.objects.all()
    return render(request, 'orders.html', {'orders':orders})
    
def add_orders(request):
    if request.user.is_authenticated:
        submitted = False
        form = OrdersForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                car = form.save(commit=False)
                car.user = request.user
                car.save()
                return redirect('all_orders')
    else:
        form = OrdersForm()
        if 'submitted' in request.GET:
            submitted=True
    return render(request, "add_orders.html", {'form':form, 'submitted':submitted})
    
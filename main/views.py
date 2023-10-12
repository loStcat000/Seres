from django.shortcuts import render, redirect
from .models import Car, Customer, WalkIn, Booking, ExchangeVehicle, Payment, Orders
from .forms import CarForm, CustomerForm, WalkInForm, ExchangeVehicleForm, PaymentForm, BookingForm, OrdersForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView
from . import models
from django.urls import reverse_lazy 

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
                return redirect('all_bookings')
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
                return redirect('exchange_vehicle')
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
    

class CarUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Car
    fields = ['car_name', 'car_model', 'car_variant', 'car_color']
    template_name = 'add_car.html'

    success_url = reverse_lazy('car_list')

    def test_func(self):
      car = self.get_object()
      return self.request.user.is_superuser
    
    def form_valid(self, form):
            car = form.save(commit=False)
            form.instance.author = self.request.user
            return super().form_valid(form)
    
class CustomerUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Customer
    fields = ['customer_firstname', 'customer_lastname', 'customer_contact']
    template_name = 'add_customer.html'

    success_url = reverse_lazy('customer_list')

    def test_func(self):
      customer = self.get_object()
      return self.request.user.is_superuser
    
    def form_valid(self, form):
            customer = form.save(commit=False)
            form.instance.author = self.request.user
            return super().form_valid(form)
    
class WalkinUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.WalkIn
    fields = ['walkin_firstname', 'walkin_lastname', 'walkin_contact', 'purpose_of_visit', 'outcome_of_visit', 'interest_level', 
              'remarks', 'test_drive', 'date_of_walkin']
    template_name = 'add_walkin.html'

    success_url = reverse_lazy('walkin_list')

    def test_func(self):
      walkin = self.get_object()
      return self.request.user.is_superuser
    
    def form_valid(self, form):
            walkin = form.save(commit=False)
            form.instance.author = self.request.user
            return super().form_valid(form)
    
class ExchangeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.ExchangeVehicle
    fields = ['customer', 'vehicle_name', 'kiloMeters_run', 'vehicle_made_year', 'license_plate', 'vehicle_color', 
              'customer_estimated_value', 'actual_value', 'exchange_status']
    template_name = 'add_exchange.html'

    success_url = reverse_lazy('exchange_vehicle')

    def test_func(self):
      exchange = self.get_object()
      return self.request.user.is_superuser
    
    def form_valid(self, form):
            exchange = form.save(commit=False)
            form.instance.author = self.request.user
            return super().form_valid(form)
    
class PaymentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Payment
    fields = ['customer', 'payment_method', 'do', 'quotation', 'remarks']
    template_name = 'add_payments.html'

    success_url = reverse_lazy('all_payments')

    def test_func(self):
      payment = self.get_object()
      return self.request.user.is_superuser
    
    def form_valid(self, form):
            payment = form.save(commit=False)
            form.instance.author = self.request.user
            return super().form_valid(form)
    
class BookingUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Booking
    fields = ['customer', 'walkin_customer', 'booking_status', 'prebooking_amount', 'booking_amount', 'booking_source']
    template_name = 'add_booking.html'

    success_url = reverse_lazy('all_bookings')

    def test_func(self):
      booking = self.get_object()
      return self.request.user.is_superuser
    
    def form_valid(self, form):
            booking = form.save(commit=False)
            form.instance.author = self.request.user
            return super().form_valid(form)
    
class OrderUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Orders
    fields = ['customer', 'payment', 'car_name', 'car_variant', 'booking', 'date_of_order', 'selling_price', 
            'total_amount_paid', 'remaining_payment', 'remarks', 'cancelled', 'reason_of_cancel']
    template_name = 'add_orders.html'

    success_url = reverse_lazy('all_orders')

    def test_func(self):
      order = self.get_object()
      return self.request.user.is_superuser
    
    def form_valid(self, form):
            order = form.save(commit=False)
            form.instance.author = self.request.user
            return super().form_valid(form)
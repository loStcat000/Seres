from django.shortcuts import render, redirect, get_object_or_404
from .models import Car, Customer, WalkIn, ExchangeVehicle, Payment, Orders, CarColor
from .forms import CarForm, CustomerForm, WalkInForm, ExchangeVehicleForm, PaymentForm, OrdersForm, CarColorForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView, DeleteView
from . import models
from django.db.models import Q, Count
from django.core.paginator import Paginator 
from django.urls import reverse_lazy 
from django.forms import modelformset_factory
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages




# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the seres index.")

def home(request):

    return render(request, 'home.html', {})


def car_list(request):
    cars = Car.objects.all()
    p = Paginator(Car.objects.all(), 5)
    page = request.GET.get('page')
    list_car = p.get_page(page)

    return render(request, 'car_list.html', {'cars': cars, 'list_car': list_car})
   

            
def add_car(request):
    submitted = 'submitted' in request.GET  # Initialize 'submitted' based on GET parameters
    
    if request.user.is_authenticated:
        form = CarForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                car = form.save(commit=False)
                car.user = request.user
                car.save()
                return redirect('car_list')
    else:
        form = CarForm()
    
    return render(request, "add_car.html", {'form': form, 'submitted': submitted})
    

  
def customer_list(request):       
    active_customers = Customer.objects.filter(active=True)
    p = Paginator(Customer.objects.filter(active=True), 5)
    page = request.GET.get('page')
    list_customer = p.get_page(page)

    return render(request, 'customer_list.html', {'customers': active_customers, 'list_customer': list_customer})
    
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
    p = Paginator(WalkIn.objects.all(), 5)
    page = request.GET.get('page')
    list_walkin = p.get_page(page)
    return render(request, 'walkin_list.html', {'walkins':walkins, 'list_walkin':list_walkin})
    
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


def exchange_vehicle(request):    
    exchange_vehicles = ExchangeVehicle.objects.all()
    p = Paginator(ExchangeVehicle.objects.all(), 5)
    page = request.GET.get('page')
    exchange_list = p.get_page(page)
    return render(request, 'exchange_vehicle.html', {'exchange_vehicles':exchange_vehicles, 'exchange_list':exchange_list})
    

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
    p = Paginator(Payment.objects.all(), 5)
    page = request.GET.get('page')
    payment_list = p.get_page(page)
    return render(request, 'payment.html', {'payments':payments, 'payment_list':payment_list})
    
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
    p = Paginator(Orders.objects.all(), 5)
    page = request.GET.get('page')
    order_list = p.get_page(page)
    return render(request, 'orders.html', {'orders':orders, 'order_list': order_list})
    
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
    else:
        return redirect('login')


class CarUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Car
    fields = ['car_name', 'car_model']
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
    
    
class OrderUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Orders
    fields = ['customer', 'walkin_customer', 'payment', 'car', 'car_color', 'booking', 'prebooking_amount', 'booking_amount', 'booking_source', 'date_of_order', 'selling_price', 
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
    
class CarDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Car
    success_url = reverse_lazy('car_list')
    template_name = 'confirm_delete.html'

    def test_func(self):
      car = self.get_object()
      return self.request.user.is_superuser
    
class CustomerDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Customer
    success_url = reverse_lazy('customer_list')
    template_name = 'confirm_delete.html'

    def test_func(self):
      customer = self.get_object()
      return self.request.user.is_superuser
    
class WalkInDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.WalkIn
    success_url = reverse_lazy('walkin_list')
    template_name = 'confirm_delete.html'

    def test_func(self):
      walkin = self.get_object()
      return self.request.user.is_superuser
    
class ExchangeVehicleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.ExchangeVehicle
    success_url = reverse_lazy('exchange_vehicle')
    template_name = 'confirm_delete.html'

    def test_func(self):
      exchange_vehicle = self.get_object()
      return self.request.user.is_superuser
    
class PaymentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Payment
    success_url = reverse_lazy('all_payments')
    template_name = 'confirm_delete.html'

    def test_func(self):
      payment = self.get_object()
      return self.request.user.is_superuser
    
class OrderDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Orders
    success_url = reverse_lazy('all_orders')
    template_name = 'confirm_delete.html'

    def test_func(self):
      order = self.get_object()
      return self.request.user.is_superuser
    
def order_search(request):
    if request.method == "POST":
        searched = request.POST.get('searched', '')  # Provide a default value if 'searched' is not in request.POST
        orders = Orders.objects.filter(
            Q(customer__customer_firstname__icontains=searched) |
            Q(car__car_name__icontains=searched) |
            Q(booking__booking_type__icontains=searched) |
            Q(payment__payment_type__icontains=searched) |
            Q(date_of_order__icontains=searched) 

        )
        return render(request, "order_search.html", {'searched': searched, 'orders': orders})
    else:
        return render(request, "order_search.html", {})
    
def exchange_search(request):
    if request.method == "POST":
        searched = request.POST.get('searched', '')  # Provide a default value if 'searched' is not in request.POST
        exchange_vehicles = ExchangeVehicle.objects.filter(
            Q(customer__customer_firstname__icontains=searched) |
            Q(vehicle_name__icontains=searched) |
            Q(license_plate__icontains=searched) |
            Q(vehicle_color__icontains=searched) 

        )
        return render(request, "exchange_search.html", {'searched': searched, 'exchange_vehicles': exchange_vehicles})
    else:
        return render(request, "exchange_search.html", {})

def payment_search(request):
    if request.method == "POST":
        searched = request.POST.get('searched', '')  # Provide a default value if 'searched' is not in request.POST
        payments = Payment.objects.filter(
            Q(customer__customer_firstname__icontains=searched) |
            Q(payment_method__payment_type__icontains=searched) |
            Q(do__icontains=searched) |
            Q(quotation__icontains=searched) 

        )
        return render(request, "payment_search.html", {'searched': searched, 'payments': payments})
    else:
        return render(request, "payment_search.html", {})
     
def walkin_search(request):
    if request.method == "POST":
        searched = request.POST.get('searched', '')  # Provide a default value if 'searched' is not in request.POST
        walkins = WalkIn.objects.filter(
            Q(walkin_firstname__icontains=searched) |
            Q(date_of_walkin__icontains=searched) 

        )
        return render(request, "walkin_search.html", {'searched': searched, 'walkins': walkins})
    else:
        return render(request, "walkin_search.html", {})
    
def customer_search(request):
    if request.method == "POST":
        searched = request.POST.get('searched', '')  # Provide a default value if 'searched' is not in request.POST
        customers = Customer.objects.filter(
            Q(customer_firstname__icontains=searched) |
            Q(customer_lastname__icontains=searched) 

        )
        return render(request, "customer_search.html", {'searched': searched, 'customers': customers})
    else:
        return render(request, "customer_search.html", {})
    
def orders_chart(request):
    # Query to get the count of orders for each car
    car_orders = Orders.objects.values('car__car_name').annotate(total_orders=Count('id'))

    # Prepare data for the chart
    chart_data = []
    for item in car_orders:
        chart_data.append({
            'car_name': item['car__car_name'],
            'total_orders': item['total_orders']
        })

    return render(request, 'home.html', {'chart_data': chart_data})






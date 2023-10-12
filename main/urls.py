from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('car_list/', views.car_list, name='car_list'),
    path('customer_list/', views.customer_list, name='customer_list'),
    path('walkin_list/', views.walkin_list, name='walkin_list'),
    path('all_bookings/', views.allbookings, name='all_bookings'), 
    path('exchange_vehicle/', views.exchange_vehicle, name='exchange_vehicle'),
    path('all_payments/', views.all_payments, name='all_payments'),
    path('all_orders/', views.all_orders, name='all_orders'),

    path('add_car/', views.add_car, name='add_car'),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('add_walkin/', views.add_walkin, name='add_walkin'),
    path('add_booking/', views.add_booking, name='add_booking'),
    path('add_exchange/', views.add_exchange, name='add_exchange'),
    path('add_payments/', views.add_payments, name='add_payments'),
    path('add_orders/', views.add_orders, name='add_orders'),

    path('car/<int:pk>/update', views.CarUpdateView.as_view(), name="car_update"),
    path('customer/<int:pk>/update', views.CustomerUpdateView.as_view(), name="customer_update"),
    path('walkin/<int:pk>/update', views.WalkinUpdateView.as_view(), name="walkin_update"),
    path('exchange_vehicle/<int:pk>/update', views.ExchangeUpdateView.as_view(), name="exchange_update"),
    path('payment/<int:pk>/update', views.PaymentUpdateView.as_view(), name="payment_update"),
    path('booking/<int:pk>/update', views.BookingUpdateView.as_view(), name="booking_update"),
    path('order/<int:pk>/update', views.OrderUpdateView.as_view(), name="order_update"),




]
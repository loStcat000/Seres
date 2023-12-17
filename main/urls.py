from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('car_list/', views.car_list, name='car_list'),
    path('customer_list/', views.customer_list, name='customer_list'),
    path('walkin_list/', views.walkin_list, name='walkin_list'),
    path('exchange_vehicle/', views.exchange_vehicle, name='exchange_vehicle'),
    path('all_payments/', views.all_payments, name='all_payments'),
    path('all_orders/', views.all_orders, name='all_orders'),
    path('all_delivery/', views.all_delivery, name='all_delivery'),

    path('add_car/', views.add_car, name='add_car'),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('add_walkin/', views.add_walkin, name='add_walkin'),
    path('add_exchange/', views.add_exchange, name='add_exchange'),
    path('add_payments/', views.add_payments, name='add_payments'),
    path('add_orders/', views.add_orders, name='add_orders'),


    path('car/<int:pk>/update', views.CarUpdateView.as_view(), name="car_update"),
    path('customer/<int:pk>/update', views.CustomerUpdateView.as_view(), name="customer_update"),
    path('walkin/<int:pk>/update', views.WalkinUpdateView.as_view(), name="walkin_update"),
    path('exchange_vehicle/<int:pk>/update', views.ExchangeUpdateView.as_view(), name="exchange_update"),
    path('payment/<int:pk>/update', views.PaymentUpdateView.as_view(), name="payment_update"),
    path('order/<int:pk>/update', views.OrderUpdateView.as_view(), name="order_update"),

    path('car/<int:pk>/delete', views.CarDeleteView.as_view(), name="car_delete"),
    path('customer/<int:pk>/delete', views.CustomerDeleteView.as_view(), name="customer_delete"),
    path('walkin/<int:pk>/delete', views.WalkInDeleteView.as_view(), name="walkin_delete"),
    path('exchange_vehicle/<int:pk>/delete', views.ExchangeVehicleDeleteView.as_view(), name="exchange_delete"),
    path('payment/<int:pk>/delete', views.PaymentDeleteView.as_view(), name="payment_delete"),
    path('order/<int:pk>/delete', views.OrderDeleteView.as_view(), name="order_delete"),
    path("order_search/", views.order_search, name="order_search"),   
    path("exchange_search/", views.exchange_search, name="exchange_search"),   
    path("payment_search/", views.payment_search, name="payment_search"),   
    path("walkin_search/", views.walkin_search, name="walkin_search"),   
    path("customer_search/", views.customer_search, name="customer_search"),   






]
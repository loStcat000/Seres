from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.

class Car(models.Model):
    car_name = models.CharField(max_length=100) 
    car_model = models.CharField(max_length=100, default = 'Full')  

    def __str__(self):
        return f'{self.car_name} - {self.car_model}' 
        
    
class CarColor(models.Model):
    car_color = models.CharField(max_length=100) 
        
    def __str__(self):
        return f'{self.car_color}' 


class Customer(models.Model):
    customer_firstname = models.CharField(max_length=100)
    customer_lastname = models.CharField(max_length=100)
    customer_contact = models.CharField(max_length=100)
    active = models.BooleanField(default=True)


    def __str__(self):
        return f'{self.customer_firstname} {self.customer_lastname}'
    


class WalkIn(models.Model):
    walkin_firstname = models.CharField(max_length=100)
    walkin_lastname = models.CharField(max_length=100)
    walkin_contact = models.CharField(max_length=100)
    purpose_of_visit = models.TextField()
    outcome_of_visit = models.TextField()
    interest_level = models.CharField(max_length=250)
    remarks = models.TextField()
    test_drive = models.BooleanField()
    date_of_walkin = models.DateField()

    def __str__(self):
        return f'{self.walkin_firstname} {self.walkin_lastname}'
    

class BookingType(models.Model):
    booking_type = models.CharField(max_length=100)
   
    def __str__(self):
        return f'{self.booking_type}'

class BookingSource(models.Model):
    booking_source = models.CharField(max_length=100)
   
    def __str__(self):
        return f'{self.booking_source}'



class PaymentType(models.Model):
    payment_type = models.CharField(max_length=100)
   
    def __str__(self):
        return f'{self.payment_type}'

class Payment(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    payment_method = models.ForeignKey('PaymentType', on_delete=models.CASCADE)
    do = models.CharField(max_length=100)
    quotation = models.CharField(max_length=100)
    remarks = models.TextField()

    def __str__(self):
        return f'{self.customer} - {self.payment_method}'
    


class ExchangeVehicle(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    vehicle_name = models.CharField(max_length=250)
    kiloMeters_run = models.IntegerField(default=1)
    vehicle_made_year = models.CharField(max_length=100)
    license_plate = models.CharField(max_length=100, unique='True')
    vehicle_color = models.CharField(max_length=100)
    customer_estimated_value = models.IntegerField(default=1)
    actual_value = models.IntegerField(default=1)
    exchange_status = models.CharField(max_length=150) 

    def __str__(self):
        return f'{self.vehicle_name}'
    
class Orders(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    walkin_customer = models.ForeignKey('WalkIn', on_delete=models.CASCADE, null=True, blank=True)
    payment = models.ForeignKey('PaymentType', on_delete=models.CASCADE)
    car = models.ForeignKey('Car', on_delete=models.CASCADE, null=True) 
    car_color = models.ForeignKey('CarColor', on_delete=models.CASCADE, null=True) 
    booking = models.ForeignKey('BookingType', on_delete=models.CASCADE)
    date_of_order = models.DateField()
    prebooking_amount = models.IntegerField(default=0, validators=[
        MinValueValidator(0)], null=True, blank=True)
    booking_amount = models.IntegerField(default=0, validators=[
        MinValueValidator(0)], null=True, blank=True)
    booking_source = models.ForeignKey('BookingSource', on_delete=models.CASCADE)
    selling_price = models.IntegerField(default=1)
    total_amount_paid = models.IntegerField(default=1)
    remaining_payment= models.IntegerField(default=1)
    remarks = models.TextField(null=True, blank=True)
    cancelled = models.BooleanField()
    reason_of_cancel = models.TextField(null=True, blank=True) 
    delivery = models.BooleanField(null=True, blank=True)
    date_of_delivery = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.customer} - {self.car}'

    def save(self, *args, **kwargs):
        # Deactivate the associated customer
        self.customer.active = False
        self.customer.save()
        super(Orders, self).save(*args, **kwargs)



   



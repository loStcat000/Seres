from django import forms
from .models import *
from django.forms import ModelForm


class CarForm(ModelForm):
	class Meta:
			model = Car
			fields = ("car_name", "car_model" )
			labels = {
				'car_name':'Car Name', 
				'car_model':'Car Model', 

			}
			widgets = {
				'car_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Car Name'}),
				'car_model': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Car Model'}),

            }
	
class CarColorForm(ModelForm):
	class Meta:
			model = CarColor
			fields = ("car_color",)
			labels = {
				'car_color':'Car Color', 
			}
			widgets = {
				'car_color': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Car Color'}),
            }
	
	
class CustomerForm(ModelForm):
	class Meta:
			model = Customer
			fields = ("customer_firstname", "customer_lastname", 
			"customer_contact")
			labels = {
				'customer_firstname':'First Name', 
				'customer_lastname':'Last Name',
				'customer_contact':'Contact Number', 
			}
			widgets = {
				'customer_firstname': forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
				'customer_lastname': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),
				'customer_contact': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Contact Number'}),
            }

class WalkInForm(ModelForm):
	class Meta:
			model = WalkIn
			fields = ("walkin_firstname", "walkin_lastname", "walkin_contact", 
			"purpose_of_visit", "outcome_of_visit", "interest_level", "remarks", "test_drive", "date_of_walkin")
			labels = {
				'walkin_firstname':'First Name', 
				'walkin_lastname':'Last Name',
				'walkin_contact':'Contact Number', 
				'purpose_of_visit':'Purpose of Visit', 
                'outcome_of_visit':'Outcome of Visit', 
				'interest_level':'Interest Level ', 
                'remarks':'Remarks', 
                'test_drive':'Test Drive', 
				'date_of_walkin':'Date of WalkIn', 
			}
			widgets = {
				'walkin_firstname': forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
				'walkin_lastname': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),
				'walkin_contact': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Contact Number'}),
				'purpose_of_visit': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Purpose of Visit '}),
				'outcome_of_visit': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Outcome of Visit '}),
				'interest_level': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Interest Level'}),
				'remarks': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Remarks'}),
				'test_drive': forms.CheckboxInput(attrs={}),
				'date_of_walkin': forms.DateInput(attrs={}),
            }


class ExchangeVehicleForm(ModelForm):
	kiloMeters_run = forms.IntegerField(min_value=1)
	customer_estimated_value = forms.IntegerField(min_value=1)
	actual_value = forms.IntegerField(min_value=1)


	class Meta:
			model = ExchangeVehicle
			fields = ("customer", "vehicle_name", "kiloMeters_run", 
			"vehicle_made_year", "license_plate", "vehicle_color", "customer_estimated_value", "actual_value", "exchange_status")
			labels = {
				'customer':'Customer Name', 
				'vehicle_name':'Vehicle Name',
				'kiloMeters_run':'KiloMeters Run', 
				'vehicle_made_year':'Vehicle Made Year', 
                'license_plate':'License Plate', 
				'vehicle_color':'Vehicle Color ', 
                'customer_estimated_value':'Customer Estimated Value', 
                'actual_value':'Actual Value', 
				'exchange_status':'Exchange Status', 
			}
			widgets = {
				'customer': forms.Select(attrs={}),
				'vehicle_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Vehicle Name'}),
				'kiloMeters_run': forms.NumberInput(attrs={'class':'form-control',}),
				'vehicle_made_year': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Vehicle Made Year '}),
				'license_plate': forms.TextInput(attrs={'class':'form-control', 'placeholder':'License Plate '}),
				'vehicle_color': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Vehicle Color'}),
				'customer_estimated_value': forms.NumberInput(attrs={'class':'form-control',}),
				'actual_value': forms.NumberInput(attrs={'class':'form-control',}),
				'exchange_status': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Exchange Status'}),
            }
	
class PaymentForm(ModelForm):
	class Meta:
			model = Payment
			fields = ("customer", "payment_method", "do", "quotation", "remarks")
			labels = {
				'customer':'Customer', 
				'payment_method':'Payment Method',
				'do':'d.o', 
				'quotation':'Quotation',
				'remarks':'Remarks',  
			}
			widgets = {
				'customer': forms.Select(attrs={}),
				'payment_method': forms.Select(attrs={}),
				'do': forms.TextInput(attrs={'class':'form-control', 'placeholder':'d.o'}),
				'quotation': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Quotation'}),
				'remarks': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Remarks'}),
            }
		

class OrdersForm(ModelForm):
	prebooking_amount = forms.IntegerField(min_value=0, required=False)
	booking_amount = forms.IntegerField(min_value=0, required=False)
	selling_price = forms.IntegerField(min_value=0)
	total_amount_paid = forms.IntegerField(min_value=0)
	remaining_payment = forms.IntegerField(min_value=0)

	
	class Meta:
			model = Orders
			fields = ("customer", "walkin_customer", "car", "car_color", "payment", "booking", "prebooking_amount", "booking_amount", "booking_source", "date_of_order", "selling_price", 
			"total_amount_paid", "remaining_payment", "remarks", "cancelled", "reason_of_cancel")
			labels = {
				'customer':'Customer', 
				'walkin_customer':'WalkIn Customer',
				'payment':'Payment', 
				'car':'Car',
				'car_color':'Car Color',
				'booking':'Booking Status', 
				'prebooking_amount':'Pre-Booking Amount',
				'booking_amount':'Booking Amount',  
				'booking_source':'Booking Source', 
				'date_of_order':'Date of Order',
				'selling_price':'Selling Price',  
				'total_amount_paid':'Total Amount Paid',  
				'remaining_payment':'Remaining Payment',  
				'remarks':'Remarks',  
				'cancelled':'Cancelled',  
				'reason_of_cancel':'Reason Of Cancel',  

			}
			widgets = {
				'customer': forms.Select(attrs={}),
				'walkin_customer': forms.Select(attrs={}),
				'payment': forms.Select(attrs={}),
				'car': forms.Select(attrs={}),
				'car_color': forms.Select(attrs={}),
				'booking': forms.Select(attrs={}),
				'prebooking_amount': forms.NumberInput(attrs={'class':'form-control'}),
				'booking_amount': forms.NumberInput(attrs={'class':'form-control'}),
            	'booking_source': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Booking Source'}),
				'date_of_order': forms.DateInput(attrs={'class':'form-control'}),
				'selling_price': forms.NumberInput(attrs={'class':'form-control'}),
            	'total_amount_paid': forms.NumberInput(attrs={'class':'form-control'}),
            	'remaining_payment': forms.NumberInput(attrs={'class':'form-control'}),
            	'remarks': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Remarks'}),
            	'cancelled': forms.CheckboxInput(attrs={}),
            	'reason_of_cancel': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Reason of Cancel'}),

            }

	def clean(self):
			cleaned_data = super().clean()
			prebooking_amount = cleaned_data.get('prebooking_amount', 0)
			booking_amount = cleaned_data.get('booking_amount', 0)

			# Calculate the total_amount_paid based on prebooking_amount and booking_amount
			total_amount_paid = prebooking_amount + booking_amount
			cleaned_data['total_amount_paid'] = total_amount_paid

			return cleaned_data
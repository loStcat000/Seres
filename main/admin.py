from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Car)

admin.site.register(models.CarColor)


admin.site.register(models.Customer)

admin.site.register(models.WalkIn)


admin.site.register(models.Payment)

admin.site.register(models.Orders)

admin.site.register(models.BookingType)

admin.site.register(models.BookingSource)

admin.site.register(models.PaymentType)


admin.site.register(models.ExchangeVehicle)



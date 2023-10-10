# Generated by Django 3.2.12 on 2023-10-09 11:48

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookingType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=250, unique=True)),
                ('car_model', models.CharField(max_length=100, unique=True)),
                ('car_variant', models.CharField(max_length=100)),
                ('car_color', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_firstname', models.CharField(max_length=100)),
                ('customer_lastname', models.CharField(max_length=100)),
                ('customer_contact', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WalkIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('walkin_firstname', models.CharField(max_length=100)),
                ('walkin_lastname', models.CharField(max_length=100)),
                ('walkin_contact', models.CharField(max_length=100)),
                ('purpose_of_visit', models.TextField()),
                ('outcome_of_visit', models.TextField()),
                ('interest_level', models.CharField(max_length=250)),
                ('remarks', models.TextField()),
                ('test_drive', models.BooleanField()),
                ('date_of_walkin', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(max_length=250)),
                ('do', models.CharField(max_length=100)),
                ('quotation', models.CharField(max_length=100)),
                ('remarks', models.TextField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment', models.CharField(max_length=250)),
                ('car_variant', models.CharField(max_length=250)),
                ('date_of_order', models.DateField()),
                ('selling_price', models.IntegerField(default=1)),
                ('total_amount_paid', models.IntegerField(default=1)),
                ('remaining_payment', models.IntegerField(default=1)),
                ('remarks', models.TextField()),
                ('cancelled', models.BooleanField()),
                ('reason_of_cancel', models.TextField(blank=True, null=True)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.bookingtype')),
                ('car_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders_car_model', to='main.car', to_field='car_model')),
                ('car_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders_car_name', to='main.car', to_field='car_name')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.customer')),
            ],
        ),
        migrations.CreateModel(
            name='ExchangeVehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_name', models.CharField(max_length=250)),
                ('kiloMeters_run', models.IntegerField(default=1)),
                ('vehicle_made_year', models.CharField(max_length=100)),
                ('license_plate', models.CharField(max_length=100)),
                ('vehicle_color', models.CharField(max_length=100)),
                ('customer_estimated_value', models.IntegerField(default=1)),
                ('actual_value', models.IntegerField(default=1)),
                ('exchange_status', models.CharField(max_length=150)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prebooking_amount', models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('booking_amount', models.IntegerField(blank=True, default=1, null=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('booking_source', models.CharField(max_length=150)),
                ('booking_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.bookingtype')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.customer')),
                ('walkin_customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.walkin')),
            ],
        ),
    ]
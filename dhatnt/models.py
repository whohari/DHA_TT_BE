from django.db import models
from django.utils.translation import gettext_lazy as _
import random
from datetime import timedelta
from django.utils.timezone import now

# Create your models here.

class UserData(models.Model):
    username= models.CharField(max_length=50)
    email = models.EmailField(_('email address'), unique=True)
    password = models.CharField(max_length=50)

    def _str_(self):
        return self.username

class VehicleType(models.Model):
    typename = models.CharField(max_length=255)

    def _str_(self):
        return self.typename

class Vehicle(models.Model):
    name = models.CharField(max_length=255)
    type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    capacity = models.IntegerField()
    price_per_km = models.DecimalField(max_digits=10, decimal_places=2)
    AVAILABILITY_CHOICES = [
        ('available', 'Available'),
        ('booked', 'Booked'),
    ]
    availability_status = models.CharField(
        max_length=20,
        choices=AVAILABILITY_CHOICES,
        default='available',
    )
    description = models.TextField(blank=True, null=True)

    def _str_(self):
        return self.name

class OneWayTrip(models.Model):
    username =models.ForeignKey(UserData, on_delete=models.CASCADE, null=True)
    pickupLocation = models.CharField()
    dropLocation = models.CharField()
    distance = models.DecimalField(max_digits=10, decimal_places=2)
    pickupDate = models.DateField()
    pickupTime = models.TimeField()
    vehicleType = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    TRIPTYPECHOICES = [
        ('oneway', 'oneway'),
        ('roundtrip', 'roundtrip'),
        ('rental', 'rental'),
    ]
    tripType = models.CharField(max_length=20, choices=TRIPTYPECHOICES, default='')
    totalFare = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)


    def __str__(self):
        return f"One-way trip from {self.pickupLocation} to {self.dropLocation} on {self.pickupDate} at {self.pickupTime}"

class RoundTrip(models.Model):
    username = models.ForeignKey(UserData, on_delete=models.CASCADE, null=True)
    pickupLocation = models.CharField()
    dropLocation = models.CharField()
    distance = models.DecimalField(max_digits=10, decimal_places=2)
    pickupDate = models.DateField()
    pickupTime = models.TimeField()
    returnDate = models.DateField()
    vehicleType = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    TRIPTYPECHOICES = [
        ('oneway', 'oneway'),
        ('roundtrip', 'roundtrip'),
        ('rental', 'rental'),
    ]
    tripType = models.CharField(max_length=20, choices=TRIPTYPECHOICES, default='')
    totalFare = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)


    def __str__(self):
        return f"Round trip from {self.pickupLocation} to {self.dropLocation} on {self.pickupDate} at {self.pickupTime}, returning on {self.returnDate}"

class Rental(models.Model):
    username = models.ForeignKey(UserData, on_delete=models.CASCADE, null=True)
    pickupLocation = models.CharField()
    pickupDate = models.DateField()
    pickupTime = models.TimeField()
    rentalDuration = models.IntegerField()
    vehicleType = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    TRIPTYPECHOICES = [
    ('oneway', 'oneway'),
    ('roundtrip', 'roundtrip'),
    ('rental', 'rental'),
    ]
    tripType = models.CharField(max_length=20, choices=TRIPTYPECHOICES, default='')

    def __str__(self):
        return f"Rental from {self.pickupLocation} on {self.pickupDate} at {self.pickupTime} for {self.rentalDuration} days"


class OTP(models.Model):
    email = models.EmailField(unique=True)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)  # This is timezone-aware

    def generate_otp(self):
        self.code = str(random.randint(100000, 999999))
        self.created_at = now()
        self.save()

    def is_expired(self):
        return now() > self.created_at + timedelta(minutes=5)

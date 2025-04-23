from django.db import models
from django.utils.translation import gettext_lazy as _
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

    def __str__(self):
        return f"One-way trip from {self.pickupLocation} to {self.dropLocation} on {self.pickupDate} at {self.pickupTime}"

class RoundTrip(models.Model):
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

    def __str__(self):
        return f"Round trip from {self.pickupLocation} to {self.dropLocation} on {self.pickupDate} at {self.pickupTime}, returning on {self.returnDate}"

class Rental(models.Model):
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
        return f"Rental from {self.pickupLocation} to {self.dropLocation} on {self.pickupDate} at {self.pickupTime} for {self.rentalDuration} days"



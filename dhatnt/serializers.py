from rest_framework import serializers
from dhatnt.models import UserData, VehicleType, Vehicle, OneWayTrip, RoundTrip, Rental, OTP

class UsersSerializer(serializers.ModelSerializer):
   class Meta:
        model = UserData
        fields = '__all__'

class VehicleTypeSerializer(serializers.ModelSerializer):
   class Meta:
        model = VehicleType
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
   class Meta:
        model = Vehicle
        fields = '__all__'

class OneWayTripSerializer(serializers.ModelSerializer):
   class Meta:
        model = OneWayTrip
        fields = '__all__'

class RoundTripSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoundTrip
        fields = '__all__'

class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = '__all__'

class OTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTP
        fields = ['email', 'code']

from rest_framework import permissions, viewsets
from dhatnt.models import UserData, VehicleType, Vehicle, OneWayTrip, RoundTrip, Rental
from dhatnt.serializers import UsersSerializer, VehicleTypeSerializer, VehicleSerializer, OneWayTripSerializer, RoundTripSerializer, RentalSerializer

# Create your views here.
class UserViewset(viewsets.ModelViewSet):
    serializer_class = UsersSerializer
    queryset = UserData.objects.all()
    lookup_field = 'id'
    permission_classes = (
        permissions.AllowAny,
    )

class VehicleTypeViewset(viewsets.ModelViewSet):
    serializer_class = VehicleTypeSerializer
    queryset = VehicleType.objects.all()
    lookup_field = 'id'
    permission_classes = (
        permissions.AllowAny,
    )

class VehicleViewset(viewsets.ModelViewSet):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()
    lookup_field = 'id'
    permission_classes = (
        permissions.AllowAny,
    )

class OneWayTripViewset(viewsets.ModelViewSet):
    serializer_class = OneWayTripSerializer
    queryset = OneWayTrip.objects.all()
    lookup_field = 'id'
    permission_classes = (
        permissions.AllowAny,
    )

    def get_queryset(self):
        queryset = OneWayTrip.objects.all()
        user_id = self.request.query_params.get('username_id')
        if user_id is not None:
            queryset = queryset.filter(username_id=user_id)
        return queryset

class RoundTripViewset(viewsets.ModelViewSet):
    serializer_class = RoundTripSerializer
    queryset = RoundTrip.objects.all()
    lookup_field = 'id'
    permission_classes = (
        permissions.AllowAny,
    )

    def get_queryset(self):
        queryset = RoundTrip.objects.all()
        user_id = self.request.query_params.get('username_id')
        if user_id is not None:
            queryset = queryset.filter(username_id=user_id)
        return queryset

class RentalViewset(viewsets.ModelViewSet):
    serializer_class = RentalSerializer
    queryset = Rental.objects.all()
    lookup_field = 'id'
    permission_classes = (
        permissions.AllowAny,
    )

    def get_queryset(self):
        queryset = Rental.objects.all()
        user_id = self.request.query_params.get('username_id')
        if user_id is not None:
            queryset = queryset.filter(username_id=user_id)
        return queryset


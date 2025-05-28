from rest_framework import permissions, viewsets
from dhatnt.models import UserData, VehicleType, Vehicle, OneWayTrip, RoundTrip, Rental
from dhatnt.serializers import UsersSerializer, VehicleTypeSerializer, VehicleSerializer, OneWayTripSerializer, RoundTripSerializer, RentalSerializer
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import OTP
import logging

# Create your views here.
class UserViewset(viewsets.ModelViewSet):
    serializer_class = UsersSerializer
    queryset = UserData.objects.all()
    lookup_field = 'id'
    permission_classes = (
        permissions.AllowAny,
    )

    def get_queryset(self):
        return UserData.objects.filter(id=self.request.user.id)  # Adjust based on your auth system

    def get_queryset(self):
        email = self.request.query_params.get("email")
        if email:
            return UserData.objects.filter(email=email)
        return UserData.objects.all()

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

class SendOTP(APIView):
    def post(self, request):
        email = request.data.get('email')

        if not email:
            return Response({'error': 'Email is required'}, status=400)

        otp_instance, _ = OTP.objects.get_or_create(email=email)
        otp_instance.generate_otp()

        send_mail(
            'Your OTP Code',
            f'Your OTP code is {otp_instance.code}. It will expire in 5 minutes.',
            'henry7ludwik@gmail.com',
            [email],
            fail_silently=False,
        )

        return Response({'message': 'OTP sent successfully'})


logger = logging.getLogger(__name__)
class VerifyOTP(APIView):
    def post(self, request):
        try:
            email = request.data.get('email')
            otp_code = request.data.get('code')
            if not email or not otp_code:
                return Response({'error': 'Email and OTP code are required'}, status=400)
            otp_instance = OTP.objects.get(email=email, code=otp_code)
            if otp_instance.is_expired():
                return Response({'error': 'OTP has expired'}, status=400)
            return Response({'message': 'OTP verified successfully'}, status=200)
        except OTP.DoesNotExist:
            return Response({'error': 'Invalid OTP'}, status=400)
        except Exception as e:
            logger.error(f"Unexpected Error: {e}")
            return Response({'error': f'Server error: {e}'}, status=500)

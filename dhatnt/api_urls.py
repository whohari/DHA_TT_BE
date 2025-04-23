from django.urls import path, re_path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('user', UserViewset)
router.register('vehicletype', VehicleTypeViewset)
router.register('vehicle', VehicleViewset)
router.register('onewaytrip', OneWayTripViewset)
router.register('roundtrip', RoundTripViewset)
router.register('rental', RentalViewset)
urlpatterns = [
    path('', include(router.urls))
]

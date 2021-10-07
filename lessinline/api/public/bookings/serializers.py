from rest_framework import serializers
from lessinline.bookings.models import Booking
from lessinline.services.models import Service, Slot


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'price']


class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields = ['start_time', 'end_time']


class BookingSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(read_only=True)
    slot = SlotSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = ['id', 'service', 'slot', 'status', 'created_at']

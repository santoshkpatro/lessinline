from rest_framework import serializers
from lessinline.services.models import Service, Slot


class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields = ['id', 'start_time', 'end_time', 'capacity', 'is_open']


class ServiceSerializer(serializers.ModelSerializer):
    slots = SlotSerializer(read_only=True, many=True)

    class Meta:
        model = Service
        fields = ['id', 'name', 'description', 'price', 'advance_booking_days', 'slots']

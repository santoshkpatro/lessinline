from rest_framework import serializers
from lessinline.services.models import Service, Slot


class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields = ['id', 'start_time', 'end_time', 'is_open']


class ServiceSerializer(serializers.ModelSerializer):
    slots = SlotSerializer(many=True, required=False)
    add_slots = SlotSerializer(many=True, write_only=True, required=False)

    class Meta:
        model = Service
        fields = ['id', 'name', 'description', 'price', 'advance_booking_days', 'slots', 'add_slots']

    def create(self, validated_data):
        slots = validated_data.pop('slots')
        service = super().create(validated_data)
        for slot in slots:
            serializer = SlotSerializer(data=slot)
            if serializer.is_valid():
                serializer.save(service=service)
        return service

    def update(self, instance, validated_data):
        slots = validated_data.pop('slots')
        service = super().update(instance, validated_data)
        for slot in slots:
            serializer = SlotSerializer(data=slot)
            if serializer.is_valid():
                serializer.save(service=service)
        return service

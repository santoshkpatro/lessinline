from rest_framework import serializers
from lessinline.bookings.models import Booking, Slot
from lessinline.accounts.models import User


class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields = ['id', 'start_time', 'end_time']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'avatar']


class BookingSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    slot = SlotSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = ['id', 'user', 'slot', 'status']

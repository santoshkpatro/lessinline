from django.http import Http404
from rest_framework import generics, permissions
from lessinline.bookings.models import Booking
from lessinline.services.models import Slot
from .serializers import BookingSerializer
from .permissions import IsBookedUser


class BookingList(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        if not 'slot_id' in self.request.query_params:
            raise Http404
        slot_id = self.request.query_params['slot_id']
        try:
            slot = Slot.objects.get(id=slot_id)
            return serializer.save(user=self.request.user, slot=slot, service=slot.service)
        except Slot.DoesNotExist:
            raise Http404


class BookingDetail(generics.RetrieveAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsBookedUser]

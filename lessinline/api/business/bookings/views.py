from rest_framework import generics, permissions
from lessinline.api.business.mixins import ServiceLookupMixins
from lessinline.bookings.models import Booking
from .serializers import BookingSerializer


class BookingsList(ServiceLookupMixins, generics.ListAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        bookings = super().get_queryset()
        return bookings.filter(service=self.service)

    def list(self, request, *args, **kwargs):
        self.get_service()
        return super().list(request, *args, **kwargs)

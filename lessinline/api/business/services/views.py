from rest_framework import generics, permissions
from lessinline.business.models import Business
from lessinline.services.models import Service, Slot
from lessinline.api.business.mixins import BusinessLookupMixins
from .serializers import ServiceSerializer
from .permissions import IsServiceOwner


class ServiceList(BusinessLookupMixins, generics.ListCreateAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(business=self.business)

    def list(self, request, *args, **kwargs):
        self.get_business()
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        self.get_business()
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        return serializer.save(business=self.business)


class ServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsServiceOwner]

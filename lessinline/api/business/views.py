from rest_framework import generics, permissions
from lessinline.api.business.serializers import BusinessSerializer, BusinessStaffSerializer
from lessinline.business.models import Business, BusinessStaff
from .permissions import IsOwner, IsBusinessOwner


class BusinessList(generics.ListCreateAPIView):
    serializer_class = BusinessSerializer
    queryset = Business.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(owner=self.request.user)

    def perform_create(self, serializer):
        business = serializer.save(owner=self.request.user)
        return business


class BusinessDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BusinessSerializer
    queryset = Business.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwner]


class BusinessStaffDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BusinessStaffSerializer
    queryset = BusinessStaff.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsBusinessOwner]

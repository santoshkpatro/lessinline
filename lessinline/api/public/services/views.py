from rest_framework import generics
from .serializers import ServiceSerializer
from lessinline.services.models import Service


class ServiceDetail(generics.RetrieveAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()

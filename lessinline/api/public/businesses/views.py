from rest_framework import generics
from lessinline.business.models import Business
from .serializers import BusinessSerializer


class BusinessList(generics.ListAPIView):
    serializer_class = BusinessSerializer
    queryset = Business.objects.all()


class BusinessDetail(generics.RetrieveAPIView):
    serializer_class = BusinessSerializer
    queryset = Business.objects.all()

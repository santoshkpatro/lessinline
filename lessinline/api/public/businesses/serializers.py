from rest_framework import serializers
from lessinline.business.models import Business, Category
from lessinline.services.models import Service


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'description', 'price']


class BusinessSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    services = ServiceSerializer(read_only=True, many=True)

    class Meta:
        model = Business
        fields = ['id', 'name', 'description', 'category', 'services']

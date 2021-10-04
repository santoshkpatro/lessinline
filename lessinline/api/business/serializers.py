from rest_framework import serializers
from lessinline.business.models import Business, Category, BusinessStaff
from lessinline.accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'phone', 'avatar']


class StaffSerializer(serializers.ModelSerializer):
    staff = UserSerializer(read_only=True)

    class Meta:
        model = BusinessStaff
        fields = ['id', 'staff', 'created_at']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class BusinessSerializer(serializers.ModelSerializer):
    category_id = serializers.UUIDField(write_only=True, required=False)
    category = CategorySerializer(required=False)
    staffs = StaffSerializer(read_only=True, many=True)

    class Meta:
        model = Business
        fields = ['id', 'name', 'category_id', 'category', 'description', 'staffs']

    def create(self, validated_data):
        category_id = validated_data.pop('category_id')
        business = super().create(validated_data)
        try:
            category = Category.objects.get(id=category_id)
            business.category = category
            business.save()
        except Category.DoesNotExist:
            raise serializers.ValidationError('Category not found')
        return business

    def update(self, instance, validated_data):
        if 'category_id' in validated_data:
            category_id = validated_data.pop('category_id')
            try:
                category = Category.objects.get(id=category_id)
                business = super().update(instance, validated_data)
                business.category = category
                business.save()
            except Category.DoesNotExist:
                raise serializers.ValidationError('Category not found')
        return super().update(instance, validated_data)

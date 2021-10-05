from rest_framework import serializers
from lessinline.business.models import Business, Category, BusinessStaff
from lessinline.accounts.models import User


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'phone', 'avatar']


class BusinessStaffSerializer(serializers.ModelSerializer):
    staff = StaffSerializer(read_only=True)

    class Meta:
        model = BusinessStaff
        fields = ['id', 'staff', 'is_active', 'created_at']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class BusinessSerializer(serializers.ModelSerializer):
    category_id = serializers.UUIDField(write_only=True, required=False)
    category = CategorySerializer(required=False)
    business_staffs = BusinessStaffSerializer(read_only=True, many=True)
    new_staffs = serializers.ListField(required=False)
    add_staffs = serializers.ListField(required=False)

    class Meta:
        model = Business
        fields = ['id', 'name', 'category_id', 'category', 'description', 'business_staffs', 'add_staffs', 'new_staffs']

    def create(self, validated_data):
        category_id = validated_data.pop('category_id')
        new_staffs = []
        if 'new_staffs' in validated_data:
            new_staffs = validated_data.pop('new_staffs')
        business = super().create(validated_data)
        try:
            category = Category.objects.get(id=category_id)
            business.category = category
            business.save()
        except Category.DoesNotExist:
            raise serializers.ValidationError('Category not found')

        if len(new_staffs) != 0:
            for staff_email in new_staffs:
                try:
                    user = User.active_users.get(email=staff_email)
                    business.staffs.add(user)
                except User.DoesNotExist:
                    pass
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

        if 'add_staffs' in validated_data:
            staffs = validated_data.pop('add_staffs')
            for staff_email in staffs:
                try:
                    user = User.active_users.get(email=staff_email)
                    instance.staffs.add(user)
                except:
                    pass
        return super().update(instance, validated_data)

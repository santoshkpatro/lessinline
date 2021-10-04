from rest_framework import serializers
from lessinline.accounts.models import User
from rest_framework_simplejwt.tokens import AccessToken


class UserLoginSerializer(serializers.ModelSerializer):
    access_token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'gender',
                  'date_of_birth', 'phone', 'last_login', 'avatar', 'access_token']

    def get_access_token(self, obj) -> str:
        return str(AccessToken.for_user(obj))


class UserRegisterSerializer(serializers.ModelSerializer):
    access_token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password',
                  'confirm_password', 'date_of_birth', 'gender', 'phone', 'access_token']

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError('password and confirm password is not same!')
        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop('password')
        confirm_password = validated_data.pop('confirm_password')

        user = super().create(validated_data)
        user.set_password(password)
        return user

    def get_access_token(self, obj) -> str:
        return str(AccessToken.for_user(obj))


class UserProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(read_only=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone', 'avatar', 'gender', 'date_of_birth']

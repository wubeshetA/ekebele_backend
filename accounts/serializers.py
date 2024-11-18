# accounts/serializers.py

from djoser.serializers import UserCreateSerializer, UserSerializer
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers


User = get_user_model()


class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'first_name', 'last_name',
                  'phone_number', 'email', 'password', 'nid')

        extra_kwargs = {
            # Ensure it's not requested
            'verification_code': {'write_only': True},
        }


class CustomUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = User
        fields = ('id', 'first_name', 'last_name',
                  'phone_number', 'email', 'is_staff', 'nid')
        extra_kwargs = {
            # Hide it from being readable
            'verification_code': {'write_only': True},
        }


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        # Get the default token from the parent class
        token = super().get_token(user)

        # Add custom claims
        token['is_staff'] = user.is_staff

        return token


class VerifyEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
    verification_code = serializers.CharField(max_length=6)


class UserProfileSerializer(serializers.ModelSerializer):
    user_type = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name',
                  'user_type', 'nid', 'phone_number']

    def get_user_type(self, obj):
        return 'staff' if obj.is_staff else 'public'

from django.contrib.auth.password_validation import validate_password as check_password
from rest_framework import serializers

from .models import User
from .services import create_user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'created_at')


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "email",
            "username",
            "password",
        ]

    def create(self, validated_data):
        return create_user(**validated_data)

    def validate_password(self, value):
        check_password(value)
        return value

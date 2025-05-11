from django.core.exceptions import ValidationError
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core.validators import EmailValidator

from ..models import CustomUser


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
    )
    email = serializers.EmailField(
        required=True,
        validators=[EmailValidator(message='Enter a valid email address.')],
    )

    bio = serializers.CharField(
        required=False,
        allow_blank=True,
    )

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password', 'password2', 'bio']

    def validate_email(self, value):
        if CustomUser.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value.lower()


    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {'password': 'Passwords must match'}
            )

        return attrs

    def create(self, validated_data):
        validated_data.pop('password2', None)

        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            bio=validated_data['bio'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

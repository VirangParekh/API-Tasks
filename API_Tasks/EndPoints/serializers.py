from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import UserProfile
from .models import User
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import update_last_login


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields=[
            'first_name',
            'last_name',
            'phone_number',
            'age',
            'gender',
        ]

JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

class UserRegistrationSerializer(serializers.ModelSerializer):

    profile = UserSerializer(required=False)

    class Meta:
        model = User
        fields = ('email', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create_user(**validated_data)
        UserProfile.objects.create(
            user=user,
            first_name=profile_data['first_name'],
            last_name=profile_data['last_name'],
            phone_number=profile_data['phone_number'],
            age=profile_data['age'],
            gender=profile_data['gender']
        )
        login_user=authenticate(username=user.get_username(), password=user.password)
        payload=JWT_PAYLOAD_HANDLER(login_user)
        jwt_token=JWT_PAYLOAD_HANDLER(payload)
        update_last_login(None, login_user)

        return {
            'email': login_user.get_username,
            'token': jwt_token,
        }


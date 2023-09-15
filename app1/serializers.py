from rest_framework import serializers
from .models import Userdata

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userdata
        fields = ('email', 'password', 'phone_number', 'profile_image', 'full_name', 'dob')

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class UserfilterSerializer(serializers.Serializer):
    full_name = serializers.CharField()

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userdata
        fields = '__all__'
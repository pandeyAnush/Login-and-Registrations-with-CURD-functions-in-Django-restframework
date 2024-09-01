from rest_framework import serializers
from accounts.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2', 'tc']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')

        if password != password2:
            raise serializers.ValidationError("Passwords don't match")

        return attrs          

    def create(self, validated_data):
        # Remove password2 from validated_data before creating the user
        validated_data.pop('password2')

        # Create and return the user using the create_user method from UserManager
        return User.objects.create_user(**validated_data)

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields = ['email', 'password']
        

"""This is for car""" 

from rest_framework import serializers
from .models import *


class CarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields =('id','model','name')


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = '__all__'
        
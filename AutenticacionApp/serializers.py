from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()  
    password = serializers.CharField(write_only=True)  
    class Meta:
        model = User
        fields = ['email', 'password']  



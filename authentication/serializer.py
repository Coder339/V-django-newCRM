from rest_framework import serializers
from .models import User,EmployeeProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = '__all__'


class EmployeeProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model  = EmployeeProfile
        fields = '__all__'


class LoginSerializer(serializers.Serializer):
    username    =   serializers.CharField(max_length=120)
    password    =   serializers.CharField(max_length=120)
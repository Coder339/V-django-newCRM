from rest_framework import serializers
from .models import User,EmployeeAccount

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = '__all__'


class EmployeeAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model  = EmployeeAccount
        fields = '__all__'


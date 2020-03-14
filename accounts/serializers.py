from rest_framework import serializers
from .models import UserCustomerAccount,UserEmployeeAccount

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model  = UserEmployeeAccount
        fields = '__all__'


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model  = UserCustomerAccount
        fields = '__all__' 
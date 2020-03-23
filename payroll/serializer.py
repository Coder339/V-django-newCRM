from rest_framework import serializers
from .models import UserPaymentReceipt,EmployeePackage,UserEmployeePaymentBill

class UserPaymentReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model  = UserPaymentReceipt
        fields = '__all__'


class EmployeePackageSerializer(serializers.ModelSerializer):
    class Meta:
        model  = EmployeePackage
        fields = '__all__'


class UserEmployeePaymentBillSerializer(serializers.ModelSerializer):
    class Meta:
        model  = UserEmployeePaymentBill
        fields = '__all__'
from rest_framework import serializers
from .models import Department,StaffRole

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Department
        fields = '__all__'


# class StaffProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model  = StaffProfile
#         fields = '__all__'


class StaffRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model  = StaffRole
        fields = '__all__'
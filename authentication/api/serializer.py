from rest_framework import serializers
from authentication.models import *
from django.contrib.auth import authenticate,login,get_user_model
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from .utils import jwt_response_payload_handler
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

# User = get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model  = Company
        fields = '__all__'


class EmployeeProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model  = EmployeeProfile
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Customer
        fields = '__all__'


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Vendor
        fields = '__all__'





# User = get_user_model()

                                                    ########### register an user
class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
    token     = serializers.SerializerMethodField(read_only = True)
    message   = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = User
        fields = ['username',
                  'email',
                  'password',
                  'password2',
                  'token',
                  'message']

        extra_kwargs = {
            'password':{'write_only':True}
        }
    

    def get_message(self,obj):
        return 'successfully registered'

    def get_token(self,obj):
        user = obj
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        print(token)
        return token




    def create(self,validated_data):       
        user = User(
            email = self.validated_data['email'],
            username = self.validated_data['username'],
        )
        password = self.validated_data['password'],
        password2 = self.validated_data['password2'],
        
        if password != password2:
            raise serializers.ValidationError({'password':'password must match'})
        user.set_password(validated_data['password'])
        user.is_active = True
        user.save()
        return user



  

    

class LoginSerializer(serializers.ModelSerializer):

    username    = serializers.CharField(max_length=120)
    password    = serializers.CharField(style={'input_type':'password'},write_only=True)
    token       = serializers.SerializerMethodField(read_only = True)
    message     = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = User
        fields = ['username',
                  'password',
                  'token',
                  'message']

        extra_kwargs = {
            'password':{'write_only':True}
        }
    
    def get_message(self,obj):
        return 'successfully logged in'

    def get_token(self,obj):
        user = obj
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        print(token)
        return token

   
from django.shortcuts import render
from serializer import ServiceSerializer
from rest_framework import generics



class ServiceCreateAPIView(generics.CreateAPIView):
    queryset               =         Service.objects.all()
    serializers_class      =         ServiceSerializer
    permission_classes     =         []
    authentication_class   =         []

class ServiceListAPIView(generics.ListAPIView):
    queryset               =         Service.objects.all()
    serializers_class      =         ServiceSerializer
    permission_classes     =         []
    authentication_class   =         []
    
class ServiceUpdateAPIView(generics.UpdateAPIView):
    queryset               =         Service.objects.all()
    serializers_class      =         ServiceSerializer
    permission_classes     =         []
    authentication_class   =         []
    lookup_field           =         'pk'


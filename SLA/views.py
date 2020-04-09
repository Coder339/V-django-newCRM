
from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializer import *

#SLA
# class SLACreateAPIView(generics.CreateAPIView):
#     queryset               =         SLA.objects.all()
#     serializers_class      =         SLASerializer
#     permission_classes     =         []
#     authentication_class   =         []

# class SLAListAPIView(generics.ListAPIView):

#     queryset               =         SLA.objects.all()
#     serializers_class      =         SLASerializer
#     permission_classes     =         []
#     authentication_class   =         []

# class SLAUpdateAPIView(generics.UpdateAPIView):
#     queryset               =         SLA.objects.all()
#     serializers_class      =         SLASerializer
#     permission_classes     =         []
#     authentication_class   =         []
#     lookup_field           =         'pk'




def sla(request):
    return render(request,'sla/dashboard.html')



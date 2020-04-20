
from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializer import *

#ServiceLevelAgreement
# class SLACreateAPIView(generics.CreateAPIView):
#     queryset               =         ServiceLevelAgreement.objects.all()
#     serializers_class      =         SLASerializer
#     permission_classes     =         []
#     authentication_class   =         []

# class SLAListAPIView(generics.ListAPIView):

#     queryset               =         ServiceLevelAgreement.objects.all()
#     serializers_class      =         SLASerializer
#     permission_classes     =         []
#     authentication_class   =         []

# class SLAUpdateAPIView(generics.UpdateAPIView):
#     queryset               =         ServiceLevelAgreement.objects.all()
#     serializers_class      =         SLASerializer
#     permission_classes     =         []
#     authentication_class   =         []
#     lookup_field           =         'pk'




def sla(request):
    return render(request,'sla/dashboard.html')



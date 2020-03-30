
from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializer import *

#SLA
class SLACreateAPIView(generics.CreateAPIView):
    queryset               =         SLA.objects.all()
    serializers_class      =         SLASerializer
    permission_classes     =         []
    authentication_class   =         []

class SLAListAPIView(generics.ListAPIView):

    queryset               =         SLA.objects.all()
    serializers_class      =         SLASerializer
    permission_classes     =         []
    authentication_class   =         []

class SLAUpdateAPIView(generics.UpdateAPIView):
    queryset               =         SLA.objects.all()
    serializers_class      =         SLASerializer
    permission_classes     =         []
    authentication_class   =         []
    lookup_field           =         'pk'

#Escalation
# class EscalationCreateAPIView(generics.CreateAPIView):
#         queryset                 =        Escalation.objects.all()
#         serializers_class        =        EscalationSerializer
#         permission_classes       =        []
#         authentication_class     =        []
# class EscalationListAPIView(generics.ListAPIView):
#         queryset                =         Escalation.objects.all()
#         serializers_class       =         EscalationSerializer
#         permission_classes      =         []
#         authentication_class    =         []
# class EscalationUpdateAPIView(generics.UpdateAPIView):
#         queryset                =         Escalation.objects.all()
#         serializers_class       =         EscalationSerializer
#         permission_classes      =         []
#         authentication_class    =         []
#         lookup_field            =          ''



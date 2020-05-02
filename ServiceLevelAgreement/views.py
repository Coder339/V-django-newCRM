
from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializer import *

#ServiceLevelAgreement
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
    queryset               =        SLA.objects.all()
    serializers_class      =         SLASerializer
    permission_classes     =         []
    authentication_class   =         []
    lookup_field           =         'pk'


# #Record

class HistoryCreateAPIView(generics.CreateAPIView):
    queryset               =        History.objects.all()
    serializers_class      =        HistorySerializer
    permission_classes     =         []
    authentication_class   =         []

class HistoryListAPIView(generics.ListAPIView):

    queryset               =        History.objects.all()
    serializers_class      =        HistorySerializer
    permission_classes     =         []
    authentication_class   =         []

class HistoryUpdateAPIView(generics.UpdateAPIView):
    queryset               =       History.objects.all()
    serializers_class      =       HistorySerializer
    permission_classes     =         []
    authentication_class   =         []
    lookup_field           =         'pk'

#
# class RecordCreateAPIView(generics.CreateAPIView):
#     queryset               =        Record.objects.all()
#     serializers_class      =        RecordSerializer
#     permission_classes     =         []
#     authentication_class   =         []
#
# class RecordListAPIView(generics.ListAPIView):
#
#     queryset               =        Record.objects.all()
#     serializers_class      =        RecordSerializer
#     permission_classes     =         []
#     authentication_class   =         []
#
# class RecordUpdateAPIView(generics.UpdateAPIView):
#     queryset               =       Record.objects.all()
#     serializers_class      =       RecordSerializer
#     permission_classes     =         []
#     authentication_class   =         []
#     lookup_field           =         'pk'
# #
# #






#
# def sla(request):
#     return render(request,'sla/dashboard.html')



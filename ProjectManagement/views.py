from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializer import *
#from  django.core.mail import send_mail

# def index (request):
#    send_mail(
#         'followup','concall with amit'+'\nmeeting with rahul','amanpreetleanvia.com',['amanpreet1052@gmail.com'],fail_silently=False)
#    return render(request,'index.html')

#BusinessDevelopment
class Business_opportunityCreateAPIView(generics.CreateAPIView):
    queryset               =         Business_opportunity.objects.all()
    serializers_class      =         Business_opportunitySerializer
    permission_classes     =         []
    authentication_class   =         []

class Business_opportunityListAPIView(generics.ListAPIView):
    queryset               =         Business_opportunity.objects.all()
    serializers_class      =         Business_opportunitySerializer
    permission_classes     =         []
    authentication_class   =         []

class Business_opportunityUpdateAPIView(generics.UpdateAPIView):
    queryset               =         Business_opportunity.objects.all()
    serializers_class      =         Business_opportunitySerializer
    permission_classes     =         []
    authentication_class   =         []
    lookup_field           =         'project_name'

#Project
class ProjectCreateAPIView(generics.CreateAPIView):
    queryset               =         Project.objects.all()
    serializers_class      =         ProjectSerializer
    permission_classes     =         []
    authentication_class   =         []
class ProjectListAPIView(generics.ListAPIView):
    queryset               =         Project.objects.all()
    serializers_class      =         ProjectSerializer
    permission_classes     =         []
    authentication_class   =         []
class ProjectUpdateAPIView(generics.UpdateAPIView):
    queryset               =         Project.objects.all()
    serializers_class      =         ProjectSerializer
    permission_classes     =         []
    authentication_class   =         []
    lookup_field           =         ''

# #Team
# class TeamCreateAPIView(generics.CreateAPIView):
#     queryset               =         Team.objects.all()
#     serializers_class      =         TeamSerializer
#     permission_classes     =         []
#     authentication_class   =         []
# class TeamListAPIView(generics.ListAPIView):
#     queryset               =         Team.objects.all()
#     serializers_class      =         TeamSerializer
#     permission_classes     =         []
#     authentication_class   =         []
# class TeamUpdateAPIView(generics.UpdateAPIView):
#     queryset               =         Team.objects.all()
#     serializers_class      =         TeamSerializer
#     permission_classes     =         []
#     authentication_class   =         []
#     lookup_field           =         ''





# def ProjectManagement(request):
#     return render(request,'project/dashboard.html')
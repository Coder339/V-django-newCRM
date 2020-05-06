from django.shortcuts import render

from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializer import *

#from  django.core.mail import send_mail

# def index (request):
#    send_mail(
#         'followup','concall with amit'+'\nmeeting with rahul','amanpreetleanvia.com',['amanpreet1052@gmail.com'],fail_silently=False)
#    return render(request,'index.html')

######################BusinessDevelopment###############################

class Business_opportunityList(APIView):

    def get(self,request):
            queryset               =         Business_opportunity.objects.all()
            serializer             =          Business_opportunitySerializer(queryset,many=True)
            permission_classes     =         []
            authentication_class   =         []
            return Response(serializer.data)


    def post(self,request):
            serializer            =      Business_opportunitySerializer(data=request.data)
            permission_classes     =      []
            authentication_class   =      []
            if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    ##no of times hit send = objects created

# class Business_opportunityUpdateAPIView(generics.UpdateAPIView):
#     queryset               =         Business_opportunity.objects.all()
#     serializers_class      =         Business_opportunitySerializer
#     permission_classes     =         []
#     authentication_class   =         []
#     lookup_field           =         'project_name'

###############################Project#################################

class ProjectList(APIView):
    def get(self,request):
            queryset               =         Project.objects.all()
            serializer             =         ProjectSerializer(queryset,many=True)
            permission_classes     =         []
            authentication_class   =         []
            return Response(serializer.data)

    def post(self,request):
            serializer            =      Business_opportunitySerializer(data=request.data)
            permission_classes     =      []
            authentication_class   =      []
            if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ProjectUpdateAPIView(generics.UpdateAPIView):
#     queryset               =         Project.objects.all()
#     serializers_class      =         ProjectSerializer
#     permission_classes     =         []
#     authentication_class   =         []
#     lookup_field           =         ''

############################Team#################################

class TeamList(APIView):
        def get(self,request):
                    queryset               =         Team.objects.all()
                    serializer             =         TeamSerializer(queryset,many=True)
                    permission_classes     =         []
                    authentication_class   =         []
                    return Response(serializer.data)

        def post(self, request):
                    serializer             =     TeamSerializer(data=request.data)
                    permission_classes      =     []
                    authentication_class    =     []
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                    else:
                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class TeamUpdateAPIView(generics.UpdateAPIView):
#     queryset               =         Team.objects.all()
#     serializers_class      =         TeamSerializer
#     permission_classes     =         []
#     authentication_class   =         []
#     lookup_field           =         ''

# def ProjectManagement(request):
#     return render(request,'project/dashboard.html')
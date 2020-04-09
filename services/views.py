from django.shortcuts import render
from .serializer import ServiceSerializer
from rest_framework import generics
from .models import *



# class ServiceCreateAPIView(generics.CreateAPIView):
#     queryset               =         Service.objects.all()
#     serializers_class      =         ServiceSerializer
#     permission_classes     =         []
#     authentication_class   =         []

# class ServiceListAPIView(generics.ListAPIView):
#     queryset               =         Service.objects.all()
#     serializers_class      =         ServiceSerializer
#     permission_classes     =         []
#     authentication_class   =         []
    
# class ServiceUpdateAPIView(generics.UpdateAPIView):
#     queryset               =         Service.objects.all()
#     serializers_class      =         ServiceSerializer
#     permission_classes     =         []
#     authentication_class   =         []
#     lookup_field           =         'pk'




def service(request):
    return render(request,'service/dashboard.html')

def serv(request):
    services = Service.objects.all()
    context = {'services':services}
    return render(request,'service/service.html',context)


def servinfo(request,pk):
    service = Service.objects.get(id=pk)
    return render(request,'service/servinfo.html',{'service':service})

def plan(request):
    plans = Plan.objects.all()
    context = {'plans':plans}
    return render(request,'service/plan.html',context)


def planinfo(request,pk):
    plan = Plan.objects.get(id=pk)
    return render(request,'service/planinfo.html',{'plan':plan})


def product(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,'service/product.html',context)


def prodinfo(request,pk):
    product = Product.objects.get(id=pk)
    return render(request,'service/prodinfo.html',{'product':product})
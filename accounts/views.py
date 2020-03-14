from django.shortcuts import render
from .serializers import EmployeeSerializer,AccountSerializer
from .models import UserEmployeeAccount,UserCustomerAccount
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView


  #json format data of employees

class EmployeeListView(ListAPIView):
    queryset = UserEmployeeAccount.objects.all()
    serializer_class = EmployeeSerializer

    
class EmployeeCreateView(CreateAPIView):
    queryset = UserEmployeeAccount.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeRetrieveView(RetrieveAPIView):
    queryset = UserEmployeeAccount.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeUpdateView(UpdateAPIView):
    queryset = UserEmployeeAccount.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDestroyView(DestroyAPIView):
    queryset = UserEmployeeAccount.objects.all()
    serializer_class = EmployeeSerializer



   #json format data of customers

class CustomerListView(ListAPIView):
    queryset = UserCustomerAccount.objects.all()
    serializer_class = AccountSerializer

class CustomerCreateView(CreateAPIView):
    queryset = UserCustomerAccount.objects.all()
    serializer_class = AccountSerializer

class CustomerRetrieveView(RetrieveAPIView):
    queryset = UserCustomerAccount.objects.all()
    serializer_class = AccountSerializer

class CustomerUpdateView(UpdateAPIView):
    queryset = UserCustomerAccount.objects.all()
    serializer_class = AccountSerializer

class CustomerDestroyView(DestroyAPIView):
    queryset = UserCustomerAccount.objects.all()
    serializer_class = AccountSerializer
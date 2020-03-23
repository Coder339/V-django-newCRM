from django.shortcuts import render
from .models import UserPaymentReceipt,EmployeePackage,UserEmployeePaymentBill
from .serializer import UserPaymentReceiptSerializer,EmployeePackageSerializer,UserEmployeePaymentBillSerializer
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

                                                     # UserPaymentReceipt View
class CreateUserPaymentReceiptView(CreateAPIView): 
    queryset = UserPaymentReceipt.objects.all()
    serializer_class = UserPaymentReceiptSerializer
    permission_classes      =   []
    authentication_classes  =   []

class ListUserPaymentReceiptView(ListAPIView):
    queryset = UserPaymentReceipt.objects.all()
    serializer_class = UserPaymentReceiptSerializer
    permission_classes      =   []
    authentication_classes  =   []

class UpdateUserPaymentReceiptView(UpdateAPIView):
    queryset = UserPaymentReceipt.objects.all()
    serializer_class = UserPaymentReceiptSerializer
    permission_classes      =   []
    authentication_classes  =   []
    lookup_field = 'paymentId'

                                                      # EmployeePackage view
class CreateEmployeePackageView(CreateAPIView): 
    queryset = EmployeePackage.objects.all()
    serializer_class = EmployeePackageSerializer
    permission_classes      =   []
    authentication_classes  =   []

class ListEmployeePackageView(ListAPIView):
    queryset = EmployeePackage.objects.all()
    serializer_class = EmployeePackageSerializer
    permission_classes      =   []
    authentication_classes  =   []

class UpdateEmployeePackageView(UpdateAPIView):
    queryset = EmployeePackage.objects.all()
    serializer_class = EmployeePackageSerializer
    lookup_field = 'pk'
    permission_classes      =   []
    authentication_classes  =   []

                                                       # UserEmployeePaymentBill
class CreateUserEmployeePaymentBillView(CreateAPIView): 
    queryset = UserEmployeePaymentBill.objects.all()
    serializer_class = UserEmployeePaymentBillSerializer
    permission_classes      =   []
    authentication_classes  =   []

class ListUserEmployeePaymentBillView(ListAPIView):
    queryset = UserEmployeePaymentBill.objects.all()
    serializer_class = UserEmployeePaymentBillSerializer
    permission_classes      =   []
    authentication_classes  =   []

class UpdateUserEmployeePaymentBillView(UpdateAPIView):
    queryset = UserEmployeePaymentBill.objects.all()
    serializer_class = UserEmployeePaymentBillSerializer
    permission_classes      =   []
    authentication_classes  =   []
    lookup_field = 'pk'
    



from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

                                                  # UserPaymentReceipt View
# class CreateUserSalaryPackageView(CreateAPIView): 
#     queryset                = SalaryPackage.objects.all()
#     serializer_class        = SalaryPackageSerializer
#     permission_classes      =   []
#     authentication_classes  =   []

# class ListUserSalaryPackageView(ListAPIView):
#     queryset                = SalaryPackage.objects.all()
#     serializer_class        = SalaryPackageSerializer
#     permission_classes      =   []
#     authentication_classes  =   []

# class UpdateUserPaymentReceiptView(UpdateAPIView):
#     queryset                = MonthlySalary.objects.all()
#     serializer_class        = SalaryPackageSerializer
#     permission_classes      =   []
#     authentication_classes  =   []
#     lookup_field            = 'paymentId'

                                                      # EmployeePackage view
class CreateEmployeePackageView(CreateAPIView): 
    queryset                = EmployeePackage.objects.all()
    serializer_class        = EmployeePackageSerializer
    permission_classes      =   []
    authentication_classes  =   []

class ListEmployeePackageView(ListAPIView):
    queryset                = EmployeePackage.objects.all()
    serializer_class        = EmployeePackageSerializer
    permission_classes      =   []
    authentication_classes  =   []

class UpdateEmployeePackageView(UpdateAPIView):
    queryset                = EmployeePackage.objects.all()
    serializer_class        = EmployeePackageSerializer
    lookup_field = 'pk'
    permission_classes      =   []
    authentication_classes  =   []

                                                       # UserEmployeePaymentBill
class CreateUserMonthlySalaryView(CreateAPIView): 
    queryset                = MonthlySalary.objects.all()
    serializer_class        = MonthlySalarySerializer
    permission_classes      =   []
    authentication_classes  =   []

class ListUserMonthlySalaryView(ListAPIView):
    queryset                = MonthlySalary.objects.all()
    serializer_class        = MonthlySalarySerializer
    permission_classes      =   []
    authentication_classes  =   []

class UpdateUserMonthlySalaryBillView(UpdateAPIView):
    queryset                = MonthlySalary.objects.all()
    serializer_class        = MonthlySalarySerializer
    permission_classes      =   []
    authentication_classes  =   []
    lookup_field = 'pk'
    



def payroll(request):
    return render(request,'payroll/dashboard.html')


def empsalary(request):
    packages = EmployeePackage.objects.all()
    context = {'packages':packages}
    return render(request,'payroll/empsalary.html',context)


def empsalinfo(request,pk):
    package = EmployeePackage.objects.get(id=pk)
    return render(request,'payroll/empsalinfo.html',{'package':package})

def monthsal(request):
    salaries = MonthlySalary.objects.all()
    context = {'salaries':salaries}
    return render(request,'payroll/monthsal.html',context)


def monthsalinfo(request,pk):
    salary = MonthlySalary.objects.get(id=pk)
    return render(request,'payroll/monthsalinfo.html',{'salary':salary})
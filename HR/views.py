from django.shortcuts import render
from .models import Department,StaffProfile
from .serializer import DepartmentSerializer,StaffProfileSerializer
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
                                        # Department View
class CreateDepartmentView(CreateAPIView): 
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class ListDepartmentView(ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class UpdateDepartmentView(UpdateAPIView):
    queryset         = Department.objects.all()
    serializer_class = DepartmentSerializer
    lookup_field     = 'deptId'

                                         
                                        #  StaffProfile view
class CreateStaffProfileView(CreateAPIView):
    queryset                = StaffProfile.objects.all()
    serializer_class        = StaffProfileSerializer
    permission_classes      =   []
    authentication_classes  =   []

class ListStaffProfileView(ListAPIView):
    queryset                = StaffProfile.objects.all()
    serializer_class        = StaffProfileSerializer
    permission_classes      =   []
    authentication_classes  =   []

class UpdateStaffProfileView(UpdateAPIView):
    queryset                = StaffProfile.objects.all()
    serializer_class        = StaffProfileSerializer
    permission_classes      =   []
    authentication_classes  =   []
    lookup_field = 'pk'
    


def hr(request):
    return render(request,'hr/dashboard.html')


def dept(request):
    depts = Department.objects.all()
    context = {'depts':depts}
    return render(request,'hr/dept.html',context)


def deptinfo(request,pk):
    dept = Department.objects.get(id=pk)
    return render(request,'hr/deptinfo.html',{'dept':dept})

def staff(request):
    staffs = StaffProfile.objects.all()
    context = {'staffs':staffs}
    return render(request,'hr/staff.html',context)


def staffinfo(request,pk):
    staff = StaffProfile.objects.get(id=pk)
    return render(request,'hr/staffinfo.html',{'staff':staff})
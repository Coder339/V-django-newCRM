from django.shortcuts import render,redirect
from .models import *
from django.views import generic
from django.urls import reverse_lazy
from .models import User,EmployeeProfile
from .serializer import LoginSerializer
from django.contrib.auth import authenticate,login,get_user_model
from rest_framework import generics
from rest_framework.response import Response
from .serializer import UserSerializer,EmployeeProfileSerializer
# from rest_framework.generics import (
#     ListAPIView,
#     CreateAPIView,
#     RetrieveAPIView,
#     UpdateAPIView,
#     DestroyAPIView,
# )

                                    
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes      =   []
    authentication_classes  =   []

class ListUserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes      =   []
    authentication_classes  =   []

class UpdateUserView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes      =   []
    authentication_classes  =   []
    lookup_field = 'pk'

                                    # user's profile
class CreateProfileView(generics.CreateAPIView):
    queryset = EmployeeProfile.objects.all()
    serializer_class = EmployeeProfileSerializer
    permission_classes      =   []
    authentication_classes  =   []

class ListProfileView(generics.ListAPIView):
    queryset = EmployeeProfile.objects.all()
    serializer_class = EmployeeProfileSerializer
    permission_classes      =   []
    authentication_classes  =   []

class UpdateProfileView(generics.UpdateAPIView):
    queryset = EmployeeProfile.objects.all()
    serializer_class = EmployeeProfileSerializer
    permission_classes      =   []
    authentication_classes  =   []
    lookup_field = 'pk'


User=get_user_model()


class LoginAPIView(generics.GenericAPIView):
    authentication_classes      =   []
    permission_classes          =   []
    serializer_class            =   LoginSerializer
    queryset                    =   User.objects.all()


    def post(self,request,*args,**kwargs):
        request             =   self.request
        username            =   request.data['username']
        password            =   request.data['password']
        user                =   authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            response    =   {'messages':'you are logged in ...'}
            return Response(response)
        response    =   {'messages':'invalid credentials'}
        return Response(response)


# from django.urls import reverse_lazy
# from django.views.generic.edit import CreateView

# from .forms import CustomUserCreationForm

# class Register(CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'register.html'

#################################################### F R O N T    E N D   VIEWS ##################


def profile(request):
    return render(request,'profile/dashboard.html')

def customer(request):
    customers = Customer.objects.all()
    context = {'customers':customers}
    return render(request,'profile/customer.html',context)

def customerinfo(request,pk):
    customer = Customer.objects.get(id=pk)
    return render(request,'profile/custinfo.html',{'customer':customer})


def company(request):
    companies = Company.objects.all()
    context ={'companies':companies}
    return render(request,'profile/company.html',context)

def compinfo(request,pk):
    company = Company.objects.get(id=pk)
    return render(request,'profile/compinfo.html',{'company':company})


def employee(request):
    employees = EmployeeProfile.objects.all()
    context ={'employees':employees}
    return render(request,'profile/employee.html',context)
    
def empinfo(request,pk):
    employee = EmployeeProfile.objects.get(id=pk)
    return render(request,'profile/empinfo.html',{'employee':employee})


def vendor(request):
    vendors = Vendor.objects.all()
    context ={'vendors':vendors}
    return render(request,'profile/vendor.html',context)

def vendinfo(request,pk):
    vendor = Vendor.objects.get(id=pk)
    return render(request,'profile/vendinfo.html',{'vendor':vendor})



def finance(request):
    return render(request,'finance/dashboard.html')

def hr(request):
    return render(request,'hr/dashboard.html')

def payroll(request):
    return render(request,'payroll/dashboard.html')

def project(request):
    return render(request,'project/dashboard.html')


def sla(request):
    return render(request,'sla/dashboard.html')


class indexview(generic.ListView):
    template_name = 'profile/index.html'
    context_object_name = 'all_users'

    def get_queryset(self):
        return User.objects.all()

class detailsview(generic.DetailView):
    model = User
    template_name = 'profile/details.html'


class usercreate(generic.CreateView):
    model = User
    fields = '__all__'

class userupdate(generic.UpdateView):
    model = User
    fields = '__all__'

class userdelete(generic.DeleteView):
    model = User
    success_url = reverse_lazy('index')






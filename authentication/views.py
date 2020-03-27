from django.shortcuts import render
from .models import User,EmployeeAccount
from .serializer import UserSerializer,EmployeeAccountSerializer
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

                                    
class CreateUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes      =   []
    authentication_classes  =   []

class ListUserView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes      =   []
    authentication_classes  =   []

class UpdateUserView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes      =   []
    authentication_classes  =   []
    lookup_field = 'pk'

                                    # user's profile
class CreateProfileView(CreateAPIView):
    queryset = EmployeeAccount.objects.all()
    serializer_class = EmployeeAccountSerializer
    permission_classes      =   []
    authentication_classes  =   []

class ListProfileView(ListAPIView):
    queryset = EmployeeAccount.objects.all()
    serializer_class = EmployeeAccountSerializer
    permission_classes      =   []
    authentication_classes  =   []

class UpdateProfileView(UpdateAPIView):
    queryset = EmployeeAccount.objects.all()
    serializer_class = EmployeeAccountSerializer
    permission_classes      =   []
    authentication_classes  =   []
    lookup_field = 'pk'



from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm

class Register(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'

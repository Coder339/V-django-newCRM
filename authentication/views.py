from django.shortcuts import render
from .models import User,EmployeeProfile
from .serializer import UserSerializer,EmployeeProfileSerializer
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
    queryset = EmployeeProfile.objects.all()
    serializer_class = EmployeeProfileSerializer
    permission_classes      =   []
    authentication_classes  =   []

class ListProfileView(ListAPIView):
    queryset = EmployeeProfile.objects.all()
    serializer_class = EmployeeProfileSerializer
    permission_classes      =   []
    authentication_classes  =   []

class UpdateProfileView(UpdateAPIView):
    queryset = EmployeeProfile.objects.all()
    serializer_class = EmployeeProfileSerializer
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

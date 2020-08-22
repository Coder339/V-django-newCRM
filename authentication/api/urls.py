from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token
from . import views

urlpatterns = [
    #custom auth api
    # path('',views.AuthAPI.as_view()),  
    # JWT
    path('jwt/',obtain_jwt_token),
    path('jwt/refresh/',refresh_jwt_token),
    
    path('register/',views.RegistrationAPIView.as_view(),name = 'register'),
    path('login/',views.LoginAPIView.as_view()),

    path('user/',views.UserListCreateView.as_view(),name = 'user'),
    path('user/<pk>/',views.UserDetailView.as_view(),name = 'user-del'),

    path('company/',views.CompanyListCreateView.as_view(),name = 'company'),
    path('company/<pk>/',views.CompanyDetailView.as_view(),name = 'company-del'),

    path('employee/',views.EmployeeListCreateView.as_view(),name = 'employee'),
    path('employee/<pk>/',views.EmployeeDetailView.as_view(),name = 'employee-del'),

    path('customer/',views.CustomerListCreateView.as_view(),name = 'customer'),
    path('customer/<pk>/',views.CustomerDetailView.as_view(),name = 'customer-del'),

    path('vendor/',views.VendorListCreateView.as_view(),name = 'vendor'),
    path('vendor/<pk>/',views.VendorDetailView.as_view(),name = 'vendor-del'),
]


# from .views import CustomerViewSet
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'', CustomerViewSet, basename='user')
# urlpatterns = router.urls
# 88
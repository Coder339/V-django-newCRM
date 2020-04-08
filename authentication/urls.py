from django.urls import path
from . import views
from .views import LoginAPIView


urlpatterns = [
    # path('',views.ListUserView.as_view(),name = 'details'),
    # path('user/add/',views.CreateUserView.as_view(),name = 'add'),
    # path('user/<pk>/edit/',views.UpdateUserView.as_view(),name = 'put'),
    
    # path('profile/',views.ListProfileView.as_view(),name = 'details'),
    # path('profile/add/',views.CreateProfileView.as_view(),name = 'add'),
    # path('profile/<pk>/edit/',views.UpdateProfileView.as_view(),name = 'put'),
    
    
    path('',views.profile,name = 'profile'),
    
    # authentication/
    path('user/', views.indexview.as_view(), name = 'user'),

    path('customer/', views.customer, name = 'customer'),
    path('customer/<pk>/', views.customerinfo, name = 'customerinfo'),

    path('company/', views.company, name = 'company'),
    path('company/<pk>/', views.compinfo, name = 'compinfo'),

    path('employee/', views.employee, name = 'employee'),
    path('employee/<pk>', views.empinfo, name = 'empinfo'),

    path('vendor/', views.vendor, name = 'vendor'),
    path('vendor/<pk>', views.vendinfo, name = 'vendinfo'),

    # path('<int:pk>/', views.detailsview.as_view(), name='details'),
    # path('user/add/',views.usercreate.as_view(), name = 'user-add'),
    # path('user/<int:pk>/', views.userupdate.as_view(), name='user-update'),
    # path('delete/<int:pk>', views.userdelete.as_view(), name='user-delete'),


    path('accounts/',LoginAPIView.as_view())


]
    
    
 



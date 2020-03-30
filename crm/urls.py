
from django.contrib import admin
from django.urls import path,include
from authentication.views import Register
from . import views
# from .views import home

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    # path('', views.ListUsers.as_view(), name='users-view'),
    # path('accounts/',include('authentication.urls')),
    path('finance/',include('finance.urls')),
    path('project/',include('ProjectManagement.urls')),
    path('hr/',include('HR.urls')),
    path('payroll/',include('payroll.urls')),
    path('sla/',include('SLA.urls')),
    path('service/',include('payroll.urls')),
    path('users/', include('django.contrib.auth.urls')), # new
    path('admin/', admin.site.urls),
    path('register/', Register.as_view(), name='signup'),
    path('auth/',include('rest_framework.urls'))
]

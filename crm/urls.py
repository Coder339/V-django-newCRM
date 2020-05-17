
from django.contrib import admin
from django.urls import include,path
# from authentication.views import Register
#from ProjectManagement import views
# from .views import home
from . import views

urlpatterns = [
    # path('', views.HomePageView.as_view(), name='home'),
    # path('', views.ListUsers.as_view(), name='users-view'),

    path('',views.home,name='home'),
    path('profile/', include('authentication.urls')),
    # path('fin/', views.finance, name = 'finance'),
    # path('hrs/', views.hr, name = 'hr'),
    # path('pay/', views.payroll, name = 'payroll'),
    # path('proj/', views.project, name = 'project'),
    # path('serv/', views.service, name = 'service'),
    # path('sl/', views.sla, name = 'sla'),
    
    path('finance/',include('finance.urls')),
    path('project/',include('ProjectManagement.urls')),
    path('hr/',include('HR.urls')),
    path('payroll/',include('payroll.urls')),
    path('sla/',include('ServiceLevelAgreement.urls')),
    path('service/',include('services.urls')),
    # path('users/', include('django.contrib.auth.urls')), # new
    path('admin/', admin.site.urls),
    
    # apis urls 
    path('api/auth/',include('authentication.api.urls')),
    path('api/finance/',include('finance.api.urls')),
    path('api/hr/',include('HR.api.urls')),
    path('api/payroll/',include('payroll.api.urls')),
    # path('api/project/',include('ProjectManagement.api.urls')),
    path('api/services/',include('services.api.urls')),
    # path('api/sla/',include('SLA.api.urls')),

    ### Aman's API's
    path('pmAPI/',include('ProjectManagement.urls')),
    path('slaAPI/',include('ServiceLevelAgreement.urls')),

    
]


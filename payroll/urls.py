from django.urls import path
from . import views

urlpatterns = [
    path('packageinfo',views.ListUserSalaryPackageView.as_view(),name = 'details'),
    path('packageinfo/add/',views.CreateUserSalaryPackageView.as_view(),name = 'add'),
    path('packageinfo/<pk>/edit/',views.UpdateUserPaymentReceiptView.as_view(),name = 'put'),

    path('package',views.ListEmployeePackageView.as_view(),name = 'details'),
    path('package/add/',views.CreateEmployeePackageView.as_view(),name = 'add'),
    path('package/<pk>/edit/',views.UpdateEmployeePackageView.as_view(),name = 'put'),

    path('salary',views.ListUserMonthlySalaryView.as_view(),name = 'details'),
    path('salary/add/',views.CreateUserMonthlySalaryView.as_view(),name = 'add'),
    path('salary/<pk>/edit/',views.UpdateUserMonthlySalaryBillView.as_view(),name = 'put'),
    

]


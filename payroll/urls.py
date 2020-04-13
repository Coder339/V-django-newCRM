from django.urls import path
from . import views
from . import api
urlpatterns = [
    # path('packageinfo',views.ListUserSalaryPackageView.as_view(),name = 'details'),
    # path('packageinfo/add/',views.CreateUserSalaryPackageView.as_view(),name = 'add'),
    # path('packageinfo/<pk>/edit/',views.UpdateUserPaymentReceiptView.as_view(),name = 'put'),

    path('package',api.ListEmployeePackageView.as_view(),name = 'details'),
    path('package/add/',api.CreateEmployeePackageView.as_view(),name = 'add'),
    path('package/<pk>/edit/',api.UpdateEmployeePackageView.as_view(),name = 'put'),

    path('salary',api.ListUserMonthlySalaryView.as_view(),name = 'details'),
    path('salary/add/',api.CreateUserMonthlySalaryView.as_view(),name = 'add'),
    path('salary/<pk>/edit/',api.UpdateUserMonthlySalaryBillView.as_view(),name = 'put'),
    
    path('',views.payroll,name='payroll'),

    path('empsal/', views.empsalary, name = 'empsal'),
    path('empsal/<pk>/', views.empsalinfo, name = 'empsalinfo'),
    path('create_empsal/',views.createEmpPac,name='create_empsal'),
    path('update_empsal/<pk>',views.updatePack,name='update_empsal'),
    path('delete_empsal/<pk>/',views.deletePack,name='delete_empsal'),

    path('monthsal/', views.monthsal, name = 'monthsal'),
    path('monthsal/<pk>/', views.monthsalinfo, name = 'monthsalinfo'),
    path('create_monthsal/',views.createMonthSal,name='create_sal'),
    path('update_monthsal/<pk>',views.updateMonthSal,name='update_monthsal'),
    path('delete_monthsal/<pk>/',views.deleteMonthSal,name='delete_monthsal'),

]





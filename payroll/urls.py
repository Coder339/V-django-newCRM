from django.urls import path
from . import views

urlpatterns = [
    path('receipt',views.ListUserPaymentReceiptView.as_view(),name = 'details'),
    path('receipt/add/',views.CreateUserPaymentReceiptView.as_view(),name = 'add'),
    path('receipt/<paymentId>/edit/',views.UpdateUserPaymentReceiptView.as_view(),name = 'put'),

    path('package',views.ListEmployeePackageView.as_view(),name = 'details'),
    path('package/add/',views.CreateEmployeePackageView.as_view(),name = 'add'),
    path('package/<pk>/edit/',views.UpdateEmployeePackageView.as_view(),name = 'put'),

    path('bill',views.ListUserEmployeePaymentBillView.as_view(),name = 'details'),
    path('bill/add/',views.CreateUserEmployeePaymentBillView.as_view(),name = 'add'),
    path('bill/<pk>/edit/',views.UpdateUserEmployeePaymentBillView.as_view(),name = 'put'),
    

]
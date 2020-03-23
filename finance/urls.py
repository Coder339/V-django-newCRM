from django.urls import path
from . import views

urlpatterns = [
    path('customer/',views.ListInvoiceView.as_view(),name = 'details'),
    path('customer/add/',views.CreateInvoiceView.as_view(),name = 'add'),
    path('customer/<customer_name>/edit/',views.UpdateInvoiceView.as_view(),name = 'put'),

    path('vendor/',views.ListPurchaseView.as_view(),name = 'details'),
    path('vendor/add/',views.CreatePurchaseView.as_view(),name = 'add'),
    path('vendor/<vendor_name>/edit/',views.UpdatePurchaseView.as_view(),name = 'put'),
    

    
]
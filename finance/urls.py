from django.urls import path
from . import views

urlpatterns = [
    # path('customer/',views.ListInvoiceView.as_view(),name = 'cust-details'),
    # path('customer/add/',views.CreateInvoiceView.as_view(),name = 'cust-add'),
    # path('customer/<pk>/',views.CreateInvoiceView.as_view(),name = 'cust-del'),

    # path('customer/<customer_name>/edit/',views.UpdateInvoiceView.as_view(),name = 'cust-put'),

    # path('vendor/',views.ListPurchaseView.as_view(),name = 'vend-details'),
    # path('vendor/add/',views.CreatePurchaseView.as_view(),name = 'vend-add'),
    # path('vendor/<vendor_name>/edit/',views.UpdatePurchaseView.as_view(),name = 'vend-put'),
    

    path('',views.finance,name='finance'),

    path('invoice/', views.invoice, name = 'invoice'),
    path('invoice/<pk>/', views.invinfo, name = 'invinfo'),
    
    # po - purchase order
    path('po/', views.po, name = 'po'),
    path('po/<pk>/', views.poinfo, name = 'poinfo'),

    
    
]
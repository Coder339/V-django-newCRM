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
    
    path('invoice/',views.InvoiceListCreateView.as_view(),name = 'invoice'),
    path('invoice/<pk>/',views.InvoiceDetailView.as_view(),name = 'invoice-del'),
    path('po/',views.PoListCreateView.as_view(),name = 'po'),
    path('po/<pk>/',views.PoDetailView.as_view(),name = 'po-del'),
    

]
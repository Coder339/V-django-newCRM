from django.urls import path
from . import views
from . import api

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
    path('create_invoice/',views.createinvoice,name='create_invoice'),
    path('update_invoice/<pk>/',views.updateinvoice,name='update_invoice'),
    path('update_inent/<pk>/',views.updateSEnt,name='update_inentry'),
    path('delete_invoice/<pk>/',views.deleteinvoice,name='delete_invoice'),
    path('delete_inent/<pk>/',views.deleteSEnt,name='delete_inentry'),


    # po - purchase order
    path('po/', views.po, name = 'po'),
    path('po/<pk>/', views.poinfo, name = 'poinfo'),
    path('create_po/',views.createPO,name='create_po'),
    path('update_po/<pk>/',views.updatePO,name='update_po'),
    path('update_poent/<pk>/',views.updatePEnt,name='update_poentry'),
    path('delete_po/<pk>/',views.deletePO,name='delete_po'),
    path('delete_poent/<pk>/',views.deletePEnt,name='delete_poentry'),


]
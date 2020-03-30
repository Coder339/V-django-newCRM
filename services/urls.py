from django.urls import path
from . import views

urlpatterns = [
    path('',views.ListInvoiceView.as_view(),name = 'details'),
    path('add/',views.CreateInvoiceView.as_view(),name = 'add'),
    path('<pk>/edit/',views.UpdateInvoiceView.as_view(),name = 'put'),    

]



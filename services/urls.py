from django.urls import path
from . import views

urlpatterns = [
    # path('',views.ListInvoiceView.as_view(),name = 'details'),
    # path('add/',views.CreateInvoiceView.as_view(),name = 'add'),
    # path('<pk>/edit/',views.UpdateInvoiceView.as_view(),name = 'put'),    

    path('',views.service,name='service'),

    path('plan/', views.plan, name = 'plan'),
    path('plan/<pk>/', views.planinfo, name = 'planinfo'),

    path('serv/', views.serv, name = 'serv'),
    path('serv/<pk>/', views.servinfo, name = 'servinfo'),

    path('prod/', views.product, name = 'prod'),
    path('prod/<pk>/', views.prodinfo, name = 'prodinfo'),

    

]



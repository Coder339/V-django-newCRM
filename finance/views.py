from django.shortcuts import render
from .models import Invoice,PurchaseOrder
from .serializer import InvoiceSerializer,PurchaseOrderSerializer
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

                                        # Invoice view
class CreateInvoiceView(CreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes      =   []
    authentication_classes  =   []

class ListInvoiceView(ListAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes      =   []
    authentication_classes  =   []

class UpdateInvoiceView(UpdateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes      =   []
    authentication_classes  =   []
    lookup_field = 'customer_name'

                                         
                                         # PurchaseOrder view
class CreatePurchaseView(CreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    permission_classes      =   []
    authentication_classes  =   []

class ListPurchaseView(ListAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    permission_classes      =   []
    authentication_classes  =   []

class UpdatePurchaseView(UpdateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    permission_classes      =   []
    authentication_classes  =   []
    lookup_field = 'vendor_name'











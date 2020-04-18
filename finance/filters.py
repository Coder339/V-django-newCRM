import django_filters

from .models import *

class InvoiceFilter(django_filters.FilterSet):
    class Meta:
        model = Invoice
        fields = '__all__'
        exclude = ['user','customer','payment_terms','Total','Invoice_date','from_company']




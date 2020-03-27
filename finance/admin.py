from django.contrib import admin
from .models import Invoice,PurchaseOrder

admin.site.register(Invoice)
admin.site.register(PurchaseOrder)
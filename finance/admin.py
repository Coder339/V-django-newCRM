from django.contrib import admin
from .models import Invoice,PurchaseOrder
from services.models import *

# admin.site.register(Invoice)
# admin.site.register(PurchaseOrder)

                                                   #----------------------------------FOR ADDING SERVICES

class ServiceEntryInline(admin.TabularInline):
    model = ServiceEntry
    # extra = 0

    # def subtotal(self, obj):
    #     return "$" + str(obj.quantity * obj.inventory.price)



class InvoiceAdmin(admin.ModelAdmin):
    inlines = [ServiceEntryInline]
    class Meta:
        model = Invoice
        fieldsets = (
        (None, {
            'fields':('from_company',
                     'customer_name',
                     'Invoice_number',
                     'cust_sno',
                     'Invoice_date',
                     )
            }),
    )

                                                    #----------------------------------FOR ADDING PRODUCTS
class ProductEntryInline(admin.TabularInline):
    model = ProductEntry
    # extra = 0


    # def subtotal(self, obj):
    #     return "$" + str(obj.quantity * obj.inventory.price)



class POAdmin(admin.ModelAdmin):
    inlines = [ProductEntryInline]
    class Meta:
        model = PurchaseOrder
        fieldsets = (
        (None, {
            'fields':('from_company',
                    'vendor_name',
                    'PO_Number',
                    'vendor_sn',
                    'PO_Date',
                     )
            }),
    )


admin.site.register(Invoice,InvoiceAdmin)
admin.site.register(PurchaseOrder,POAdmin)

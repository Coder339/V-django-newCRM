from django.contrib import admin
from .models import Invoice,PurchaseOrder
from services.models import *

# admin.site.register(Invoice)
# admin.site.register(PurchaseOrder)

                                                   #----------------------------------FOR ADDING SERVICES

class ServiceEntryInline(admin.TabularInline):
    model = ServiceEntry
    extra = 0
    readonly_fields = ['unit_price','amount']
    
    def unit_price(self, obj):
        return "$" + str(float(obj.service.cost))

    def amount(self, obj):
        value = (obj.service.cost * obj.Qty) - (((obj.Discount)/100) * (obj.Qty * obj.service.cost))
        return "$" + str(float(value + obj.Tax))
    



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
    extra = 0
    readonly_fields = ['unit_price','amount']
    
    def unit_price(self, obj):
        return "$" + str(float(obj.Product.cost))

    def amount(self, obj):
        value = (obj.Product.cost * obj.Qty) - (((obj.Discount)/100) * (obj.Qty * obj.Product.cost))
        return "$" + str(float(value + obj.Tax))


                                                    
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

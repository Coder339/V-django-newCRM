from django.contrib import admin
from .models import Invoice,PurchaseOrder
from services.models import *
from django.db.models import Sum,F

# admin.site.register(Invoice)
# admin.site.register(PurchaseOrder)


                                                   #----------------------------------FOR ADDING SERVICES

class ServiceEntryInline(admin.TabularInline):
    model = ServiceEntry
    extra = 0

    readonly_fields = ['unit_price','amount']             
    
    def unit_price(self,obj):
        return "$" + str((obj.rate))


    def amount(self,obj):          # remember :      obj.rate -> nonetype(due to current instance which is not saved yet)  will show error                                                 
        value = (obj.service.cost * obj.Qty) - (((obj.Discount)/100) * (obj.Qty * obj.service.cost))     # important: taking value from Service model
        return "$" + str(float(value + obj.Tax))                                                          # i.e (service.cost) which is saved already
                                                                                                           # till now this is the only solution
                                                                                                            # gives error on obj.rate instead of obj.service.cost



class InvoiceAdmin(admin.ModelAdmin):
    inlines = [ServiceEntryInline]                        # if you want to show subtotal in diffrent table then add ServiceTotalInline in inlines
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
    readonly_fields = ['customer_ID','subtotal']
    
    def customer_ID(self,obj):
        return  str(obj.customer_name) + str(obj.from_company) + str(obj.id)

    def subtotal(self,obj):
        # q = Service.objects.aggregate(Sum('cost'))
        qs = ServiceEntry.objects.all()
        # ps = Service.objects.all()
        s = 0
        for q in qs.iterator():
            s += (q.rate * q.Qty) - (((q.Discount)/100) * (q.Qty * q.rate)) + q.Tax
        

        return "$" + str(s) 






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
    inlines = [ProductEntryInline]           # ,ProductTotalInline
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
    readonly_fields = ['vendor_ID','subtotal']
    
    def vendor_ID(self,obj):
        return  str(obj.vendor_name) + str(obj.from_company) + str(obj.id)

    def subtotal(self,obj):
        # q = Service.objects.aggregate(Sum('cost'))
        qs = ProductEntry.objects.all()
        # ps = Service.objects.all()
        s = 0
        for q in qs.iterator():
            s += (q.rate * q.Qty) - (((q.Discount)/100) * (q.Qty * q.rate)) + q.Tax
        

        return "$" + str(s) 


admin.site.register(Invoice,InvoiceAdmin)
admin.site.register(PurchaseOrder,POAdmin)

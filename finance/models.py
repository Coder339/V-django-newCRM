from django.db import models
from authentication.models import *
from django.contrib.auth import get_user_model
# from django.db.models import F
from services.models import *
from django.db.models.signals import pre_save,post_save

User = get_user_model()


class Invoice(models.Model):  # for customers
    user                   = models.ForeignKey(User,on_delete=models.CASCADE,null=True,editable=False)
    
    customer               = models.ForeignKey(Customer, on_delete=models.CASCADE,editable=False,null=True)
    from_company           = models.CharField(max_length=20, blank=False, null=True)
    customer_name          = models.CharField(max_length=20, blank=False, null=True)
    # date_time              = models.DateTimeField(verbose_name = 'date and time of order',auto_now=False, 
    #                                               auto_now_add=True)
        
    Invoice_number         = models.CharField(max_length=30)  # keep in the format of fisrt customername then date then any serial_number
                                                               # example ; "customername_date_serialnumber"
                                                                # you can use first 2 or 3 letters of every word like
                                                                 # customer: CU, january: JAN,
                                                                  # serial number: numerals like 123,

    # cust_sno               = models.CharField(verbose_name ='customerID',max_length=20, blank=True,
                                            #   null=True)  # format :- first client_name then customer_name
    Invoice_date           = models.DateField()
    
    payment_terms          = models.TextField(max_length=250, blank=False, null=True)
    
    Total                  = models.FloatField(blank=True, null=True)

    
    
    # def __init__(self,*args, **kwargs):
    #     super(ServiceEntry,self).__init__(*args, **kwargs)


    def __str__(self):
        return self.customer_name

    class Meta:
        verbose_name_plural = 'invoice'


    ###################################################################################

    # def save(self,*args,**kwargs):       ################ WILL NOT WORK IF YOU GOING TO INITIALIZE FIRST OBJECT
    #     # super(ServiceEntry,self).save(*args, **kwargs)
    #     invoice = Invoice.objects.get(id=self.id)
    #     entries = invoice.serviceentry_set.all()
    #     self.Total = 0
    #     for q in entries.iterator():
    #         self.Total += ((q.rate * q.Qty) - (((q.Discount)/100) * (q.Qty * q.rate)) + q.Tax )

    #     # print(self.Total)
    #     super(Invoice,self).save(*args, **kwargs)

def pre_save_Stotal(instance,sender,*args,**kwrags):
    # invoice = Invoice.objects.get(id=instance.id)
    entries = instance.serviceentry_set.all()
    instance.Total = 0
    for q in entries.iterator():
        instance.Total += ((q.rate * q.Qty) - (((q.Discount)/100) * (q.Qty * q.rate)) + q.Tax)

pre_save.connect(pre_save_Stotal, sender=Invoice)


    
class PurchaseOrder(models.Model):  # for vendors
    Vendor                 = models.ForeignKey(Vendor, on_delete=models.CASCADE,editable=False,null=True)
    from_company           = models.CharField(max_length=50, blank=False, null=True)
    vendor_name            = models.CharField(max_length=50, blank=False, null=True)
    # date_time              = models.DateTimeField(verbose_name ='date and time of Purchasing Order',
    #                                               auto_now=False, auto_now_add=True)  
    PO_Number              = models.CharField(max_length=50)  # keep in the format of fisrt vendorname 
                                                               # then date then any serial_number
                                                                # example ; "customername_date_serialnumber"
                                                                 # you can use first 2 or 3 letters of every word like
                                                                  # customer: CU, january: JAN,
                                                                   # serial number: numerals like 123,

    # vendor_sn              = models.CharField(verbose_name = 'vendorID',max_length=20, blank=False,
                                            # null=True)  # format :- first client_name then vendor_name
    PO_Date                = models.DateField()

    Total                  = models.FloatField(blank=True, null=True)



    def __str__(self):
        return self.vendor_name

    class Meta:
        verbose_name_plural = 'purchaseOrder'
    
def pre_save_Ptotal(instance,sender,*args,**kwrags):
    # invoice = Invoice.objects.get(id=instance.id)
    entries = instance.productentry_set.all()
    instance.Total = 0
    for q in entries.iterator():
        instance.Total += ((q.rate * q.Qty) - (((q.Discount)/100) * (q.Qty * q.rate)) + q.Tax)

pre_save.connect(pre_save_Ptotal, sender=PurchaseOrder)


    # def save(self,*args,**kwargs):    ################ WILL NOT WORK IF YOU GOING TO INITIALIZE FIRST OBJECT
    #     po = PurchaseOrder.objects.get(id=self.id)
    #     entries = po.productentry_set.all()
    #     self.PTotal = 0
    #     for q in entries.iterator():
    #         self.PTotal += ((q.rate * q.Qty) - (((q.Discount)/100) * (q.Qty * q.rate)) + q.Tax )
        
    
    #     super(PurchaseOrder,self).save(*args, **kwargs)



class ServiceEntry(models.Model):
    invoice                = models.ForeignKey(Invoice,on_delete=models.CASCADE,null=True)
    service                = models.ForeignKey(Service,on_delete=models.CASCADE,null=True)
    description            = models.TextField(max_length=250, blank=False, null=True)    
    # price                  = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    rate                   = models.FloatField()
    Qty                    = models.FloatField()
    Discount               = models.FloatField()
    Tax                    = models.FloatField()
    # SubTotal               = models.IntegerField()

    

    

    def __str__(self):
        return str(self.service)
    
        
                                                            #--------------------FOR PRODUCT INLINE
class ProductEntry(models.Model):
    PO                     = models.ForeignKey(PurchaseOrder,on_delete=models.CASCADE,null=True)
    Product                = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    description            = models.TextField(max_length=250, blank=False, null=True)
    # price                  = models.DecimalField(max_digits=20,decimal_places=2, blank=True, null=True)
    rate                   = models.FloatField()    
    Qty                    = models.FloatField()
    Discount               = models.FloatField()
    Tax                    = models.FloatField()

    # payment_terms          = models.TextField(max_length=250, blank=False, null=True)

    def __str__(self):
        return str(self.Product)










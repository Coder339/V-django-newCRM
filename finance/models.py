from django.db import models
from authentication.models import *
from .utils import unique_cust_sno_generator
from django.db.models.signals import pre_save
# from django.db.models import F
# from services.models import *


class Invoice(models.Model):  # for customers
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
    
    def __str__(self):
        return self.customer_name

    # def __str__(self):
    #     return self.cust_sno


    # def pre_save_create_cust_sno(sender, instance, *args, **kwargs):
    #     if not instance.cust_sno:
    #         instance.order_id= unique_cust_sno_generator(instance)


    #     pre_save.connect(pre_save_create_cust_sno, sender=Invoice)
    
    # @property
    # def total(self,*args,**kwargs):
    #     return self.cost + self.Tax

    # t = models.CharField(total(),max_length=50)
    

    
    

    
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

    vendor_sn              = models.CharField(verbose_name = 'vendorID',max_length=20, blank=False,
                                            null=True)  # format :- first client_name then vendor_name
    PO_Date                = models.DateField()
    # Products               = models.ManyToManyField(Product)
    # description            = models.TextField(max_length=250, blank=False, null=True)
    # price                  = models.DecimalField(max_digits=20,decimal_places=2, blank=True, null=True)
    # Qty                    = models.IntegerField()
    # Discount               = models.IntegerField()
    # Tax                    = models.IntegerField()
    # SubTotal               = models.IntegerField()
    # payment_terms          = models.TextField(max_length=250, blank=False, null=True)

    def __str__(self):
        return self.vendor_name
    

# interdependancies are pending
# need some changes

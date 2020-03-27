from django.db import models
from django.db.models import F

class Invoice(models.Model):  # for customers
    from_client            = models.CharField(max_length=20, blank=False, null=True)
    customer_name          = models.CharField(max_length=20, blank=False, null=True)
    # date_time              = models.DateTimeField(verbose_name = 'date and time of order',auto_now=False, 
    #                                               auto_now_add=True)
        
    Invoice_number         = models.CharField(max_length=30)  # keep in the format of fisrt customername then date then any serial_number
                                                               # example ; "customername_date_serialnumber"
                                                                # you can use first 2 or 3 letters of every word like
                                                                 # customer: CU, january: JAN,
                                                                  # serial number: numerals like 123,

    cust_sno               = models.CharField(verbose_name ='customerID',max_length=20, blank=False,
                                              null=True)  # format :- first client_name then customer_name
    Invoice_date           = models.DateField()
    cost                   = models.IntegerField()
    Tax                    = models.IntegerField()
    TotalAmount            = models.IntegerField()
    description            = models.TextField(max_length=250, blank=False, null=True)
    payment_terms          = models.TextField(max_length=250, blank=False, null=True)
    
    def __str__(self):
        return self.customer_name
    
    @property
    def total(self,*args,**kwargs):
        return self.cost + self.Tax

    # t = models.CharField(total(),max_length=50)
    

    
    

    
class PurchaseOrder(models.Model):  # for vendors
    from_client            = models.CharField(max_length=50, blank=False, null=True)
    vendor_name            = models.CharField(max_length=50, blank=False, null=True)
    # date_time              = models.DateTimeField(verbose_name ='date and time of Purchasing Order',
    #                                               auto_now=False, auto_now_add=True)  
    InvoiceNumber          = models.CharField(max_length=50)  # keep in the format of fisrt vendorname 
                                                               # then date then any serial_number
                                                                # example ; "customername_date_serialnumber"
                                                                 # you can use first 2 or 3 letters of every word like
                                                                  # customer: CU, january: JAN,
                                                                   # serial number: numerals like 123,

    vendor_sn              = models.CharField(verbose_name = 'vendorID',max_length=20, blank=False,
                                            null=True)  # format :- first client_name then vendor_name
    PO_Date            = models.DateField()
    rate_or_price          = models.IntegerField()
    Tax                    = models.IntegerField()
    TotalAmount            = models.IntegerField()
    description            = models.TextField(max_length=250, blank=False, null=True)
    payment_terms          = models.TextField(max_length=250, blank=False, null=True)

    def __str__(self):
        return self.vendor_name
    

# interdependancies are pending
# need some changes

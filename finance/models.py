from django.db import models

class Invoice(models.Model):     # for customers
    from_client            = models.CharField(max_length=20,blank=False,null=True)
    customer_name          = models.CharField(max_length=20,blank=False,null=True)
    date_and_time_of_order = models.DateTimeField(auto_now=False, auto_now_add=True)
    Invoice_number         = models.TextField(max_length=30)   # keep in the format of fisrt customername then date then any serial_number
                                                                # example ; "customername_date_serialnumber"
                                                                 # you can use first 2 or 3 letters of every word like
                                                                  # customer: CU, january: JAN,
                                                                   # serial number: numerals like 123,

    customer_serial_number = models.TextField(max_length=20,blank=False,null=True) # format :- first client_name then customer_name
    Invoice_date           = models.DateField()
    rate_or_cost           = models.IntegerField()
    Tax                    = models.IntegerField()
    Total_Amount           = models.IntegerField()
    description            = models.TextField(max_length=20,blank=False,null=True)
    payment_terms          = models.TextField(max_length=20,blank=False,null=True)


class PurchaseOrder(models.Model): # for vendors
    from_client            = models.CharField(max_length=20,blank=False,null=True)
    vendor_name            = models.CharField(max_length=20,blank=False,null=True)
    date_and_time_of_PO    = models.DateTimeField(auto_now=False, auto_now_add=True)  # PO : Purchasing Order
    Invoice_number         = models.TextField(max_length=30)   # keep in the format of fisrt vendorname then date then any serial_number
                                                                # example ; "customername_date_serialnumber"
                                                                 # you can use first 2 or 3 letters of every word like
                                                                  # customer: CU, january: JAN,
                                                                   # serial number: numerals like 123,

    vendor_serial_number   = models.TextField(max_length=20,blank=False,null=True) # format :- first client_name then vendor_name
    Invoice_date           = models.DateField()
    rate_or_price          = models.IntegerField()
    Tax                    = models.IntegerField()
    Total_Amount           = models.IntegerField()
    description            = models.TextField(max_length=20,blank=False,null=True)
    payment_terms          = models.TextField(max_length=20,blank=False,null=True)

    

# interdependancies are pending
# need some changes 

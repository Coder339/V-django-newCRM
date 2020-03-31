from django.db import models
from finance.models import *

class Service(models.Model) :
    
#     services = (
#     ('INTERNET','Netwrok Service'),
#     ('TV', 'Tv Premium'),
#     ('CALL', 'Call Service'),
#     ('MEDIA', 'Digital Media'),
#     ('CLOUD','Cloud Service')
#     # ('UNKNOWN','Unknown')
# )   
    
    
    # invoice       = models.ForeignKey(Invoice,on_delete=models.CASCADE,null=True)
    serviceId     = models.CharField(max_length=50,null=True,blank=False)
    # name          = models.CharField(max_length=100,blank=False)
    name_c        = models.CharField(verbose_name='company',max_length=100,blank=False,null=True)
    Type          = models.CharField(verbose_name='Type',max_length=20, blank = False,default='Unknown',null = True)
    # code          = models.CharField(max_length=100)
    description   = models.CharField(max_length=100)
    cost          = models.IntegerField()
    isActive      = models.BooleanField(default='true')

    def __str__(self):
        return self.serviceId 
    

class Plan(models.Model):
#     plans = (
#     ('MONTHLY','Monthly'),
#     ('YEARLY', 'Yearly'),
#     # ('UNKNOWN','Unknown')
# )
    types = (
    ('PREPAID','Prepaid'),
    ('POSTPAID', 'Postpaid'),
    # ('UNKNOWN','Unknown')
)
    
    planId        = models.CharField(max_length=30, primary_key=True,blank=False)   
    Type          = models.CharField(max_length=20,choices=types,null=True)
    plan          = models.CharField(verbose_name='plan',max_length=20,null = True)
    validity      = models.DateField(null=True)
    dateOfBooking = models.DateField(null=True)
    dateOfBill    = models.DateField(null=True)
    dueDate       = models.DateField(null=True)
    terms         = models.TextField(max_length=250,verbose_name='PlanTerms',null=True)

    def __str__(self):
        return self.planId
    


class Product(models.Model):
    Product_no         = models.CharField(max_length=30, primary_key=True,blank=False)   
    Product_name       = models.CharField(max_length=20,blank=False)   
    Company_name       = models.CharField(max_length=20,blank=False)
    Product_Description = models.TextField(max_length=250,null=True)

    def __str__(self):
        return self.Product_no


##################################################################################################

                                                            #--------------------FOR SERVICE INLINE
class ServiceEntry(models.Model):
    invoice                = models.ForeignKey(Invoice,on_delete=models.CASCADE,null=True)
    service                = models.ForeignKey(Service,on_delete=models.CASCADE,null=True)
    description            = models.CharField(max_length=250, blank=False, null=True)    
    price                  = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    Qty                    = models.IntegerField()
    Discount               = models.IntegerField()
    Tax                    = models.IntegerField()
    SubTotal               = models.IntegerField()

                                                            #--------------------FOR PRODUCT INLINE
class ProductEntry(models.Model):
    PO                     = models.ForeignKey(PurchaseOrder,on_delete=models.CASCADE,null=True)
    Product                = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    description            = models.CharField(max_length=250, blank=False, null=True)
    price                  = models.DecimalField(max_digits=20,decimal_places=2, blank=True, null=True)
    Qty                    = models.IntegerField()
    Discount               = models.IntegerField()
    Tax                    = models.IntegerField()
    SubTotal               = models.IntegerField()
    # payment_terms          = models.TextField(max_length=250, blank=False, null=True)

    



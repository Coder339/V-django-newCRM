from django.db import models

class Service(models.Model) :
    
#     services = (
#     ('INTERNET','Netwrok Service'),
#     ('TV', 'Tv Premium'),
#     ('CALL', 'Call Service'),
#     ('MEDIA', 'Digital Media'),
#     ('CLOUD','Cloud Service')
#     # ('UNKNOWN','Unknown')
# )   
    
    

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
    plans = (
    ('MONTHLY','Monthly'),
    ('YEARLY', 'Yearly'),
    # ('UNKNOWN','Unknown')
)
    types = (
    ('PREPAID','Prepaid'),
    ('POSTPAID', 'Postpaid'),
    # ('UNKNOWN','Unknown')
)
    
    planId        = models.CharField(max_length=30, primary_key=True,blank=False)   
    Type          = models.CharField(max_length=20,choices=types,null=True)
    plan          = models.CharField(verbose_name='plan', choices=plans, max_length=20, default='Unknown',null = True)
    validity      = models.DateField(null=True)
    dateOfBooking = models.DateField(null=True)
    dateOfBill    = models.DateField(null=True)
    dueDate       = models.DateField(null=True)
    terms         = models.TextField(max_length=250,verbose_name='PlanTerms',null=True)

    def __str__(self):
        return self.planId
    


class Item(models.Model):
    item_no      = models.CharField(max_length=30, primary_key=True,blank=False)   
    item_name    = models.CharField(max_length=10,blank=False)   
    company_name = models.CharField(max_length=10,blank=False)

    def __str__(self):
        return self.item_no
    



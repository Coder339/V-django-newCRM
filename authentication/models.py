from django.db import models
# from model_utils import Choices
# from services.models import Service
# from multiselectfield import MultiSelectField
from django.db.models.signals import pre_save
from django.contrib.auth.models import (
    AbstractUser,

)

govId_choices = (
    ('driving license', 'DRIVING LICENSE'),
    ('passport', 'PASSPORT'),
    ('aadhar', 'AADHAR CARD'),
    ('other', 'OTHER')
)

position = (
    ('SUPER USER', 'super user'),
    ('MANAGER', 'manager'),
    ('HR', 'hr'),
    ('STAFF', 'staff')
)

############################################# for generating unique cust_id,vend_id,emp_id

def counter(start,interval):
    count = start

    if count == 999999:
        count = 1

    while True:
        yield count
        count+= interval


count = counter(start=1,interval=1)

def autoinc():
    return str(next(count)).zfill(6)

############################################## ALL PROFILES



# employeeaccount

class User(AbstractUser):
    role = models.CharField(verbose_name='user role', choices=position, max_length=20, default='unknown',null = True)
    
    class Meta:
        verbose_name_plural = 'user'

class EmployeeProfile(models.Model):

    
    first_name        = models.CharField(max_length=150, blank=False, null=True)
    last_name         = models.CharField(max_length=150, blank=False, null=True)
    username          = models.ForeignKey(User, on_delete=models.CASCADE,default='')
    # username        = models.CharField(max_length=20, primary_key=True)
    email_id          = models.EmailField(max_length=150, blank=False, null=True)
    # password        = models.CharField(max_length=100)
    dob               = models.DateField()
    contact           = models.CharField(verbose_name='PhoneNo.',max_length=20,blank=False, null=True)
    address_1         = models.CharField(max_length=150, blank=False, null=True)
    address_2         = models.CharField(max_length=150, blank=False, null=True)
    city              = models.CharField(max_length=150, blank=False, null=True)
    state             = models.CharField(max_length=150, blank=False, null=True)
    country           = models.CharField(max_length=150, blank=False, null=True)
    zip_code          = models.CharField(max_length=150, blank=False, null=True)
    govt_id           = models.CharField(max_length=150, blank=False, null=True,choices=govId_choices)
    id_no             = models.CharField(verbose_name='',max_length=150, unique=True,blank=False, null=True)
    employee_id       = models.CharField(max_length=50, blank=True, null=True, unique=True)
    p_id1             = models.CharField(verbose_name='PersonalID',max_length=150, blank=False, null=True)  #type of pid
    p_id2             = models.CharField(verbose_name='',max_length=500, blank=False, null=True, unique=True)                      #link of pid
    upload_documents  = models.FileField(default='',blank=True)
    company_code      = models.CharField(max_length=150, blank=False, null=True)
    position          = models.CharField(max_length=150, blank=False, null=True)
    staff             = models.BooleanField(default=False)  # staff user
    admin             = models.BooleanField(default=False)  # super user
    hr                = models.BooleanField(default=False)
    manager           = models.BooleanField(default=False)
    active            = models.BooleanField(default=False)

    # USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = []

    def __str__(self):
        return self.employee_id

    @property
    def is_superUser(self):
        return self.admin

    @property
    def is_hr(self):
        return self.hr

    @property
    def is_active(self):
        return self.active

    @property
    def is_manager(self):
        return self.manager
    
    class Meta:
        verbose_name_plural = 'employee'
    

def pre_save_emp_id(instance,sender,*args,**kwargs):
    # print(instance.company_code)
    def Letters(*args, **kwargs):
        string = instance.company_code[0:2]
        for i in range(len(instance.company_code)):
            if instance.company_code[i] == ' ':
                if len(string) == 4:
                    break
                else:
                    string += instance.company_code[i+1:i+3]
        # print(self.string)
        return str(string)   

    

    instance.employee_id = Letters() + autoinc()

    
pre_save.connect(pre_save_emp_id,sender=EmployeeProfile)




# customeraccount
class Customer(models.Model):

    
    first_name        = models.CharField(max_length=150, blank=False, null=True)
    last_name         = models.CharField(max_length=150, blank=False, null=True)
    email_id          = models.CharField(max_length=150, blank=False, null=True)
    govt_id           = models.CharField(max_length=150, blank=False, null=True, choices=govId_choices)
    id_no             = models.CharField(verbose_name='',max_length=150, unique = True,blank=False, null=True)
    p_id1             = models.CharField(verbose_name='PersonalID',max_length=150, blank=False, null=True) # type of id
    p_id_link         = models.CharField(verbose_name='',max_length=500, blank=False, null=True, unique=True)                      #link of pid
    contact           = models.CharField(verbose_name='PhoneNo.'
                                                      '',max_length=20,blank=False, null=True)
    address_1         = models.CharField(max_length=150, blank=False, null=True)
    address_2         = models.CharField(max_length=150, blank=False, null=True)
    city              = models.CharField(max_length=150, blank=False, null=True)
    state             = models.CharField(max_length=150, blank=False, null=True)
    country           = models.CharField(max_length=150, blank=False, null=True)
    zip_code          = models.CharField(max_length=150, blank=False, null=True) 
    createdBy         = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE, default='',editable=False,null=True)
    company_code      = models.CharField(max_length=150, blank=False, null=True)
    customer_id       = models.CharField(max_length=150, blank=True, null=True)
    # services          = MultiSelectField(choices=MY_CHOICES,null=True)
    # serviceTAG        = models.ManyToManyField(Service)


    # creationDate    = models.DateTimeField(auto_now_add=True)
    # updatedAt       = models.DateTimeField(auto_now=True)
    # board             = ArrayField(
    #                        ArrayField(
    #                             models.CharField(max_length=10, blank=True),
    #                             size=8,
    #                       ),
    #                       size=8,null=True
    # )
    

    def __str__(self):
        return (self.first_name)

    class Meta:
        verbose_name_plural = 'Customer'

  

def pre_save_cust_id(instance,sender,*args,**kwargs):
    # print(instance.company_code)
    def Letters(*args, **kwargs):
        string = instance.company_code[0:2]
        for i in range(len(instance.company_code)):
            if instance.company_code[i] == ' ':
                if len(string) == 4:
                    break
                else:
                    string += instance.company_code[i+1:i+3]
        # print(self.string)
        return str(string)   

    

    instance.customer_id = Letters() + autoinc()

    
pre_save.connect(pre_save_cust_id,sender=Customer)


class Vendor(models.Model):

    

    first_name         = models.CharField(max_length=150, blank=False, null=True)
    last_name          = models.CharField(max_length=150, blank=False, null=True)
    email_id           = models.CharField(max_length=150, blank=False, null=True)
    govt_id            = models.CharField(max_length=150, blank=False, choices=govId_choices,null=True)
    id_no              = models.CharField(verbose_name='',max_length=150, blank=False, unique = True, null=True)
    p_id1              = models.CharField(verbose_name='PersonalID',max_length=150, blank=False, null=True) # type of id
    p_id_link          = models.CharField(verbose_name='',max_length=500, blank=False, null=True, unique=True)                      #link of pid
    contact            = models.CharField(verbose_name='PhoneNo.',max_length=20,blank=False, null=True)
    address_1          = models.CharField(max_length=150, blank=False, null=True)
    address_2          = models.CharField(max_length=150, blank=False, null=True)
    city               = models.CharField(max_length=150, blank=False, null=True)
    state              = models.CharField(max_length=150, blank=False, null=True)
    country            = models.CharField(max_length=150, blank=False, null=True)
    zip_code           = models.CharField(max_length=150, blank=False, null=True) 
    company_Name       = models.CharField(max_length=150, blank=False, null=True) 
    company_Address1   = models.CharField(max_length=150, blank=False, null=True) 
    company_Address2   = models.CharField(max_length=150, blank=False, null=True) 
    company_Phone      = models.CharField(max_length=150, blank=False, null=True) 
    company_EmailId    = models.CharField(max_length=150, blank=False, null=True) 

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = 'vendor'



class Company(models.Model):

    company_Name       = models.CharField(max_length=150, blank=False, null=True) 
    company_Address1   = models.CharField(max_length=150, blank=False, null=True) 
    company_Address2   = models.CharField(max_length=150, blank=False, null=True) 
    city               = models.CharField(max_length=150, blank=False, null=True) 
    zip_code           = models.CharField(max_length=150, blank=False, null=True) 
    country            = models.CharField(max_length=150, blank=False, null=True) 
    company_Phone      = models.CharField(max_length=150, blank=False, null=True) 
    company_EmailId    = models.CharField(max_length=150, blank=False, null=True) 

    def __str__(self):
        return self.company_Name

    class Meta:
        verbose_name_plural = 'company'
    






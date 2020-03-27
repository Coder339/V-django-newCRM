from django.db import models
# from model_utils import Choices
from multiselectfield import MultiSelectField
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



# employeeaccount

class User(AbstractUser):
    role = models.CharField(verbose_name='user role', choices=position, max_length=20, default='unknown',null = True)


class EmployeeAccount(models.Model):
    personalId_choices = (
    ('FACEBOOK', 'Facebook'),
    ('TWITTER', 'Twitter'),
    ('SKYPE', 'Skype'),
    ('LINKEDin', 'Linkedin')

)
    user           = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name     = models.CharField(max_length=150, blank=False, null=True)
    last_name      = models.CharField(max_length=150, blank=False, null=True)
    username       = models.CharField(max_length=20, primary_key=True)
    email_id       = models.EmailField(max_length=150, blank=False, null=True)
    # password     = models.CharField(max_length=100)
    dob            = models.DateField()
    contact        = models.CharField(verbose_name='PhoneNo.',max_length=20,blank=False, null=True)
    address_1      = models.CharField(max_length=150, blank=False, null=True)
    address_2      = models.CharField(max_length=150, blank=False, null=True)
    city           = models.CharField(max_length=150, blank=False, null=True)
    state          = models.CharField(max_length=150, blank=False, null=True)
    country        = models.CharField(max_length=150, blank=False, null=True)
    zip_code       = models.CharField(max_length=150, blank=False, null=True)
    govt_id        = models.CharField(max_length=150, blank=False, null=True,choices=govId_choices)
    id_no             = models.CharField(verbose_name='',max_length=150, blank=False, null=True)
    employee_id    = models.CharField(max_length=50, blank=False, null=True, unique=True)
    p_id1          = models.CharField(verbose_name='PersonalID',max_length=150, blank=False, null=True,choices=personalId_choices)  #type of pid
    p_id2          = models.CharField(verbose_name='',max_length=500, blank=False, null=True, unique=True)                      #link of pid
    position       = models.CharField(max_length=150, blank=False, null=True)
    staff          = models.BooleanField(default=False)  # staff user
    admin          = models.BooleanField(default=False)  # super user
    hr             = models.BooleanField(default=False)
    manager        = models.BooleanField(default=False)
    active         = models.BooleanField(default=False)

    # USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = []

    def __str__(self):
        return self.first_name

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


# customeraccount
class CustomerAccount(models.Model):
    personalId_choices = (
    ('FACEBOOK', 'Facebook'),
    ('TWITTER', 'Twitter'),
    ('SKYPE', 'Skype'),
    ('OTHER', 'Other'),

)
    MY_CHOICES = (
    ('INTERNET','Netwrok Service'),
    ('TV', 'Tv Premium'),
    ('CALL', 'Call Service'),
    ('MEDIA', 'Digital Media'),
    ('CLOUD','Cloud Service'),
    ('UNKNOWN','Unknown')
)

    first_name        = models.CharField(max_length=150, blank=False, null=True)
    last_name         = models.CharField(max_length=150, blank=False, null=True)
    email_id          = models.CharField(max_length=150, blank=False, null=True)
    govt_id           = models.CharField(max_length=150, blank=False, null=True, unique=True, choices=govId_choices)
    id_no             = models.CharField(verbose_name='',max_length=150, blank=False, null=True)
    p_id1             = models.CharField(verbose_name='PersonalID',max_length=150, blank=False, null=True,choices=personalId_choices) # type of id
    p_id_link         = models.CharField(verbose_name='',max_length=500, blank=False, null=True, unique=True)                      #link of pid
    contact           = models.CharField(verbose_name='PhoneNo.',max_length=20,blank=False, null=True)
    address_1         = models.CharField(max_length=150, blank=False, null=True)
    address_2         = models.CharField(max_length=150, blank=False, null=True)
    city              = models.CharField(max_length=150, blank=False, null=True)
    state             = models.CharField(max_length=150, blank=False, null=True)
    country           = models.CharField(max_length=150, blank=False, null=True)
    zip_code          = models.CharField(max_length=150, blank=False, null=True)
    createdBy         = models.ForeignKey(EmployeeAccount, on_delete=models.CASCADE, default='')
    services          = MultiSelectField(choices=MY_CHOICES,null=True)
    


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
        return self.first_name










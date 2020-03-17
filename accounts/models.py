from django.db import models
from django.contrib.auth.models import (
    AbstractUser,

)

govId_choices = (
    ('driving license', 'DRIVING LICENSE'),
    ('passport', 'PASSPORT'),
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
    role = models.CharField(verbose_name='user role', choices=position, max_length=20, default='admin')


class EmployeeAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=20, primary_key=True)
    email_id = models.EmailField(max_length=150, blank=False, null=True)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=150, blank=False, null=True)
    last_name = models.CharField(max_length=150, blank=False, null=True)
    dob = models.DateField()
    contact = models.IntegerField(blank=False, null=True)
    address_1 = models.CharField(max_length=150, blank=False, null=True)
    address_2 = models.CharField(max_length=150, blank=False, null=True)
    city = models.CharField(max_length=150, blank=False, null=True)
    state = models.CharField(max_length=150, blank=False, null=True)
    country = models.CharField(max_length=150, blank=False, null=True)
    zip_code = models.TextField(max_length=150, blank=False, null=True)
    govt_id = models.CharField(max_length=150, blank=False, null=True, unique=True, choices=govId_choices)
    employee_id = models.TextField(max_length=250, blank=False, null=True, unique=True)
    position = models.CharField(max_length=150, blank=False, null=True)
    staff = models.BooleanField(default=False)  # staff user
    admin = models.BooleanField(default=False)  # super user
    hr = models.BooleanField(default=False)
    manager = models.BooleanField(default=False)
    active = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

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
    first_name = models.CharField(max_length=150, blank=False, null=True)
    last_name = models.CharField(max_length=150, blank=False, null=True)
    email_id = models.CharField(max_length=150, blank=False, null=True)
    govt_id = models.CharField(max_length=150, blank=False, null=True, unique=True, choices=govId_choices)
    contact = models.IntegerField(blank=False, null=True)
    address_1 = models.CharField(max_length=150, blank=False, null=True)
    address_2 = models.CharField(max_length=150, blank=False, null=True)
    city = models.CharField(max_length=150, blank=False, null=True)
    state = models.CharField(max_length=150, blank=False, null=True)
    country = models.CharField(max_length=150, blank=False, null=True)
    zip_code = models.TextField(max_length=150, blank=False, null=True)
    # creationDate    = models.DateField(auto_now_add=True)
    # updatedAt       = models.DateField(auto_now=True)
    createdBy = models.ForeignKey(EmployeeAccount, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.first_name










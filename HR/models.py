from django.db import models
from accounts.models import EmployeeAccount
from payroll.models import EmployeePackage

GENDER_CHOICES = (
    ('Not Known', 'NOT_KNOWN'),
    ('Male', 'MALE'),
    ('Female', 'FEMALE')
)


class Department(models.Model):
    deptId        = models.CharField(max_length=10)
    dept_name     = models.CharField(max_length=20)  # abc / xyz etc.
    branch        = models.CharField(max_length=20)  # location :- chandigarh/pune/banglore etc.

    def __str__(self):
        return self.dept_name


class StaffProfile(models.Model):  # employee record stored as static
    Id             = models.ForeignKey(EmployeeAccount, on_delete=models.CASCADE)
    packageId      = models.ForeignKey(EmployeePackage, on_delete=models.CASCADE)
    father_name    = models.CharField(max_length=20, blank=False)
    mother_name    = models.CharField(max_length=20, blank=False)
    marital_status = models.CharField(max_length=20, blank=False)
    gender         = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)


class StaffRole(models.Model):  # dynamic
    Irole                  = models.ForeignKey(StaffProfile, on_delete=models.CASCADE)
    departmentId           = models.ForeignKey(Department, on_delete=models.CASCADE)
    packageId              = models.ForeignKey(EmployeePackage, models.CASCADE)
    description            = models.TextField(blank=True, default='')
    leave_days             = models.PositiveIntegerField()
    sick_days              = models.PositiveIntegerField()
    no_of_holidays_allowed = models.IntegerField()
    package                = models.IntegerField()
    start_date             = models.IntegerField()
    end_date               = models.IntegerField()  # on contract basis : bond duration

    def __str__(self):
        return self.name

# incomplete ^
# phonenumberfield package need to be installed through cmd




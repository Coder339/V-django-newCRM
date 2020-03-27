from django.db import models
from authentication.models import EmployeeAccount
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


# class StaffProfile(models.Model):  # employee record stored as static
    # Id             = models.ForeignKey(EmployeeAccount, on_delete=models.CASCADE,null=True)
#     packageId      = models.ForeignKey(EmployeePackage, on_delete=models.CASCADE,null=True)
#     father_name    = models.CharField(max_length=20, blank=False)
#     mother_name    = models.CharField(max_length=20, blank=False)
#     marital_status = models.CharField(max_length=20, blank=False)
#     gender         = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)

#     def __str__(self):
#         return self.Id.first_name
   
    
    


class StaffRole(models.Model):  # dynamic
    Id                     = models.ForeignKey(EmployeeAccount,on_delete=models.CASCADE,null=True)
    departmentId           = models.ForeignKey(Department, on_delete=models.CASCADE,null=True)
    packageId              = models.ForeignKey(EmployeePackage, models.CASCADE,editable = False,null=True)
    description            = models.TextField(blank=True, default='')
    leave_days             = models.PositiveIntegerField()
    sick_days              = models.PositiveIntegerField()
    no_of_holidays_allowed = models.IntegerField()
    package                = models.IntegerField()
    start_date             = models.DateField(null=True,auto_now_add=True)
    # end_date               = models.DateField(null=True)  # on contract basis : bond duration

    def __str__(self):
        return self.Id.first_name





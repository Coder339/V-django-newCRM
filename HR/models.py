from django.db import models
from authentication.models import EmployeeProfile
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
   


class StaffProfile(models.Model):  # dynamic
    EmpId                     = models.ForeignKey(EmployeeProfile,on_delete=models.CASCADE,null=True)
    departmentId              = models.ForeignKey(Department, on_delete=models.CASCADE,null=True)
    packageId                 = models.ForeignKey(EmployeePackage, models.CASCADE,editable = False,null=True)
    
    # leave_days             = models.PositiveIntegerField()
    # sick_days              = models.PositiveIntegerField()
    no_of_holidays_allowed    = models.IntegerField()
    package                   = models.IntegerField()
    joined_date               = models.DateField(null=True)
    description               = models.TextField(blank=True, default='')
    # end_date               = models.DateField(null=True)  # on contract basis : bond duration
    isactive                 = models.BooleanField(default=False)

    def __str__(self):
        return self.Id.first_name





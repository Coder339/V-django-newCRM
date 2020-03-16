from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from accounts.models import UserEmployeeAccount
from payroll import EmployeePackage

GENDER_CHOICES = (
    ('Not Known', 'NOT_KNOWN'),
    ('Male', 'MALE'),
    ('Female', 'FEMALE')
)


class StaffProfile(models.Model):  # employee record stored as static
    Id = models.ForeignKey(UserEmployeeAccount, on_delete=models.SET_NULL)
    packageId = models.ForeignKey(EmployeePackage, on_delete=)
    father_name = models.CharField(max_length=20, blank=False)
    mother_name = models.CharField(max_length=20, blank=False)
    marital_status = models.CharField(max_length=20, blank=False)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10,
                              default=NOT_KNOWN, blank=True)


class StaffRole(models.Model):
    staffId = models.ForeignKey(StaffProfile, on_delete=models.SET_NULL)
    departmentId = models.CharField(max_length=10)
    packageId = models.ForeignKey()
    role = models.ForeignKey(StaffProfile, on_delete=models.SET_NULL)
    description = models.TextField(blank=True, default='')
    leave_days = models.PositiveIntegerField()
    sick_days = models.PositiveIntegerField()
    no_of_holidays_allowed = models.IntegerField()
    package = models.IntegerField()
    start_date = models.IntegerField()
    end_date = models.IntegerField()  # on contract basis : bond duration

    def __str__(self):
        return self.name

# incomplete ^
# phonenumberfield package need to be installed through cmd




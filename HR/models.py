from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

GENDER_CHOICES = (
        ('Not Known','NOT_KNOWN'),
        ('Male','MALE'),
        ('Female','FEMALE'),
        ('Not Applicable','NOT_APPLICABLE')
    )


class StaffRole(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True, default='') 
    
    def __str__(self):
        return self.name
    

class StaffProfile(models.Model):     #employee record
    role         = models.ForeignKey(Role,on_delete = models.SET_NULL)
    gender       = models.CharField(choices=GENDER_CHOICES, max_length=10,
                            default=NOT_KNOWN, blank=True)
    phone        = models.PhoneNumberField()
    address      = models.TextField(blank=True, default="")
    birthday     = models.DateField(blank=True, default=None,
                                null=True)
    leave_days   = models.PositiveIntegerField()
    sick_days    = models.PositiveIntegerField()


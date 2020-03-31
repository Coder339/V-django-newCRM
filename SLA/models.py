from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from authentication.models import *

priority=(('HIGH','High'),
          ('LOW','Low'),
          ('MODERATE','Moderate'))
stage=(('IN PROGRESS','In Progress'),
       ('RESOLVED','Resolved'))

class SLA(models.Model):
    customer_details         =              models.ForeignKey(Customer,on_delete=models.CASCADE,default='',null=True)
    ticket_no               =               models.IntegerField()
    issue_details           =               models.TextField(blank='Flase', null='False')
    priority                =               models.CharField(choices=priority,max_length=200)
    employee_details        =               models.ForeignKey(EmployeeProfile,on_delete=models.CASCADE,default='')
    status                  =               models.CharField(choices=stage,max_length=200,null=True)
   
    class Meta():
        verbose_name_plural = 'SLA'

    def __str__(self,*agrs,**kwargs):
        return self.customer_details.first_name
    
    
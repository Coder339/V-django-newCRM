from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from authentication.models import *

priority=(('HIGH','High'),
          ('LOW','Low'),
          ('MODERATE','Moderate'))
stage=(('INITIATED','Initiated'),('IN PROGRESS','In Progress'),
       ('RESOLVED','Resolved'))

class SLA(models.Model):
    customer_details        =               models.ManyToManyField(Customer)
    ticket_no               =               models.AutoField(primary_key=True)
    problem_details         =               models.TextField(blank='False', null='False')
    priority                =               models.CharField(choices=priority,max_length=200)
    date                    =               models.DateField()
    responsible_person      =               models.ForeignKey(EmployeeProfile,on_delete=models.CASCADE,default='')
    status                  =               models.CharField(choices=stage,max_length=200,null=True)
   
    class Meta():
        verbose_name_plural = 'SLA'

    def __str__(self):
        return self.problem_details


#class History(model.Model):
    #customer_name             =             model.ForeignKey(Customer,on_delete=models.CASCADE,null=True,verbose_name='Customer')



    #def __str__(self,*agrs,**kwargs):
        #return self.customer_details.ticket_no
    
    
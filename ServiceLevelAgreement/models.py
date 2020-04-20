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
   # ticket_no               =               models.IntegerField()
    issue                   =               models.CharField(max_length=100,blank='False', null='False')
    priority                =               models.CharField(choices=priority,max_length=200)
    date                    =               models.DateField()
    responsible_person      =               models.ManyToManyField(EmployeeProfile)
    status                  =               models.CharField(choices=stage,max_length=200,null=True)
    solution_details        =               models.CharField(max_length=200,null='True')
   
    class Meta():
        verbose_name_plural = 'SLA'

    def __str__(self):
        return str(self.id)





    
'''class Record(models.Model):

    customer_name                 =         models.ForeignKey(SLA,on_delete=models.CASCADE,related_name='name',default='')
    #ID                            =         models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='customer_id',default='')
    issue                         =         models.ManyToManyField(SLA,related_name='issue_datail')
    date                          =         models.ForeignKey(SLA, on_delete=models.CASCADE,related_name='issue_date',default='')
    current_status                 =         models.ForeignKey(SLA, on_delete=models.CASCADE,related_name='stage',default='')

    def get_issue(self):
        return ','.join([str(i) for i in self.issue.all()])


    class Meta():
        verbose_name_plural = 'Record'

    def __str__(self):
        return str(self.customer_name)'''



from django.db import models
from django.contrib.auth.models import AbstractUser
from authentication.models import *
import datetime
stage=( ('PLANNING','Planning'), ('DEVELOPMENT','Development'),('TESTING','Testing'),
              ('EXECUTION','Execution'),('COMPLETION','Completion'))
class Business_opportunity(models.Model):
       Company_name            =               models.CharField(max_length=100,blank=False,null=False)
       Project_name            =               models.CharField(max_length=100,blank=False,null=False)
       description             =               models.TextField(max_length=300,blank=False,null=False)
       start_date              =               models.DateTimeField()
       deadline                =               models.DateTimeField()
       employee_name           =               models.ForeignKey(EmployeeProfile,on_delete=models.CASCADE,default='',null=True)
       followup_date           =               models.DateTimeField()

       class Meta():
              verbose_name_plural='Business_opportunity'

class Project(models.Model):
       project_name            =               models.CharField(max_length=100,blank=False,null=False)
       description             =               models.TextField(max_length=300, blank=False, null=False)
       start_date              =               models.DateTimeField()
       deadline                =               models.DateTimeField()
       owner                   =               models.CharField(max_length=100,blank=False,null=False)
       team_lead               =               models.CharField(max_length=100, blank=False, null=False)
       team_members            =               models.ForeignKey(EmployeeProfile,on_delete=models.CASCADE,null=True)
       task_assigned           =               models.CharField(max_length=300,blank=False,default='')
       current_stage           =               models.CharField(choices=stage,max_length=200,blank=False,null=False)
       
       class Meta():
              verbose_name_plural='Project'

class TodoList(models.Model):
    employee_name               =              models.ForeignKey(EmployeeProfile,on_delete=models.CASCADE,null=True)
    update                      =              models.CharField(max_length=300,blank=False,null='False')
    
    class Meta():
           verbose_name_plural = 'TodoList'


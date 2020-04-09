from django.db import models
from django.contrib.auth.models import AbstractUser
from authentication.models import *

stage=( ('PLANNING','Planning'), ('DEVELOPMENT','Development'),('TESTING','Testing'),
              ('DEPLOYMENT','Deployment'),('COMPLETED','Completed'))
class Business_opportunity(models.Model):

       project_name            =               models.CharField(max_length=100,blank=False,null=False,default='')
       description             =               models.TextField(max_length=300,blank=False,null=False)
       company_name            =               models.CharField(max_length=100, blank=False, null=False)
       address                 =               models.CharField(max_length=100, blank=False, null=False)
       email_id                =               models.EmailField(max_length=100, blank=False, null=False,default='')
       phone_no                =               models.CharField(max_length=100,blank=False,null=False,default='')
       additional_contact      =               models.CharField(max_length=300,blank=False,null='False',default='')
       details                 =               models.CharField(verbose_name='',max_length=300,blank=False,null='False')
       start_date              =               models.DateField()
       deadline                =               models.DateField()
       responsible_person      =               models.ForeignKey(EmployeeProfile,on_delete=models.CASCADE,default='',null=True)
       followup_date           =               models.DateField()
       upload_documents        =               models.FileField(default='')

       class Meta():
              verbose_name_plural='Business Opportunity'

       def __str__(self):
              return self.company_name


class Project(models.Model):
       project_name            =               models.CharField(max_length=100,blank=False,null=False)
       description             =               models.TextField(max_length=300, blank=False, null=False)
       start_date              =               models.DateField()
       deadline                =               models.DateField()
       owner                   =               models.CharField(max_length=100,blank=False,null=False)
       team_lead               =               models.CharField(max_length=100, blank=False, null=False)
       team_members            =               models.ManyToManyField(EmployeeProfile)
       task_assigned           =               models.CharField(max_length=300,blank=False,default='')
       project_status          =               models.CharField(choices=stage,max_length=200,blank=False,null=False,default='')
       #selected                =               models.Boolean

#class team_members(model.Model):
       #TeamMenbers             =               models.

       def __str__(self):
           return self.project_name



class TodoList(models.Model):
    employee_name               =              models.ForeignKey(EmployeeProfile,on_delete=models.CASCADE,null=True)
    project                     =              models.CharField(max_length=300,blank=False,null='False')
    task                        =              models.CharField(max_length=300,blank=False,null='False')
    update                      =              models.CharField(max_length=300,blank=False,null='False')
    
    class Meta():
           verbose_name_plural = 'Employee Report'


    def __str__(self):
        return self.employee_name



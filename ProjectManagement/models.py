from django.db import models
from django.contrib.auth.models import AbstractUser
from authentication.models import *

stage=( ('PLANNING','Planning'), ('DEVELOPMENT','Development'),('TESTING','Testing'),
              ('DEPLOYMENT','Deployment'),('COMPLETED','Completed'))
class Business_opportunity(models.Model):

       project_name            =               models.CharField(max_length=100,blank=False,null=False,default='')
       description             =               models.TextField(max_length=300,blank=False,null=False)
       company_name            =               models.CharField(max_length=100, blank=False, null=False)
       address                 =               models.CharField(max_length=100, default='')
       contact_person          =               models.CharField(max_length=100, blank=False, null=False,default='')
       email_id                =               models.EmailField(max_length=100, blank=False, null=False,default='')
       phone_no                =               models.CharField(max_length=100,blank=False,null=False,default='')
       additional_contact      =               models.CharField(max_length=300,blank=False,null='False',default='')
       details                 =               models.CharField(verbose_name='',max_length=300,blank=False,null='False')
       start_date              =               models.DateField()
       deadline                =               models.DateField()
       responsible_person      =               models.ManyToManyField(EmployeeProfile)
       followup_date           =               models.DateField()
       followup_message        =               models.TextField(max_length=150,default='')
       upload_documents        =               models.FileField(default='')

       class Meta():
              verbose_name_plural='Business Opportunity'

       def __str__(self):
              return self.company_name


class Project(models.Model):
       project_name            =               models.CharField(max_length=100,blank=False,null=False)
       description             =               models.CharField(max_length=100, blank=False, null=False)
       start_date              =               models.DateField()
       project_deadline        =               models.DateField()
       owner                   =               models.CharField(max_length=100,blank=False,null=False)
       project_status          =               models.CharField(choices=stage, max_length=200, blank=False, null=False, default='')
       team_lead               =               models.CharField(max_length=100, blank=False, null=False)

       class Meta():
              verbose_name_plural='Project'

       def __str__(self):
              return self.project_name



class Team(models.Model):

       project                 =               models.ForeignKey(Project, on_delete=models.CASCADE,default='')
       team_member             =               models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE, default='')
       task_assigned           =               models.CharField(max_length=100,blank=False,default='')
       updates                 =               models.CharField(max_length=100,default='')
       task_deadline           =               models.DateField()

       class Meta():
              verbose_name_plural='Team'









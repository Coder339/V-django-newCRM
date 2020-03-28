from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
class Business_opportunity(models.Model):
       Company_name            =               models.CharField('Company Name',max_length=100,blank=False,null=False)
       Project_name            =               models.CharField(max_length=100,blank=False,null=False)
       description             =               models.TextField(max_length=300,blank=False,null=False)
       start_date              =               models.DateField()
       deadline                =               models.DateField()
       followup_date           =               models.DateField()

       class Meta():
              verbose_name_plural='Business_opportunity'

class Project(models.Model):
       project_name            =               models.CharField(max_length=100,blank=False,null=False)
       owner                   =               models.CharField(max_length=100,blank=False,null=False)
       team_members            =               models.TextField(max_length=100,blank=False,null=False)
       team_lead               =               models.CharField(max_length=100,blank=False,null=False)
       description             =               models.TextField(max_length=300,blank=False,null=False)
       start_date              =               models.DateField()
       deadline                =               models.DateField()
       current_stage           =               models.CharField(max_length=200,blank=False,null=False)
       done                    =               models.BooleanField(default=False)
       
       class Meta():
              verbose_name_plural='Project'

class Task(models.Model):
       number                   =              models.IntegerField()
       name                     =              models.CharField(max_length=200)
       #project                  =              models.ForeignKey(Project)
       parent_task_num          =              models.IntegerField(null=True, blank=True)
       #responsible_person       =              models.ForeignKey(User, null=True, blank=True)
       start_date               =              models.DateField()
       end_date                 =              models.DateField(null=True, blank=True)
       is_complete              =              models.BooleanField(default=False)
       created_on               =              models.DateTimeField(auto_now_add=1)
       #is_deleted               =              models.BooleanField(default=False)
       #created_by               =              models.ForeignKey(User, related_name='created_tasks')
       #last_updated_by          =              models.ForeignKey(User, related_name='updated_tasks')
       
       class Meta():
              verbose_name_plural='Task'

class TodoList(models.Model):
    name                        =              models.CharField(max_length = 200)
     #user                       =              models.ForeignKey(User)
     #project                    =              models.ForeignKey(Project)
    is_complete                 =              models.BooleanField(default = False)
    created_on                  =              models.DateTimeField(auto_now_add = 1)
    
    class Meta():
           verbose_name_plural = 'TodoList'

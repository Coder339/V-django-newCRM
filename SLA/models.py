from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

applicable=(('created','CREATED'),
            ('Modify','MODIFY'),
            ('followup','FOLLOWUP'))

class SLA(models.Model):
    ticket_no               =               models.IntegerField()
    priority                =               models.CharField(max_length=200,default="")
    discription             =               models.TextField(blank=True, default="")
    warn_from               =               models.DateTimeField(default="")
    failure_after           =               models.DateTimeField(default="")
    created                 =               models.DateTimeField(default="")
    modified                =               models.DateTimeField(default="")
   
    class Meta():
        verbose_name_plural = 'SLA'

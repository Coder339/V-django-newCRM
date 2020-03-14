from django.db import models
from accounts.models import UserEmployeeAccount


class UserEmployeePaymentBill(models.Model):
    userId           = models.ForeignKey(UserEmployeeAccount,on_delete='CASCADE')
    packageId        = models.CharField(max_length=50)
    paymentReceipt   = models.ForeignKey(userPaymentReceipt, on_delete='PROTECT')
    totalAttendance  = models.IntegerField()
    totalDays        = models.DateField()
    package_amount   = models.IntegerField()
    paid_amount      = models.IntegerField()            # according to no. of days spent
    isActive         = models.BooleanField(default='true')
    description      = models.CharField(max_length=250)


class UserPaymentReceipt(models.Model):                 #to be send
    paymentId        = models.CharField(max_length=7, primary_key=True)  
    salary           = models.IntegerField()                 # paid_amount
    dateOfPayment    = models.DateField()
    modeOfPayment    = models.CharField(max_length=10)
    comments         = models.CharField(max_length=100)


#   need some changes ^



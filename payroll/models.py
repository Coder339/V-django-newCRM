from django.db import models
from accounts.models import UserEmployeeAccount

class EmployeePackage(models.Model):
    Id = models.CharField(max_length=50,primary_key=True)
    UserId = models.ForeignKey(UserEmployeeAccount,on_delete='CASCADE')
    package_amount   = models.IntegerField()
    description      = models.TextField(max_length=250)
    isActive         = models.BooleanField(default='true')


class UserEmployeePaymentBill(models.Model):
    userId           = models.models.CharField(max_length=20,primary_key=True)
    packageId        = models.ForeignKey(EmployeePackage,on_delete='CASCADE')
    totalAttendance  = models.IntegerField()
    totalDays        = models.DateField()
    paymentReceipt   = models.ForeignKey(userPaymentReceipt, on_delete='PROTECT')
    paid_amount      = models.IntegerField()            # according to no. of days spent



class UserPaymentReceipt(models.Model):                 #to be send
    paymentId        = models.CharField(max_length=20, primary_key=True)
    salary           = models.IntegerField()                 # paid_amount
    dateOfPayment    = models.DateField()
    modeOfPayment    = models.CharField(max_length=10)
    comments         = models.CharField(max_length=100)


#   need some changes ^


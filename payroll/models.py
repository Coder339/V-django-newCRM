from django.db import models
from accounts.models import EmployeeAccount


class UserPaymentReceipt(models.Model):  # to be send
    paymentId       = models.CharField(max_length=20, primary_key=True)
    salary          = models.IntegerField()  # paid_amount
    dateOfPayment   = models.DateField()
    modeOfPayment   = models.CharField(max_length=10)
    comments        = models.CharField(max_length=100)


class EmployeePackage(models.Model):
    Id              = models.CharField(max_length=50, primary_key=True)
    UserId          = models.ForeignKey(EmployeeAccount, on_delete=models.CASCADE)
    package_amount  = models.IntegerField()
    description     = models.TextField(max_length=250)
    isActive        = models.BooleanField(default='true')


class UserEmployeePaymentBill(models.Model):
    userId          = models.CharField(max_length=20, primary_key=True)
    packageId       = models.ForeignKey(EmployeePackage, on_delete=models.CASCADE)
    totalAttendance = models.IntegerField()
    totalDays       = models.DateField()
    paymentReceipt  = models.ForeignKey(UserPaymentReceipt, on_delete=models.CASCADE)
    paid_amount     = models.IntegerField()  # according to no. of days spent

# need some changes ^



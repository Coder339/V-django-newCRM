from django.db import models
from authentication.models import EmployeeProfile





class EmployeePackage(models.Model):
    Id              = models.CharField(max_length=50, primary_key=True)
    UserId          = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE)
    package_amount  = models.IntegerField()
    description     = models.TextField(max_length=250)
    isActive        = models.BooleanField(default='true')

    def __str__(self):
        return self.Id
    


class UserEmployeePaymentBill(models.Model):
    # userId          = models.CharField(max_length=20, primary_key=True)
    billId          = models.ForeignKey(EmployeePackage, on_delete=models.CASCADE)
    totalAttendance = models.IntegerField()
    totalDays       = models.IntegerField()
    # paymentReceipt  = models.ForeignKey(UserPaymentReceipt, on_delete=models.CASCADE)
    paid_amount     = models.IntegerField()  # according to no. of days spent

    def __str__(self):
        return self.billId.Id
    
    

class UserPaymentReceipt(models.Model):  # to be send
    months = (
        ('JAN','JAN'),('FEB','FEB'),('MAR','MAR'),('APR','APR'),
        ('MAY','MAY'),('JUN','JUN'),('JULY','JULY'),('AUG','AUG'),
        ('SEP','SEP'),('OCT','OCT'),('NOV','NOV'),('DEC','DEC'),
    )
    paymentId       = models.CharField(max_length=20, primary_key=True)
    ReceiptId       = models.ForeignKey(UserEmployeePaymentBill,on_delete=models.CASCADE)
    salary          = models.IntegerField()  # paid_amount
    salaryMonth     = models.CharField(max_length=20,choices=months,null=True)
    dateOfPayment   = models.DateField()
    modeOfPayment   = models.CharField(max_length=10)
    comments        = models.CharField(max_length=100)

    def __str__(self):
        return self.paymentId
    

# need some changes ^



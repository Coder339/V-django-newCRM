from django.db import models
from authentication.models import EmployeeProfile





class SalaryPackage(models.Model):  #static
    Id              = models.CharField(verbose_name = 'packageId',max_length=50, primary_key=True)
    EmpId           = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE)
    package_amount  = models.IntegerField()
    description     = models.TextField(max_length=250)
    isActive        = models.BooleanField(default='true')

    def __str__(self):
        return self.Id
    

class EmployeePackage(models.Model):  # to be send
    # months = (
    #     ('JAN','JAN'),('FEB','FEB'),('MAR','MAR'),('APR','APR'),
    #     ('MAY','MAY'),('JUN','JUN'),('JULY','JULY'),('AUG','AUG'),
    #     ('SEP','SEP'),('OCT','OCT'),('NOV','NOV'),('DEC','DEC'),
    # )

    Name                  = models.CharField(max_length=20,null=True)
    empId                 = models.ForeignKey(EmployeeProfile,on_delete=models.CASCADE,null=True,default = 1)
    packageId             = models.ForeignKey(SalaryPackage,on_delete=models.CASCADE,null=True,editable=False)
    salary                = models.IntegerField()  # paid_amount
    # salaryMonth     = models.CharField(max_length=20,choices=months,null=True)
    dateOfPayment         = models.DateField(null=True)
    modeOfPayment         = models.CharField(max_length=10)
    unpaid_leaves_allowed = models.PositiveIntegerField()
    paid_leaves_allowed   = models.PositiveIntegerField()
    comments              = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.Name

class MonthlySalary(models.Model):  #dynamic
    # userId          = models.CharField(max_length=20, primary_key=True)
    EmpId                      = models.ForeignKey(EmployeeProfile,on_delete=models.CASCADE,null=True)
    salaryId                   = models.ForeignKey(SalaryPackage, on_delete=models.CASCADE,editable=False,null=True)
    activeDays                 = models.PositiveIntegerField()
    workingDays                = models.PositiveIntegerField()
    # paymentReceipt  = models.ForeignKey(UserPaymentReceipt, on_delete=models.CASCADE)
    total_Salary_Amount        = models.PositiveIntegerField()  # according to no. of days spent

    def __str__(self):
        return self.EmpId.employee_id
    
    


    

# need some changes ^



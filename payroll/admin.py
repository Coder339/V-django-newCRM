from django.contrib import admin
from .models import UserEmployeePaymentBill,UserPaymentReceipt,EmployeePackage

admin.site.register(UserEmployeePaymentBill)
admin.site.register(UserPaymentReceipt)
admin.site.register(EmployeePackage)
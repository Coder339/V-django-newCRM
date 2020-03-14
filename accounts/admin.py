from django.contrib import admin
from .models import UserEmployeeAccount,UserCustomerAccount

admin.site.register(UserEmployeeAccount)
admin.site.register(UserCustomerAccount)

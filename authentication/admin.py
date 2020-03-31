# from django.contrib import admin
# from .models import EmployeeAccount,CustomerAccount,User
# # from django.contrib.auth.models import Group

# admin.site.register(User)
# admin.site.register(EmployeeAccount)
# admin.site.register(CustomerAccount)

from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User


admin.site.unregister(Group)
admin.site.register(EmployeeProfile)
admin.site.register(Customer)
admin.site.register(Vendor)
admin.site.register(Company)

class CustomUserAdmin(UserAdmin):
    model = User
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

admin.site.register(User, CustomUserAdmin)


# from django.db import models
# from django.forms import CheckboxSelectMultiple

# class MyModelAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         models.ManyToManyField: {'widget': CheckboxSelectMultiple},
#     }
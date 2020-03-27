# from django.contrib import admin
# from .models import EmployeeAccount,CustomerAccount,User
# # from django.contrib.auth.models import Group

# admin.site.register(User)
# admin.site.register(EmployeeAccount)
# admin.site.register(CustomerAccount)

from django.contrib import admin
from .models import EmployeeAccount,CustomerAccount
from django.contrib.auth.models import Group
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User


admin.site.unregister(Group)
admin.site.register(EmployeeAccount)
admin.site.register(CustomerAccount)





class CustomUserAdmin(UserAdmin):
    model = User
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

admin.site.register(User, CustomUserAdmin)



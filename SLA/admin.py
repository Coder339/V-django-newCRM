from django.contrib import admin
from .models import *
from django.db import models

class ticket_generate(admin.ModelAdmin):

    class Meta:
        model=SLA

    readonly_fields=['ticket_no']

    def autogenerate(self,obj):
        return str (obj.ticket_no)

admin.site.register(SLA,ticket_generate)
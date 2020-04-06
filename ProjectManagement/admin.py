from django.contrib import admin
from .models import *
#from authentication.models import *
from django.db import models
#InlineModelAdmin.model

admin.site.register(Business_opportunity)
admin.site.register(TodoList)

'''class MembersEntryInline(admin.TabularInline):          #addMembersInline has no attribute_meta
    model=Members
    extra=0

    def addmembers(self,object):
        return (team_members)

class ProjectAdmin(admin.ModelAdmin):
    Inlines=[MembersEntryInline]
    class Meta:
        model=Project
        Fieldsets=((None,{
            'fields':()
        }))'''



admin.site.register(Project)


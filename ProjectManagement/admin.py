from django.contrib import admin
from .models import *

admin.site.register(Business_opportunity)




class TeamInline(admin.TabularInline):
    model        =           Team
    extra         =         0


class ProjectAdmin(admin.ModelAdmin):
    inlines      =          [TeamInline]
    class Meta():
        model           =       Project
        fieldsets       =(
            (None,
            {
                'fields': ('project_name','description','start_date','project_deadline','owner','project_status','team_lead',)
            }
        ),
        )

admin.site.register(Project,ProjectAdmin)
#admin.site.register(Team)
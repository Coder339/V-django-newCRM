from django.urls import path
from . import views

urlpatterns = [

        # path('mail',views.index),
         path('Business_opportunity/',views.Business_opportunityListAPIView.as_view(),name='details'),
        path('Business_opportunity/add/',views.Business_opportunityCreateAPIView.as_view(),name='add'),
        path('Business_opportunity/<project_name>/edit/',views.Business_opportunityUpdateAPIView.as_view(),name='put'),
        path('Project/',views.ProjectListAPIView.as_view(),name='details'),
        path('Project/add/',views.ProjectCreateAPIView.as_view(),name='add'),
        path('Project/<project_name>/edit/',views.ProjectUpdateAPIView.as_view(),name='put'),
        # path('Team/',views.TeamListAPIView.as_view(),name='details'),
        # path('Team/add/',views.TeamCreateAPIView.as_view(),name='add'),
        # path('Team/<name>/edit/',views.TeamUpdateAPIView.as_view(),name='put'),


        #path('',views.ProjectManagement,name='project')
        
]

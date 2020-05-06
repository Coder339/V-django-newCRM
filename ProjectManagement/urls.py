from django.urls import path
from . import views

urlpatterns = [

        # path('mail',views.index),

         path('Business_opportunity/',views.Business_opportunityList.as_view(),name='details'),
        # path('Business_opportunity/<project_name>/edit/',views.Business_opportunityUpdateAPIView.as_view(),name='put'),
         path('Project/',views.ProjectList.as_view(),name='details'),
        # path('Project/<project_name>/edit/',views.ProjectUpdateAPIView.as_view(),name='put'),
         path('Team/',views.TeamList.as_view(),name='details'),
        # path('Team/<name>/edit/',views.TeamUpdateAPIView.as_view(),name='put'),

        #path('',views.ProjectManagement,name='project')
        
]

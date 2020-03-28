from django.urls import path
from . import views
urlpatterns = [
        path('mail',views.index),
        path('Business_opportunity',views.Business_opprotunityListAPIView.as_view(),name='details'),
        path('Business_opportunity',views.Business_opportunityCreateAPIView.as_view(),name='add'),
        path('Business_opportunity/<project_name>/edit/',views.Business_opportunityUpdateAPIView.as_view(),name='put'),
        path('Project',views.ProjectListAPIView.as_view(),name='details'),
        path('Project',views.ProjectCreateAPIView.as_view(),name='add'),
        path('Project/<project_name>/edit/',views.ProjectUpdateAPIView.as_view(),name='put'),
        path('Task',views.TaskListAPIView.as_view(),name='details'),
        path('Task',views.TaskCreateAPIView.as_view(),name='add'),
        path('Task/<name>/edit/',views.TaskUpdateAPIView.as_view(),name='put'),
        path('TodoList',views.TodoListListAPIView.as_view(),name='details'),
        path('TodoList',views.TodoListCreateAPIView.as_view(),name='add'),
        path('TodoList/<name>/edit/',views.TodoListUpdateAPIView.as_view(),name='put'),
        ]

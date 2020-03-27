from django.urls import path
from . import views

urlpatterns = [
    path('department',views.ListDepartmentView.as_view(),name = 'details'),
    path('department/add/',views.CreateDepartmentView.as_view(),name = 'add'),
    path('department/<deptId>/edit/',views.UpdateDepartmentView.as_view(),name = 'put'),

    # path('profile',views.ListStaffProfileView.as_view(),name = 'details'),
    # path('profile/add/',views.CreateStaffProfileView.as_view(),name = 'add'),
    # path('profile/<pk>/edit/',views.UpdateStaffProfileView.as_view(),name = 'put'),

    path('role',views.ListStaffRoleView.as_view(),name = 'details'),
    path('role/add/',views.CreateStaffRoleView.as_view(),name = 'add'),
    path('role/<pk>/edit/',views.UpdateStaffRoleView.as_view(),name = 'put'),
    

]
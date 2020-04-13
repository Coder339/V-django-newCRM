from django.urls import path
from . import views

urlpatterns = [
    path('department',views.ListDepartmentView.as_view(),name = 'details'),
    path('department/add/',views.CreateDepartmentView.as_view(),name = 'add'),
    path('department/<deptId>/edit/',views.UpdateDepartmentView.as_view(),name = 'put'),

    # path('profile',views.ListStaffProfileView.as_view(),name = 'details'),
    # path('profile/add/',views.CreateStaffProfileView.as_view(),name = 'add'),
    # path('profile/<pk>/edit/',views.UpdateStaffProfileView.as_view(),name = 'put'),

    path('role',views.ListStaffProfileView.as_view(),name = 'details'),
    path('role/add/',views.CreateStaffProfileView.as_view(),name = 'add'),
    path('role/<pk>/edit/',views.UpdateStaffProfileView.as_view(),name = 'put'),
    
    path('',views.hr,name='hr'),

    path('dept/', views.dept, name = 'dept'),
    path('dept/<pk>/', views.deptinfo, name = 'deptinfo'),
    path('create_department/', views.createdept, name = 'createdept'),
    path('update_department/<pk>/',views.updatedept,name='update_dept'),
    path('delete_dept/<pk>/',views.deleteDept,name='delete_dept'),
   


    path('staff/', views.staff, name = 'staff'),
    path('staff/<pk>/', views.staffinfo, name = 'staffinfo'),
    path('create_staff/', views.createstaff, name = 'createstaff'),
    path('update_staff/<pk>/',views.updatestaff,name='update_staff'),
    path('delete_staff/<pk>/',views.deleteStaff,name='delete_staff'),

]
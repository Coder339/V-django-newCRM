from django.urls import path
from authentication import views


urlpatterns = [
    path('',views.ListUserView.as_view(),name = 'details'),
    path('user/add/',views.CreateUserView.as_view(),name = 'add'),
    path('user/<pk>/edit/',views.UpdateUserView.as_view(),name = 'put'),
    
    path('profile/',views.ListProfileView.as_view(),name = 'details'),
    path('profile/add/',views.CreateProfileView.as_view(),name = 'add'),
    path('profile/<pk>/edit/',views.UpdateProfileView.as_view(),name = 'put'),
    

    
]


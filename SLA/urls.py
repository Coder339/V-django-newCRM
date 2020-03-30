from django.urls import path
from .import views

urlpatterns = [
        path('', views.SLAListAPIView.as_view(), name='details'),
        path('add/', views.SLACreateAPIView.as_view(), name='add'),
        path('<pk>/edit/', views.SLAUpdateAPIView.as_view(), name='put'),
        # path('Escalation', views.EscalationListAPIView.as_view(), name='details'),
        # path('Escalation', views.EscalationCreateAPIView.as_view(), name='add'),
        # path('Escalation/<ticket_no>/edit/', views.EscalationUpdateAPIView.as_view(), name='put'),
]
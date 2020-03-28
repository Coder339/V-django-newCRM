from django.urls import path
from .import views

urlpatterns = [
        path('SLA', views.SLAListAPIView.as_view(), name='details'),
        path('SLA', views.SLACreateAPIView.as_view(), name='add'),
        path('SLA/<ticket_no>/edit/', views.SLAUpdateAPIView.as_view(), name='put'),
        path('Escalation', views.EscalationListAPIView.as_view(), name='details'),
        path('Escalation', views.EscalationCreateAPIView.as_view(), name='add'),
        path('Escalation/<ticket_no>/edit/', views.EscalationUpdateAPIView.as_view(), name='put'),
]
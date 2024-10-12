from django.urls import path
from .views import TaskAPIView, RegisterAPIView

urlpatterns = [
    path('auth/register/', RegisterAPIView.as_view(), name='register'),
    path('tasks/', TaskAPIView.as_view(), name='task-list-create'), 
    path('tasks/<int:task_id>/', TaskAPIView.as_view(), name='task-retrieve-update-delete'),  
]

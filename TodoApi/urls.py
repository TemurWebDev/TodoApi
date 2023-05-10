from django.urls import path
from .views import TaskallApiView,TaskCrudApiView,TaskStatusView

urlpatterns = [
    path('api/tasks/', TaskallApiView.as_view()),
    path('api/tasks/<int:pk>/', TaskCrudApiView.as_view()),
    path('api/tasks/<str:pk>/', TaskStatusView.as_view()),

]

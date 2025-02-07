from django.urls import path
from .views import TareaListCreate, TareaDetailUpdateDelete

urlpatterns = [
    path('tareas/', TareaListCreate.as_view(), name='tarea-list-create'),
    path('tareas/<int:pk>/', TareaDetailUpdateDelete.as_view(), name='tarea-detail'),
]
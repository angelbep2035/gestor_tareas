from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist
from .models import Tarea, Usuario
from .serializers import TareaSerializer

class TareaListCreate(generics.ListCreateAPIView):
    serializer_class = TareaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Filtra las tareas solo del usuario autenticado"""
        try:
            usuario = Usuario.objects.get(username=self.request.user.username)
            return Tarea.objects.filter(owner=usuario)
        except ObjectDoesNotExist:
            return Tarea.objects.none()  # Devuelve una lista vacía si el usuario no existe

    def perform_create(self, serializer):
        """Asigna automáticamente el usuario autenticado al crear una tarea"""
        try:
            usuario = Usuario.objects.get(username=self.request.user.username)
            serializer.save(owner=usuario)
        except ObjectDoesNotExist:
            pass  # No guarda nada si el usuario no existe

class TareaDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TareaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Filtra las tareas solo del usuario autenticado"""
        try:
            usuario = Usuario.objects.get(username=self.request.user.username)
            return Tarea.objects.filter(owner=usuario)
        except ObjectDoesNotExist:
            return Tarea.objects.none()

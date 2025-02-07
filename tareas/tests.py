from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from rest_framework import status
from tareas.models import Usuario, Tarea

class TareaTestCase(APITestCase):

    def setUp(self):
        self.usuario = Usuario.objects.create_user(username="testuser", password="testpass")
        self.client.force_authenticate(user=self.usuario)
    
    def test_crear_tarea(self):
        data = {"title": "Nueva Tarea", "description": "Descripción de prueba", "completed": False}
        response = self.client.post("/api/tareas/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_listar_tareas(self):
        response = self.client.get("/api/tareas/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_validacion_titulo(self):
        data = {"title": "No", "description": "Muy corto", "completed": False}
        response = self.client.post("/api/tareas/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

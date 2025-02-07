# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
# Modelo de Usuario
class Usuario(AbstractUser):
    
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="usuarios",
        blank=True
    )
    
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="usuarios_permisos",
        blank=True
    )

    def __str__(self):
        return self.username

# Modelo de Tarea
class Tarea(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)  # Opcional
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
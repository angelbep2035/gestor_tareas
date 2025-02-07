from rest_framework import serializers
from .models import Usuario, Tarea

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'is_active']

class TareaSerializer(serializers.ModelSerializer):

    title = serializers.CharField(min_length=3)
        
    class Meta:
        model = Tarea
        exclude = ['owner']  # Excluye owner para que no pueda ser enviado en la petición

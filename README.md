Requisitos: 
Tener python y git instalados 

//Clonar el Repositorio
git clone https://github.com/angelbep2035/gestor_tareas.git
cd gestor_tareas

Crear un Entorno Virtual
python -m venv venv

//Activar el Entorno Virtual
venv\Scripts\activate

//Instalar Dependencias
pip install -r requirements.txt


//Aplicar Migraciones (Base de Datos)
python manage.py makemigrations tareas
python manage.py migrate

Crear un Usuario Administrador (Opcional para Django Admin)
python manage.py createsuperuser

//Crear usuario normal
python manage.py shell
from tareas.models import Usuario
usuario = Usuario.objects.create_user(username="usuario", email="usuario@example.com", password="contraseña")
exit()

//Ejecutar el Servidor
python manage.py runserver

//Pruebas Unitarias
python manage.py test

Documentación Swagger
Se ha integrado drf-yasg para generar documentación interactiva.
Swagger UI: http://127.0.0.1:8000/swagger/
Redoc: http://127.0.0.1:8000/redoc/
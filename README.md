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

//Creación de usuarios en la base de datos
python manage.py shell
from django.contrib.auth.hashers import make_password
print(make_password("TuContraseñaSegura"))
//Ejemplo salida: pbkdf2_sha256$870000$DGwxpKuS4hG5xGyYf3n2dJ$ZnIqG313vJWw1DYT9gLJAXwjygbPK7f71ZzACCLUX4Q=

//Insertar un usuario en PostgreSQL directamente
INSERT INTO tareas_usuario (username, email, password, first_name, last_name, is_superuser, is_staff, is_active, date_joined)
VALUES ('admin', 'admin@example.com', 'pbkdf2_sha256$870000$DGwxpKuS4hG5xGyYf3n2dJ$ZnIqG313vJWw1DYT9gLJAXwjygbPK7f71ZzACCLUX4Q=', 'Admin', 'User', TRUE, TRUE, TRUE, NOW());

Crear usuario normal desde Django Shell
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
Swagger UI: https://gestor-tareas-sq08.onrender.com/swagger/
Redoc: https://gestor-tareas-sq08.onrender.com/redoc/
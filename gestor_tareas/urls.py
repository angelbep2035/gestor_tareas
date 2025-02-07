from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# Configuración de Swagger/OpenAPI
schema_view = get_schema_view(
    openapi.Info(
        title="Gestor de Tareas API",
        default_version='v1',
        description="API para la gestión de tareas con Django REST Framework",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="tuemail@ejemplo.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Añadir seguridad JWT manualmente
from drf_yasg.inspectors import SwaggerAutoSchema

class JWTSecurityAutoSchema(SwaggerAutoSchema):
    def get_security_definitions(self):
        return {
            "Bearer": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header"
            }
        }

    def get_security_requirements(self):
        return [{"Bearer": []}]

# Aplicar el esquema de seguridad JWT a todas las vistas
schema_view = get_schema_view(
    openapi.Info(
        title="Gestor de Tareas API",
        default_version='v1',
        description="API para la gestión de tareas con Django REST Framework",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="tuemail@ejemplo.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Sobrescribir el esquema de seguridad en Swagger
from drf_yasg.generators import OpenAPISchemaGenerator

class JWTSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.securityDefinitions = {
            "Bearer": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header"
            }
        }
        schema.security = [{"Bearer": []}]
        return schema

schema_view = get_schema_view(
    openapi.Info(
        title="Gestor de Tareas API",
        default_version='v1',
        description="API para la gestión de tareas con Django REST Framework",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="tuemail@ejemplo.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    generator_class=JWTSchemaGenerator,  # Usar el generador personalizado
)

urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta del panel de administración de Django
    path('api/', include('tareas.urls')),  # Rutas de la aplicación "tareas"

    # Rutas de autenticación con JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Documentación con Swagger/OpenAPI
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
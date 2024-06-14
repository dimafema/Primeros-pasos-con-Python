"""
URL configuration for incidencias project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.panel_crear, name='inicio'),
    path('crear_zona/', views.crear_zona, name='crear_zona'), 
    path('crear_parque/', views.crear_parque, name='crear_parque'),
    path('crear_brigada/', views.crear_brigada, name='crear_brigada'),
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('edit_usuario/<int:id>/', views.editar_usuario, name='editar_usuario'),
    path('list_delete/', views.list_delete_user, name='list_delete'),
    path('list_edit/', views.list_edit_user, name='list_edit'),
    path('eliminar_usuario/<int:id>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('list_vacaciones/', views.list_vacaciones_user, name='list_vacaciones'),
    path('vacaciones_usuario/<int:id>/', views.crear_permisos, name='vacaciones_usuario'),
    
]
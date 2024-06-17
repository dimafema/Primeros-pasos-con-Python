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
    path('edit_zona/<int:id>/', views.editar_zona, name='editar_zona'),
    path('list_edit_zona/', views.list_edit_zona, name='list_edit_zona'),
    path('eliminar_zona/<int:id>/', views.eliminar_zona, name='eliminar_zona'),
    path('list_delete_zona/', views.list_delete_zona, name='list_delete_zona'),
    
    path('crear_parque/', views.crear_parque, name='crear_parque'),
    path('edit_parque/<int:id>/', views.editar_parque, name='editar_parque'),
    path('list_edit_parque/', views.list_edit_parque, name='list_edit_parque'),
    path('eliminar_parque/<int:id>/', views.eliminar_parque, name='eliminar_parque'),
    path('list_delete_parque/', views.list_delete_parque, name='list_delete_parque'),
    
    path('crear_brigada/', views.crear_brigada, name='crear_brigada'),
    path('edit_brigada/<int:id>/', views.editar_brigada, name='editar_brigada'),
    path('list_edit_brigada/', views.list_edit_brigada, name='list_edit_brigada'),
    path('eliminar_brigada/<int:id>/', views.eliminar_brigada, name='eliminar_brigada'),
    path('list_delete_brigada/', views.list_delete_brigada, name='list_delete_brigada'),
    
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('edit_usuario/<int:id>/', views.editar_usuario, name='editar_user'),
    path('list_edit_user/', views.list_edit_user, name='list_edit_user'),
    path('eliminar_usuario/<int:id>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('list_delete_user/', views.list_delete_user, name='list_delete_user'),
    
    
    path('list_vacaciones/', views.list_vacaciones_user, name='list_vacaciones'),
    path('vacaciones_usuario/', views.crear_vacaciones, name='vacaciones_usuario'),
    
]
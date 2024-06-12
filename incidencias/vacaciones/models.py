from django.db import models

# Create your models here.
class Zona(models.Model):
    nombre = models.CharField(max_length=100)

class Parque(models.Model):
    codigo_parque = models.CharField(max_length=100, unique=True)
    nombre = models.CharField(max_length=100)

class Brigada(models.Model):
    nombre = models.CharField(max_length=100)
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    numero_casco = models.CharField(max_length=100)
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE)
    parque = models.ForeignKey(Parque, on_delete=models.CASCADE)
    brigada = models.ForeignKey(Brigada, on_delete=models.CASCADE)

class Vacaciones(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    dias_totales = models.IntegerField()
    estado = models.CharField(max_length=100)
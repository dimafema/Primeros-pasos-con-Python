from django.db import models

# Create your models here.
class Zona(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Parque(models.Model):
    codigo_parque = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Brigada(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
    
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    numero_casco = models.IntegerField(unique=True)
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE)
    parque = models.ForeignKey(Parque, on_delete=models.CASCADE)
    brigada = models.ForeignKey(Brigada, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre + ' ' + str(self.numero_casco);

class Vacaciones(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    dias_totales = models.IntegerField(blank=True, null=True)
    disfrutada = models.BooleanField(default=False)
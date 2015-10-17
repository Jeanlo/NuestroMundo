from django.db import models

# Create your models here.
class Pais(models.Model):
    codigo = models.CharField(max_length=3)
    nombre = models.CharField(max_length=60)
    continente = models.CharField(max_length=60)
    region = models.CharField(max_length=40)
    area = models.DecimalField(max_digits=22, decimal_places=2)
    independencia = models.IntegerField(default=1948)
    poblacion = models.IntegerField(default=1000000)
    esperanza_vida = models.DecimalField(max_digits=3, decimal_places=1)
    PIB = models.DecimalField(max_digits=18, decimal_places=2)
    PIB_anterior = models.DecimalField(max_digits=18, decimal_places=2)
    nombre_local = models.CharField(max_length=60)
    tipo_gobierno = models.CharField(max_length=80)
    lider_estado = models.CharField(max_length=60)
    capital = models.IntegerField()
    codigo_corto = models.CharField(max_length=2)
    def __str__(self):              
        return self.nombre + ", " + self.continente
	
class Ciudad(models.Model):
    nombre = models.CharField(max_length=60)
    codigo_pais = models.CharField(max_length=3)
    distrito = models.CharField(max_length=60)
    poblacion = models.IntegerField(default=10000)
    def __str__(self):              
        return self.nombre
	
class Idioma_Pais(models.Model):
    codigo_pais = models.CharField(max_length=3)
    idioma = models.CharField(max_length=40)	
    porcentaje = models.DecimalField(max_digits=3, decimal_places=1)
    def __str__(self):              
        return self.idioma

class Idioma(models.Model):
    nombre = models.CharField(max_length=40)
    def __str__(self):              
        return self.nombre
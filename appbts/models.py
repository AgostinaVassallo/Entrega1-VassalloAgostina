from django.db import models

# Create your models here.

#titulo subtitulo imagen fecha autor

class Bts(models.Model):
    # trayectoria=models.CharField(max_length=50)
    integrantes=models.CharField(max_length=200)
    #edadcoreana= models.Intergerfield(label="edad coreana") 
    #carrera_musical=models.CharField(max_length=50)
    def __str__(self):
        return ("BTS")

class Coreasur(models.Model):
    #historia=models.CharField(max_length=50)
    #industria_cultural=models.CharField(max_length=50)
    soft_power=models.CharField(max_length=200)
   #servicio_militar=models.CharField(max_length=50)
    def __str__(self):
        return ("Corea del Sur")

class Army(models.Model):
    resumen=models.CharField(max_length=200)
    #capital_economico=models.CharField(max_length=50)
    #influencia=models.CharField(max_length=50)
    def __str__(self):
        return ("Army")



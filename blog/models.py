from audioop import maxpp
from datetime import datetime
from django.db import models
from django.utils import timezone

class Posteos(models.Model):
    Titulo=models.CharField(max_length=40)
    Autor=models.CharField(max_length=20)
    Texto=models.TextField(default="Texto de Prueba")
    Fecha=models.DateTimeField(datetime.now)

class Suscriptores(models.Model):
    Nombre=models.CharField(max_length=20)
    Email=models.EmailField()
    Telefono=models.CharField(max_length=10)
    Gusto=models.BooleanField()

class Contacto(models.Model):
    Nombre=models.CharField(max_length=20)
    Email=models.EmailField()
    Texto=models.TextField()

class Busqueda(models.Model):
    Texto=models.TextField()
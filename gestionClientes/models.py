from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=12)
    comuna = models.CharField(max_length=50)
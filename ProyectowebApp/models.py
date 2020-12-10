from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=10)
    comuna = models.CharField(max_length=50)
    class Meta:
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'
    
    def __str__(self):
        return self.nombre
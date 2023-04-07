from django.db import models

# Create your models here.

class Usuario(models.Model):

    nombre_usuario = models.CharField(max_length= 15)
    email = models.EmailField(max_length= 30)
    contraseña = models.CharField(max_length= 2000)
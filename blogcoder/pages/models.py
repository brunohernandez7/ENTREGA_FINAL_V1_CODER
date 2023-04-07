from django.db import models

# Create your models here.

class Blog(models.Model):

    titulo = models.CharField(max_length= 100)
    resumen = models.CharField(max_length= 500)
    texto = models.CharField(max_length= 2000)

    def __str__(self):
        return f"Titulo: {self.titulo}"


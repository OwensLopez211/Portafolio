from django.db import models

# Create your models here.

class proyectos(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=100)
    image = models.ImageField(upload_to='proyectos/img')
    url = models.URLField(blank=True)

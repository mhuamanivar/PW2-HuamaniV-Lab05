from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

class Personal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Ingreso de identificación')
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    email = models.EmailField()
    
    class Meta:
        ordering = ['apellido', 'nombre']

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])


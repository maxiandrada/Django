from django.db import models
from django.urls import reverse

# Create your models here.
class Negocio(models.Model):
	"""
	Modelo que representa un negocio
	"""
	nombre = models.CharField(max_length=100)
	comentarios = models.CharField(max_length=400, default='')
	mail = models.CharField(max_length=100)

	def __str__(self):
 		return self.nombre

class Noticia(models.Model):
	"""
	Modelo que representa un Idioma
	"""
	titulo = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=400, default='')
	fecha = models.DateField(null=True, blank=True)
	
	TIPO_NOTICIA = (
		('Cafayate','Cafayate'),
		('Policiales','Policiales'),
		('Deportes','Deportes'),
		('Clasificados','Clasificados'),
		('Vacaciones','Vacaciones'),
		('Salud', 'Salud'),
		('Tecnología', 'Tecnología'),
	)

	noticia_choice = models.CharField(max_length=50, choices=TIPO_NOTICIA, blank=True, default='d',
							help_text='Seccion de Noticia')
	
	# class Meta:
	# 	ordering = ["fechaDevolucion"]
	
	def __str__(self):
		return self.noticia_choice



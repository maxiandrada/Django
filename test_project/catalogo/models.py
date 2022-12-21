from django.db import models
from django.urls import reverse
import uuid # Requerida para las instancias de libros únicos

# Create your models here.
class Genero(models.Model):
	"""
	Modelo que representa un género literario
	"""
	nombre = models.CharField(max_length=50, help_text="Ingrese el nombre del género (xej. Programación, BD, SO, etc)")
	
	def __str__(self):
 		return self.nombre

class Idioma(models.Model):
	"""
	Modelo que representa un Idioma
	"""
	idioma = models.CharField(max_length=100)
	
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, 
		help_text="ID idioma")
	
	TIPO_IDIOMA = (
		('esp', 'Español'),
		('eng', 'Ingles'),
		('por', 'Portugues'),
		('jap', 'Japones'),
	)

	idioma_choice = models.CharField(max_length=4, choices=TIPO_IDIOMA, blank=True, default='d',
							help_text='Idioma')
	
	# class Meta:
	# 	ordering = ["fechaDevolucion"]
	
	def __str__(self):
		return self.idioma_choice


class Autor(models.Model):
	"""
	Modelo que representa un autor
	"""
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	fechaNac = models.DateField(null=True, blank=True)
	fechaDeceso = models.DateField('Fallecido', null=True, blank=True)

	# Devuelve la url para acceder a un autor.	
	def get_absolute_url(self):
		return reverse('autorInfo', args=[str(self.id)])
	
	# Para imprimir en pantalla
	def __str__(self):
		return '%s, %s' % (self.nombre, self.apellido)


class Libro(models.Model):
	"""
	Modelo que representa un libro (no un Ejemplar)
	"""
	titulo = models.CharField(max_length=200)
	
	# autor: ForeignKey, ya que un libro tiene un solo autor, pero el mismo autor puede haber escrito muchos libros.
	autor = models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True)
	resumen = models.TextField(max_length=1000, help_text="Ingrese un resumen del libro")
	isbn = models.CharField('ISBN',max_length=13,
	help_text='13 Caracteres <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
	
	# genero: ManyToManyField, porque un género puede contener muchos libros y un libro puede cubrir varios géneros.
	genero = models.ManyToManyField(Genero, help_text="Seleccione un genero (o varios) para el libro")
	
	# La clase Genero ya fue definida, entonces podemos especificar el objeto arriba.

	idioma = models.ForeignKey(Idioma, on_delete=models.SET_NULL, null=True)

	def get_absolute_url(self):
		return reverse('LibroInfo', args=[str(self.id)])
	
	def __str__(self):
		return self.titulo

	def muestra_genero(self):
		return ', '.join([ genero.nombre for genero in self.genero.all()[:3]]) #solo muestra tres generos
	muestra_genero.short_description = 'Género/s'


class Ejemplar(models.Model):
	"""
	Modelo que representa un ejemplar de un libro.
	"""
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, 
		help_text="ID único para este libro particular en toda la biblioteca")

	libro = models.ForeignKey(Libro, on_delete=models.SET_NULL, null=True)
	fechaDevolucion = models.DateField(null=True, blank=True)
	
	ESTADO_EJEMPLAR = (
		('m', 'en Mantenimiento'),
		('p', 'Prestado'),
		('d', 'Disponible'),
		('r', 'Reservado'),
	)

	estado = models.CharField(max_length=1, choices=ESTADO_EJEMPLAR, blank=True, default='d',
							  help_text='Disponibilidad del Ejemplar')
	
	class Meta:
		ordering = ["fechaDevolucion"]
	
	def __str__(self):
		return '%s (%s)' % (self.id,self.libro.titulo)


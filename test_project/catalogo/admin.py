from django.contrib import admin
from catalogo.models import Autor, Genero, Idioma, Libro, Ejemplar
# from catalogo.models import Autor, Genero, Libro, Ejemplar

# Register your models here.
# admin.site.register(Autor)
admin.site.register(Genero)
admin.site.register(Idioma) # dejar esta línea como está ;)
# admin.site.register(Libro)
admin.site.register(Ejemplar)

# Define la clase Admin
class AutorAdmin(admin.ModelAdmin):
	# list_display = ('nombre', 'apellido', 'fechaNac', 'fechaDeceso')
	list_display = ('nombre', 'apellido', 'fechaNac')
	list_filter = ('nombre', 'apellido')

class LibroAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'autor', 'idioma', 'muestra_genero')
	
	# list_filter = ('titulo', 'autor', 'genero')
	

# Registra la clase Admin junto al modelo base
admin.site.register(Autor, AutorAdmin)
admin.site.register(Libro, LibroAdmin)

from django.contrib import admin

# Register your models here.
from compraEnCafa.models import Negocio, Noticia, Usuario

# admin.site.register(Negocio)
# admin.site.register(Noticia)

# Define la clase Admin
class NegocioAdmin(admin.ModelAdmin):
	# list_display = ('nombre', 'apellido', 'fechaNac', 'fechaDeceso')
	list_display = ('nombre', 'mail')
	list_filter = ('nombre', 'mail')

class NoticiaAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'fecha', 'noticia_choice')
	
	# list_filter = ('titulo', 'autor', 'genero')
	
class UsuarioAdmin(admin.ModelAdmin):
	list_display = ('dni', 'nombres', 'apellidos', 'usuario_choice')

# Registra la clase Admin junto al modelo base
admin.site.register(Negocio, NegocioAdmin)
admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Usuario, UsuarioAdmin)
from django.shortcuts import render

# Create your views here.
# def hello2(request):
# 	return render(request, 'hello2.html', {})

# def index(request):
# 	return render(request, 'index.html', {})

from compraEnCafa.models import Negocio, Noticia

def index(request):
	nroNegocios=Negocio.objects.all().count()
	nroNoticias=Noticia.objects.all().count()

	# nroLibros=Libro.objects.all().count()
	# nroEjemplares=Ejemplar.objects.all().count()
	# nroDisponibles=Ejemplar.objects.filter(estado__exact='d').count()
	# nroAutores=Autor.objects.count() # El 'all()' esta implícito por defecto (no se necesita).

	context = {
		'nroNegocios':nroNegocios,
		'nroNoticias':nroNoticias,
	}

	return render(request, 'index.html',context)


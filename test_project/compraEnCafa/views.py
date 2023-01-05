from django.shortcuts import render

# Create your views here.
# def hello2(request):
# 	return render(request, 'hello2.html', {})

# def index(request):
# 	return render(request, 'index.html', {})

from compraEnCafa.models import Negocio, Noticia, Usuario

def index(request):
	nroNegocios=Negocio.objects.all().count()
	nroNoticias=Noticia.objects.all().count()

	# nroNegocios=Libro.objects.all().count()
	# nroNoticias=Ejemplar.objects.all().count()
	# nroDisponibles=Ejemplar.objects.filter(estado__exact='d').count()
	# nroAutores=Autor.objects.count() # El 'all()' esta implícito por defecto (no se necesita).

	context = {
		'nroNegocios':nroNegocios,
		'nroNoticias':nroNoticias,
	}

	return render(request, 'index.html',context)

def noticias(request):
	notices = Noticia.objects.all()

	context = {
		'notices': notices
	}

	return render(request, 'noticias.html',context)

def noticiaDetalles(request, pk):
	notice = Noticia.objects.get(pk=pk)

	context = {
		'notice': notice
	}

	return render(request, 'noticiaDetalles.html', context)

def negocios(request):
	nroNegocios=Negocio.objects.all().count()
	nroNoticias=Noticia.objects.all().count()

	context = {
		'nroNegocios':nroNegocios,
		'nroNoticias':nroNoticias,
	}

	return render(request, 'negocios.html',context)

def usuarios(request):
	nroNegocios=Negocio.objects.all().count()
	nroNoticias=Noticia.objects.all().count()

	context = {
		'nroNegocios':nroNegocios,
		'nroNoticias':nroNoticias,
	}

	return render(request, 'usuarios.html',context)

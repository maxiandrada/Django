from django.shortcuts import render

# Create your views here.
# def hello2(request):
# 	return render(request, 'hello2.html', {})

# def index(request):
# 	return render(request, 'index.html', {})

from catalogo.models import Idioma, Genero, Libro, Ejemplar, Autor

def index(request):
	nroGeneros=Genero.objects.all().count()
	nroIdiomas=Idioma.objects.all().count()

	nroLibros=Libro.objects.all().count()
	nroEjemplares=Ejemplar.objects.all().count()
	nroDisponibles=Ejemplar.objects.filter(estado__exact='d').count()
	nroAutores=Autor.objects.count() # El 'all()' esta implícito por defecto (no se necesita).

	context = {
		'nroGeneros':nroGeneros,
		'nroIdiomas':nroIdiomas,
		'nroLibros':nroLibros,
		'nroEjemplares': nroEjemplares,
		'nroDisponibles': nroDisponibles,
		'nroAutoress': nroAutores,
	}

	return render(request, 'index.html',context)

from django.views import generic

class LibroListView(generic.ListView):
	model = Libro
	paginate_by = 2

	context_object_name = 'libros'
	# en este caso va un modelo
	
	queryset = Libro.objects.all()
	# si quiero filtrar
	
	template_name='libros.html'
	# nombre del template
	
	def get_context_data(self, **kwargs):
		libros = Libro.objects.all()
		context = super(LibroListView,
		self).get_context_data(**kwargs)
		context['libros'] = libros

		return context


from django.shortcuts import redirect, get_object_or_404
from catalogo.forms import GeneroForm, AutorForm


def genero_new(request):
	if request.method == "POST":
		formulario = GeneroForm(request.POST)
		if formulario.is_valid():
			genero = formulario.save(commit=False)
			genero.nombre = formulario.cleaned_data['nombre']
			genero.save()
			return redirect('generos')
	else:
		formulario = GeneroForm()
	
	return render(request, 'genero_new.html', {'formulario': formulario})


def genero_update(request, pk):
	genero = get_object_or_404(Genero, pk=pk)
	
	if request.method == "POST":
		formulario = GeneroForm(request.POST, instance=genero)
		if formulario.is_valid():
			genero = formulario.save(commit=False)
			genero.nombre = formulario.cleaned_data['nombre']
			genero.save()
			return redirect('generos')
	else:
		formulario = GeneroForm(instance=genero)
	
	return render(request, 'genero_new.html', {'formulario': formulario})




class GeneroListView(generic.ListView):
	model = Genero
	paginate_by = 2

	context_object_name = 'generos'
	# en este caso va un modelo
	
	queryset = Genero.objects.all()
	# si quiero filtrar
	
	template_name='generos.html'
	# nombre del template
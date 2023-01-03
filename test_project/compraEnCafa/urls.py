from django.urls import path
from compraEnCafa import views

urlpatterns = [
	path('', views.index, name='index'),
	path('compraEnCafa/', views.index, name='index'),
	path('compraEnCafa/noticias', views.noticias, name='noticias'),
	path('compraEnCafa/negocios', views.negocios, name='negocios'),
	
	# path('generos/', views.GeneroListView.as_view(), name='generos'),
	# path('genero/new/', views.genero_new, name='genero_new'),
	# path('genero/update/<pk>', views.genero_update, name='genero_update'),
]

# path('', views.index, name='index'),
# Estamos por matchear:
# - el home o el comportamiento del home (como va a acceder el usuario): path('', ...) .
# - Busca una "funcion de vista" que se llama 'index': path('', views.index, ...)
# - Alias 'index' sirve para invocar la funcion de vista en el template: path(..., name='index'),



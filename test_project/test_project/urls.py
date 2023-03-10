"""test_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 
# from catalogo import views
# from catalogo import forms
# from compraEnCafa import views
# from compraEnCafa import forms

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include('hello.urls')),
    # path('catalogo/admin/', admin.site.urls),
    # path('catalogo/', include('catalogo.urls')),
    # path('libros/', views.LibroListView.as_view(), name='libros'),
    # path('generos/', views.GeneroListView.as_view(), name='generos'),
    # path('portfolio/', include('portfolio.urls')),
    path('compraEnCafa/admin', admin.site.urls),
    path('compraEnCafa/', include('compraEnCafa.urls')),
    path('', include('compraEnCafa.urls')),
]

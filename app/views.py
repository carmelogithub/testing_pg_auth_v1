from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Producto, Categoria
from django.urls import reverse_lazy

class ProductoListView(ListView):
    model = Producto
    template_name = 'app/lista.html'

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'app/lista_categorias.html'
class ProductoCreateView(CreateView):
    model = Producto
    fields = ['nombre', 'unidades','precio','categoria']
    template_name = 'app/formulario.html'
    success_url = reverse_lazy('lista_productos')

class CategoriaCreateView(CreateView):
    model = Categoria
    fields = ['nombre', 'descripcion']
    template_name = 'app/formulario_categorias.html'
    success_url = reverse_lazy('lista_categorias')

class ProductoUpdateView(UpdateView, LoginRequiredMixin):
    model = Producto
    fields = ['nombre', 'unidades','precio','categoria']
    template_name = 'app/formulario.html'
    success_url = reverse_lazy('lista_productos')

class CategoriaUpdateView(UpdateView, LoginRequiredMixin):
    model = Categoria
    fields = ['nombre', 'descripcion']
    template_name = 'app/formulario_categorias.html'
    success_url = reverse_lazy('lista_categorias')
class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'app/eliminar.html'
    success_url = reverse_lazy('lista_productos')

class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = 'app/eliminar_categoria.html'
    success_url = reverse_lazy('lista_categorias')
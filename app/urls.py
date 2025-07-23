from django.urls import path
from . import views

urlpatterns = [
path('', views.ProductoListView.as_view(), name='lista_productos'),
path('categorias/', views.CategoriaListView.as_view(), name='lista_categorias'),
path('nuevo/', views.ProductoCreateView.as_view(), name='crear_producto'),
path('nuevo_categoria/', views.CategoriaCreateView.as_view(), name='crear_categoria'),
path('editar/<int:pk>/', views.ProductoUpdateView.as_view(), name='editar_producto'),
path('editar_categoria/<int:pk>/', views.CategoriaUpdateView.as_view(), name='editar_categoria'),
path('eliminar/<int:pk>/', views.ProductoDeleteView.as_view(), name='eliminar_producto'),
path('eliminar_categoria/<int:pk>/', views.CategoriaDeleteView.as_view(), name='eliminar_categoria'),
]
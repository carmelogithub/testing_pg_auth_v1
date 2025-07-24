from django.urls import path

from concurrencia import views

urlpatterns = [
    path('',views.home,name='home'),
path('sincrono/', views.sync_api_view, name='comunicacion_sincrona'),
path('asincrono/', views.async_api_view, name='comunicacion_asincrona'),
    ]
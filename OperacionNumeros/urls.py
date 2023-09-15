from django.urls import path

from . import views

app_name = 'OperacionNumeros'

urlpatterns = [
    path('', views.index, name='index'),
    path('resultado/', views.resultado, name='resultado'),
]
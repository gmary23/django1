from django.urls import path
from .views import index, contato, linkproduto

urlpatterns = [
    path('', index, name='index'),
    path('contato', contato, name='contato'),
    path('linkproduto/<int:pk>', linkproduto, name='rotaproduto'), # name é o nome da rota
]

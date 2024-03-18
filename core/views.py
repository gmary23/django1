from django.shortcuts import render
from .models import Produto
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader

def index(request):
    variavelExemplo = Produto.objects.all()

    context = {
    'curso':'Curso de Python com Framework Django',
    'outro':'Agora eu aprendo Django',
    'variavelCriadaExemplo': variavelExemplo,
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

def linkproduto(request, pk):
    #product = Produto.objects.get(id=pk)
    product = get_object_or_404(Produto, id=pk)
    print (f'PK: {pk}') # só visualiza qual o id do produto está chamando

    context = {
        'produto': product
    }
    return render(request, 'produto.html', context)

def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)

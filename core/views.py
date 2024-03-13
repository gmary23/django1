from django.shortcuts import render
from .models import Produto


def index(request):
    variavelExemplo = Produto.objects.all()
   
    #print(dir(request.user))
    #print(f'User: {request.user}')

    # verifica se o usuário está logado
    # if str(request.user) == 'AnonymousUser':
    #     teste = 'Usuário não logado!'
    # else:
    #     teste = 'Usuário logado!'
    # finaliza a verificação do usuário logado
        
    context = {
    'curso':'Curso de Python com Framework Django',
    'outro':'Agora eu aprendo Django',
    'variavelCriadaExemplo': variavelExemplo,
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

def linkproduto(request, pk):
    product = Produto.objects.get(id=pk)
    print (f'PK: {pk}') # só visualiza qual o id do produto está chamando

    context = {
        'produto': product
    }
    return render(request, 'produto.html', context)



from django.shortcuts import render

def index(request):
    print(dir(request.user))
    print(f'User: {request.user}')

    # verifica se o usuário está logado
    if str(request.user) == 'AnonymousUser':
        teste = 'Usuário não logado!'
    else:
        teste = 'Usuário logado!'
    # finaliza a verificação do usuário logado
        
    context = {
    'curso':'Curso de Python com Framework Django',
    'outro':'Agora eu aprendo Django',
    'logado': teste
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')



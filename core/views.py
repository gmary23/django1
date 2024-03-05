from django.shortcuts import render

def index(request):
    context = {
    'curso':'Curso de Python com Framework Django',
    'outro':'Agora eu aprendo Django'
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')



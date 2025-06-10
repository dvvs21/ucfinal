from django.shortcuts import render
from instrutor.models import instrutor

# Create your views here.
def listar(request):
    lista_instrutores = instrutor.objects.all()
    contexto = {
        'instrutores': lista_instrutores
    }

    return render(request, 'instrutor/listarInstrutores.html', context=contexto)

def cadastrar(request):
    return render(request, 'instrutor/cadastroInstrutor.html')
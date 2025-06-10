from django.shortcuts import render
from titulo.models import titulo

# Create your views here.
def listar(request):
    lista_titulos = titulo.objects.all()
    contexto = {
        'titulos': lista_titulos
    }



    return render(request, 'titulo/listarTitulos.html', context=contexto)

def cadastrar(request):
    return render(request, 'titulo/cadastroTitulos.html')
from django.shortcuts import render, redirect
from titulo.models import titulo
from titulo.forms import TituloForm
from instrutor.models import instrutor  
# Create your views here.
def listar(request):
    lista_titulos = titulo.objects.all()
    contexto = {
        'titulos': lista_titulos
    }
    return render(request, 'titulo/listarTitulos.html', context=contexto)

def cadastro(request):
    
    return render(request, 'titulo/cadastroTitulos.html')

def cadastrar(request):
    form = TituloForm(request.POST)
    if form.is_valid():
        dados_titulos = form.cleaned_data
        Titulo = titulo(
            descricao=dados_titulos['descricao']
        )
        Titulo.save()
        
    return render(request, 'titulo/cadastroTitulos.html')

def exclui(request, codigo):
    Titulo = titulo.objects.get(pk=codigo)
    # instrutores = instrutor.objects.filter(codigo_titulo=codigo)
    # if not instrutores:
    Titulo.delete()

    return redirect('titulo:listar')
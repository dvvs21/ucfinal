from django.shortcuts import render, redirect
from titulo.models import titulo
from titulo.forms import TituloForm, TituloAtualizarForm
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


#carregar o título para edição/atualização
def carregar_titulo(request, codigo):
    Titulo = titulo.objects.get(pk=codigo)
    contexto = {
        'titulo': Titulo,
        
    }
    
    return render (request, 'titulo/atualizarTitulo.html', context=contexto)
    
    
#atualizar a base de dados para o título selecionado

def atualizar_titulo (request):
    if request.method == 'POST':
        form = TituloAtualizarForm(request.POST)
        if form.is_valid():
            dados_titulo = form.cleaned_data
            codigo = dados_titulo['codigo']
            Titulo = titulo.objects.get(pk=codigo)
            Titulo.descricao = dados_titulo['descricao']
            Titulo.save()
            
        else: 
            print (form.errors)
    return redirect('titulo:listar')
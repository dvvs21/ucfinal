from django.shortcuts import render, redirect
from instrutor.models import instrutor


# Create your views here.
def listar(request):
    lista_instrutores = instrutor.objects.all()
    contexto = {
        'instrutores': lista_instrutores
    }

    return render(request, 'instrutor/listarInstrutores.html', context=contexto)


def cadastro(request):
    return render(request, 'instrutor/cadastroInstrutor.html')


# def cadastrar(request):
    
#     if request.method == 'POST':
#         form = frmCadastrarInstrutor(request.POST)
#         if form.is_valid():
#             dados_instrutor = form.cleaned_data
#             instrutor_obj = instrutor(
#                 rg=dados_instrutor['rg'],
#                 nome=dados_instrutor['nome'],
#                 dtnascimento=dados_instrutor['dtnascimento'],
#                 telefone=dados_instrutor['telefone'],
#                 ddd=dados_instrutor['ddd'],
#                 #codigo_titulo=dados_instrutor['codigo_titulo']
#             )
#             instrutor_obj.save()
#         return redirect('instrutor:listar')


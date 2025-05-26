from django.shortcuts import HttpResponse, render 


def listar (request):
    return render(request, 'aluno/listarAluno.html')
    
    return HttpResponse("Olá! Eu sou o index.")
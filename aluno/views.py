from django.shortcuts import HttpResponse


def aluno (request):
    return HttpResponse("Olá! Eu sou o index.")
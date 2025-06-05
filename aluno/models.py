from django.db import models
from django.utils import timezone

# Create your models here.
class aluno(models.Model):
    matricula = models.AutoField(primary_key=True, help_text="Código da Matrícula do Aluno")
    dtinicial = models.DateField(help_text="Informe a Data de Início do Aluno", NULL=False, default=timezone.now(),)
    dtfinal = models.DateField(help_text="Informe a Data Final do Aluno", NULL=True, blank=True)
    nome = models.CharField(max_length=70, help_text="Informe o Nome do Aluno")

    def __str__(self):
        return f'{self.nome} - {self.dtinicial} a {self.dtfinal}'   
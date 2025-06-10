from django.db import models

from tiposdeatividade.models import TipoDeAtividade
from aluno.models import aluno
from instrutor.models import instrutor

# Create your models here.
class turma(models.Model):
    numero = models.AutoField(primary_key=True, help_text="Código da Turma")
    hraula = models.DateTimeField(help_text="Código do Instrutor")
    drcaula = models.SmallIntegerField(help_text="Informe a Duração da Aula (em minutos)")
    dtinicial = models.DateField(help_text="Data de Início da Aula")
    dtfinal = models.DateField(help_text="Data de Fim da Aula")    
    codigo_atividade = models.ForeignKey(TipoDeAtividade, 
                                         null=True, blank=True, on_delete=models.CASCADE,
                                         related_name='atividades')
    
    matricula_monitor = models.ForeignKey(aluno, null=True, blank=True, 
                                          on_delete=models.SET_NULL,
                                          related_name='alunos')
    
    id_instrutor = models.ForeignKey(instrutor, null=True, blank=True, on_delete=models.CASCADE,
                                     related_name='instrutores')

    def __str__(self):
        return f'Turma {self.numero}'
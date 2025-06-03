from django.db import models

# Create your models here.
class turma(models.Model):
    numero = models.AutoField(primary_key=True, help_text="Código da Turma")
    hraula = models.DateTimeField(help_text="Código do Instrutor")
    drcaula = models.SmallIntegerField(help_text="Informe a Duração da Aula (em minutos)")
    dtinicial = models.DateField(help_text="Data de Início da Aula")
    dtfinal = models.DateField(help_text="Data de Fim da Aula")    

    def __str__(self):
        return f'Turma {self.numero} - Horário da aula {self.hraula}, com duração {self.drcaula} de {self.dtinicial} a {self.dtfinal}'
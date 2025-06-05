from django.db import models

# Create your models here.
class instrutor(models.Model):
    id = models.AutoField(primary_key=True, help_text="Código do Instrutor")
    rg = models.CharField(max_length=15, help_text="Informe o RG do Instrutor (apenas números)")
    nome = models.CharField(max_length=70, help_text="Informe o Nome do Instrutor")
    dtnascimento = models.DateField(help_text="Informe a Data de Nascimento do Instrutor")
    telefone = models.CharField(max_length=9, help_text="Informe o Telefone do Instrutor (apenas números)")
    ddd = models.IntegerField(max_length=2, help_text="Informe o DDD do Telefone do Instrutor (apenas números)")
    

    def __str__(self):
        return f'{self.id} - Professor(a): {self.nome} RG: {self.rg} - Telefone: ({self.ddd}) {self.telefone} - Nascimento: {self.dtnascimento}'
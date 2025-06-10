from django.db import models
from django.utils import timezone

from titulo.models import titulo

# Create your models here.
class instrutor(models.Model):
    id = models.AutoField(primary_key=True, help_text="Código do Instrutor")
    rg = models.CharField(max_length=15, help_text="Informe o RG do Instrutor (apenas números)")
    nome = models.CharField(max_length=70, help_text="Informe o Nome do Instrutor")
    dtnascimento = models.DateField(help_text="Informe a Data de Nascimento do Instrutor",blank=True, null = True, default=timezone.now())
    telefone = models.CharField(max_length=9, help_text="Informe o Telefone do Instrutor (apenas números)")
    ddd = models.CharField(max_length=3, help_text="Informe o DDD do Telefone do Instrutor (apenas números)",blank=True, null = False)
    codigo_titulo = models.ForeignKey(titulo, 
                                      null=True,
                                      blank=True,
                                      related_name='titulos', 
                                      on_delete=models.SET_NULL,
                                      db_column='titulo_codigo')

    def __str__(self):
        return f'{self.id} - {self.nome}'
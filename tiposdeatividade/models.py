from django.db import models

# Create your models here.
class TipoDeAtividade(models.Model):
    codigo = models.AutoField(primary_key=True, help_text="Código do Tipo de atividade")

    descricao = models.CharField(max_length=100, help_text="Informe a Descrição do Tipo de atividade")

    def __str__(self):
        return f'{self.codigo}- {self.descricao}'
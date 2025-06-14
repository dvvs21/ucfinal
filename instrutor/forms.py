from django import forms
from django.utils import timezone
# from titulo.models import titulo

#classe formulário para inclusão 

class frmCadastrarInstrutor(forms.Form):
    #id = forms.AutoField(primary_key=True, help_text="Código do Instrutor")
    rg = forms.CharField(max_length=15, help_text="Informe o RG do Instrutor (apenas números)",required=True)
    nome = forms.CharField(max_length=70, help_text="Informe o Nome do Instrutor",required=True)
    dtnascimento = forms.DateField(help_text="Informe a Data de Nascimento do Instrutor",required=True)
    telefone = forms.CharField(max_length=9, help_text="Informe o Telefone do Instrutor (apenas números)",required=True)
    ddd = forms.CharField(max_length=3, help_text="Informe o DDD do Telefone do Instrutor (apenas números)",required=True)
    # codigo_titulo = forms.ForeignKey(titulo, 
    #                                   null=True,
    #                                   blank=True,
    #                                   related_name='titulos', 
    #                                   on_delete=forms.SET_NULL,
    #                                   db_column='titulo_codigo')

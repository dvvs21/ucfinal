from django import forms

#classe formulário para inclusão 

class TituloForm(forms.Form):
    descricao = forms.CharField(max_length=100, required=True,help_text="Informe a Descrição do Título")
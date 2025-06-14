from tiposdeatividade.models import TipoDeAtividade
from titulo.models import titulo
from aluno.models import aluno
from instrutor.models import instrutor
from turma.models import turma

from django.db import connection
from datetime import date
import random
#gerar valor aleatorio
def gerar_numero_aleatorio_faixa(inicio, fim):
    return random.randint(inicio, fim)


# gerar data aleatória para os alunos
def gerar_data_aleatoria(tipo_data):
    dia = gerar_numero_aleatorio_faixa(1, 28)
    mes = gerar_numero_aleatorio_faixa(1, 12)
    ano = 0

    if tipo_data == 'inicial':
        ano = gerar_numero_aleatorio_faixa(1970, 2007)
    else:
        ano = gerar_numero_aleatorio_faixa(2021, 2024)
    return date(ano, mes, dia)


#gerar rg aletório
def gerar_rg_aleatorio(registro_geral):
    rg = 0

    if registro_geral == 'inicial':
        rg = gerar_numero_aleatorio_faixa(1, 99999999999999)
    return rg


def gerar_numero_aleatorio_sequencia(lista_valores):
    return random.choice(lista_valores)



# truncar tableas para zerar o contador de auto-incremento
def truncate_table(nome_tabela):
    with connection.cursor() as cursor:
        cursor.execute(f'DELETE FROM {nome_tabela}')
        cursor.execute(f'DELETE FROM sqlite_sequence WHERE name = "{nome_tabela}"')

def truncar_tabelas():
    truncate_table('turma_turma')
    truncate_table('instrutor_instrutor')
    truncate_table('aluno_aluno')
    truncate_table('titulo_titulo')
    truncate_table('tiposdeatividade_tipodeatividade')

# popular tabela com tipos de atividade
def popular_tiposdeatividade():
    lista_tiposdeatividade = []

    for i in range(1,10):
        lista_tiposdeatividade.append(TipoDeAtividade(descricao='Atividade ' + f'{i:02}'))

    TipoDeAtividade.objects.bulk_create(lista_tiposdeatividade)


def popular_titulo():
    lista_titulos = []

    for i in range(1, 10):
       titulos = titulo(descricao='Titulo ' + f'{i:02}')
       lista_titulos.append(titulos)

    titulo.objects.bulk_create(lista_titulos)
    

def popular_aluno():
    lista_alunos = []

    for i in range(1, 50):
        lista_alunos.append(
            aluno(nome='Aluno ' + f'{i:02}', dtinicial = gerar_data_aleatoria('inicial'))
        )              
    aluno.objects.bulk_create(lista_alunos)

def popular_instrutor():
    lista_instrutores = []

    lista_valores_titulo = titulo.objects.values_list('codigo', flat=True)
    codigo_selecionado = gerar_numero_aleatorio_sequencia(lista_valores_titulo)
    titulos = titulo.objects.get(pk=codigo_selecionado)  

    for i in range(1, 20):
        lista_instrutores.append(instrutor(nome='Instrutor ' + f'{i:02}', dtnascimento = gerar_data_aleatoria('inicial'),rg = gerar_rg_aleatorio('inicial'), telefone = f'{gerar_numero_aleatorio_faixa(1, 999999999):09}', ddd = f'{gerar_numero_aleatorio_faixa(1, 99):03}', codigo_titulo=titulos))     
    instrutor.objects.bulk_create(lista_instrutores)

def popular_turma():
    pass
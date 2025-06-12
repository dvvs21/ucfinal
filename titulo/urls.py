from django.urls import path
from . import views 

app_name = 'titulo'

urlpatterns = [
    path('lista/', views.listar, name="listar"),
    path('cadastro', views.cadastro, name="cadastro"),
    path('cadastrar', views.cadastrar, name="cadastrar"),
    path('excluir/<int:codigo>', views.exclui, name="excluir_titulo"),
    ]
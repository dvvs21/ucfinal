from django.urls import path 
from . import views

urlpatterns = [ 
    path("", views.index, name="index"),
    path ("test_render", views.test_render, name="exibir_mensagem"),
]
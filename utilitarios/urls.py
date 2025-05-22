from django.urls import path 
from . import views

urlpatterns = [ 
    path("", views.utilitarios, name="utilitarios"),
    ]
from django.urls import path

import vtr.views
from django.urls import path
from .views import (
    DashboardView, 
    UnidadeDetailView, 
    GerenciamentoFrotaListView, 
    ViaturaCreateView, 
    ViaturaUpdateView, 
    ViaturaDeleteView)

from django.contrib.auth import views as auth_view

app_name='vtr'

urlpatterns = [

    
    #path('criar-sindicancia/', inicio.views.criar_sindicancia, name='criar_sindicancia'),
    path('vtr/', DashboardView.as_view(), name='home'),
    path('unidade/<int:pk>/', UnidadeDetailView.as_view(), name='unidade_detail'),
    path('gerenciar/', GerenciamentoFrotaListView.as_view(), name='gerenciar_frota'),
    path('viatura/novo/', ViaturaCreateView.as_view(), name='viatura_add'),
    path('viatura/<int:pk>/editar/', ViaturaUpdateView.as_view(), name='viatura_edit'),
    path('viatura/<int:pk>/excluir/', ViaturaDeleteView.as_view(), name='viatura_delete'),
    #path('sindicancia/editar_sindicancia/<int:id>', inicio.views.editar_sindicancia, name='editar_sindicancia'),
    #path('sindicancia/excluir_sindicancia/<int:id>', inicio.views.excluir_sindicancia, name='excluir_sindicancia'),
   
    

]

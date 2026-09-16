from django.urls import path

import efetivo.views
from .views import (cadastrar_policial,painel_escala,visualizacao_escala,gerar_pdf_fichas_ponto,efetivo_unidade_grade,dashboard_efetivo,admin_criar_cartao_programa,salvar_cartao_programa)

from django.contrib.auth import views as auth_view

app_name='efetivo'

urlpatterns = [
    path('escala/', painel_escala, name='painel_escala'),
    path('ver/', visualizacao_escala, name='visualizacao_escala'), # Nova rota
    path('militares/',cadastrar_policial, name='cadastrar_policial'),
    path('relatorios/ponto-pdf/', gerar_pdf_fichas_ponto, name='gerar_pdf_fichas_ponto'),
    #path('unidade/<int:unidade_id>/efetivo/', efetivo_unidade_grade, name='efetivo_unidade_grade'),
    path('efetivo/unidade/<int:unidade_id>/', efetivo_unidade_grade, name='efetivo_unidade_grade'),
    path('pessoal/', dashboard_efetivo, name='dash'),
    path('cartao-programa/configurar/<int:escala_id>/', admin_criar_cartao_programa, name='configurar_cartao_programa'),
    path('cartao-programa/enviar/<int:escala_id>/', salvar_cartao_programa, name='salvar_cartao_programa'),
    #path('sobre/', views.sobre, name='sobre'),
    #path('contato/', views.contato, name='contato'),
# CBV básica
    #path('minhaview/', MinhaView.as_view(), name='minha-view'),
    
    # TemplateView
    #path('', HomeView.as_view(), name='home'),
    
    # ListView
    #path('itens/', ListaItensView.as_view(), name='lista-itens'),
    
    # DetailView com parâmetro na URL
    #path('item/<int:pk>/', DetalheItemView.as_view(), name='detalhe-item'),

]

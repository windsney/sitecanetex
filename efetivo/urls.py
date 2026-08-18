from django.urls import path

import efetivo.views
from .views import (cadastrar_policial,painel_escala,visualizacao_escala,gerar_pdf_fichas_ponto,efetivo_unidade_grade,dashboard_efetivo)

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

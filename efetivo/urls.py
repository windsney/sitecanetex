from django.urls import path

import efetivo.views
from .views import (cadastrar_policial,painel_escala,visualizacao_escala,gerar_pdf_fichas_ponto)

from django.contrib.auth import views as auth_view

app_name='efetivo'

urlpatterns = [
    path('painel/', painel_escala, name='painel_escala'),
    path('ver/', visualizacao_escala, name='visualizacao_escala'), # Nova rota
    path('militares/',cadastrar_policial, name='cadastrar_policial'),
    path('relatorios/ponto-pdf/', gerar_pdf_fichas_ponto, name='gerar_pdf_fichas_ponto'),
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

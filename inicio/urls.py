

from django.urls import path

import inicio.views
from.views import Sind_Cadastradas,Cd,Inquerito,RIOG,Criar_conta
from django.contrib.auth import views as auth_view

app_name='inicio'

urlpatterns = [
    path('cad_ipm', Inquerito.as_view(),name='inquerito'),
    path('sind_cadastradas', Sind_Cadastradas.as_view(),name='sind_cadastradas'),
    path('cad_cd', Cd.as_view(),name='cd'),
    path('cad_riog', RIOG.as_view(),name='riog'),
    path('', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(next_page='inicio:login'), name='logout'),
    path('criar_conta/', Criar_conta.as_view(), name='criar_conta'),
    #path('cad_sind/<int:pk>',Detalhe_sind.as_view(), name='detalhe'),
    #path('cad_investigado_sind/<int:pk>',Cadastro_investigado_sind.as_view(), name='cadastro_investigado_sind'),
    path('sindicancia/<int:sindicancia_id>/cadastrar_sindicado/', inicio.views.cadastrar_sindicado, name='cadastrar_sindicado'),
    path('sindicancia/<int:sindicancia_id>/cadastrar_testemunha/', inicio.views.cadastrar_testemunha, name='cadastrar_testemunha'),
    path('sindicancia/<int:sindicancia_id>/cadastrar_ofendido/', inicio.views.cadastrar_ofendido, name='cadastrar_ofendido'),
    path('sindicancia/<int:sindicancia_id>/', inicio.views.detalhes_sindicancia, name='detalhes_sindicancia'),
    path('sindicancia/<int:sindicancia_id>/iniciot', inicio.views.gerar_inicio_dos_trabalhos, name='inicio_dos_trabalhos'),
    path('sindicancia/<int:sindicancia_id>/relatorio_sind', inicio.views.gerar_relatorio, name='relatorio_sind'),
    path('sindicancia/<int:sindicancia_id>/decsind/<int:id>', inicio.views.gerar_declaracao_sindicado, name='declaracao_sindicado'),
    path('sindicancia/<int:sindicancia_id>/dectest/<int:id>', inicio.views.gerar_declaracao_testemunha, name='declaracao_testemunha'),
    path('sindicancia/<int:sindicancia_id>/decofe/<int:id>', inicio.views.gerar_declaracao_ofendido, name='declaracao_ofendido'),
    path('sindicancia/<int:sindicancia_id>/editar_sindicado/<int:id>', inicio.views.editar_sindicado, name='editar_sindicado'),
    path('sindicancia/<int:sindicancia_id>/editar_testemunha/<int:id>', inicio.views.editar_testemunha, name='editar_testemunha'),
    path('sindicancia/<int:sindicancia_id>/editar_ofendido/<int:id>', inicio.views.editar_ofendido, name='editar_ofendido'),
    path('sindicancia/<int:sindicancia_id>/excluir_sindicado/<int:id>', inicio.views.excluir_sindicado, name='excluir_sindicado'),
    path('sindicancia/<int:sindicancia_id>/excluir_testemunha/<int:id>', inicio.views.excluir_testemunha, name='excluir_testemunha'),
    path('sindicancia/<int:sindicancia_id>/excluir_ofendido/<int:id>', inicio.views.excluir_ofendido, name='excluir_ofendido'),
    path('criar-sindicancia/', inicio.views.criar_sindicancia, name='criar_sindicancia'),
    path('sindicancia/editar_sindicancia/<int:id>', inicio.views.editar_sindicancia, name='editar_sindicancia'),
    path('sindicancia/excluir_sindicancia/<int:id>', inicio.views.excluir_sindicancia, name='excluir_sindicancia'),



]





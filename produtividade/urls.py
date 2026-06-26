

from django.contrib.auth import views as auth_view
from django.urls import path

from .views import dashboard_view,api_dados_materiais,api_dados_produtividade,registrar_ocorrencia


app_name='produtividade'


urlpatterns = [
    # Rota para o Operador realizar o lançamento
    #path('registrar/', RegistrarOcorrenciaView.as_view(), name='registrar_ocorrencia'),
    
    # Rota para o Gestor visualizar o Dashboard
    path('p3/', dashboard_view, name='dashboard'),
    path('api/materiais/', api_dados_materiais, name='api_materiais'),
    path('api/produtividade/', api_dados_produtividade, name='api_produtividade'),
    path('registrar/', registrar_ocorrencia, name='registrar_ocorrencia'),
]
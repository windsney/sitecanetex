

from django.contrib.auth import views as auth_view
from django.urls import path
from .views import RegistrarOcorrenciaView, DashboardView


app_name='produtividade'


urlpatterns = [
    # Rota para o Operador realizar o lançamento
    path('registrar/', RegistrarOcorrenciaView.as_view(), name='registrar_ocorrencia'),
    
    # Rota para o Gestor visualizar o Dashboard
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
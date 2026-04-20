from django.urls import path

import cd.views
from .views import Home

from django.contrib.auth import views as auth_view

app_name='cd'

urlpatterns = [

    
    #path('criar-sindicancia/', inicio.views.criar_sindicancia, name='criar_sindicancia'),
    path('cd_cadastradas/', Home.as_view(),name='cd_cadastradas'),
    #path('sindicancia/editar_sindicancia/<int:id>', inicio.views.editar_sindicancia, name='editar_sindicancia'),
    #path('sindicancia/excluir_sindicancia/<int:id>', inicio.views.excluir_sindicancia, name='excluir_sindicancia'),
   
    

]
from django.contrib import admin
from .models import Unidade, PontoFixo, EscalaDiaria, CartaoPoliciamento, Policial, ValorHoraCategoria

# 1. Registra o modelo Unidade para poder cadastrá-las
@admin.register(Unidade)
class UnidadeAdmin(admin.ModelAdmin):
    list_display = ('sigla', 'nome')
    search_fields = ('sigla', 'nome')

# 2. Registra o Policial com o campo de Unidade em destaque
@admin.register(Policial)
class PolicialAdmin(admin.ModelAdmin):
    list_display = ('posto_graduacao', 'nome_guerra', 'rgpm', 'unidade')  # Exibe a unidade na tabela
    list_filter = ('unidade', 'posto_graduacao')                          # Cria um filtro lateral por unidade
    search_fields = ('nome_completo', 'nome_guerra', 'rgpm')

# Demais registros mantidos
admin.site.register(ValorHoraCategoria)
admin.site.register(PontoFixo)
admin.site.register(EscalaDiaria)
admin.site.register(CartaoPoliciamento)
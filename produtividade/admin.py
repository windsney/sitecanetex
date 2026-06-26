from django.contrib import admin
from .models import (
    NaturezaOcorrencia, TipoMaterial, UnidadeMedida, 
    RegistroDiario, MaterialApreendido
)

# 1. Registro dos modelos de apoio para aparecerem no menu do Admin
@admin.register(NaturezaOcorrencia, TipoMaterial, UnidadeMedida)
class CatalogoAdmin(admin.ModelAdmin):
    list_display = ('nome',)

# 2. Configuração do formulário de materiais dentro do registro principal
class MaterialApreendidoInline(admin.TabularInline):
    model = MaterialApreendido
    extra = 1  # Quantidade de linhas em branco extras para facilitar o cadastro
    fields = ('tipo_material', 'quantidade', 'unidade')

# 3. Configuração do Registro Diário com os materiais inclusos
@admin.register(RegistroDiario)
class RegistroDiarioAdmin(admin.ModelAdmin):
    list_display = ('data_servico', 'natureza_ocorrencia', 'comandante', 'pessoas_conduzidas')
    list_filter = ('data_servico', 'natureza_ocorrencia')
    search_fields = ('comandante', 'componente')
    
    # Isso conecta os materiais ao formulário do RegistroDiario
    inlines = [MaterialApreendidoInline]
    
    # Campo para organizar a visualização no formulário
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('data_servico', 'comandante', 'componente', 'natureza_ocorrencia', 'detalhes_ocorrencia')
        }),
        ('Produtividade', {
            'fields': (
                'pessoas_abordadas', 'veiculos_abordados', 'notificacoes', 
                'veiculos_apreendidos', 'tco', 'pessoas_conduzidas', 'starts', 'barreiras'
            )
        }),
    )
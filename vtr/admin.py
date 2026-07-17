from django.contrib import admin
from .models import Unidade, Viatura, ModeloViatura,Policial

@admin.register(ModeloViatura)
class ModeloViaturaAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'tipo')
    list_filter = ('tipo',)
    search_fields = ('modelo',)

@admin.register(Unidade)
class UnidadeAdmin(admin.ModelAdmin):
    list_display = ('sigla', 'nome', 'exibir_operacionais', 'exibir_baixadas', 'exibir_total')
    search_fields = ('sigla', 'nome')

    def exibir_operacionais(self, obj):
        return obj.total_operacionais()
    exibir_operacionais.short_description = 'Vtrs Operacionais'

    def exibir_baixadas(self, obj):
        return obj.total_baixadas()
    exibir_baixadas.short_description = 'Vtrs Baixadas'

    def exibir_total(self, obj):
        return obj.viaturas.count()
    exibir_total.short_description = 'Total na Frota'


@admin.register(Viatura)
class ViaturaAdmin(admin.ModelAdmin):
    # Atualizado para mostrar prefixo e placa separadamente na lista
    list_display = ('prefixo', 'placa', 'get_modelo', 'get_tipo', 'unidade', 'situacao', 'condicao', 'km')
    list_filter = ('unidade', 'situacao', 'condicao', 'modelo_veiculo__tipo')
    search_fields = ('prefixo', 'placa', 'subunidade', 'modelo_veiculo__modelo')
    
    def get_modelo(self, obj):
        return obj.modelo_veiculo.modelo
    get_modelo.short_description = 'Modelo'

    def get_tipo(self, obj):
        return obj.modelo_veiculo.get_tipo_display()
    get_tipo.short_description = 'Tipo'

    fieldsets = (
        ('Identificação da Viatura', {
            'fields': ('unidade', 'subunidade', 'prefixo', 'placa', 'modelo_veiculo')
        }),
        ('Status e Quilometragem', {
            'fields': ('situacao', 'condicao', 'km')
        }),
        ('Informações de Manutenção', {
            'fields': ('observacao',)
        }),
    )

@admin.register(Policial)
class PolicialAdmin(admin.ModelAdmin):
    # Colunas que aparecerão na tabela de listagem geral
    list_display = ('posto_graduacao', 'nome_guerra', 'num_matricula', 'unidade', 'status')
    
    # Filtros rápidos na lateral direita para facilitar a busca do Comandante
    list_filter = ('unidade', 'status', 'posto_graduacao')
    
    # Permite pesquisar digitando apenas o nome de guerra ou a matrícula do PM
    search_fields = ('nome_guerra', 'num_matricula')
    
    # Permite alterar o status (Serviço, Férias, etc.) clicando direto na lista geral
    list_editable = ('status',)
from django.contrib import admin
from django import forms
from .models import (
    NaturezaOcorrencia, TipoMaterial, UnidadeMedida, 
    CategoriaProdutividade, RegistroDiario, ValorProdutividade, MaterialApreendido
)

# Formulário para o seletor de cores
class CategoriaProdutividadeForm(forms.ModelForm):
    class Meta:
        model = CategoriaProdutividade
        fields = '__all__'
        widgets = {'cor': forms.TextInput(attrs={'type': 'color'})}

@admin.register(CategoriaProdutividade)
class CategoriaProdutividadeAdmin(admin.ModelAdmin):
    form = CategoriaProdutividadeForm
    list_display = ('nome', 'cor')

# Inlines para edição dentro do RegistroDiario
class ValorProdutividadeInline(admin.TabularInline):
    model = ValorProdutividade
    extra = 1 # Quantidade de linhas vazias para preencher

class MaterialApreendidoInline(admin.TabularInline):
    model = MaterialApreendido
    extra = 1

@admin.register(RegistroDiario)
class RegistroDiarioAdmin(admin.ModelAdmin):
    list_display = ('data_servico', 'natureza_ocorrencia', 'comandante')
    inlines = [ValorProdutividadeInline, MaterialApreendidoInline]

# Registro dos outros modelos
@admin.register(TipoMaterial)
class TipoMaterialAdmin(admin.ModelAdmin):
    form = CategoriaProdutividadeForm # Reutilizando o widget de cor

admin.site.register(NaturezaOcorrencia)
admin.site.register(UnidadeMedida)
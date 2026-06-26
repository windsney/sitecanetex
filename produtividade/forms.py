from django import forms
from django.forms import inlineformset_factory
from .models import RegistroDiario, MaterialApreendido

class RegistroDiarioForm(forms.ModelForm):
    class Meta:
        model = RegistroDiario
        fields = '__all__'
        widgets = {
            'data_servico': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'pessoas_conduzidas': forms.NumberInput(attrs={'class': 'form-control'}),
            'veiculos_apreendidos': forms.NumberInput(attrs={'class': 'form-control'}),
            'notificacoes': forms.NumberInput(attrs={'class': 'form-control'}),
            'tco': forms.NumberInput(attrs={'class': 'form-control'}),
            'starts': forms.NumberInput(attrs={'class': 'form-control'}),
            'barreiras': forms.NumberInput(attrs={'class': 'form-control'}),
        }

# Isso permite adicionar vários materiais na mesma tela da ocorrência
MaterialFormSet = inlineformset_factory(
    RegistroDiario, 
    MaterialApreendido, 
    fields=('tipo_material', 'quantidade', 'unidade'),
    extra=1,  # Quantidade de campos vazios para novos materiais
    can_delete=True
)
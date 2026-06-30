from django import forms
from .models import RegistroDiario, MaterialApreendido

class RegistroDiarioForm(forms.ModelForm):
    class Meta:
        model = RegistroDiario
        fields = '__all__'
        widgets = {
            'data_servico': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
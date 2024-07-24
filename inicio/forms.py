from django import forms
from .models import Sindicado,Sindicancia,Testemunha,Ofendido

class SindicadoForm(forms.ModelForm):
    class Meta:
        model = Sindicado
        fields = ['nome', 'rgpm', 'cpf', 'email', 'endereco', 'posto_sindicado',
                  'pai', 'mae', 'telefone', 'data_nascimento', 'data_inquiricao',
                  'naturalidade', 'declaracao', 'lotacao', 'hora_inicio', 'hora_fim']

        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
            'data_inquiricao': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in ['data_nascimento', 'data_inquiricao']:
            if self.initial.get(field):
                self.initial[field] = self.initial[field].strftime('%Y-%m-%d')

class TestemunhaForm(forms.ModelForm):
    class Meta:
        model = Testemunha
        fields = ['nome', 'rgpm', 'cpf', 'email', 'endereco',
                  'pai', 'mae', 'telefone', 'data_nascimento', 'data_inquiricao',
                  'naturalidade', 'declaracao', 'profissao', 'hora_inicio', 'hora_fim']

        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
            'data_inquiricao': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in ['data_nascimento', 'data_inquiricao']:
            if self.initial.get(field):
                self.initial[field] = self.initial[field].strftime('%Y-%m-%d')

class OfendidoForm(forms.ModelForm):
    class Meta:
        model = Ofendido
        fields = ['nome', 'rgpm', 'cpf', 'email', 'endereco',
                  'pai', 'mae', 'telefone', 'data_nascimento', 'data_inquiricao',
                  'naturalidade', 'declaracao', 'profissao', 'hora_inicio', 'hora_fim']

        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
            'data_inquiricao': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in ['data_nascimento', 'data_inquiricao']:
            if self.initial.get(field):
                self.initial[field] = self.initial[field].strftime('%Y-%m-%d')

class SindicanciaForm(forms.ModelForm):
    class Meta:
        model = Sindicancia
        fields = [
            'numero', 'unidade', 'delegante', 'posto_delegante', 'delegada',
            'posto_delegada', 'rg_delegada', 'data_portaria', 'data_inicio',
            'dia_recebido','historico', 'usuario', 'funcao_delegante',
            'bairro_quartel', 'cep_quartel', 'cidade_quartel', 'email_quartel',
            'lotacao_delegada', 'numero_quartel', 'rua_quartel', 'telefone_quartel'
        ]

        widgets = {
        'data_portaria': forms.DateInput(attrs={'type': 'date'}),
        'dia_recebido': forms.DateInput(attrs={'type': 'date'}),
        'data_inicio': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in ['data_portaria', 'data_inicio', 'dia_recebido']:
            if self.initial.get(field):
                self.initial[field] = self.initial[field].strftime('%Y-%m-%d')

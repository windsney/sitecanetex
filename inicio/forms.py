from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Sindicado,Sindicancia,Testemunha,Ofendido,Usuario

class SindicadoForm(forms.ModelForm):
    class Meta:
        model = Sindicado
        fields = ['nome', 'rgpm', 'cpf', 'email', 'endereco', 'posto_sindicado',
                  'pai', 'mae', 'telefone', 'data_nascimento', 'data_inquiricao',
                  'naturalidade', 'declaracao', 'lotacao', 'hora_inicio', 'hora_fim','fls',]

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
    MILITAR_CHOICES = [
        ('sim', 'Sim'),
        ('nao', 'Não'),
    ]

   


    militar = forms.ChoiceField(
        choices=MILITAR_CHOICES,
        widget=forms.RadioSelect,
        label="A testemunha é Militar?"  # Defina o rótulo aqui
    )





    class Meta:
        model = Testemunha
        fields = ['nome', 'rgpm', 'cpf', 'email', 'endereco',
                  'pai', 'mae', 'telefone', 'data_nascimento', 'data_inquiricao',
                  'naturalidade', 'declaracao', 'profissao', 'hora_inicio', 'hora_fim','fls','militar','graduacao',
                  ]

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
                  'naturalidade', 'declaracao', 'profissao', 'hora_inicio', 'hora_fim','fls']

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
    EM_SERVICO_CHOICES = [
        ('SIM', 'Sim'),
        ('NÃO', 'Não'),
    ]

    em_servico = forms.ChoiceField(choices=EM_SERVICO_CHOICES, widget=forms.Select)

    class Meta:
        model = Sindicancia
        fields = [
            'numero', 'delegante', 'posto_delegante',
            'data_portaria', 'data_inicio',
            'dia_recebido','historico', 'funcao_delegante',
            'rua_fato','bairro_fato','cidade_fato','em_servico',
            'data_fato','hora_fato'

        ]

        widgets = {
        'data_portaria': forms.DateInput(attrs={'type': 'date'}),
        'dia_recebido': forms.DateInput(attrs={'type': 'date'}),
        'data_inicio': forms.DateInput(attrs={'type': 'date'}),
        'data_fato': forms.DateInput(attrs={'type': 'date', 'placeholder': 'dd/mm/aaaa'}, format='%d/%m/%Y'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in ['data_portaria', 'data_inicio', 'dia_recebido','data_fato']:
            if self.initial.get(field):
                self.initial[field] = self.initial[field].strftime('%Y-%m-%d')


class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['nome_completo','cr','unidade','posto','rgpm','username', 'password1', 'password2','rua','numero','bairro','cidade','cep','email_bpm','telefone']

        widgets = {
            'nome_completo': forms.TextInput(attrs={'placeholder': 'Nome Completo'}),
            'cr': forms.TextInput(attrs={'placeholder': 'CR'}),
            'unidade': forms.TextInput(attrs={'placeholder': 'Unidade'}),
            'posto': forms.TextInput(attrs={'placeholder': 'Posto'}),
            'rgpm': forms.TextInput(attrs={'placeholder': 'RGPM'}),
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
            'rua': forms.TextInput(attrs={'placeholder': 'Rua da sua UPM'}),
            'numero': forms.TextInput(attrs={'placeholder': 'Número da sua UPM'}),
            'bairro': forms.TextInput(attrs={'placeholder': 'Bairro da sua UPM'}),
            'cidade': forms.TextInput(attrs={'placeholder': 'Cidade-UF da sua UPM'}),
            'cep': forms.TextInput(attrs={'placeholder': 'CEP da sua UPM'}),
            'email_bpm': forms.EmailInput(attrs={'placeholder': 'Email da sua UPM'}),
            'telefone': forms.TextInput(attrs={'placeholder': 'Telefone da sua UPM'}),


        }
        labels = {
            'cr': 'Comando Regional/Diretoria',
        }

    POSTO_CHOICES = [
        ('3º Sgt PM', '3º Sgt PM'),
        ('2º Sgt PM', '2º Sgt PM'),
        ('1º Sgt PM', '1º Sgt PM'),
        ('Sub Ten PM', 'Sub Ten PM'),
        ('Asp Of PM', 'Asp Of PM'),
        ('2º Ten PM', '2º Ten PM'),
        ('1º Ten PM', '1º Ten PM'),
        ('Cap PM', 'Cap PM'),
        ('Maj PM', 'Maj PM'),
        ('Ten Cel PM', 'Ten Cel PM'),
        ('Cel PM', 'Cel PM'),
    ]

    posto = forms.ChoiceField(choices=POSTO_CHOICES)


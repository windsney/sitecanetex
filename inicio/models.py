from django.db import models
from datetime import date

from django.contrib.auth.models import AbstractUser

# Create your models here.
class Sindicancia (models.Model):
    numero=models.CharField(max_length=100)
    unidade=models.CharField(max_length=100)
    delegante=models.CharField(max_length=100)
    posto_delegante=models.CharField(max_length=100)

    delegada=models.CharField(max_length=100)
    posto_delegada=models.CharField(max_length=50)
    rg_delegada = models.CharField(max_length=50,default=0)
    lotacao_delegada = models.CharField(max_length=100,default=0)
    rua_quartel=models.CharField(max_length=100,default=0)
    numero_quartel=models.CharField(max_length=10,default=0)
    bairro_quartel=models.CharField(max_length=100,default=0)
    cidade_quartel=models.CharField(max_length=100,default=0)
    cep_quartel=models.CharField(max_length=100,default=0)
    telefone_quartel=models.CharField(max_length=100,default=0)
    email_quartel=models.CharField(max_length=100,default=0)



    data_portaria=models.DateField(default=date(2024, 7, 3))
    data_inicio= models.DateField(default=date(2024, 7, 3))
    dia_recebido = models.DateField(default=date(2024, 7, 3))
    historico=models.TextField(max_length=2000)
    usuario = models.CharField(max_length=100,default=0)
    funcao_delegante = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.numero

class Sindicado (models.Model):
    portaria = models.ForeignKey("Sindicancia",related_name="sindicados",on_delete=models.CASCADE)
    nome=models.CharField(max_length=100)
    rgpm=models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    posto_sindicado=models.CharField(max_length=100)
    pai=models.CharField(max_length=100)
    mae = models.CharField(max_length=100)
    telefone=models.CharField(max_length=50)
    data_nascimento = models.DateField()
    data_inquiricao = models.DateField()
    naturalidade=models.CharField(max_length=100)
    declaracao=models.TextField(max_length=2000)
    lotacao = models.CharField(max_length=100,default=0)
    hora_inicio=models.CharField(max_length=50,default=0)
    hora_fim=models.CharField(max_length=50,default=0)


    def __str__(self):
        return self.posto_sindicado + " - " +  self.nome


class Testemunha (models.Model):
    portaria = models.ForeignKey("Sindicancia",related_name="testemunhas",on_delete=models.CASCADE)
    nome=models.CharField(max_length=100)
    rgpm=models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    pai=models.CharField(max_length=100)
    mae = models.CharField(max_length=100)
    telefone=models.CharField(max_length=50)
    data_nascimento = models.DateField()
    data_inquiricao = models.DateField()
    naturalidade=models.CharField(max_length=100)
    declaracao=models.TextField(max_length=2000)
    profissao = models.CharField(max_length=100,default=0)
    hora_inicio=models.CharField(max_length=50,default=0)
    hora_fim=models.CharField(max_length=50,default=0)

    def __str__(self):
        return self.nome


class Ofendido (models.Model):
    portaria = models.ForeignKey("Sindicancia",related_name="ofendidos",on_delete=models.CASCADE)
    nome=models.CharField(max_length=100)
    rgpm=models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    pai=models.CharField(max_length=100)
    mae = models.CharField(max_length=100)
    telefone=models.CharField(max_length=50)
    data_nascimento = models.DateField()
    data_inquiricao = models.DateField()
    naturalidade=models.CharField(max_length=100)
    declaracao=models.TextField(max_length=2000)
    profissao = models.CharField(max_length=100,default=0)
    hora_inicio=models.CharField(max_length=50,default=0)
    hora_fim=models.CharField(max_length=50,default=0)

    def __str__(self):
        return self.nome
class Ipm (models.Model):
    numero=models.CharField(max_length=100)
    unidade=models.CharField(max_length=100)
    delegante=models.CharField(max_length=100)
    posto_delegante=models.CharField(max_length=100)
    delegada=models.CharField(max_length=100)
    posto_delegada=models.CharField(max_length=50)
    data_portaria=models.DateField(default=0)
    data_inicio= models.DateField(default=0)
    historico=models.TextField(max_length=2000)

    def __str__(self):
        return self.numero

class Conselho (models.Model):
    numero=models.CharField(max_length=100)
    unidade=models.CharField(max_length=100)
    delegante=models.CharField(max_length=100)
    posto_delegante=models.CharField(max_length=100)
    delegada=models.CharField(max_length=100)
    posto_delegada=models.CharField(max_length=50)
    data_portaria=models.DateField(default=0)
    data_inicio= models.DateField(default=0)
    historico=models.TextField(max_length=2000)

    def __str__(self):
        return self.numero

class Riog (models.Model):
    numero=models.CharField(max_length=100)
    unidade=models.CharField(max_length=100)
    delegante=models.CharField(max_length=100)
    posto_delegante=models.CharField(max_length=100)
    delegada=models.CharField(max_length=100)
    posto_delegada=models.CharField(max_length=50)
    data_portaria=models.DateField(default=0)
    data_inicio= models.DateField(default=0)
    historico=models.TextField(max_length=2000)

    def __str__(self):
        return self.numero

class Usuario(AbstractUser):
    nome_completo=models.CharField(max_length=100)
    posto=models.CharField(max_length=100)
    cr=models.CharField(max_length=100)
    unidade=models.CharField(max_length=100)
    rgpm=models.CharField(max_length=10)
    rua=models.CharField(max_length=100)
    numero=models.CharField(max_length=100)
    bairro=models.CharField(max_length=100)
    cidade=models.CharField(max_length=100)
    cep=models.CharField(max_length=100)
    email_bpm=models.CharField(max_length=100)
    telefone=models.CharField(max_length=100)

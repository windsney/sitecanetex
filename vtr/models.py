from django.db import models

class ModeloViatura(models.Model):
    """
    Nova tabela para cadastrar as opções de veículos no Admin.
    Você cadastra 'Toyota Hilux (Pick-up)' ou 'Renault Duster (SUV)' uma vez,
    e depois apenas seleciona ao cadastrar a viatura.
    """
    TIPO_CHOICES = [
        ('SUV', 'SUV'),
        ('PICK-UP', 'Pick-up'),
        ('SEDAN', 'Sedan'),
        ('BASE MOVEL', 'Base Móvel'),
        ('MOTOCICLETA', 'Motocicleta'),
        ('ONIBUS', 'Ônibus'),
        ('MICRO-ONIBUS', 'Micro-ônibus'),
    ]

    modelo = models.CharField(
        max_length=100, 
        unique=True,
        help_text="Ex: Toyota Hilux, Renault Duster, Chevrolet S10",
        verbose_name="Modelo do Veículo"
    )
    tipo = models.CharField(
        max_length=30, 
        choices=TIPO_CHOICES, 
        default='SUV',
        verbose_name="Tipo de Veículo"
    )

    class Meta:
        verbose_name = "Modelo de Viatura"
        verbose_name_plural = "Modelos de Viaturas"
        ordering = ['modelo']

    def __str__(self):
        return f"{self.modelo} ({self.get_tipo_display()})"


class Unidade(models.Model):
    """
    Removido o NOME_CHOICES. Agora os campos de texto são livres,
    permitindo digitar qualquer OPM à vontade.
    """
    nome = models.CharField(
        max_length=150, 
        unique=True,
        help_text="Ex: 5º Batalhão da Polícia Militar, Sede do Comando Regional",
        verbose_name="Nome Completo da Unidade"
    )
    sigla = models.CharField(
        max_length=50, # Aumentado o limite de caracteres
        help_text="Ex: 5º BPM, 14ª CIPMFT, Inteligência",
        verbose_name="Sigla"
    )

    class Meta:
        verbose_name = "Unidade"
        verbose_name_plural = "Unidades"
        ordering = ['sigla']

    def __str__(self):
        return self.sigla

    def total_operacionais(self):
        return self.viaturas.filter(situacao='OPERACIONAL').count()

    def total_baixadas(self):
        return self.viaturas.filter(situacao='BAIXADA').count()


class Viatura(models.Model):
    SITUACAO_CHOICES = [
        ('OPERACIONAL', 'Operacional'),
        ('BAIXADA', 'Baixada'),
    ]
    
    CONDICAO_CHOICES = [
        ('BOM', 'Bom Estado'),
        ('REGULAR', 'Regular'),
        ('RUIM', 'Ruim / Necessita Reparo'),
    ]

    unidade = models.ForeignKey(
        Unidade, 
        on_delete=models.CASCADE, 
        related_name='viaturas',
        verbose_name="Unidade Pertencente"
    )
    subunidade = models.CharField(
        max_length=100, 
        blank=True, 
        null=True, 
        help_text="Ex: Força Tática, Rádio Patrulha, SGO",
        verbose_name="Subunidade / Setor"
    )
    
    # CAMPOS SEPARADOS E EXPANDIDOS: Placa e Prefixo agora são independentes
    placa = models.CharField(
        max_length=20, # Aumentado para suportar formatos antigos, Mercosul ou especiais
        blank=True,
        null=True,
        verbose_name="Placa"
    )
    prefixo = models.CharField(
        max_length=30, # Permite mais caracteres para prefixos complexos
        blank=True,
        null=True,
        verbose_name="Prefixo / Código da Vtr"
    )
    
    # CHAVE ESTRANGEIRA PARA OS MODELOS CADASTRADOS
    modelo_veiculo = models.ForeignKey(
        ModeloViatura,
        on_delete=models.PROTECT, # Impede apagar um modelo se houver vtr usando ele
        related_name='viaturas',
        verbose_name="Modelo / Tipo de Veículo"
    )
    
    condicao = models.CharField(
        max_length=10, 
        choices=CONDICAO_CHOICES, 
        default='BOM',
        verbose_name="Condição Geral"
    )
    km = models.PositiveIntegerField(
        verbose_name="Quilometragem (KM)"
    )
    situacao = models.CharField(
        max_length=15, 
        choices=SITUACAO_CHOICES, 
        default='OPERACIONAL',
        verbose_name="Situação Atual"
    )
    observacao = models.TextField(
        blank=True, 
        null=True, 
        verbose_name="Observações / Motivo da Baixa"
    )

    class Meta:
        verbose_name = "Viatura"
        verbose_name_plural = "Viaturas"
        ordering = ['unidade', 'situacao', 'modelo_veiculo__modelo']

    def __str__(self):
        identificacao = self.prefixo if self.prefixo else self.placa
        return f"{self.modelo_veiculo.modelo} ({identificacao}) - {self.unidade.sigla}"
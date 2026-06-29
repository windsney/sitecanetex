from django.db import models

# --- MODELOS DE APOIO (Catálogos) ---

class NaturezaOcorrencia(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Natureza da Ocorrência")
    def __str__(self): return self.nome

class TipoMaterial(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Tipo (ex: Droga, Arma)")
    cor = models.CharField(max_length=7, default="#36a2eb", verbose_name="Cor (Hexadecimal)") # Adicione este campo
    def __str__(self): return self.nome

class UnidadeMedida(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Unidade (ex: petecas, gramas)")
    def __str__(self): return self.nome

# --- MODELO PRINCIPAL ---

class RegistroDiario(models.Model):
    # Identificação
    data_servico = models.DateField(verbose_name="Data do Serviço")
    comandante = models.CharField(max_length=150, blank=True, null=True, verbose_name="Comandante da GUPM")
    componente = models.CharField(max_length=150, blank=True, null=True, verbose_name="Componente da GUPM")
    
    # Ocorrência
    natureza_ocorrencia = models.ForeignKey(
        NaturezaOcorrencia, on_delete=models.SET_NULL, null=True, blank=True, 
        verbose_name="Natureza da Ocorrência"
    )
    detalhes_ocorrencia = models.TextField(blank=True, null=True, verbose_name="Detalhes da Ocorrência")
    
    # Produtividade (Contadores Diários)
    pessoas_abordadas = models.IntegerField(default=0, verbose_name="Pessoas Abordadas")
    veiculos_abordados = models.IntegerField(default=0, verbose_name="Veículos Abordados")
    notificacoes = models.IntegerField(default=0, verbose_name="Notificações Aplicadas")
    veiculos_apreendidos = models.IntegerField(default=0, verbose_name="Veículos Apreendidos")
    tco = models.IntegerField(default=0, verbose_name="TCO Confeccionados")
    pessoas_conduzidas = models.IntegerField(default=0, verbose_name="Pessoas Conduzidas")
    starts = models.IntegerField(default=0, verbose_name="Starts Realizados")
    barreiras = models.IntegerField(default=0, verbose_name="Barreiras Realizadas")
    
    class Meta:
        verbose_name = "Registro Diário"
        verbose_name_plural = "Registros Diários"

    def __str__(self):
        return f"{self.data_servico} - {self.natureza_ocorrencia or 'Produtividade'}"

# --- MODELO DE MATERIAIS (Vinculado ao Registro) ---

class MaterialApreendido(models.Model):
    # O related_name='materiais' é crucial para buscar os itens de um RegistroDiario
    ocorrencia = models.ForeignKey(
        RegistroDiario, 
        on_delete=models.CASCADE, 
        related_name='materiais',
        verbose_name="Registro de Origem"
    )
    
    tipo_material = models.ForeignKey(TipoMaterial, on_delete=models.PROTECT, verbose_name="Tipo")
    unidade = models.ForeignKey(UnidadeMedida, on_delete=models.PROTECT, verbose_name="Unidade")
    
    
    quantidade = models.IntegerField(default=0, verbose_name="Quantidade")

    class Meta:
        verbose_name = "Material Apreendido"
        verbose_name_plural = "Materiais Apreendidos"

    def __str__(self):
        return f"{self.tipo_material} ({self.quantidade} {self.unidade})"
from django.db import models

from django.db import models

# --- MODELOS DE APOIO (O seu "Catálogo" no Admin) ---

class NaturezaOcorrencia(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Natureza da Ocorrência")
    def __str__(self): return self.nome

class TipoMaterial(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Tipo (ex: Droga, Arma)")
    def __str__(self): return self.nome

class UnidadeMedida(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Unidade (ex: petecas, gramas)")
    def __str__(self): return self.nome

# --- MODELOS PRINCIPAIS ---

class RegistroDiario(models.Model):
    # Identificação
    data_servico = models.DateField(verbose_name="Data do Serviço")
    comandante = models.CharField(max_length=150, blank=True, null=True, verbose_name="Comandante da GUPM")
    componente = models.CharField(max_length=150, blank=True, null=True, verbose_name="Componente da GUPM")
    
    # Ocorrência: agora usa ForeignKey para buscar o catálogo
    natureza_ocorrencia = models.ForeignKey(
        NaturezaOcorrencia, on_delete=models.SET_NULL, null=True, blank=True, 
        verbose_name="Natureza da Ocorrência"
    )
    detalhes_ocorrencia = models.TextField(blank=True, null=True, verbose_name="Detalhes da Ocorrência")
    
    # Produtividade (Mantemos como Inteiros para facilitar os gráficos)
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

class MaterialApreendido(models.Model):
    ocorrencia = models.ForeignKey(
        RegistroDiario, 
        on_delete=models.CASCADE, 
        related_name='materiais'
    )
    
    # Agora usa ForeignKey para buscar o catálogo de tipos e unidades
    tipo_material = models.ForeignKey(TipoMaterial, on_delete=models.PROTECT, verbose_name="Tipo")
    unidade = models.ForeignKey(UnidadeMedida, on_delete=models.PROTECT, verbose_name="Unidade")
    
    natureza_especifica = models.CharField(max_length=100, verbose_name="Ex: Cocaína, Maconha")
    quantidade = models.IntegerField(default=0, verbose_name="Quantidade")

    class Meta:
        verbose_name = "Material Apreendido"
        verbose_name_plural = "Materiais Apreendidos"

    def __str__(self):
        return f"{self.natureza_especifica} ({self.quantidade} {self.unidade})"
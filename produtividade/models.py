from django.db import models

# --- MODELOS DE APOIO ---

class NaturezaOcorrencia(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Natureza da Ocorrência")
    def __str__(self): return self.nome

class TipoMaterial(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Tipo (ex: Droga, Arma)")
    cor = models.CharField(max_length=7, default="#36a2eb", verbose_name="Cor (Hex)")
    def __str__(self): return self.nome

class UnidadeMedida(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Unidade")
    def __str__(self): return self.nome

# --- MODELO DE CATEGORIAS DINÂMICAS ---

class CategoriaProdutividade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Categoria (ex: Escolas Visitadas)")
    cor = models.CharField(max_length=7, default="#36a2eb", verbose_name="Cor (Hex)")

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
    
    class Meta:
        verbose_name = "Registro Diário"
        verbose_name_plural = "Registros Diários"

    def __str__(self):
        return f"{self.data_servico} - {self.natureza_ocorrencia or 'Produtividade'}"

# --- MODELO DE VALORES DINÂMICOS ---

class ValorProdutividade(models.Model):
    registro = models.ForeignKey(RegistroDiario, on_delete=models.CASCADE, related_name='valores')
    categoria = models.ForeignKey(CategoriaProdutividade, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.categoria.nome}: {self.quantidade}"

# --- MODELO DE MATERIAIS ---

class MaterialApreendido(models.Model):
    ocorrencia = models.ForeignKey(
        RegistroDiario, 
        on_delete=models.CASCADE, 
        related_name='materiais',
        verbose_name="Registro de Origem"
    )
    tipo_material = models.ForeignKey(TipoMaterial, on_delete=models.PROTECT, verbose_name="Tipo")
    unidade = models.ForeignKey(UnidadeMedida, on_delete=models.PROTECT, verbose_name="Unidade")
    quantidade = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Material Apreendido"
        verbose_name_plural = "Materiais Apreendidos"

    def __str__(self):
        return f"{self.tipo_material} ({self.quantidade} {self.unidade})"
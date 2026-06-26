from django.contrib import admin
from .models import NaturezaOcorrencia, TipoMaterial, UnidadeMedida, RegistroDiario, MaterialApreendido

admin.site.register(NaturezaOcorrencia)
admin.site.register(TipoMaterial)
admin.site.register(UnidadeMedida)
admin.site.register(RegistroDiario)
admin.site.register(MaterialApreendido)
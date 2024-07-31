from django.contrib import admin
from .models import Sindicancia,Sindicado,Ipm,Conselho,Riog,Testemunha,Ofendido,Usuario
from django.contrib.auth.admin import UserAdmin

campos= list(UserAdmin.fieldsets)
campos.append(
    ("Informações profissionais",{'fields':('nome_completo','posto','cr','unidade','rgpm','rua','numero','bairro','cidade','cep','email_bpm','telefone')})
)

UserAdmin.fieldsets=tuple(campos)

admin.site.register(Sindicancia)
admin.site.register(Sindicado)
admin.site.register(Testemunha)
admin.site.register(Ofendido)
admin.site.register(Ipm)
admin.site.register(Conselho)
admin.site.register(Riog)
admin.site.register(Usuario,UserAdmin)


[
    ("Informações pessoais",{'fields':('Primeiro nome','Último nome')})
]
# Register your models here.

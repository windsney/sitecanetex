from .models import Sindicancia


def lista_sindicancia(request):
    lista_sindicancia= Sindicancia.objects.all().order_by('numero')
    return {"lista_sindicancia": lista_sindicancia}

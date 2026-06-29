from django.shortcuts import render, redirect
from django.db.models import Sum
from django.http import JsonResponse
from datetime import date, timedelta
from .models import RegistroDiario, MaterialApreendido
from .forms import RegistroDiarioForm, MaterialFormSet

# --- VIEWS DO DASHBOARD ---

def dashboard_view(request):
    """Renderiza a página principal do Dashboard."""
    return render(request, 'dashboard.html')

def api_dados_materiais(request):
    """Retorna a soma de materiais agrupados por TipoMaterial."""
    inicio = request.GET.get('inicio')
    fim = request.GET.get('fim')
    
    queryset = MaterialApreendido.objects.all()
    if inicio and fim:
        queryset = queryset.filter(ocorrencia__data_servico__range=[inicio, fim])
        
    # Agrupa pelo nome do tipo de material e da unidade
    dados = queryset.values('tipo_material__nome', 'tipo_material__cor', 'unidade__nome') \
        .annotate(total=Sum('quantidade')) \
        .filter(quantidade__gt=0) \
        .order_by('-total')
    
    return JsonResponse(list(dados), safe=False)

def api_dados_produtividade(request):
    """Retorna os dados de produtividade diária."""
    inicio = request.GET.get('inicio')
    fim = request.GET.get('fim')
    
    # Se não houver filtro, limita aos últimos 30 dias para evitar sobrecarga
    if not inicio or not fim:
        fim = date.today()
        inicio = fim - timedelta(days=30)
        
    queryset = RegistroDiario.objects.filter(data_servico__range=[inicio, fim])
        
    dados = queryset.aggregate(
        total_pessoas=Sum('pessoas_conduzidas'),
        total_veiculos=Sum('veiculos_apreendidos'),
        total_notificacoes=Sum('notificacoes'),
        total_tco=Sum('tco'),
        total_starts=Sum('starts'),
        total_barreiras=Sum('barreiras')
    )
    
    return JsonResponse([dados], safe=False)

# --- VIEWS DE LANÇAMENTO (P3) ---

def registrar_ocorrencia(request):
    """View para o operador P3 lançar registros."""
    if request.method == "POST":
        form = RegistroDiarioForm(request.POST)
        formset = MaterialFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            registro = form.save()
            formset.instance = registro
            formset.save()
            return redirect('produtividade:dashboard')
    else:
        form = RegistroDiarioForm()
        formset = MaterialFormSet()
    
    return render(request, 'registrar.html', {'form': form, 'formset': formset})
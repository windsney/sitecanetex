from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db.models import Sum
from .models import RegistroDiario, ValorProdutividade, MaterialApreendido
from datetime import date, timedelta

# --- API PARA O GRÁFICO 1 (MATERIAIS) ---
def api_dados_materiais(request):
    inicio = request.GET.get('inicio')
    fim = request.GET.get('fim')
    
    queryset = MaterialApreendido.objects.all()
    if inicio and fim:
        queryset = queryset.filter(ocorrencia__data_servico__range=[inicio, fim])
        
    dados = queryset.values('tipo_material__nome', 'tipo_material__cor', 'unidade__nome') \
        .annotate(total=Sum('quantidade')) \
        .filter(quantidade__gt=0) \
        .order_by('-total')
    
    return JsonResponse(list(dados), safe=False)

# --- API PARA O GRÁFICO 2 (PRODUTIVIDADE DINÂMICA) ---
def api_dados_produtividade(request):
    inicio = request.GET.get('inicio')
    fim = request.GET.get('fim')
    
    # Se não houver filtro, pega os últimos 30 dias
    if not inicio or not fim:
        fim = date.today()
        inicio = fim - timedelta(days=30)
        
    # Filtra os valores baseados na data do RegistroDiario pai
    queryset = ValorProdutividade.objects.filter(registro__data_servico__range=[inicio, fim])
        
    # Agrupa pelo nome da categoria e cor, somando as quantidades
    dados = queryset.values('categoria__nome', 'categoria__cor') \
        .annotate(total=Sum('quantidade')) \
        .filter(total__gt=0) \
        .order_by('-total')
    
    return JsonResponse(list(dados), safe=False)

# --- VIEW DO DASHBOARD ---
def dashboard_view(request):
    return render(request, 'dashboard.html')
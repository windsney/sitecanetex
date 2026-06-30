from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db.models import Sum
from .models import NaturezaOcorrencia,RegistroDiario, ValorProdutividade, MaterialApreendido, CategoriaProdutividade,TipoMaterial, UnidadeMedida
from datetime import date, timedelta

# --- API PARA O GRÁFICO 1 (MATERIAIS) ---
def api_dados_materiais(request):
    inicio = request.GET.get('inicio')
    fim = request.GET.get('fim')
    
    
    queryset = MaterialApreendido.objects.all()
    if inicio and fim:
        queryset = queryset.filter(ocorrencia__data_servico__range=[inicio, fim])
        
    dados = queryset.values('tipo_material__nome', 'tipo_material__cor', 'unidade__nome','ocorrencia__natureza_ocorrencia__cor') \
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


def registrar_ocorrencia(request):
    # Busca dados para exibir no formulário
    context = {
        'categorias': CategoriaProdutividade.objects.all(),
        'naturezas': NaturezaOcorrencia.objects.all(),
        'tipos_material': TipoMaterial.objects.all(),
        'unidades': UnidadeMedida.objects.all()
    }

    if request.method == "POST":
        # 1. Cria o Registro base
        natureza_id = request.POST.get('natureza_ocorrencia')
        novo_registro = RegistroDiario.objects.create(
            data_servico=request.POST.get('data_servico'),
            comandante=request.POST.get('comandante'),
            componente=request.POST.get('componente'),
            natureza_ocorrencia_id=natureza_id if natureza_id else None,
            detalhes_ocorrencia=request.POST.get('detalhes_ocorrencia')
        )
        
        # 2. Salva as categorias de produtividade
        for cat in context['categorias']:
            valor = request.POST.get(f'cat_{cat.id}', 0)
            if int(valor) > 0:
                ValorProdutividade.objects.create(
                    registro=novo_registro, 
                    categoria=cat, 
                    quantidade=valor
                )
        
        # 3. Salva os materiais apreendidos (processa as listas do formulário)
        tipos = request.POST.getlist('material_tipo[]')
        qtds = request.POST.getlist('material_qtd[]')
        unis = request.POST.getlist('material_unidade[]')
        
        for i in range(len(tipos)):
            if tipos[i] and int(qtds[i] or 0) > 0:
                MaterialApreendido.objects.create(
                    ocorrencia=novo_registro,
                    tipo_material_id=tipos[i],
                    quantidade=qtds[i],
                    unidade_id=unis[i]
                )
        
        return redirect('produtividade:dashboard')
        
    return render(request, 'registrar.html', context)
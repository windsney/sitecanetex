from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Unidade, Viatura

class DashboardView(LoginRequiredMixin, ListView):
    model = Unidade
    template_name = 'home.html'  # Apontando para o seu home.html dentro de vtr
    context_object_name = 'unidades'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # 1. Totais Gerais do topo do Painel (Cards grandes vermelhos e verdes)
        context['total_geral_operacional'] = Viatura.objects.filter(situacao='OPERACIONAL').count()
        context['total_geral_baixada'] = Viatura.objects.filter(situacao='BAIXADA').count()

        # 2. Varre as unidades e usa os métodos do seu Model para fazer os cálculos
        unidades_processadas = []
        for unidade in Unidade.objects.all():
            total_vtrs = unidade.viaturas.count()
            
            # Executa os métodos que você acabou de criar no models.py:
            operacionais = unidade.total_operacionais()
            baixadas = unidade.total_baixadas()
            
            # Faz a regra de três da porcentagem (evitando divisão por zero)
            pct_operacional = int((operacionais / total_vtrs) * 100) if total_vtrs > 0 else 0
            pct_baixada = int((baixadas / total_vtrs) * 100) if total_vtrs > 0 else 0
            
            # Monta o dicionário mastigado que o HTML vai ler
            unidades_processadas.append({
                'pk': unidade.pk,
                'sigla': unidade.sigla,
                'nome': unidade.nome, # Pega o nome extenso do CHOICES
                'operacionais': operacionais,
                'baixadas': baixadas,
                'pct_operacional': pct_operacional,
                'pct_baixada': pct_baixada,
                'total_vtrs': total_vtrs,
            })
            
        # Devolve para o HTML a lista com os cálculos prontos
        context['unidades'] = unidades_processadas
        return context


# Mantendo as outras Views do seu sistema estruturadas:
class UnidadeDetailView(LoginRequiredMixin, DetailView):
    model = Unidade
    template_name = 'unidade_detail.html'
    context_object_name = 'unidade'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vtrs = self.object.viaturas.all()
        
        # Filtros da barra de pesquisa
        pesquisa = self.request.GET.get('pesquisa', '').strip()
        situacao = self.request.GET.get('situacao', '').strip()
        condicao = self.request.GET.get('condicao', '').strip()

        if pesquisa:
            # AJUSTADO AQUI: Adicionado prefixo__icontains e alterado para modelo_veiculo__modelo__icontains
            vtrs = vtrs.filter(
                Q(placa__icontains=pesquisa) | 
                Q(prefixo__icontains=pesquisa) | 
                Q(modelo_veiculo__modelo__icontains=pesquisa) | 
                Q(subunidade__icontains=pesquisa)
            )
        if situacao:
            vtrs = vtrs.filter(situacao=situacao)
        if condicao:
            vtrs = vtrs.filter(condicao=condicao)

        # AJUSTADO AQUI: Mudado a ordenação para buscar o campo através do relacionamento correto
        context['viaturas'] = vtrs.order_by('situacao', 'modelo_veiculo__modelo')
        context['filtros'] = {'pesquisa': pesquisa, 'situacao': situacao, 'condicao': condicao}
        return context

class GerenciamentoFrotaListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Viatura
    template_name = 'gerenciar_frota.html'
    context_object_name = 'viaturas'
    permission_required = 'vtr.view_viatura' # Exige permissão de ver a lista interna

    def get_queryset(self):
        return Viatura.objects.all().order_by('unidade__sigla', 'situacao', 'modelo_veiculo__modelo')

class ViaturaCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Viatura
    fields = '__all__'
    template_name = 'viatura_form.html'
    permission_required = 'vtr.add_viatura' # Exige permissão de adicionar
    success_url = reverse_lazy('vtr:gerenciar_frota')

class ViaturaUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Viatura
    fields = '__all__'
    template_name = 'viatura_form.html'
    permission_required = 'vtr.change_viatura' # Exige permissão de editar
    success_url = reverse_lazy('vtr:gerenciar_frota')

class ViaturaDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Viatura
    template_name = 'viatura_confirm_delete.html'
    permission_required = 'vtr.delete_viatura' # Exige permissão de deletar
    success_url = reverse_lazy('vtr:gerenciar_frota')


class EfetivoView(LoginRequiredMixin, ListView):
    model = Unidade
    template_name = 'efetivo.html'  # Apontando para o seu home.html dentro de vtr
    context_object_name = 'unidades'

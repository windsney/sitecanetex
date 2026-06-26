from .models import RegistroDiario, MaterialApreendido # Importe do models aqui
from .forms import RegistroDiarioForm, MaterialFormSet
from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from django.db.models import Sum, Count
from .models import RegistroDiario
from .forms import RegistroDiarioForm, MaterialFormSet,MaterialApreendido
import json

# --- LANÇAMENTO (Operador) ---
class RegistrarOcorrenciaView(CreateView):
    model = RegistroDiario
    form_class = RegistroDiarioForm
    template_name = 'registrar.html'
    success_url = reverse_lazy('produtividade:dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = MaterialFormSet(self.request.POST)
        else:
            context['formset'] = MaterialFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        return self.form_invalid(form)

# --- DASHBOARD (Visualizador/Gestor) ---
class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data_inicio = self.request.GET.get('data_inicio')
        data_fim = self.request.GET.get('data_fim')
        
        registros = RegistroDiario.objects.all()
        materiais = MaterialApreendido.objects.all()
        
        if data_inicio and data_fim:
            registros = registros.filter(data_servico__range=[data_inicio, data_fim])
            materiais = materiais.filter(ocorrencia__data_servico__range=[data_inicio, data_fim])
            
        # Produtividade
        context['totais'] = registros.aggregate(
            abordados=Sum('pessoas_abordadas'),
            notificacoes=Sum('notificacoes'),
            apreensoes=Sum('veiculos_apreendidos'),
            pessoas_conduzidas=Sum('pessoas_conduzidas')
        )
        
        # Materiais - Usando json.dumps para enviar dados perfeitos ao JS
        dados = materiais.values('tipo_material__nome', 'natureza_especifica', 'unidade__nome') \
                         .annotate(total=Sum('quantidade')) \
                         .order_by('-total')

        # Criamos duas listas separadas, mas garantimos que o índice 0 de labels
        # seja o índice 0 de totais
        labels = []
        totais = []
        
        for d in dados:
            labels.append(f"{d['unidade__nome']} de {d['natureza_especifica']} ({d['tipo_material__nome']})")
            totais.append(d['total'])
            
        context['mat_labels'] = json.dumps(labels)
        context['mat_totais'] = json.dumps(totais)
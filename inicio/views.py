from django.shortcuts import render,reverse
from .models import Sindicancia,Sindicado,Ofendido,Testemunha
from django.views.generic import TemplateView,ListView,DetailView, FormView

import os
from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from .forms import SindicadoForm,SindicanciaForm,TestemunhaForm,OfendidoForm,UsuarioForm
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from .models import Sindicancia
import os
from django.conf import settings
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx import Document
from docx.shared import Cm,Pt

from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docxtpl import DocxTemplate
from django.http import HttpResponse
from meu_modulo.data_escrita import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required






'''class Home(TemplateView):
    template_name = "login.html"
'''

class Sind_Cadastradas(LoginRequiredMixin,ListView):

    template_name = "sindicancias_cadastradas.html"
    model = Sindicancia

'''class Detalhe_sind(DetailView):

    template_name = "detalhe_sind.html"
    model = Sindicancia
'''
'''class Cadastro_investigado_sind(DetailView):

    template_name = "cad_investigado_sind.html"
    model = Sindicado
'''
class Cd(TemplateView):

    template_name = "cad_cd.html"

class Inquerito (TemplateView):
    template_name = "cad_ipm.html"


class RIOG(TemplateView):
    template_name = "cad_riog.html"
class Criar_conta(FormView):
    template_name = "criar_conta.html"
    form_class = UsuarioForm
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('inicio:login')


@login_required(login_url='/')
def criar_sindicancia(request):
    usuario= request.user.rgpm
    if request.method == 'POST':
        form = SindicanciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio:sind_cadastradas')  # Redirecione para uma página de sucesso após salvar
    else:
        form = SindicanciaForm()
    return render(request, 'criar_sindicancia.html', {'form': form,'usuario':usuario})

@login_required(login_url='/')
def editar_sindicancia(request, id):
    usuario = request.user.rgpm
    sindicancia = get_object_or_404(Sindicancia, id=id)

    if request.method == 'POST':
        form = SindicanciaForm(request.POST, instance=sindicancia)
        if form.is_valid():
            form.save()
            return redirect('inicio:sind_cadastradas')  # Redirecione para uma página de sucesso após salvar
    else:
        form = SindicanciaForm(instance=sindicancia)

    print(sindicancia.data_portaria)

    return render(request, 'editar_sindicancia.html', {'form': form, 'sindicancia': sindicancia})

@login_required(login_url='/')
def excluir_sindicancia(request, id):
    sindicancia = get_object_or_404(Sindicancia, id=id)

    if request.method == 'POST':
        sindicancia.delete()
        return redirect('inicio:sind_cadastradas')  # Redirecionar após exclusão

    return render(request,'sindicancias_cadastradas.html' , {'sindicancia': sindicancia})
@login_required(login_url='/')
def detalhes_sindicancia(request, sindicancia_id):



    sindicancia = get_object_or_404(Sindicancia, pk=sindicancia_id)
    sindicados = sindicancia.sindicados.all()
    testemunhas = sindicancia.testemunhas.all()
    ofendidos = sindicancia.ofendidos.all()
    email = request.user.telefone


    # Adicione as queries para testemunhas, ofendidos e ofícios conforme necessário
    # testemunhas = sindicancia.testemunhas.all()
    # ofendidos = sindicancia.ofendidos.all()
    # oficios = sindicancia.oficios.all()
    vixi= len(sindicados)





    context = {
        'sindicancia': sindicancia,
        'sindicados': sindicados,
        'testemunhas': testemunhas,
        'ofendidos': ofendidos,
        'user_email': email,

        # Adicione as queries para testemunhas, ofendidos e ofícios conforme necessário
        # 'testemunhas': testemunhas,
        # 'ofendidos': ofendidos,

         'vixi': vixi,

    }


    return render(request, 'detalhe_sind.html', context)
@login_required(login_url='/')
def gerar_inicio_dos_trabalhos(request, sindicancia_id):
    template_path = os.path.join(settings.BASE_DIR, 'inicio/templates', 'inicio_dos_trabalhos.docx')

    sindicancia = get_object_or_404(Sindicancia, pk=sindicancia_id)
    sindicados = sindicancia.sindicados.all()
    documento = DocxTemplate(template_path)  # DOCUMENTO  EXEMPLO#

    #dia_inicio = sindicancia.data_inicio

    mes_ini = sindicancia.data_inicio.month
    mesescritoini = mes_escrito(mes_ini)
    diaini = sindicancia.data_inicio.strftime('%d') if sindicancia.data_inicio else ''
    anoini = sindicancia.data_inicio.year

    dia_inicio = f'{diaini} de {mesescritoini} de {anoini}'


    posto_delegante = sindicancia.posto_delegante
    nome_delegante = sindicancia.delegante
    funcao_delegante = sindicancia.funcao_delegante
    portaria = sindicancia.numero

    #datada = sindicancia.data_portaria
    mes_port= sindicancia.data_portaria.month
    mesescritoport=mes_escrito(mes_port)
    diaport=sindicancia.data_portaria.strftime('%d') if sindicancia.data_portaria else ''
    anoport=sindicancia.data_portaria.year


    datada= f'{diaport} de {mesescritoport} de {anoport}'




    #dia_recebido = sindicancia.dia_recebido
    mes_rec = sindicancia.dia_recebido.month
    mesescritorec = mes_escrito(mes_rec)
    diarec = sindicancia.dia_recebido.strftime('%d') if sindicancia.dia_recebido else ''
    anorec = sindicancia.dia_recebido.year

    dia_recebido = f'{diarec} de {mesescritorec} de {anorec}'



    nome_delegada = sindicancia.delegada
    posto_delegada = sindicancia.posto_delegada
    rg_delegada = sindicancia.rg_delegada
    context = {  # VARIÁ
        "dia_inicio": f"{dia_inicio}",
        "posto_delegante": f"{posto_delegante}",
        "nome_delegante": f"{nome_delegante}",
        "funcao_delegante": f"{funcao_delegante}",
        "portaria": f"{portaria}",
        "datada": f"{datada}",
        "dia_recebido": f"{dia_recebido}",
        "nome_delegada": f"{nome_delegada}",
        "posto_delegada": f"{posto_delegada}",
        "rg_delegada": f"{rg_delegada}",

    }
    documento.render(context)

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = f'attachment; filename= inicio_dos_trabalhos {portaria}.docx'
    documento.save(response)

    return response


@login_required(login_url='/')
def gerar_declaracao_sindicado(request,sindicancia_id,id):
    sindicado = get_object_or_404(Sindicado, id=id)
    sindicancia = get_object_or_404(Sindicancia, pk=sindicancia_id)
    template_path = os.path.join(settings.BASE_DIR, 'inicio/templates', 'declaracao_sindicado.docx')




    documento = DocxTemplate(template_path)  # DOCUMENTO  EXEMPLO#

    #dia_inicio = sindicancia.data_inicio



    decla_sindicado = sindicado.declaracao
    nome_sindicado= sindicado.nome
    posto_sindicado= sindicado.posto_sindicado
    mae_sindicado= sindicado.mae
    pai_sindicado= sindicado.pai
    rg_sindicado= sindicado.rgpm
    lotacao_sindicado=sindicado.lotacao
    endereco_sindicado=sindicado.endereco
    portaria= sindicancia.numero

    mes_port = sindicancia.data_portaria.month
    mesescritoport = mes_escrito(mes_port)
    diaport = sindicancia.data_portaria.strftime('%d') if sindicancia.data_portaria else ''
    anoport = sindicancia.data_portaria.year

    datada = f'{diaport} de {mesescritoport} de {anoport}'

    hora_inicio=sindicado.hora_inicio
    hora_fim=sindicado.hora_fim
    sindicante= sindicancia.delegada
    posto_sindicante=sindicancia.posto_delegada
    rg_sindicante= sindicancia.rg_delegada
    cpf=sindicado.cpf
    email=sindicado.email
    telefone= sindicado.telefone

    mes_nasc = sindicado.data_nascimento.month
    mesescritonasc = mes_escrito(mes_nasc)
    dianasc = sindicado.data_nascimento.strftime('%d') if sindicancia.data_portaria else ''
    anonasc = sindicado.data_nascimento.year

    data_nascimento = f'{dianasc} de {mesescritonasc} de {anonasc}'



    mes_inqui = sindicado.data_inquiricao.month
    mesescritoinqui = mes_escrito(mes_inqui)
    diainqui = sindicado.data_inquiricao.day
    diaescritoinqui = dia_escrito(diainqui)
    anoinqui = sindicado.data_inquiricao.year
    anoescritoinqui = ano_escrito(anoinqui)

    data_inquiricao = f'{diaescritoinqui} dias do mês de {mesescritoinqui} do ano de {anoescritoinqui}'



    naturalidade=sindicado.naturalidade

    cr= sindicancia.unidade.upper()

    lotacao_delegada= sindicancia.lotacao_delegada
    lotacao_delegada1 = sindicancia.lotacao_delegada.upper()
    rua_quartel=sindicancia.rua_quartel
    numero_quartel=sindicancia.numero_quartel
    bairro_quartel=sindicancia.bairro_quartel
    cidade_quartel=sindicancia.cidade_quartel
    cep_quartel=sindicancia.cep_quartel
    telefone_quartel=sindicancia.telefone_quartel
    email_quartel=sindicancia.email_quartel


    context = {  # VARIÁ
        "cr": f"{cr}",
        "lotacao_delegada": f"{lotacao_delegada}",
        "lotacao_delegada1": f"{lotacao_delegada1}",
        "rua_quartel": f"{rua_quartel}",
        "numero_quartel": f"{numero_quartel}",
        "bairro_quartel": f"{bairro_quartel}",
        "cidade_quartel": f"{cidade_quartel}",
        "cep_quartel": f"{cep_quartel}",
        "telefone_quartel": f"{telefone_quartel}",
        "email_quartel": f"{email_quartel}",

        "decla_sindicado": f"{decla_sindicado}",
        "nome_sindicado": f"{nome_sindicado}",
        "posto_sindicado": f"{posto_sindicado}",
        "mae_sindicado": f"{mae_sindicado}",
        "pai_sindicado": f"{pai_sindicado}",
        "rg_sindicado": f"{rg_sindicado}",
        "cpf": f"{cpf}",
        "email": f"{email}",
        "telefone": f"{telefone}",
        "data_nascimento": f"{data_nascimento}",
        "naturalidade": f"{naturalidade}",
       "endereco_sindicado": f"{endereco_sindicado}",
        "lotacao_sindicado": f"{lotacao_sindicado}",
        "portaria": f"{portaria}",
        "datada": f"{datada}",
        "hora_inicio": f"{hora_inicio}",
        "hora_fim": f"{hora_fim}",
        "sindicante": f"{sindicante}",
        "posto_sindicante": f"{posto_sindicante}",
        "rg_sindicante": f"{rg_sindicante}",
        "data_inquiricao": f"{data_inquiricao}"

    }
    documento.render(context)

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = f'attachment; filename= declaração {nome_sindicado}.docx'
    documento.save(response)

    return response


@login_required(login_url='/')
def gerar_declaracao_testemunha(request,sindicancia_id,id):
    testemunha = get_object_or_404(Testemunha, id=id)
    sindicancia = get_object_or_404(Sindicancia, pk=sindicancia_id)
    template_path = os.path.join(settings.BASE_DIR, 'inicio/templates', 'declaracao_testemunha.docx')




    documento = DocxTemplate(template_path)  # DOCUMENTO  EXEMPLO#

    #dia_inicio = sindicancia.data_inicio



    decla_sindicado = testemunha.declaracao
    nome_sindicado= testemunha.nome

    mae_sindicado= testemunha.mae
    pai_sindicado= testemunha.pai
    rg_sindicado= testemunha.rgpm
    profissao=testemunha.profissao
    endereco_sindicado=testemunha.endereco
    portaria= sindicancia.numero

    mes_port = sindicancia.data_portaria.month
    mesescritoport = mes_escrito(mes_port)
    diaport = sindicancia.data_portaria.strftime('%d') if sindicancia.data_portaria else ''
    anoport = sindicancia.data_portaria.year

    datada = f'{diaport} de {mesescritoport} de {anoport}'

    hora_inicio=testemunha.hora_inicio
    hora_fim=testemunha.hora_fim
    sindicante= sindicancia.delegada
    posto_sindicante=sindicancia.posto_delegada
    rg_sindicante= sindicancia.rg_delegada
    cpf=testemunha.cpf
    email=testemunha.email
    telefone= testemunha.telefone

    mes_nasc = testemunha.data_nascimento.month
    mesescritonasc = mes_escrito(mes_nasc)
    dianasc = testemunha.data_nascimento.strftime('%d') if sindicancia.data_portaria else ''
    anonasc = testemunha.data_nascimento.year

    data_nascimento = f'{dianasc} de {mesescritonasc} de {anonasc}'



    mes_inqui = testemunha.data_inquiricao.month
    mesescritoinqui = mes_escrito(mes_inqui)
    diainqui = testemunha.data_inquiricao.day
    diaescritoinqui = dia_escrito(diainqui)
    anoinqui = testemunha.data_inquiricao.year
    anoescritoinqui = ano_escrito(anoinqui)

    data_inquiricao = f'{diaescritoinqui} dias do mês de {mesescritoinqui} do ano de {anoescritoinqui}'



    naturalidade=testemunha.naturalidade

    cr= sindicancia.unidade.upper()

    lotacao_delegada= sindicancia.lotacao_delegada
    lotacao_delegada1 = sindicancia.lotacao_delegada.upper()
    rua_quartel=sindicancia.rua_quartel
    numero_quartel=sindicancia.numero_quartel
    bairro_quartel=sindicancia.bairro_quartel
    cidade_quartel=sindicancia.cidade_quartel
    cep_quartel=sindicancia.cep_quartel
    telefone_quartel=sindicancia.telefone_quartel
    email_quartel=sindicancia.email_quartel


    context = {  # VARIÁ
        "cr": f"{cr}",
        "lotacao_delegada": f"{lotacao_delegada}",
        "lotacao_delegada1": f"{lotacao_delegada1}",
        "rua_quartel": f"{rua_quartel}",
        "numero_quartel": f"{numero_quartel}",
        "bairro_quartel": f"{bairro_quartel}",
        "cidade_quartel": f"{cidade_quartel}",
        "cep_quartel": f"{cep_quartel}",
        "telefone_quartel": f"{telefone_quartel}",
        "email_quartel": f"{email_quartel}",

        "decla_sindicado": f"{decla_sindicado}",
        "nome_sindicado": f"{nome_sindicado}",

        "mae_sindicado": f"{mae_sindicado}",
        "pai_sindicado": f"{pai_sindicado}",
        "rg_sindicado": f"{rg_sindicado}",
        "cpf": f"{cpf}",
        "email": f"{email}",
        "telefone": f"{telefone}",
        "data_nascimento": f"{data_nascimento}",
        "naturalidade": f"{naturalidade}",
       "endereco_sindicado": f"{endereco_sindicado}",
        "profissao": f"{profissao}",
        "portaria": f"{portaria}",
        "datada": f"{datada}",
        "hora_inicio": f"{hora_inicio}",
        "hora_fim": f"{hora_fim}",
        "sindicante": f"{sindicante}",
        "posto_sindicante": f"{posto_sindicante}",
        "rg_sindicante": f"{rg_sindicante}",
        "data_inquiricao": f"{data_inquiricao}"

    }
    documento.render(context)

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = f'attachment; filename= declaração {nome_sindicado}.docx'
    documento.save(response)

    return response

@login_required(login_url='/')
def gerar_declaracao_ofendido(request, sindicancia_id, id):
    ofendido = get_object_or_404(Ofendido, id=id)
    sindicancia = get_object_or_404(Sindicancia, pk=sindicancia_id)
    template_path = os.path.join(settings.BASE_DIR, 'inicio/templates', 'declaracao_ofendido.docx')

    documento = DocxTemplate(template_path)  # DOCUMENTO  EXEMPLO#

    # dia_inicio = sindicancia.data_inicio

    decla_sindicado = ofendido.declaracao
    nome_sindicado = ofendido.nome

    mae_sindicado = ofendido.mae
    pai_sindicado = ofendido.pai
    rg_sindicado = ofendido.rgpm
    profissao = ofendido.profissao
    endereco_sindicado = ofendido.endereco
    portaria = sindicancia.numero

    mes_port = sindicancia.data_portaria.month
    mesescritoport = mes_escrito(mes_port)
    diaport = sindicancia.data_portaria.strftime('%d') if sindicancia.data_portaria else ''
    anoport = sindicancia.data_portaria.year

    datada = f'{diaport} de {mesescritoport} de {anoport}'

    hora_inicio = ofendido.hora_inicio
    hora_fim = ofendido.hora_fim
    sindicante = sindicancia.delegada
    posto_sindicante = sindicancia.posto_delegada
    rg_sindicante = sindicancia.rg_delegada
    cpf = ofendido.cpf
    email = ofendido.email
    telefone = ofendido.telefone

    mes_nasc = ofendido.data_nascimento.month
    mesescritonasc = mes_escrito(mes_nasc)
    dianasc = ofendido.data_nascimento.strftime('%d') if sindicancia.data_portaria else ''
    anonasc = ofendido.data_nascimento.year

    data_nascimento = f'{dianasc} de {mesescritonasc} de {anonasc}'

    mes_inqui = ofendido.data_inquiricao.month
    mesescritoinqui = mes_escrito(mes_inqui)
    diainqui = ofendido.data_inquiricao.day
    diaescritoinqui = dia_escrito(diainqui)
    anoinqui = ofendido.data_inquiricao.year
    anoescritoinqui = ano_escrito(anoinqui)

    data_inquiricao = f'{diaescritoinqui} dias do mês de {mesescritoinqui} do ano de {anoescritoinqui}'

    naturalidade = ofendido.naturalidade

    cr = sindicancia.unidade.upper()

    lotacao_delegada = sindicancia.lotacao_delegada
    lotacao_delegada1 = sindicancia.lotacao_delegada.upper()
    rua_quartel = sindicancia.rua_quartel
    numero_quartel = sindicancia.numero_quartel
    bairro_quartel = sindicancia.bairro_quartel
    cidade_quartel = sindicancia.cidade_quartel
    cep_quartel = sindicancia.cep_quartel
    telefone_quartel = sindicancia.telefone_quartel
    email_quartel = sindicancia.email_quartel

    context = {  # VARIÁ
        "cr": f"{cr}",
        "lotacao_delegada": f"{lotacao_delegada}",
        "lotacao_delegada1": f"{lotacao_delegada1}",
        "rua_quartel": f"{rua_quartel}",
        "numero_quartel": f"{numero_quartel}",
        "bairro_quartel": f"{bairro_quartel}",
        "cidade_quartel": f"{cidade_quartel}",
        "cep_quartel": f"{cep_quartel}",
        "telefone_quartel": f"{telefone_quartel}",
        "email_quartel": f"{email_quartel}",

        "decla_sindicado": f"{decla_sindicado}",
        "nome_sindicado": f"{nome_sindicado}",

        "mae_sindicado": f"{mae_sindicado}",
        "pai_sindicado": f"{pai_sindicado}",
        "rg_sindicado": f"{rg_sindicado}",
        "cpf": f"{cpf}",
        "email": f"{email}",
        "telefone": f"{telefone}",
        "data_nascimento": f"{data_nascimento}",
        "naturalidade": f"{naturalidade}",
        "endereco_sindicado": f"{endereco_sindicado}",
        "profissao": f"{profissao}",
        "portaria": f"{portaria}",
        "datada": f"{datada}",
        "hora_inicio": f"{hora_inicio}",
        "hora_fim": f"{hora_fim}",
        "sindicante": f"{sindicante}",
        "posto_sindicante": f"{posto_sindicante}",
        "rg_sindicante": f"{rg_sindicante}",
        "data_inquiricao": f"{data_inquiricao}"

    }
    documento.render(context)

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = f'attachment; filename= declaração {nome_sindicado}.docx'
    documento.save(response)

    return response



@login_required(login_url='/')
def gerar_relatorio(request, sindicancia_id):
    sindicancia = get_object_or_404(Sindicancia, pk=sindicancia_id)
    template_path = os.path.join(settings.BASE_DIR, 'inicio/templates', 'relatorio_modelo.docx')
    # Criar um novo documento
    doc = Document(template_path)


    # Adiciona um parágrafo com o texto desejado
    paragrafo = doc.add_paragraph()
    run = paragrafo.add_run(
        "Este é um texto em itálico e com recfdfdfjdflkdjfkdjflkdjflkdsjfldkfjdlskfjdslkfjdlfjdslfjdlfjdslfjlkjdfjdslfjdslkfjdslkfsdjflkjflksdfjdskfjdlfjkdlfjdskfjdflkjsdfklsdjflsdkfjsdklfjslkuo até o meio da página.")
    run.italic = True

    # Define o recuo do parágrafo até o meio da página (assumindo uma largura de página padrão de 21 cm)
    # Metade da página seria 10.5 cm
    paragrafo.paragraph_format.left_indent = Cm(8.5)

    paragrafo = doc.add_paragraph()
    run = paragrafo.add_run(
        "Este é um texto em normal e com recfdfdfjdflkdjfkdjflkdjflkdsjfldkfjdlskfjdslkfjdlfjdslfjdlfjdslfjlkjdfjdslfjdslkfjdslkfsdjflkjflksdfjdskfjdlfjkdlfjdskfjdflkjsdfklsdjflsdkfjsdklfjslkuo até o meio da página.")
    run.italic = False

    # Define o recuo do parágrafo até o meio da página (assumindo uma largura de página padrão de 21 cm)
    # Metade da página seria 10.5 cm
    

    # Salva o documento



    # Nome do arquivo
    nome = 'foisim'

    # Configurar a resposta HTTP para download do arquivo
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = f'attachment; filename="relatorio_{nome}.docx"'

    # Salvar o documento modificado na resposta
    try:
        doc.save(response)
    except Exception as e:
        return HttpResponse(f"Erro ao salvar o documento: {e}", status=500)

    return response

@login_required(login_url='/')
def cadastrar_sindicado(request, sindicancia_id):
    sindicancia = get_object_or_404(Sindicancia, pk=sindicancia_id)

    if request.method == 'POST':
        form = SindicadoForm(request.POST)
        if form.is_valid():
            sindicado = form.save(commit=False)
            sindicado.portaria = sindicancia
            sindicado.save()
            return redirect('inicio:detalhes_sindicancia', sindicancia_id=sindicancia.id)
    else:
        form = SindicadoForm()

    return render(request, 'cadastrar_sindicado.html', {'form': form, 'sindicancia': sindicancia})

@login_required(login_url='/')
def editar_sindicado(request,sindicancia_id, id):
    sindicado = get_object_or_404(Sindicado, id=id)
    sindicancia = get_object_or_404(Sindicancia, pk=sindicancia_id)
    if request.method == 'POST':
        form = SindicadoForm(request.POST, instance=sindicado)
        if form.is_valid():
            form.save()
            return redirect('inicio:detalhes_sindicancia',sindicancia_id=sindicancia.id)
    else:
        form = SindicadoForm(instance=sindicado)


    return render(request, 'editar_sindicado.html', {'form': form,'sindicado':sindicado,'sindicancia':sindicancia})
@login_required(login_url='/')
def excluir_sindicado(request, sindicancia_id, id):
    sindicado = get_object_or_404(Sindicado, id=id)
    if request.method == 'POST':
        sindicado.delete()
        return redirect('inicio:detalhes_sindicancia', sindicancia_id=sindicancia_id)
    return render(request, 'sindicancias_cadastradas.html', {'sindicado': sindicado})



@login_required(login_url='/')
def cadastrar_testemunha(request, sindicancia_id):
    sindicancia = get_object_or_404(Sindicancia, pk=sindicancia_id)

    if request.method == 'POST':
        form = TestemunhaForm(request.POST)
        if form.is_valid():
            testemunha = form.save(commit=False)
            testemunha.portaria = sindicancia
            testemunha.save()
            return redirect('inicio:detalhes_sindicancia', sindicancia_id=sindicancia.id)
    else:
        form = TestemunhaForm()

    return render(request, 'cadastrar_testemunha.html', {'form': form, 'sindicancia': sindicancia})

@login_required(login_url='/')
def editar_testemunha(request,sindicancia_id, id):
    testemunha = get_object_or_404(Testemunha, id=id)
    sindicancia = get_object_or_404(Sindicancia, pk=sindicancia_id)
    if request.method == 'POST':
        form = TestemunhaForm(request.POST, instance=testemunha)
        if form.is_valid():
            form.save()
            return redirect('inicio:detalhes_sindicancia',sindicancia_id=sindicancia.id)
    else:
        form = TestemunhaForm(instance=testemunha)


    return render(request, 'editar_testemunha.html', {'form': form,'testemunha':testemunha,'sindicancia':sindicancia})
@login_required(login_url='/')
def excluir_testemunha(request, sindicancia_id, id):
    testemunha = get_object_or_404(Testemunha, id=id)
    if request.method == 'POST':
        testemunha.delete()
        return redirect('inicio:detalhes_sindicancia', sindicancia_id=sindicancia_id)
    return render(request, 'sindicancias_cadastradas.html', {'testemunha': testemunha})

@login_required(login_url='/')
def cadastrar_ofendido(request, sindicancia_id):
    sindicancia = get_object_or_404(Sindicancia, pk=sindicancia_id)

    if request.method == 'POST':
        form = OfendidoForm(request.POST)
        if form.is_valid():
            ofendido = form.save(commit=False)
            ofendido.portaria = sindicancia
            ofendido.save()
            return redirect('inicio:detalhes_sindicancia', sindicancia_id=sindicancia.id)
    else:
        form = OfendidoForm()

    return render(request, 'cadastrar_ofendido.html', {'form': form, 'sindicancia': sindicancia})

@login_required(login_url='/')
def editar_ofendido(request,sindicancia_id, id):
    ofendido = get_object_or_404(Ofendido, id=id)
    sindicancia = get_object_or_404(Sindicancia, pk=sindicancia_id)
    if request.method == 'POST':
        form = OfendidoForm(request.POST, instance=ofendido)
        if form.is_valid():
            form.save()
            return redirect('inicio:detalhes_sindicancia',sindicancia_id=sindicancia.id)
    else:
        form = OfendidoForm(instance=ofendido)


    return render(request, 'editar_ofendido.html', {'form': form,'ofendido':ofendido,'sindicancia':sindicancia})
@login_required(login_url='/')
def excluir_ofendido(request, sindicancia_id, id):
    ofendido = get_object_or_404(Ofendido, id=id)
    if request.method == 'POST':
        ofendido.delete()
        return redirect('inicio:detalhes_sindicancia', sindicancia_id=sindicancia_id)
    return render(request, 'sindicancias_cadastradas.html', {'ofendido': ofendido})
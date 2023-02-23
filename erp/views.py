from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect

from erp.forms import FuncionarioForm
from erp.models import Funcionario

def home(requisicao: HttpRequest):
    if requisicao.method == 'GET':
        return render(requisicao, template_name='erp/index.html')


def cria_funcionario(requisicao: HttpRequest):
    if requisicao.method == 'GET':
        form = FuncionarioForm()

        return render(requisicao, template_name='erp/funcionarios/novo.html', context={'form': form})

    elif requisicao.method == 'POST':
        form = FuncionarioForm(requisicao.POST)
        
        if form.is_valid():
            funcionario = Funcionario(**form.cleaned_data)
            '''
            O **form.cleaned_data faz exatamente o mesmo que isso ->

            nome = form.cleaned_data.get('nome'),
            sobrenome = form.cleaned_data.get('sobrenome'),
            cpf = form.cleaned_data.get('cpf'),
            email = form.cleaned_data.get('email'),
            remuneracao = form.cleaned_data.get('remuneracao'),'''

            funcionario.save()

            return HttpResponseRedirect(redirect_to='/')
        

def lista_funcionarios(requisicao: HttpRequest):
    if requisicao.method == 'GET':
        funcionarios = Funcionario.objects.all()

        return render(requisicao, template_name='erp/funcionarios/lista.html', context={'funcionarios': funcionarios})


def busca_funcionario_por_id(requisicao: HttpRequest, pk: int):
    if requisicao.method == 'GET':
        try:
            funcionario = Funcionario.objects.get(pk=pk)
        except Funcionario.DoesNotExist:
            funcionario = None
        return render(requisicao, template_name='erp/funcionarios/detalhe.html', context={'funcionario': funcionario})


def atualiza_funcionario(requisicao: HttpRequest, pk: int):
    if requisicao.method == 'GET':
        funcionario = Funcionario.objects.get(pk=pk)
        form = FuncionarioForm(instance=funcionario)

        return render(requisicao, template_name='erp/funcionarios/atualiza.html', context={'form': form})
    
    elif requisicao.method == 'POST':
        funcionario = Funcionario.objects.get(pk=pk)
        form = FuncionarioForm(requisicao.POST, instance=funcionario)

        if form.is_valid():

            form.save()

            return HttpResponseRedirect(redirect_to=f'/funcionarios/detalhe/{pk}')
from django.shortcuts import render, redirect
from django.contrib import messages
from estoque.forms import CategoriasForm, MateriaisForm, TiposForm
from estoque.models import Materiais, Categorias, Tipos

from django.shortcuts import render
from .models import Materiais

def cadastrar_materiais(request):
    # Se for uma requisição POST, processa o formulário
    if request.method == 'POST':
        materiais_form = MateriaisForm(request.POST)
        if materiais_form.is_valid():
            materiais_form.save()  # Salva o novo material no banco de dados
            messages.success(request, 'Material cadastrado com sucesso!')  # Mensagem de sucesso

            return redirect('cadastrar_materiais')  # Redireciona para a mesma página após salvar
    else:
        materiais_form = MateriaisForm()

    materiais_fields = Materiais._meta.get_fields()  # Obtém todos os campos do modelo Materiais
    material_rows = [
        [getattr(material, field.name) for field in materiais_fields]
        for material in Materiais.objects.all()
    ]  # Pega todos os materiais cadastrados

    context = {
        'form': materiais_form,  # O formulário para cadastro dados dos materiais
        'messages': messages.get_messages(request),
        'fields': materiais_fields,  # Inclui os campos no contexto
        'rows': material_rows,
    }

    return render(request, 'cadastro/cadastrar_materiais.html', context)

def cadastrar_tipos_materiais(request):
# Se for uma requisição POST, processa o formulário
    if request.method == 'POST':
        tipos_form = TiposForm(request.POST)
        if tipos_form.is_valid():
            tipos_form.save()  # Salva o novo material no banco de dados
            messages.success(request, 'Material cadastrado com sucesso!')  # Mensagem de sucesso

            return redirect('cadastrar_tipos_materiais')  # Redireciona para a mesma página após salvar
    else:
        tipos_form = TiposForm()

    tipos_fields = Tipos._meta.get_fields()  # Obtém todos os campos do modelo Materiais
    tipos_rows = [
        [getattr(tipos, field.name) for field in tipos_fields]
        for tipos in Tipos.objects.all()
    ]  # Pega todos os materiais cadastrados

    context = {
        'form': tipos_form,  # O formulário para cadastro dados dos materiais
        'messages': messages.get_messages(request),
        'fields': tipos_fields,  # Inclui os campos no contexto
        'rows': tipos_rows,
    }

    return render(request, 'cadastro/cadastrar_tipos.html', context)


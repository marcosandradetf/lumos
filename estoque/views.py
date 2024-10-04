from lib2to3.fixes.fix_input import context

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from estoque.forms import CategoriasForm, MateriaisForm
from estoque.models import Materiais, Categorias


from django.shortcuts import render
from .models import Materiais

def cadastrar_materiais(request):
    # Se for uma requisição POST, processa o formulário
    if request.method == 'POST':
        form = MateriaisForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o novo material no banco de dados
            messages.success(request, 'Material cadastrado com sucesso!')  # Mensagem de sucesso

            return redirect('cadastrar_materiais')  # Redireciona para a mesma página após salvar
    else:
        form = MateriaisForm()

    fields = Materiais._meta.get_fields()  # Obtém todos os campos do modelo Materiais
    rows = [
        [getattr(material, field.name) for field in fields]
        for material in Materiais.objects.all()
    ]  # Pega todos os materiais cadastrados

    context = {
        'form': form,  # O formulário para cadastro dados dos materiais
        'messages': messages.get_messages(request),
        'fields': fields,  # Inclui os campos no contexto
        'rows': rows,
    }

    return render(request, 'cadastro/cadastrar_materiais.html', context)

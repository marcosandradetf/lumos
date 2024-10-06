from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.template.loader import render_to_string

from estoque.forms import CategoriasForm, MateriaisForm, TiposForm
from estoque.models import Materiais, Categorias, Tipos

from django.shortcuts import render
from .models import Materiais

def view_material(request):
    # # Se for uma requisição POST, processa o formulário
    # if request.method == 'POST':
    #     materiais_form = MateriaisForm(request.POST)
    #     if materiais_form.is_valid():
    #         materiais_form.save()  # Salva o novo material no banco de dados
    #         messages.success(request, 'Material cadastrado com sucesso!')  # Mensagem de sucesso
    #
    #         return redirect('cadastrar_materiais')  # Redireciona para a mesma página após salvar
    # else:
    #     materiais_form = MateriaisForm()
    #
    # materiais_obj = Materiais.objects.all()
    #
    # context = {
    #     'form': materiais_form,  # O formulário para cadastro dados dos materiais
    #     'messages': messages.get_messages(request),
    #     'materiais_obj': materiais_obj,  # Inclui os campos no contexto
    # }
    materiais_obj = Materiais.objects.all()
    materiais_form = MateriaisForm()
    context = {'form': materiais_form,
               'materiais_obj': materiais_obj,}

    return render(request, 'materiais/gerenciar/materiais.html', context)

def insert_material(request):
    materiais_form = MateriaisForm(request.POST)
    materiais_obj = Materiais.objects.all()
    context = {'materiais_form': materiais_form,
               'materiais_obj': materiais_obj,
               'messages': messages.get_messages(request),}
    if materiais_form.is_valid():
        materiais_form.save()  # Salva o novo material no banco de dados
        messages.success(request, 'Material cadastrado com sucesso!')  # Mensagem de sucesso
        response = render_to_string('materiais/tabelas/tabela_materiais.html', context)
        return HttpResponse(response)

    messages.error(request, "Erro ao cadastrar materiais")
    response = render_to_string('materiais/tabelas/tabela_materiais.html', context)
    return HttpResponse(response)


def update_material(request, id):
    # Recupera o material com base no ID ou retorna um 404 se não encontrado
    material = Materiais.objects.get(pk=id)

    # Se a requisição for POST, estamos tentando atualizar os dados
    if request.method == "POST":
        # Preenche o formulário com os dados da requisição e a instância do material
        materiais_form_update = MateriaisForm(request.POST, instance=material)

        # Verifica se o formulário é válido
        if materiais_form_update.is_valid():
            # Salva as alterações no banco de dados
            materiais_form_update.save()
            # Redireciona para alguma página (por exemplo, lista de materiais)
            return redirect('materiais_view')  # Substitua pelo nome correto da URL de destino
    else:
        # Se for uma requisição GET, exibe o formulário com os dados atuais do material
        materiais_form_update = MateriaisForm(instance=material)

    # Renderiza o template com o formulário
    return render(request, 'materiais/gerenciar/update_material.html', {'form': materiais_form_update})


def delete_material(request, id):
    material = get_object_or_404(Materiais, id_material=id)

    if not material.inativo:
        messages.error(request, f"O material {id} - {material.nome_material} não pode ser excluído pois está ativo.")
        message_html = render_to_string('materiais/messages/messages_server.html', {'messages': messages.get_messages(request)})
        return HttpResponse(message_html)

    # Se chegar aqui, o material pode ser excluído
    material.delete()
    messages.success(request, f"Material {id} - {material.nome_material} foi excluído com sucesso.")
    message_html = render_to_string('materiais/messages/messages_server.html', {'messages': messages.get_messages(request)})
    return HttpResponse(message_html)


def view_tipos(request):
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

    return render(request, 'tipos/gerenciar/tipos.html', context)

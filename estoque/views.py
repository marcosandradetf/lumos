from django.contrib.messages import success
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.template.loader import render_to_string

from estoque.forms import CategoriasForm, MateriaisForm, TiposForm
from estoque.models import Materiais, Categorias, Tipos

from django.shortcuts import render

from estoque.models import Log
from .models import Materiais


def view_material(request):
    materiais_obj = Materiais.objects.all()
    materiais_form = MateriaisForm()
    context = {'form': materiais_form,
               'materiais_obj': materiais_obj, }

    return render(request, 'materiais/gerenciar/materiais.html', context)


def materiais_messages(request):
    messages_obj = Log.objects.filter(category='material').order_by('-created_at')[:30]
    return render(request, 'materiais/messages/messages_server.html', {'messages_obj': messages_obj})


def insert_material(request):
    materiais_form = MateriaisForm(request.POST)
    nome_material = materiais_form.cleaned_data.get('nome_material',
                                                    'desconhecido') if materiais_form.is_valid() else 'desconhecido'
    materiais_obj = Materiais.objects.all()
    # Inicializa o dicionário de mensagens vazio
    response_message = {}

    if materiais_form.is_valid():
        # Salva o novo material no banco de dados
        materiais_form.save()
        # Cria um log de sucesso e define a mensagem de sucesso
        Log.objects.create(type="success", message=f'Material {nome_material} cadastrado com sucesso!',
                           category='material')
        response_message['success'] = f'Material {nome_material} cadastrado com sucesso!'
    else:
        # Cria um log de erro e define a mensagem de erro
        Log.objects.create(type="error", message=f'Erro ao cadastrar material {nome_material}.', category='material')
        response_message['error'] = f'Erro ao cadastrar material {nome_material}.'
    # Atualiza o contexto com o dicionário de mensagens
    context = {
        'form': MateriaisForm(),
        'materiais_obj': materiais_obj,
        'message': response_message,
    }
    # Renderiza o template com o contexto atualizado
    response = render_to_string('materiais/gerenciar/client.html', context)
    return HttpResponse(response)


def update_material(request, id):
    # Recupera o material com base no ID ou retorna um 404 se não encontrado
    material = Materiais.objects.get(pk=id)

    # Se a requisição for POST, estamos tentando atualizar os dados

    if request.method == "GET":
        # Se for uma requisição GET, exibe o formulário com os dados atuais do material
        materiais_form_update = MateriaisForm(instance=material)
        return render(request, 'materiais/forms/form_update_material.html', {'formUpdate': materiais_form_update})

    else:
        # Preenche o formulário com os dados da requisição e a instância do material
        materiais_form_update = MateriaisForm(request.POST, instance=material)

        # Verifica se o formulário é válido
        if materiais_form_update.is_valid():
            # Salva as alterações no banco de dados
            materiais_form_update.save()
            # Redireciona para alguma página (por exemplo, lista de materiais)
            return redirect('materiais_view')  # Substitua pelo nome correto da URL de destino

    # Renderiza o template com o formulário



def delete_material(request, id):
    material = get_object_or_404(Materiais, id_material=id)
    response_message = {}

    if not material.inativo:
        # Cria um log de erro e define a mensagem de erro
        Log.objects.create(type="error",
                           message=f"O material {id} - {material.nome_material} não pode ser excluído pois está ativo.",
                           category='material')
        response_message['error'] = f"O material {id} - {material.nome_material} não pode ser excluído pois está ativo."
    else:
        material.delete()
        Log.objects.create(type="success",
                           message=f"Material {id} - {material.nome_material} foi excluído com sucesso.",
                           category='material')
        response_message['success'] = f"Material {id} - {material.nome_material} foi excluído com sucesso."

    context = {
        'form': MateriaisForm(),
        'materiais_obj': Materiais.objects.all(),
        'message': response_message,
    }
    # Renderiza o template com o contexto atualizado
    response = render_to_string('materiais/gerenciar/client.html', context)
    return HttpResponse(response)


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

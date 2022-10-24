from django.shortcuts import render, get_object_or_404, redirect
from .models import Contato
from django.core.paginator import Paginator
from django.http import Http404
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages
# Create your views here.


def index(request):

    contatos = Contato.objects.order_by('-id').filter(
        mostrar=True
    )
    paginador = Paginator(contatos, 20)

    page = request.GET.get('p')
    contatos = paginador.get_page(page)

    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })


def show_contato_id(request, contato_id):
    #contato = Contato.objects.get(id=contato_id)
    contato = get_object_or_404(Contato, id=contato_id)

    if not contato.mostrar:
        raise Http404()

    return render(request, 'contatos/show_contato_id.html', {
        'contato': contato
    })


def busca(request):
    termo = request.GET.get('termo')

    if termo is None or not termo:
        messages.add_message(request, messages.ERROR,
                             'Campo Busco não pode ficar vazio.')
        return redirect('index')

    compos = Concat('nome', Value(' '), 'sobrenome')

    contatos = Contato.objects.annotate(nome_completo=compos).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo),
        mostrar=True
    )
    paginador = Paginator(contatos, 20)

    page = request.GET.get('p')
    contatos = paginador.get_page(page)

    return render(request, 'contatos/busca.html', {
        'contatos': contatos
    })

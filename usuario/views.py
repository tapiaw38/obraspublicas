from django.shortcuts import render
from django.core.paginator import Paginator
from usuario.forms import UsuarioForm
from usuario.models import Usuario
# Create your views here.

from django.views.generic import CreateView, ListView, UpdateView, TemplateView
from django.urls import reverse_lazy

class index(TemplateView):
    template_name = 'usuario/index.html'

class usuario_create(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuario/usuario_form.html'
    success_url = reverse_lazy('usuario_listar')

class usuario_list(ListView):
    model = Usuario
    template_name = 'usuario/usuario_list.html'
    paginate_by = 7

class usuario_edit(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuario/usuario_form.html'
    success_url = reverse_lazy('usuario_listar')


def usuario_search(request):
    buscar = request.POST.get('buscalo')
    if buscar:
        usuario=Usuario.objects.filter(dni__contains=buscar)
        paginator = Paginator(usuario, 7)
        page = request.GET.get('page')
        usuario = paginator.get_page(page)
    else:
        usuario = Usuario.objects.all()
        paginator = Paginator(usuario, 7)
        page = request.GET.get('page')
        usuario = paginator.get_page(page)
    contexto = {'usuarios': usuario}
    return render(request, 'usuario/buscar.html',contexto)

from django.shortcuts import render
from plano.forms import PlanoForm
from plano.models import Plano
#from usuario.forms import UsuarioForm
from django.core.paginator import Paginator
from django.views.generic import CreateView, ListView, UpdateView, TemplateView
from django.urls import reverse_lazy
# Create your views here.

class plano_create(CreateView):
    model = Plano
    form_class = PlanoForm
    template_name = 'plano/plano_form.html'
    success_url = reverse_lazy('plano_listar')

class plano_list(ListView):
    model = Plano
    template_name = 'plano/plano_list.html'
    paginate_by = 7

class plano_edit(UpdateView):
    model = Plano
    form_class = PlanoForm
    template_name = 'plano/plano_form.html'
    success_url = reverse_lazy('plano_listar')


def plano_search(request):
    buscar = request.POST.get('buscalo')
    if buscar:
        plano=Plano.objects.filter(usuario__dni__contains=buscar)
        paginator = Paginator(plano, 7)
        page = request.GET.get('page')
        plano = paginator.get_page(page)
    else:
        plano = Plano.objects.all()
        paginator = Paginator(plano, 7)
        page = request.GET.get('page')
        plano = paginator.get_page(page)
    contexto = {'planos': plano}
    return render(request, 'plano/buscar.html',contexto)
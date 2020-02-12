from django.shortcuts import render
from django.core.paginator import Paginator
from proyectista.forms import ProyectistaForm
from proyectista.models import Proyectista
# Create your views here.

from django.views.generic import CreateView, ListView, UpdateView, TemplateView
from django.urls import reverse_lazy

class proyectista_create(CreateView):
    model = Proyectista
    form_class = ProyectistaForm
    template_name = 'proyectista/proyectista_form.html'
    success_url = reverse_lazy('proyectista_listar')

class proyectista_list(ListView):
    model = Proyectista
    template_name = 'proyectista/proyectista_list.html'
    paginate_by = 7

class proyectista_edit(UpdateView):
    model = Proyectista
    form_class = ProyectistaForm
    template_name = 'proyectista/proyectista_form.html'
    success_url = reverse_lazy('proyectista_listar')

def proyectista_search(request):
    buscar = request.POST.get('buscalo')
    if buscar:
        proyectista = Proyectista.objects.filter(dni__contains=buscar)
        paginator = Paginator(proyectista, 7)
        page = request.GET.get('page')
        proyectista = paginator.get_page(page)
    else:
        proyectista = Proyectista.objects.all()
        paginator = Paginator(proyectista, 7)
        page = request.GET.get('page')
        proyectista = paginator.get_page(page)
    contexto = {'proyectistas': proyectista}
    return render(request, 'proyectista/buscar.html',contexto)

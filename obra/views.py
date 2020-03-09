from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from obra.forms import ObraForm, PresentaForm
from obra.models import Obra
import datetime
from datetime import timezone
from django.views.generic import View
# Create your views here.
from obraspublicas.utileria import render_pdf


class obra_create(CreateView):
    model = Obra
    form_class = ObraForm
    template_name = 'obra/obra_form.html'
    success_url = reverse_lazy('obra_listar')

class obra_edit(UpdateView):
    model = Obra
    form_class = ObraForm
    template_name = 'obra/obra_form.html'
    success_url = reverse_lazy('obra_listar')

class presenta_update(UpdateView):
    model = Obra
    form_class = PresentaForm
    template_name = 'obra/presenta_form.html'
    success_url = reverse_lazy('obra_listar')

def obra_list(request):
    obra = Obra.objects.all()
    for i in obra:
        i.fecha_limite = i.fecha + datetime.timedelta(days=i.dias)
    contexto = {'object_list':obra, 'f_actual':datetime.datetime.now(timezone.utc)}
    paginator = Paginator(obra, 7)
    page = request.GET.get('page')
    obra = paginator.get_page(page)
    return render(request,'obra/obra_list.html',contexto)

def obra_search(request):
    buscar = request.POST.get('buscalo')
    if buscar:
        obra=Obra.objects.filter(usuario__dni__contains=buscar)
    else:
        obra = Obra.objects.all()
    for i in obra:
        i.fecha_limite = i.fecha + datetime.timedelta(days=i.dias)
    paginator = Paginator(obra, 7)
    page = request.GET.get('page')
    obra = paginator.get_page(page)
    contexto = {'object_list': obra,'f_actual':datetime.datetime.now(timezone.utc)}
    return render(request, 'obra/buscar.html',contexto)

class notifica_obra_pdf(View):
    #regresa PDF basada en templae html
    def get(self,request,id_obra):
        obra=Obra.objects.get(id=id_obra)
        f = datetime.datetime.now()
        f_hoy = f.strftime("%d de %B de %Y")
        pdf=render_pdf("obra/obra_pdf.html",{'obras':obra,'fecha_hoy':f_hoy})
        return HttpResponse(pdf, content_type='application/pdf')
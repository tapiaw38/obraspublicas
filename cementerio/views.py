from django.core.paginator import Paginator
from django.shortcuts import render
import datetime
from datetime import timezone
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from cementerio.forms import cementerioForm, anualForm_1, anualForm_2, anualForm_3, anualForm_4, permisoForm, \
    fintrabajoForm
from cementerio.models import Cementerio
# Create your views here.

class cementerio_create(CreateView):
    model = Cementerio
    form_class = cementerioForm
    template_name = 'cementerio/cementerio_form.html'
    success_url = reverse_lazy('notifica_listar')

class cementerio_edit(UpdateView):
    model = Cementerio
    form_class = cementerioForm
    template_name = 'cementerio/cementerio_form.html'
    success_url = reverse_lazy('cementerio_listar')

def cementerio_list(request):
    cementerio = Cementerio.objects.all()
    for i in cementerio:
        i.caduca = i.fecha_compra + datetime.timedelta(days=i.vigencia*365)
        # calcular la finalizacion prorroga para comenzar
        i.caduca_concesion = i.caduca + datetime.timedelta(days=i.dias_concesion)
        i.fin_prorroga_iniciar = i.fecha_compra + datetime.timedelta(days=i.prorroga_iniciar)
        # calcular la finalizacion de prorroga para terminar
        if i.fecha_inicio != None:
            i.fecha_final = i.fecha_inicio + datetime.timedelta(days=i.prorroga_trabajo)
        i.fecha_anual1 = i.fecha_compra + datetime.timedelta(days=365)
        i.fecha_anual2 = i.fecha_compra + datetime.timedelta(days=365*2)
        i.fecha_anual3 = i.fecha_compra + datetime.timedelta(days=365*3)
        i.fecha_anual4 = i.fecha_compra + datetime.timedelta(days=365*4)
        if i.fecha_inicio != None:
            i.trabajo_inicio=True
        if i.trabajo_final == True:
            i.trabajo_final_fecha = datetime.datetime.now(timezone.utc)
    paginator = Paginator(cementerio, 7)
    page = request.GET.get('page')
    cementerio = paginator.get_page(page)
    contexto = {'object_list':cementerio, 'f_actual':datetime.datetime.now(timezone.utc)}
    return render(request,'cementerio/cementerio_list.html',contexto)

def cementerio_search(request):
    buscar = request.POST.get('buscalo')
    if buscar:
        cementerio =Cementerio.objects.filter(usuario__dni__contains=buscar)
    else:
        cementerio = Cementerio.objects.all()
    for i in cementerio:
        i.caduca = i.fecha_compra + datetime.timedelta(days=i.vigencia*365)
        # calcular la finalizacion prorroga para comenzar
        i.caduca_concesion = i.caduca + datetime.timedelta(days=i.dias_concesion)
        i.fin_prorroga_iniciar = i.fecha_compra + datetime.timedelta(days=i.prorroga_iniciar)
        # calcular la finalizacion de prorroga para terminar
        if i.fecha_inicio != None:
            i.fecha_final = i.fecha_inicio + datetime.timedelta(days=i.prorroga_trabajo)
        i.fecha_anual1 = i.fecha_compra + datetime.timedelta(days=365)
        i.fecha_anual2 = i.fecha_compra + datetime.timedelta(days=365*2)
        i.fecha_anual3 = i.fecha_compra + datetime.timedelta(days=365*3)
        i.fecha_anual4 = i.fecha_compra + datetime.timedelta(days=365*4)
        if i.fecha_inicio != None:
            i.trabajo_inicio=True
        if i.trabajo_final == True:
            i.trabajo_final_fecha = datetime.datetime.now(timezone.utc)
    paginator = Paginator(cementerio, 7)
    page = request.GET.get('page')
    cementerio = paginator.get_page(page)
    contexto = {'object_list': cementerio,'f_actual':datetime.datetime.now(timezone.utc)}
    return render(request, 'cementerio/buscar.html',contexto)

class pago1_edit(UpdateView):
    model = Cementerio
    form_class = anualForm_1
    template_name = 'cementerio/pago1_form.html'
    success_url = reverse_lazy('cementerio_listar')

class pago2_edit(UpdateView):
    model = Cementerio
    form_class = anualForm_2
    template_name = 'cementerio/pago1_form.html'
    success_url = reverse_lazy('cementerio_listar')

class pago3_edit(UpdateView):
    model = Cementerio
    form_class = anualForm_3
    template_name = 'cementerio/pago1_form.html'
    success_url = reverse_lazy('cementerio_listar')

class pago4_edit(UpdateView):
    model = Cementerio
    form_class = anualForm_4
    template_name = 'cementerio/pago1_form.html'
    success_url = reverse_lazy('cementerio_listar')

class permiso_edit(UpdateView):
    model = Cementerio
    form_class = permisoForm
    template_name = 'cementerio/permiso_form.html'
    success_url = reverse_lazy('cementerio_listar')

class final_trabajo_edit(UpdateView):
    model = Cementerio
    form_class = fintrabajoForm
    template_name = 'cementerio/final_trabajo_form.html'
    success_url = reverse_lazy('cementerio_listar')


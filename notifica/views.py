from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from notifica.forms import NotificaForm, PresentaForm
from notifica.models import Notifica
import datetime
from datetime import timezone
from django.views.generic import View
# Create your views here.

from django.views.generic import CreateView, ListView, UpdateView, TemplateView
from django.urls import reverse_lazy


class notifica_create(CreateView):
    model = Notifica
    form_class = NotificaForm
    template_name = 'notifica/notifica_form.html'
    success_url = reverse_lazy('notifica_listar')

class presenta_update(UpdateView):
    model = Notifica
    form_class = PresentaForm
    template_name = 'notifica/presenta_form.html'
    success_url = reverse_lazy('notifica_listar')

'''
class notifica_list(ListView):
    model = Notifica
    template_name = 'notifica/notifica_list.html'
    paginate_by = 7
'''

def notifica_list(request):
    notifica = Notifica.objects.all()
    for i in notifica:
        i.fecha_limite = i.fecha + datetime.timedelta(days=30)
    contexto = {'object_list':notifica, 'f_actual':datetime.datetime.now(timezone.utc)}
    return render(request,'notifica/notifica_list.html',contexto)

class notifica_edit(UpdateView):
    model = Notifica
    form_class = NotificaForm
    template_name = 'notifica/notifica_form.html'
    success_url = reverse_lazy('notifica_listar')


def notifica_search(request):
    buscar = request.POST.get('buscalo')
    if buscar:
        notifica=Notifica.objects.filter(usuario__dni__contains=buscar)
        paginator = Paginator(notifica, 7)
        page = request.GET.get('page')
        notifica = paginator.get_page(page)
    else:
        notifica = Notifica.objects.all()
        paginator = Paginator(notifica, 7)
        page = request.GET.get('page')
        notifica = paginator.get_page(page)
    for i in notifica:
        i.fecha_limite = i.fecha + datetime.timedelta(days=30)
    contexto = {'object_list': notifica,'f_actual':datetime.datetime.now(timezone.utc)}
    return render(request, 'notifica/buscar.html',contexto)

class datos(View):
    def get(self, request,id_notifica):
        notifica = Notifica.objects.get(id=id_notifica)
        contexto = {'notificas':notifica}
        datos = render(request,'notifica/notifica_datos.html',contexto)
        return HttpResponse(datos)

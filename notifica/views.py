from django.shortcuts import render
from django.core.paginator import Paginator
from notifica.forms import NotificaForm
from notifica.models import Notifica
import datetime
from datetime import timezone
# Create your views here.

from django.views.generic import CreateView, ListView, UpdateView, TemplateView
from django.urls import reverse_lazy


class notifica_create(CreateView):
    model = Notifica
    form_class = NotificaForm
    template_name = 'notifica/notifica_form.html'
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
        notifica=Notifica.objects.filter(dni__contains=buscar)
        paginator = Paginator(notifica, 7)
        page = request.GET.get('page')
        notifica = paginator.get_page(page)
    else:
        notifica = Notifica.objects.all()
        paginator = Paginator(notifica, 7)
        page = request.GET.get('page')
        notifica = paginator.get_page(page)
    contexto = {'notificas': notifica}
    return render(request, 'notifica/buscar.html',contexto)

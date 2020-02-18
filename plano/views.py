from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from obraspublicas.utileria import render_pdf
from plano.forms import *
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

class pago_create(UpdateView):
    model = Plano
    form_class = DeudaForm
    template_name = 'plano/pago_form.html'
    success_url = reverse_lazy('plano_listar')

class pago_create2(UpdateView):
    model = Plano
    form_class = DeudaForm2
    template_name = 'plano/pago_form2.html'
    success_url = reverse_lazy('plano_listar')

class pago_create3(UpdateView):
    model = Plano
    form_class = DeudaForm3
    template_name = 'plano/pago_form3.html'
    success_url = reverse_lazy('plano_listar')

class pago_create4(UpdateView):
    model = Plano
    form_class = DeudaForm3
    template_name = 'plano/pago_form4.html'
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

class pago(View):
    #regresa PDF basada en templae html
    def get(self,request,id_plano):
        plano=Plano.objects.get(id=id_plano)
        pdf=render_pdf("plano/pago_pdf.html",{'planos':plano})
        return HttpResponse(pdf, content_type='application/pdf')

class pago2(View):
    #regresa PDF basada en templae html
    def get(self,request,id_plano):
        plano=Plano.objects.get(id=id_plano)
        pdf=render_pdf("plano/pago2_pdf.html",{'planos':plano})
        return HttpResponse(pdf, content_type='application/pdf')

class pago3(View):
    #regresa PDF basada en templae html
    def get(self,request,id_plano):
        plano=Plano.objects.get(id=id_plano)
        pdf=render_pdf("plano/pago3_pdf.html",{'planos':plano})
        return HttpResponse(pdf, content_type='application/pdf')

class pago4(View):
    #regresa PDF basada en templae html
    def get(self,request,id_plano):
        plano=Plano.objects.get(id=id_plano)
        pdf=render_pdf("plano/pago4_pdf.html",{'planos':plano})
        return HttpResponse(pdf, content_type='application/pdf')

class datos(View):
    def get(self, request,id_plano):
        plano = Plano.objects.get(id=id_plano)
        contexto = {'planos':plano}
        datos = render(request,'plano/datos_planos.html',contexto)
        return HttpResponse(datos)

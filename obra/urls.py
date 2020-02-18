from django.urls import path
from obra import views
from obra.views import *


urlpatterns = [
    path('nuevo/', views.obra_create.as_view(), name='obra_nuevo'),
    path('listar/', views.obra_list, name='obra_listar'),
    path('editar/<pk>/',views.obra_edit.as_view(), name='obra_editar'),
    path('obra_editar/<pk>/', views.presenta_update.as_view(), name='presenta_editar'),
    path('buscar/', views.obra_search, name='obra_buscar'),
    path('notificar/<str:id_obra>/',notifica_obra_pdf.as_view(), name='notifica_obra_pdf'),
]
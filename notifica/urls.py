from django.urls import path
from notifica import views
from notifica.views import *


urlpatterns = [
    path('nuevo/', views.notifica_create.as_view(), name='notifica_nuevo'),
    path('listar/', views.notifica_list, name='notifica_listar'),
    path('editar/<pk>/',views.notifica_edit.as_view(), name='notifica_editar'),
    path('presenta_editar/<pk>/', views.presenta_update.as_view(), name='presenta_editar'),
    path('buscar/', views.notifica_search, name='notifica_buscar'),
    path('dato_notifica/<str:id_notifica>/', datos.as_view(), name='dato_notifica'),
]
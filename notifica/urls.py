from django.urls import path
from notifica import views


urlpatterns = [
    path('nuevo/', views.notifica_create.as_view(), name='notifica_nuevo'),
    path('listar/', views.notifica_list, name='notifica_listar'),
    path('editar/<pk>/',views.notifica_edit.as_view(), name='notifica_editar'),
    path('buscar/', views.notifica_search, name='notifica_buscar'),
]
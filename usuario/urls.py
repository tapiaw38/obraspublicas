from django.urls import path
from usuario import views


urlpatterns = [
    path('nuevo/', views.usuario_create.as_view(), name='usuario_nuevo'),
    path('listar/', views.usuario_list.as_view(), name='usuario_listar'),
    path('editar/<pk>/',views.usuario_edit.as_view(), name='usuario_editar'),
    path('buscar/', views.usuario_search, name='usuario_buscar'),
]
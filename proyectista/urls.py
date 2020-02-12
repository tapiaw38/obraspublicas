from django.urls import path
from proyectista import views


urlpatterns = [
    path('nuevo/', views.proyectista_create.as_view(), name='proyectista_nuevo'),
    path('listar/', views.proyectista_list.as_view(), name='proyectista_listar'),
    path('editar/<pk>/',views.proyectista_edit.as_view(), name='proyectista_editar'),
    path('buscar/', views.proyectista_search, name='proyectista_buscar'),
]
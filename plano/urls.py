from django.urls import path
from plano import views


urlpatterns = [
    path('nuevo/', views.plano_create.as_view(), name='plano_nuevo'),
    path('listar/', views.plano_list.as_view(), name='plano_listar'),
    path('editar/<pk>/',views.plano_edit.as_view(), name='plano_editar'),
    path('buscar/', views.plano_search, name='plano_buscar'),
]
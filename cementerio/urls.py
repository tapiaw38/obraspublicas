from django.urls import path
from cementerio import views
from cementerio.views import *


urlpatterns = [
    path('nuevo/', views.cementerio_create.as_view(), name='cementerio_nuevo'),
    path('listar/', views.cementerio_list, name='cementerio_listar'),
    path('editar/<pk>/',views.cementerio_edit.as_view(), name='cementerio_editar'),
    path('buscar/', views.cementerio_search, name='cementerio_buscar'),
    path('pago_1/<pk>/', views.pago1_edit.as_view(), name='pago_1'),
    path('pago_2/<pk>/', views.pago1_edit.as_view(), name='pago_2'),
    path('pago_3/<pk>/', views.pago1_edit.as_view(), name='pago_3'),
    path('pago_4/<pk>/', views.pago1_edit.as_view(), name='pago_4'),
    path('permiso/<pk>/', views.permiso_edit.as_view(), name='permiso_edit'),
    path('finalizar_trabajo/<pk>/', views.final_trabajo_edit.as_view(), name='permiso_edit'),
    path('contrato/<str:id_cementerio>/', contrato.as_view(), name='contrato'),
    path('compra/<str:id_cementerio>/', compra.as_view(), name='compra'),
]
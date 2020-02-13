from django.urls import path
from plano import views
from plano.views import *

urlpatterns = [
    path('nuevo/', views.plano_create.as_view(), name='plano_nuevo'),
    path('pago_nuevo/<pk>/', views.pago_create.as_view(), name='pago_nuevo'),
    path('pago_cuota_2/<pk>/', views.pago_create2.as_view(), name='pago_cuota_2'),
    path('pago_cuota_3/<pk>/', views.pago_create3.as_view(), name='pago_cuota_3'),
    path('pago_cuota_4/<pk>/', views.pago_create4.as_view(), name='pago_cuota_4'),
    path('listar/', views.plano_list.as_view(), name='plano_listar'),
    path('editar/<pk>/',views.plano_edit.as_view(), name='plano_editar'),
    path('buscar/', views.plano_search, name='plano_buscar'),
    path('pago/<str:id_plano>/', pago.as_view(), name='pago_pdf'),
    path('pago2/<str:id_plano>/', pago2.as_view(), name='pago2_pdf'),
    path('pago3/<str:id_plano>/', pago3.as_view(), name='pago3_pdf'),
    path('dato_plano/<str:id_plano>/', datos.as_view(), name='dato_plano'),
]
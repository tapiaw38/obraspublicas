from django.urls import path
from plano import views
from plano.views import pago

urlpatterns = [
    path('nuevo/', views.plano_create.as_view(), name='plano_nuevo'),
    path('pago_nuevo/<pk>/', views.pago_create.as_view(), name='pago_nuevo'),
    path('pago_cuota_2/<pk>/', views.pago_create2.as_view(), name='pago_cuota_2'),
    path('pago_cuota_3/<pk>/', views.pago_create3.as_view(), name='pago_cuota_3'),
    path('listar/', views.plano_list.as_view(), name='plano_listar'),
    path('editar/<pk>/',views.plano_edit.as_view(), name='plano_editar'),
    path('buscar/', views.plano_search, name='plano_buscar'),
    path('pago/<str:id_plano>/', pago.as_view(), name='pago_pdf'),
]
from django.urls import include, path

from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('',views.catalogo, name='catalogo'),
    path('producto/<int:product_id>', views.product_view, name='product_view'),

    path('pagar/', views.pago_usuario_no_registrado, name='pago_usuario_no_registrado'),
    path('pagar_user/', views.pago_usuario_registrado, name='pago_usuario_registrado'),    
    path('agregar_al_carrito/', agregar_al_carrito, name='agregar_al_carrito'),    
    path('agregar_opinion/', views.agregar_opinion, name='agregar_opinion'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, show_indexes=True)
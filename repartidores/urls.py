from django.urls import path

from repartidores.views import lista_repartidores, crear_repartidor


urlpatterns = [
    path('lista_repartidores/', lista_repartidores),
    path('crear_repartidor/', crear_repartidor)]
from django.urls import path

from platos.views import lista_platos, crear_plato


urlpatterns = [
    path('lista_platos/', lista_platos),
    path('crear_plato/', crear_plato)]
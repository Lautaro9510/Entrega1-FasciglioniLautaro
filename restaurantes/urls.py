from django.urls import path

from restaurantes.views import lista_restaurantes, crear_restaurante


urlpatterns = [
    path('lista_restaurantes/', lista_restaurantes),
    path('crear_restaurante/', crear_restaurante)]
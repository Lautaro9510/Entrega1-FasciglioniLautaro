from django.contrib import admin

from restaurantes.models import Restaurantes
# Register your models here.

@admin.register(Restaurantes)
class RestaurantesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'especialidad', 'direccion', 'telefono')
    list_filter = ('abierto',)
    search_fields = ('nombre',)
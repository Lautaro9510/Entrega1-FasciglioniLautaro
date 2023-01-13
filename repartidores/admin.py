from django.contrib import admin

from repartidores.models import Repartidores
# Register your models here.

@admin.register(Repartidores)
class RepartidoresAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'vehiculo', 'direccion', 'telefono',)
    list_filter = ()
    search_fields = ('nombre',)
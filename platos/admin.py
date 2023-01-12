from django.contrib import admin
from platos.models import Platos
# Register your models here.
@admin.register(Platos)
class PlatosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'especialidad', 
    'apto_vegano', 'apto_vegetariano', 'apto_celiaco')
    list_filter = ('stock',)
    search_fields = ('nombre',)
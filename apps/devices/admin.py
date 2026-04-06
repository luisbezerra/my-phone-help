from django.contrib import admin
from .models import Brand, Device

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')  # Mostra o nome e se está ativa na lista
    search_fields = ('name',)             # Cria uma barra de busca por nome
    list_filter = ('is_active',)          # Cria um filtro lateral por status

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('model_name', 'brand', 'slug')
    list_filter = ('brand',)              # Filtra dispositivos por marca
    search_fields = ('model_name', 'slug')
    prepopulated_fields = {'slug': ('model_name',)} # Gera o slug automaticamente enquanto você digita o nome!

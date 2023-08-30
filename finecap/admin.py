from django.contrib import admin
from .models import Stand, Reserva

# Register your models here. 
@admin.register(Stand)
class StandAdmin(admin.ModelAdmin):
    list_display = ("localizacao", "valor")

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ("cnpj", "nome_empresa", "categoria_empresa", "quitado")
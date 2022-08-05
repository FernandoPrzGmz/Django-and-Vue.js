from django.contrib import admin

from src.apps.refugio import models


@admin.register(models.Vacuna)
class VacunaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)


@admin.register(models.Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'edad', 'telefono', 'email')
    search_fields = ('nombre', 'apellidos', 'email')


@admin.register(models.Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'sexo', 'edad', 'fecha_rescate', 'persona')
    search_fields = ('nombre',)
    list_filter = ('sexo',)

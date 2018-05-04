from django.contrib import admin
from .models import Usuario


class UserAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'data_criacao', 'data_atualizacao')
    ordering = ('nome',)


admin.site.register(Usuario, UserAdmin)

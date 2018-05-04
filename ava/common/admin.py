from django.contrib import admin
from .models import Usuario, Curso, Disciplina, Turma


admin.site.register(Usuario)
class UserAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'data_criacao', 'data_atualizacao')
    ordering = ('nome',)


admin.site.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    pass


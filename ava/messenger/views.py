from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from common.models import Turma, Usuario


@login_required
def room(request, turma_id=None):
    if request.user.papel == Usuario.ALUNO:
        qs = Turma.objects.filter(alunos=request.user)
    elif request.user.papel == Usuario.PROFESSOR:
        qs = Turma.objects.filter(professor=request.user)
    else:
        qs = Turma.objects.all()
    context = {
        'turmas': qs,
    }
    if turma_id is None:
        context['turma_atual'] = qs.first()
    else:
        context['turma_atual'] = qs.get(pk=turma_id)
    return render(request, 'messenger/room.html', context)

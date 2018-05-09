from django.shortcuts import render
from common.models import Turma


def room(request, turma_id=None):
    context = {
        'turmas': Turma.objects.all(),
    }
    if turma_id is None:
        context['turma_atual'] = Turma.objects.first()
    else:
        context['turma_atual'] = Turma.objects.get(pk=turma_id)
    return render(request, 'messenger/room.html', context)

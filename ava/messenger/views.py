from django.shortcuts import render
from common.models import Turma


def room(request, turma_id):
    context = {
        'turmas': Turma.objects.all(),
        'turma_atual': Turma.objects.get(pk=turma_id)
    }
    return render(request, 'messenger/room.html', context)

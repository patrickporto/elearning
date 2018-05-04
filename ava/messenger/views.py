from django.shortcuts import render
from common.models import Turma


def room(request):
    context = {
        'turmas': Turma.objects.all(),
    }
    return render(request, 'messenger/room.html', context)

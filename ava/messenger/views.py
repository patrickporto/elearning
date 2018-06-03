from asgiref.sync import async_to_sync
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.views import View
from channels.layers import get_channel_layer
from common.models import Turma, Usuario
from .models import Duvida, Mensagem


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


@method_decorator(login_required, name='dispatch')
class Duvidas(View):
    template_name = 'messenger/duvidas.html'
    def get(self, request, turma_id):
        if request.user.papel == Usuario.ALUNO:
            qs = Turma.objects.filter(alunos=request.user)
        elif request.user.papel == Usuario.PROFESSOR:
            qs = Turma.objects.filter(professor=request.user)
        else:
            qs = Turma.objects.all()
        context = {
            'turma_atual': get_object_or_404(Turma, pk=turma_id),
            'turmas': qs,
            'duvidas': Duvida.objects.filter(turma_id=turma_id)
        }
        return render(request, self.template_name, context)

    def post(self, request, turma_id):
        answers = []
        for key, value in request.POST.items():
            if key.startswith('duvida-'):
                duvida = Duvida.objects.get(pk=int(key[7:]))
                duvida.resposta = value
                duvida.save()
                answers.append(duvida)
        mensagem = Mensagem.objects.create(
            tipo='duvidas',
            turma_id=turma_id,
            autor=request.user,
            conteudo='\n'.join([';'.join([str(answer.mensagem.id), answer.mensagem.mensagem, answer.resposta])
                                for answer in answers]),
        )
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.send)(str(turma_id), {
            'type': mensagem.tipo,
            'id': mensagem.id,
            'message': mensagem.conteudo,
            'sendingDate': mensagem.data_publicacao.isoformat(),
            'likes': mensagem.curtidas.count(),
            'author': {
                'me': request.user.id == mensagem.autor.id,
                'id': mensagem.autor.id,
                'name': mensagem.autor.nome,
                'photo': mensagem.autor.foto.url,
            },
        })
        return redirect('duvidas', turma_id)

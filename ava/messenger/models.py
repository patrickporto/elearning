from django.db import models
from django.conf import settings
from common.models import Usuario


class Mensagem(models.Model):
    tipo = models.CharField(max_length=40, default='chat_message')
    turma = models.ForeignKey('common.Turma', on_delete=models.CASCADE)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mensagem


class Curtida(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    mensagem = models.ForeignKey('Mensagem', on_delete=models.CASCADE, related_name='curtidas')


class Duvida(models.Model):
    turma = models.ForeignKey('common.Turma', on_delete=models.CASCADE)
    mensagem = models.ForeignKey('Mensagem', on_delete=models.CASCADE)
    resposta = models.TextField(null=True, default=None)

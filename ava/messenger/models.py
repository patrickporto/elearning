from django.db import models
from django.conf import settings
from common.models import Usuario


class ChatMessagem(models.Model):
    tipo = models.CharField(max_length=40, default='chat_message')
    turma = models.ForeignKey('common.Turma', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    mensagem = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.mensagem


class Curtida(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    mensagem = models.ForeignKey('ChatMessagem', on_delete=models.CASCADE, related_name='curtidas')


class Duvida(models.Model):
    turma = models.ForeignKey('common.Turma', on_delete=models.CASCADE)
    mensagem = models.ForeignKey('ChatMessagem', on_delete=models.CASCADE)
    resposta = models.TextField(null=True, default=None)

from django.db import models
from common.models import Usuario


class Conteudo(models.Model):
    disciplina = models.ForeignKey('common.Disciplina', on_delete=models.CASCADE)
    autor = models.ForeignKey(
        'common.Usuario',
        on_delete=models.CASCADE,
        limit_choices_to={'papel': Usuario.PROFESSOR},
    )
    data_criacao = models.DateTimeField(auto_now_add=True)


class Questionario(models.Model):
    descricao = models.TextField()
    nome = models.CharField(max_length=100)
    questoes = models.ManyToManyField('Questao')


class Questao(models.Model):
    nome = models.CharField(max_length=100)
    enunciado = models.TextField()


class Respondido(models.Model):
    aluno = models.ForeignKey(
        'common.Usuario',
        on_delete=models.CASCADE,
        limit_choices_to={'papel': Usuario.ALUNO},
    )
    questao = models.ForeignKey('Questao', on_delete=models.CASCADE)
    resposta = models.TextField()

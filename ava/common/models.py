from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _


class Usuario(AbstractBaseUser, PermissionsMixin):
    PROFESSOR = 0
    ALUNO = 1
    PAPEL_CHOICES = (
        (PROFESSOR, 'Professor',),
        (ALUNO, 'Aluno',),
    )

    email = models.EmailField(_('email address'), unique=True)
    nome = models.CharField('nome', max_length=255, blank=True)
    is_active = models.BooleanField(_('active'), default=True)
    foto = models.ImageField(upload_to='avatars/', null=True, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    papel = models.IntegerField(choices=PAPEL_CHOICES)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')


class Curso(models.Model):
    nome = models.CharField(max_length=255)
    disciplinas = models.ManyToManyField('Disciplina')


class Disciplina(models.Model):
    nome = models.CharField(max_length=255)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)


class Turma(models.Model):
    vagas = models.IntegerField(default=50)
    professor = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        limit_choices_to={'papel': Usuario.PROFESSOR},
    )
    periodo = models.CharField(max_length=7)
    inicio = models.DateTimeField()
    fim = models.DateTimeField()

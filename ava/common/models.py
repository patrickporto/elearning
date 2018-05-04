from django.db import models
from django.contrib.auth.models import PermissionsMixin, BaseUserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
    ADMIN = 0
    PROFESSOR = 1
    ALUNO = 2
    PAPEL_CHOICES = (
        (PROFESSOR, 'Professor',),
        (ALUNO, 'Aluno',),
        (ADMIN, 'Admin',),
    )

    email = models.EmailField(_('email address'), unique=True)
    nome = models.CharField('nome', max_length=255, blank=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('active'), default=True)
    foto = models.ImageField(upload_to='avatars/', null=True, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    papel = models.IntegerField(choices=PAPEL_CHOICES, default=ADMIN)

    objects = UserManager()

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
    disciplina = models.ForeignKey(
        Disciplina,
        on_delete=models.CASCADE,
    )
    professor = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        limit_choices_to={'papel': Usuario.PROFESSOR},
    )
    periodo = models.CharField(max_length=7)
    inicio = models.DateTimeField()
    fim = models.DateTimeField()

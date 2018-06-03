# Generated by Django 2.0.5 on 2018-06-03 01:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0008_disciplina_carga_horaria'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('messenger', '0007_auto_20180522_0421'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(default='chat_message', max_length=40)),
                ('conteudo', models.TextField()),
                ('data_publicacao', models.DateTimeField(auto_now_add=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.Turma')),
            ],
        ),
        migrations.RemoveField(
            model_name='chatmessagem',
            name='author',
        ),
        migrations.RemoveField(
            model_name='chatmessagem',
            name='turma',
        ),
        migrations.AlterField(
            model_name='curtida',
            name='mensagem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='curtidas', to='messenger.Mensagem'),
        ),
        migrations.AlterField(
            model_name='duvida',
            name='mensagem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='messenger.Mensagem'),
        ),
        migrations.DeleteModel(
            name='ChatMessagem',
        ),
    ]
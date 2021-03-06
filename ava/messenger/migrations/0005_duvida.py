# Generated by Django 2.0.5 on 2018-05-22 01:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0007_turma_alunos'),
        ('messenger', '0004_curtida'),
    ]

    operations = [
        migrations.CreateModel(
            name='Duvida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resposta', models.TextField(default=None, null=True)),
                ('mensagem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='messenger.ChatMessagem')),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.Turma')),
            ],
        ),
    ]

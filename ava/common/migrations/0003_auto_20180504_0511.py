# Generated by Django 2.0.5 on 2018-05-04 05:11

import common.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20180504_0458'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='usuario',
            managers=[
                ('objects', common.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='turma',
            name='professor',
            field=models.ForeignKey(limit_choices_to={'papel': 1}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='foto',
            field=models.ImageField(default='https://api.adorable.io/avatars/192/abott@adorable.png', upload_to='avatars/'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='papel',
            field=models.IntegerField(choices=[(1, 'Professor'), (2, 'Aluno'), (0, 'Admin')], default=0),
        ),
    ]
